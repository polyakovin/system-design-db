---
title: Designing Data-Intensive Applications
url: https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/
type: book
category: sources
tags: [system-design, distributed-systems, data-systems, storage, replication, consistency]
added: 2026-07-06
status: used
---

# Designing Data-Intensive Applications

Книга Martin Kleppmann о проектировании надежных, масштабируемых и сопровождаемых data-intensive applications. Источник полезен как фундаментальная рамка для выбора storage, понимания replication, partitioning, consistency, transactions, batch processing и stream processing.

## Описание

- Автор: Martin Kleppmann.
- Издатель: O'Reilly Media.
- Выпуск: March 2017.
- ISBN: `9781491903063`.
- Формат в проекте: локальный PDF, 613 страниц, `/Users/polyakovin/Downloads/Designing Data Intensive Applications by Martin Kleppmann.pdf`.

## Практическая ценность

- Дает устойчивую модель tradeoffs между reliability, scalability и maintainability.
- Помогает сравнивать storage engines, replication modes, partitioning schemes и consistency guarantees без привязки к одному vendor.
- Подходит как primary provenance для заметок о data systems, distributed transactions и stream processing.

## Связи

- [System design principles](../../patterns/fundamentals/system-design-principles.md) — reliability, scalability, maintainability и ограничения до выбора технологий.
- [Capacity estimation](../../patterns/fundamentals/capacity-estimation.md) — load parameters, response-time distribution и limiting resource.
- [Latency and throughput](../../patterns/fundamentals/latency-and-throughput.md) — tail latency, saturation и fanout amplification.
- [Availability and reliability](../../patterns/fundamentals/availability-and-reliability.md) — fault tolerance, recovery paths и partial failures.
- [API design](../../patterns/architecture-design/api-design.md) — encoding, schema evolution и rolling upgrades.
- [Storage selection](../../patterns/architecture-design/storage-selection.md) — выбор primary store, индексов и read models.
- [Replication strategy](../../patterns/architecture-design/replication-strategy.md) — replicas, lag, failover и read consistency.
- [Data partitioning](../../patterns/architecture-design/data-partitioning.md) — sharding, routing и rebalancing.
- [Caching strategy](../../patterns/architecture-design/caching-strategy.md) — cache как derived data и invalidation strategy.
- [Consistency models](../../patterns/fundamentals/consistency-models.md) — freshness, coordination, conflicts и user-visible guarantees.
- [Distributed transactions](../../patterns/advanced/distributed-transactions.md) — coordination, sagas и transactional outbox.
- [Queues and streams](../../patterns/architecture-design/queues-and-streams.md) — async processing, ordering и consumer groups.
- [Multi-region architecture](../../patterns/advanced/multi-region-architecture.md) — geo-distribution, conflict policy и coordination cost.
- [PostgreSQL](../../tools/databases/postgresql.md) — relational model, transactions, indexes и read replicas.
- [MySQL](../../tools/databases/mysql.md) — relational OLTP, read replicas и sharding constraints.
- [MongoDB](../../tools/databases/mongodb.md) — document model, schema-on-read и aggregate boundaries.
- [Kafka](../../tools/messaging/kafka.md) — durable event log для streams, replay и fanout.
- [Cassandra](../../tools/databases/cassandra.md) — wide-column store для high-write distributed workloads.
- [Redis](../../tools/caches/redis.md) — cache state, coordination state и eviction/hot-key behavior.
- [RabbitMQ](../../tools/messaging/rabbitmq.md) — task queues, acknowledgements и retry semantics.

## Статус

Добавлено: 2026-07-06. Устойчивые рекомендации перенесены в существующие canonical заметки как короткие секции "Рекомендации из DDIA"; source-карточка остается provenance, а не самостоятельным конспектом книги.
