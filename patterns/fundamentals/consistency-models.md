# Consistency models

## Проблема

Разные части системы могут видеть разные версии данных. Если не назвать guarantee явно, пользователи увидят странные состояния, а разработчики будут чинить симптомы.

## Решение

Для каждого critical workflow определи:

- нужна ли read-your-writes гарантия;
- допустима ли eventual consistency;
- где возможны concurrent writes;
- как система решает conflicts;
- какие операции должны быть idempotent.

## Tradeoffs

Сильная согласованность упрощает reasoning, но увеличивает coordination cost и может ухудшить latency. Более слабые модели требуют компенсирующих workflow и понятного UX.

## Рекомендации из DDIA

- Называй конкретную гарантию, а не просто "strong" или "eventual": read committed, snapshot isolation, serializability, linearizability, causal consistency.
- Linearizability удобна для reasoning, но дорога при network delays и плохо сочетается с geo-distribution.
- Causality дешевле linearizability, но constraints вроде unique username или non-negative inventory часто требуют coordination.
- Не полагайся на physical clocks для correctness: clock skew, pauses и timestamp ordering могут создавать hidden anomalies.
- Для слабых моделей явно опиши anomalies, которые продукт допускает, и recovery workflow для тех, которые недопустимы.

## Когда применять

- При проектировании денежных, inventory, booking и permission flows.
- При выборе replication mode.
- При переходе от monolith storage к distributed storage.

## Связанные материалы

- [Replication strategy](../architecture-design/replication-strategy.md)
- [Distributed transactions](../advanced/distributed-transactions.md)
- [Storage selection](../architecture-design/storage-selection.md)
- [API design](../architecture-design/api-design.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
