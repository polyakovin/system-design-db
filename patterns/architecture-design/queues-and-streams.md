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

## Рекомендации из DDIA

- Различай task queue и event log: task queue распределяет work между workers, event log хранит ordered history для replay и independent consumers.
- Retained log полезен, когда derived state нужно rebuild from scratch: search index, cache, analytics view или materialized view.
- Change data capture и event sourcing превращают database writes в stream, но требуют schema evolution, idempotent consumers и replay-safe side effects.
- Exactly-once semantics не появляются от broker alone: end-to-end correctness требует operation identifiers, idempotency и transactional boundary для state change плюс message publication.
- Для stream processing отдельно моделируй event time, processing time, late events и window completeness.

## Когда применять

- Work can complete after user response.
- Нужно сгладить traffic spikes.
- Есть несколько consumers одного event flow.

## Связанные материалы

- [Latency and throughput](../fundamentals/latency-and-throughput.md)
- [Capacity estimation](../fundamentals/capacity-estimation.md)
- [Kafka](../../tools/messaging/kafka.md)
- [RabbitMQ](../../tools/messaging/rabbitmq.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
