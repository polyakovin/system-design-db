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

## Связанные материалы

- [Aggregates](aggregates.md) — репозиторий работает с aggregate root
- [Entities](entities.md)
- [Layered Architecture](layered-architecture.md) — интерфейс в domain, реализация в infrastructure
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 6
