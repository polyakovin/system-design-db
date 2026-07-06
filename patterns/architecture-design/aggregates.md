---
title: Aggregates
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, aggregates, invariants]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Aggregates

## Проблема

Доменные объекты связаны друг с другом. Без явных границ изменения расползаются по всему графу объектов, а инварианты (бизнес-правила, которые всегда должны быть истинны) нарушаются при конкурентных изменениях.

## Решение

Aggregate — это кластер [Entity](entities.md) и [Value Objects](value-objects.md), рассматриваемый как единое целое для изменений данных. У каждого агрегата есть **Aggregate Root** — единственная точка входа для внешних ссылок.

- **Aggregate Root (AR):** Entity, через которую идут все изменения агрегата. Только AR может быть загружен из Repository.
- **Инварианты:** бизнес-правила, которые агрегат гарантирует при каждом изменении (например, «сумма строк заказа = общая сумма», «статус не может перейти из Shipped в Draft»).
- **Граница транзакции:** изменение агрегата — это одна транзакция. Один агрегат = один consistency boundary.
- **Ссылки по ID:** другие агрегаты ссылаются на AR только по identity, не по объектной ссылке.

## Правила дизайна

1. **Маленькие агрегаты:** предпочитай агрегаты из одного Entity + VO, а не большие кластеры.
2. **Ссылайся по ID:** не храни прямые ссылки на другие агрегаты.
3. **Eventual consistency между агрегатами:** внутри агрегата — immediate consistency, между агрегатами — eventual через [Domain Events](domain-events.md).
4. **Один агрегат — одна транзакция в БД.**

## Пример

```
Order (Aggregate Root)
├── OrderId (identity)
├── CustomerId (reference by ID)
├── status: OrderStatus
├── items: List[OrderLine]   (Value Objects)
├── shippingAddress: Address (Value Object)
├── total: Money             (Value Object)

Invariant: total == sum(item.price * item.qty for item in items)
```

## Антипаттерны

- **God Aggregate:** один агрегат на весь [Bounded Context](bounded-context.md) — проблемы с конкуренцией и производительностью.
- **Прямые ссылки между агрегатами:** `order.customer.name` вместо `order.customerId`.
- **Изменение нескольких агрегатов в одной транзакции.**

## Vaughan Vernon's Rules of Aggregate Design (Chapter 10)

Vernon operationalises Evans' theory into four practical rules:

**Rule 1: Protect business invariants inside aggregates.** Only the aggregate root enforces invariants. Other parts of the model see only the root, never internal entities directly. No external object may hold a reference to an aggregate member.

**Rule 2: Design small aggregates.** Vernon's heuristic: prefer aggregates with a single root entity and a few value objects. Large aggregates increase transaction contention and memory pressure. If a child entity has its own lifecycle and invariants, extract it into its own aggregate.

**Rule 3: Reference other aggregates by identity only.** Never store a direct object reference to another aggregate inside an aggregate. Use the target's ID as a value object. This keeps aggregates loosely coupled and avoids lazy-loading surprises. Resolve references via a repository or service when needed.

**Rule 4: Use eventual consistency between aggregates.** A single transaction modifies exactly one aggregate instance. Cross-aggregate consistency is achieved through domain events processed asynchronously. Vernon's mantra: "one transaction, one aggregate." If a use case must update two aggregates atomically, reconsider your aggregate boundaries — they may belong in the same aggregate after all.

### Practical considerations

- **ORM navigation properties are a trap:** ORMs encourage `order.Customer.Name` — this violates reference-by-identity. Disable navigation properties across aggregate boundaries.
- **Consistency vs. availability:** immediate consistency within an aggregate (single DB row lock), eventual consistency between aggregates (domain event + async handler).
- **Deletion:** deleting an aggregate root removes the entire aggregate. Marking individual children as "soft deleted" suggests they should be their own aggregate.

## Связанные материалы

- [Entities](entities.md) — aggregate root это entity
- [Value Objects](value-objects.md) — строительные блоки внутри агрегата
- [Repositories](repositories.md) — загрузка агрегатов
- [Domain Events](domain-events.md) — eventual consistency между агрегатами
- [Event Sourcing](event-sourcing.md) — event-sourced aggregates
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 6 (Life Cycle of a Domain Object)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 10 (Aggregates)
- [Learning Domain-Driven Design](../../sources/books/learning-domain-driven-design.md) — глава 9 (Aggregate)
