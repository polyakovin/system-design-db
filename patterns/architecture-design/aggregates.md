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

Aggregate — это кластер Entity и Value Objects, рассматриваемый как единое целое для изменений данных. У каждого агрегата есть **Aggregate Root** — единственная точка входа для внешних ссылок.

- **Aggregate Root (AR):** Entity, через которую идут все изменения агрегата. Только AR может быть загружен из Repository.
- **Инварианты:** бизнес-правила, которые агрегат гарантирует при каждом изменении (например, «сумма строк заказа = общая сумма», «статус не может перейти из Shipped в Draft»).
- **Граница транзакции:** изменение агрегата — это одна транзакция. Один агрегат = один consistency boundary.
- **Ссылки по ID:** другие агрегаты ссылаются на AR только по identity, не по объектной ссылке.

## Правила дизайна

1. **Маленькие агрегаты:** предпочитай агрегаты из одного Entity + VO, а не большие кластеры.
2. **Ссылайся по ID:** не храни прямые ссылки на другие агрегаты.
3. **Eventual consistency между агрегатами:** внутри агрегата — immediate consistency, между агрегатами — eventual через Domain Events.
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

- **God Aggregate:** один агрегат на весь bounded context — проблемы с конкуренцией и производительностью.
- **Прямые ссылки между агрегатами:** `order.customer.name` вместо `order.customerId`.
- **Изменение нескольких агрегатов в одной транзакции.**

## Связанные материалы

- [Entities](entities.md) — aggregate root это entity
- [Value Objects](value-objects.md) — строительные блоки внутри агрегата
- [Repositories](repositories.md) — загрузка агрегатов
- [Domain Events](domain-events.md) — eventual consistency между агрегатами
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 6 (Life Cycle of a Domain Object)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 10 (Aggregates)
- [Learning Domain-Driven Design](../../sources/books/learning-domain-driven-design.md) — глава 9 (Aggregate)
