---
title: RabbitMQ
url: https://www.rabbitmq.com/
type: url
category: tools
tags: [messaging, queue, broker]
added: 2026-07-06
status: starter
---

# RabbitMQ

Message broker для task queues, routing rules, acknowledgements и workload decoupling.

## Где применять

- Background jobs.
- Work queues with acknowledgement.
- Routing-heavy message flows.
- Moderate-throughput asynchronous processing.

## Сильные стороны

- Flexible exchange and routing model.
- Mature acknowledgement semantics.
- Useful for worker pools.
- Simpler fit for task queues than full event-log systems.

## Ограничения

- Replay is not the primary design center.
- Queue growth can become an operational risk.
- Message ordering depends on topology and consumers.

## Design notes

Good fit when the system needs work distribution and retry semantics more than long-term event replay.

## Рекомендации из DDIA

- AMQP/JMS-style broker fits asynchronous RPC and work distribution, where acknowledged messages can be removed after processing.
- Use dead-letter queues, retry limits and idempotent handlers because delivery failure is part of the contract.
- Do not use a transient task queue as durable system history if consumers need replay, rebuild or independent derived state.
- Queue depth is a user-facing freshness signal when tasks represent delayed workflow completion.

## Связанные материалы

- [Queues and streams](../../patterns/architecture-design/queues-and-streams.md)
- [Incident response](../../patterns/production-operations/incident-response.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
