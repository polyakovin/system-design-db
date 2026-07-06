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

## Связанные материалы

- [Aggregates](aggregates.md) — события рождаются из агрегатов
- [Bounded Context](bounded-context.md) — события соединяют контексты
- [Strategic Design](strategic-design.md) — event-driven отношения в context map
- [Anti-Corruption Layer](anti-corruption-layer.md) — трансляция событий между BC
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 14 (Maintaining Model Integrity)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 8 (Domain Events)
