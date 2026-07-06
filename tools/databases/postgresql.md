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

## Связанные материалы

- [Storage selection](../../patterns/architecture-design/storage-selection.md)
- [Consistency models](../../patterns/fundamentals/consistency-models.md)
- [Replication strategy](../../patterns/architecture-design/replication-strategy.md)

