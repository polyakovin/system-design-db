# Queues in system design

## Проблема

Синхронная обработка запросов связывает producer и consumer по времени: если consumer медленный или временно недоступен, producer блокируется или теряет данные. Без очереди сложно организовать async processing, load leveling, graceful degradation и decoupling.

## Решение

Очередь — промежуточный buffer между producer и consumer:

- **Decoupling** — producer не знает consumer'а и наоборот.
- **Load leveling** — очередь сглаживает пиковую нагрузку, consumer работает в своём темпе.
- **Buffering** — данные сохраняются, даже если consumer временно недоступен.
- **Fanout** — одно сообщение может быть прочитано несколькими consumer'ами (через topic/exchange).

## Типы очередей

| Тип | Пример | Особенности |
|---|---|---|
| In-memory queue | Channel в Go, ArrayBlockingQueue | Быстро, но теряется при перезапуске |
| Persistent message broker | RabbitMQ, ActiveMQ | Гарантия доставки, routing, retries |
| Log-based event store | Kafka, Pulsar | Replay, ordering, retention по времени |
| Cloud-managed queue | SQS, Pub/Sub, Azure Queue | Маштабируется, SLA, интеграция |

## Tradeoffs

- **Ordering** — строгий порядок сообщений ограничивает параллелизм (single partition consumer).
- **At-least-once vs exactly-once** — at-least-once проще, но требует идемпотентности consumer'ов.
- **Latency** — очередь добавляет задержку по сравнению с прямым sync вызовом.
- **Operational complexity** — брокер требует мониторинга (lag, throughput, disk usage).

## Когда применять

- Когда нужно decouple части системы.
- Когда нагрузка неравномерная (пики/спады).
- Когда consumer может быть временно недоступен.
- Когда нужен replay или audit trail событий.

## Когда не применять

- Если latency < 10ms критична (синхронный вызов быстрее).
- Если data объём мал и пики редки (overhead очереди не оправдан).

## Связанные материалы

- [Queues and streams](../architecture-design/queues-and-streams.md)
- [Kafka](../../tools/messaging/kafka.md)
- [RabbitMQ](../../tools/messaging/rabbitmq.md)
- [Backpressure](backpressure.md)
- [Latency and throughput](latency-and-throughput.md)
