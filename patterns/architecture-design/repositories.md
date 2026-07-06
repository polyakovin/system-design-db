---
title: Repositories
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, repositories, persistence]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Repositories

## Проблема

Доменная модель не должна знать детали хранения (SQL, NoSQL, файловая система). Прямой доступ к БД через ORM или сырые запросы размывает границы домена и привязывает модель к инфраструктуре.

## Решение

Repository — это абстракция коллекции агрегатов, скрывающая детали хранилища. Предоставляет интерфейс как для in-memory коллекции: add, get, remove, find by criteria.

- **Один Repository на Aggregate Root** — только AR может быть загружен или сохранён через репозиторий.
- **Интерфейс в domain-слое, реализация в infrastructure-слое.**
- Не раскрывает детали БД: никаких `JOIN`, `WHERE`, transaction management в интерфейсе.
- Может возвращать агрегаты, списки агрегатов, или `Optional` для поиска по ID.

## Пример

```python
# domain layer — interface
class OrderRepository(ABC):
    @abstractmethod
    def get(self, order_id: OrderId) -> Optional[Order]:
        ...
    @abstractmethod
    def save(self, order: Order) -> None:
        ...
    @abstractmethod
    def find_pending_by_customer(self, customer_id: CustomerId) -> List[Order]:
        ...

# infrastructure layer — implementation
class PostgresOrderRepository(OrderRepository):
    def get(self, order_id: OrderId) -> Optional[Order]:
        row = self.db.execute("SELECT ... WHERE id = ?", order_id)
        return self._to_aggregate(row) if row else None
```

## Tradeoffs

Плюсы: развязывает домен и хранилище, упрощает тестирование (in-memory fake), сохраняет доменную модель чистой.
Минусы: дополнительный слой абстракции, риск N+1 запросов при загрузке связанных агрегатов.

## Implementation Patterns (Vaughan Vernon, Chapter 12)

### ORM vs. hand-rolled persistence

**ORM approach (Hibernate/Entity Framework):**
- Pro: automatic mapping, less boilerplate, built-in dirty checking and change tracking.
- Con: "magic" lazy loading that breaks aggregate boundaries, impedance mismatch, N+1 query traps.
- Vernon's advice: use an ORM for simple CRUD aggregates but disable lazy loading across aggregate boundaries. Explicitly configure eager fetch for value objects within the aggregate.

**Hand-rolled (raw SQL / lightweight mapper like MyBatis/Dapper):**
- Pro: full control over queries, no hidden lazy-load surprises, reads map explicitly to aggregates.
- Con: more boilerplate, ORM conveniences (identity map, change tracking) must be built or lived without.
- Vernon's advice: prefer hand-rolled for complex query models (CQRS read side) or when ORM behaviour causes more friction than it removes.

### Lazy vs. eager loading

- **Eager (within an aggregate):** load all value objects and child entities in one query. The aggregate is a consistency boundary — you always need the whole thing.
- **Lazy (across aggregates):** never lazy-load another aggregate through an ORM navigation property. If the view needs data from two aggregates, use a read model (CQRS) or an application service that calls two repositories.
- **Vernon's rule:** if you find yourself adding `fetch = FetchType.EAGER` annotations to fix `LazyInitializationException`, your aggregate boundary is wrong or you're crossing it.

### Factory patterns for aggregates

Vernon describes two factory placements:

1. **Factory method on the aggregate root:** `Order.place(orderId, customerId, items)` — when creation logic is simple and belongs to the aggregate's ubiquitous language.
2. **Standalone domain factory:** `OrderFactory.createFromQuote(quote)` — when creation involves complex rules, multiple steps, or dependencies on services. Keeps the aggregate constructor clean.

The factory produces a fully-valid aggregate. Never expose a public no-arg constructor that leaves invariants unsatisfied.

## Связанные материалы

- [Aggregates](aggregates.md) — репозиторий работает с aggregate root
- [Entities](entities.md)
- [Layered Architecture](layered-architecture.md) — интерфейс в domain, реализация в infrastructure
- [CQRS](cqrs.md) — read models bypass repositories
- [Event Sourcing](event-sourcing.md) — event-sourced repositories
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 6
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 12 (Repositories)
