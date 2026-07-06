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

## Связанные материалы

- [PostgreSQL](../../tools/databases/postgresql.md)
- [MySQL](../../tools/databases/mysql.md)
- [MongoDB](../../tools/databases/mongodb.md)
- [Cassandra](../../tools/databases/cassandra.md)
- [Redis](../../tools/caches/redis.md)
- [Data partitioning](data-partitioning.md)
- [Replication strategy](replication-strategy.md)

