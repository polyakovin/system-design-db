# Storage selection

## Проблема

Неправильный primary store усложняет schema evolution, queries, consistency guarantees и operations.

## Решение

Выбирай storage по access patterns:

- transactional writes и relational constraints;
- document-centric reads;
- high-write wide-row workloads;
- ephemeral cache state;
- append-only event streams;
- analytical queries.

## Design questions

- Какие queries должны быть быстрыми?
- Где source of truth?
- Нужны ли transactions?
- Как будет расти dataset?
- Какие restore и migration paths нужны?

## Рекомендации из DDIA

- Выбирай data model по форме связей: document model удобен для self-contained aggregates, relational model сильнее для many-to-one и many-to-many relationships, graph model нужен для densely connected data.
- Разделяй OLTP и OLAP workloads: user-facing point lookups и analytical scans требуют разных storage layouts, индексов и operational paths.
- Учитывай storage engine: B-tree engines обычно хороши для read-heavy point/range access, LSM-based engines часто сильны на write-heavy workloads, но требуют внимания к compaction и read amplification.
- Derived data systems, например search indexes, caches и analytics views, должны быть rebuildable из source of truth или append-only log.

## Связанные материалы

- [PostgreSQL](../../tools/databases/postgresql.md)
- [MySQL](../../tools/databases/mysql.md)
- [MongoDB](../../tools/databases/mongodb.md)
- [Cassandra](../../tools/databases/cassandra.md)
- [Redis](../../tools/caches/redis.md)
- [Data partitioning](data-partitioning.md)
- [Replication strategy](replication-strategy.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
