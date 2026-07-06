---
title: Kafka
url: https://kafka.apache.org/
type: url
category: tools
tags: [messaging, streaming, event-log]
added: 2026-07-06
status: starter
---

# Kafka

Distributed event log для durable streams, replay, fanout и event-driven integration.

## Где применять

- Event streams with replay.
- Multiple consumers of the same event flow.
- High-throughput ingestion.
- Audit-like append-only records.

## Сильные стороны

- Durable ordered partitions.
- Consumer groups.
- Replay by offset.
- Strong ecosystem for stream processing.

## Ограничения

- Partitioning choices are hard to change.
- Exactly-once semantics still require careful end-to-end design.
- Operational footprint is higher than simple task queues.

## Design notes

Use an event log when replay and independent consumers are core requirements, not just because a workflow is asynchronous.

## Связанные материалы

- [Queues and streams](../../patterns/architecture-design/queues-and-streams.md)
- [Distributed transactions](../../patterns/advanced/distributed-transactions.md)

