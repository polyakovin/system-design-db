---
title: Domain Events
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, events, integration]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Domain Events

## Проблема

Изменения в одной части системы должны вызывать реакции в других частях, но прямая синхронная связь создаёт coupling, снижает надёжность и мешает независимой эволюции компонентов.

## Решение

Domain Event — это сообщение о значимом факте, который уже произошёл в домене. Назван в прошедшем времени, неизменяем, содержит все данные, нужные потребителям.

- **Имя в прошедшем времени:** `OrderPlaced`, `PaymentReceived`, `CustomerRegistered`.
- **Иммутабельность:** событие — это факт, его нельзя изменить или отозвать (можно опубликовать компенсирующее событие).
- **Причина — изменение агрегата:** событие создаётся aggregate root и содержит identity агрегата.
- **Интеграция Bounded Contexts:** события — основной способ связи между BC (через event bus / message broker).

## Структура

```
OrderPlaced {
    event_id: UUID,
    occurred_at: DateTime,
    order_id: OrderId,
    customer_id: CustomerId,
    items: List[OrderLineItem],
    total: Money
}
```

## Tradeoffs

Плюсы: decoupling, независимая эволюция, естественная поддержка eventual consistency, audit trail из коробки.
Минусы: eventual consistency (не для всего подходит), сложность отладки и трассировки, ordering гарантии.

## Implementation Details (Vaughan Vernon, Chapter 8)

### Event model

Vernon defines a domain event as an immutable value object with at minimum:
- `occurredOn` — timestamp of the event
- `eventId` — unique identifier
- Identity of the aggregate that produced it (e.g., `tenantId` in multi-tenant systems)

Events are named in past tense and belong to the ubiquitous language.

### Publishing infrastructure

Vernon describes three tiers of event infrastructure:

1. **Lightweight (in-process):** Use a simple `DomainEventPublisher` with a `List<Subscriber>` registry. Events fire synchronously within the same transaction. Simple, no external dependency — but no cross-BC integration and no at-least-once delivery.

2. **Message middleware (broker-based):** RabbitMQ, or any message broker. Events published after the aggregate is persisted. Requires idempotent consumers — duplicate delivery is inevitable.

3. **Event store (persistent):** Events are the source of truth. The event store is both the persistence mechanism and the message bus. Enables event sourcing (see [Event Sourcing](event-sourcing.md)).

### When to publish

Vernon's rule: publish the event **after** the transaction commits, not inside it. If the broker is down, the transaction still succeeds. Three approaches:

- **Application-layer publisher:** Application service persists the aggregate, then publishes events from the returned event list.
- **Domain event publisher with transaction synchronisation:** Register events during the aggregate method, flush after commit.
- **Outbox pattern:** Write events to an outbox table in the same transaction, a separate process polls and publishes.

### Event enrichment

Events should carry enough data for consumers to act without calling back. Vernon calls this "event-carried state transfer." Include full value objects, not just IDs, when the consumer needs them.

## Связанные материалы

- [Aggregates](aggregates.md) — события рождаются из агрегатов
- [Bounded Context](bounded-context.md) — события соединяют контексты
- [Strategic Design](strategic-design.md) — event-driven отношения в context map
- [Anti-Corruption Layer](anti-corruption-layer.md) — трансляция событий между BC
- [Event Sourcing](event-sourcing.md) — events as source of truth
- [CQRS](cqrs.md) — events feeding read models
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 14 (Maintaining Model Integrity)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 8 (Domain Events)
