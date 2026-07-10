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

## Сравнение SQL / NoSQL / Search Engine / Object Storage

| Характеристика | SQL (PostgreSQL, MySQL) | Document NoSQL (MongoDB) | Wide-Column (Cassandra) | Search Engine (Elasticsearch) | Object Storage (S3) |
|---|---|---|---|---|---|
| **Data model** | Tables, rows, schemas | Collections, documents, flexible schema | Column families, rows with dynamic columns | Inverted index, JSON documents | Key → blob (+ metadata) |
| **Transactions** | ACID, multi-row | Single-document atomic, multi-doc optional | Single-partition light, batch | Нет | Нет (single-object put) |
| **Consistency** | Strong (configurable) | Strong (replica set primary) | Tunable (quorum/one/all) | Eventual (stronger in 8.x) | Strong (S3 since Dec 2020) |
| **Indexes** | B-Tree, GiST, GIN, BRIN, bitmap | B-Tree, compound, text, geospatial | Primary key + secondary (3.x+) | Inverted + term + vector (HNSW) | No (prefix-only listing) |
| **Queries** | SQL, joins, aggregations | Aggregation pipeline, geospatial | CQL, single-table, denormalized | Full-text, aggregations, vector | GET/PUT/DELETE by key, list by prefix |
| **Write throughput** | Moderate (index + constraint cost) | Moderate-good | Very high (peer-to-peer) | Moderate (indexing cost) | Very high (HTTP PUT) |
| **Read latency** | Single-digit ms | Single-digit ms | Single-digit ms (partition-local) | Sub-50ms (full-text) | 10-100ms (HTTP + network) |
| **Storage capacity** | TB–low PB | TB–PB | PB | PB | EB |
| **Schema evolution** | Migration required | Flexible (add fields) | Flexible (add columns) | Reindex on mapping change | No schema |
| **Best for** | Transactions, relational data, complex queries | Product catalogs, event sourcing, heterogeneous docs | Time series, IoT, messaging, high-write apps | Full-text search, log analytics, vector search | Blobs, backups, data lakes, static assets |
| **Not for** | High-write without sharding | Complex joins, multi-row transactions | Range scans without partition key, joins | Primary store, ACID workloads | Low-latency (ms-level), random writes |

### Практические рекомендации

| Use case | Рекомендуемый primary store | Derived / вспомогательный |
|---|---|---|
| E-commerce (orders, cart) | PostgreSQL | Elasticsearch (search), Redis (cart cache) |
| Social feed (high write) | Cassandra | Redis (hot feed), S3 (media) |
| Log analytics | Elasticsearch | S3 (cold storage, long-term retention) |
| Media hosting | S3 | CDN (edge delivery), PostgreSQL (metadata) |
| Chat / messaging | Cassandra / ScyllaDB | Kafka (event log), Redis (presence) |
| IoT sensor data | Cassandra / TimescaleDB | S3 (raw archives), Kafka (streaming) |

## Design questions

- Какие queries должны быть быстрыми?
- Где source of truth?
- Нужны ли transactions?
- Как будет расти dataset?
- Какие restore и migration paths нужны?

## Рекомендации из DDIA

- Выбирай data model по форме связей: document model удобен для self-contained [aggregates](../architecture-design/aggregates.md), relational model сильнее для many-to-one и many-to-many relationships, graph model нужен для densely connected data.
- Разделяй OLTP и OLAP workloads: user-facing point lookups и analytical scans требуют разных storage layouts, индексов и operational paths.
- Учитывай storage engine: B-tree engines обычно хороши для read-heavy point/range access, LSM-based engines часто сильны на write-heavy workloads, но требуют внимания к compaction и read amplification.
- Derived data [systems](../code-quality/systems.md), например [search indexes](../fundamentals/indexes.md), caches и analytics views, должны быть rebuildable из source of truth или append-only log.

## Связанные материалы

- [PostgreSQL](../../tools/databases/postgresql.md)
- [MySQL](../../tools/databases/mysql.md)
- [MongoDB](../../tools/databases/mongodb.md)
- [Cassandra](../../tools/databases/cassandra.md)
- [Redis](../../tools/caches/redis.md)
- [Object Storage](../../tools/storage/object-storage.md)
- [Search Engine](../../tools/storage/search-engine.md)
- [CDN](../../tools/caches/cdn.md)
- [Data partitioning](data-partitioning.md)
- [Replication strategy](replication-strategy.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
