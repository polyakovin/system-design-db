---
title: PostgreSQL
url: https://www.postgresql.org/
type: url
category: tools
tags: [database, relational, sql]
added: 2026-07-06
status: starter
---

# PostgreSQL

Relational database для transactional workloads, relational constraints, rich indexing и extensibility.

## Где применять

- Primary store для business entities.
- Workflows, где важны transactions и constraints.
- Queries с joins, secondary indexes и reporting needs.
- Systems, где schema evolution должна быть явной.

## Сильные стороны

- ACID transactions.
- Mature indexing и query planner.
- Strong ecosystem и managed availability.
- Extensions for specialized workloads.

## Ограничения

- Horizontal write scaling требует аккуратного partitioning.
- Long-running migrations могут влиять на availability.
- Не все workloads хорошо ложатся на relational model.

## Design notes

Начинай с relational model, если данные имеют устойчивые связи и correctness важнее premature horizontal scale.

## Рекомендации из DDIA

- Relational model особенно полезна, когда domain содержит many-to-one и many-to-many relationships, а query language должен оставаться declarative.
- B-tree indexes хорошо подходят для common OLTP access paths, но каждый secondary index увеличивает write amplification и migration cost.
- Transactions и constraints лучше использовать для локальных invariants внутри одного database boundary; cross-system invariants требуют отдельного integration design.
- При read replicas явно документируй replication lag и user-visible consistency guarantees.

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Consistency models](../../patterns/fundamentals/consistency-models.md)
- [Replication strategy](../../patterns/architecture-design/replication-strategy.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
