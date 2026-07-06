# Queues and streams

## Проблема

Синхронный request path становится длинным, brittle и дорогим. Но async boundary меняет guarantees и делает failures менее очевидными.

## Решение

Выдели asynchronous workflow:

- queue для background jobs и load smoothing;
- stream для ordered event log и fanout;
- retry policy с dead-letter handling;
- idempotent consumers;
- lag metrics и backpressure.

## Tradeoffs

Async processing улучшает resilience и throughput, но добавляет eventual completion, duplicate delivery и delayed failures.

## Когда применять

- Work can complete after user response.
- Нужно сгладить traffic spikes.
- Есть несколько consumers одного event flow.

## Связанные материалы

- [Latency and throughput](../fundamentals/latency-and-throughput.md)
- [Capacity estimation](../fundamentals/capacity-estimation.md)
- [Kafka](../../tools/messaging/kafka.md)
- [RabbitMQ](../../tools/messaging/rabbitmq.md)

