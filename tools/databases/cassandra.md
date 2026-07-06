---
title: Cassandra
url: https://cassandra.apache.org/
type: url
category: tools
tags: [database, wide-column, distributed]
added: 2026-07-06
status: starter
---

# Cassandra

Distributed wide-column database для high-write workloads, predictable access patterns и large-scale partitioned data.

## Где применять

- Time-series-like writes.
- Event metadata и high-volume append workloads.
- Multi-node deployments with tunable consistency.
- Workloads, где query patterns известны заранее.

## Сильные стороны

- Horizontal scale.
- High write throughput.
- Fault tolerance через replication.
- Tunable consistency per operation.

## Ограничения

- Data model проектируется под queries.
- Ad hoc joins и complex filtering не являются strong path.
- Operational tuning требует опыта.

## Design notes

Сначала моделируй access patterns и partition keys. Потом проверяй hot partitions и compaction behavior.

## Рекомендации из DDIA

- LSM-style storage favors high write throughput, but compaction, tombstones and read amplification become operational design constraints.
- Partition key должен распределять load и сохранять нужный query shape; hot partitions are a design bug, not just an ops issue.
- Tunable consistency is per-operation tradeoff: quorum settings reduce some stale reads, but do not eliminate all anomalies under failures and concurrent writes.
- Leaderless replication требует repair mechanisms: hinted handoff, read repair, anti-entropy and clear monitoring for replica divergence.

## Связанные материалы

- [Data partitioning](../../patterns/architecture-design/data-partitioning.md)
- [Replication strategy](../../patterns/architecture-design/replication-strategy.md)
- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Consistency models](../../patterns/fundamentals/consistency-models.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
