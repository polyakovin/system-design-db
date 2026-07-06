---
title: MySQL
url: https://www.mysql.com/
type: url
category: tools
tags: [database, relational, sql]
added: 2026-07-06
status: starter
---

# MySQL

Relational database, часто используемая для web workloads, managed deployments и read-heavy transactional systems.

## Где применять

- CRUD-heavy applications.
- Workloads с понятной relational schema.
- Environments, где managed ecosystem уже стандартизирован.
- Read scaling через replicas.

## Сильные стороны

- Mature tooling.
- Wide hosting support.
- Familiar operational model.
- Хорошо подходит для многих OLTP-сценариев.

## Ограничения

- Complex analytical queries лучше выносить в отдельный analytical path.
- Schema migrations требуют дисциплины.
- Cross-shard design усложняет transactions и joins.

## Design notes

Выбор relational engine должен опираться на access patterns, team experience и operational ecosystem.

## Рекомендации из DDIA

- Relational schema дает явную schema-on-write дисциплину, полезную для correctness и evolvability.
- Read replicas масштабируют reads, но не отменяют stale reads; для critical workflows нужны read-your-writes rules или routing на leader.
- Sharding relational data усложняет joins, uniqueness и transactions, поэтому shard key должен следовать из access patterns, а не из размера таблицы alone.
- Analytical scans лучше выносить в derived OLAP path, чтобы не смешивать user-facing OLTP latency и heavy reporting workload.

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Replication strategy](../../patterns/architecture-design/replication-strategy.md)
- [Consistency models](../../patterns/fundamentals/consistency-models.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
