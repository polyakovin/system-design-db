# Latency and throughput

## Проблема

Команда может увеличить throughput и случайно ухудшить user-visible latency. Эти метрики связаны, но отвечают на разные вопросы.

## Решение

Разделяй:

- latency: сколько времени занимает один запрос;
- throughput: сколько работы система делает за единицу времени;
- tail latency: насколько плохи p95, p99 и p999;
- saturation: когда добавленная нагрузка начинает резко ухудшать latency.

## Design notes

Оптимизация latency часто требует уменьшить количество network hops, синхронных зависимостей и contention. Оптимизация throughput часто требует batching, partitioning, async processing и backpressure.

## Рекомендации из DDIA

- Смотри на distribution, а не только average: p95, p99 и p999 показывают user-visible tail latency.
- Saturation проявляется как резкий рост latency при небольшой добавке load; держи alerts на queue length, utilization и tail latency вместе.
- Batch processing и async processing повышают throughput, но могут ухудшить freshness и time-to-completion для отдельных users.
- После fanout запроса оцени tail amplification: много параллельных downstream calls повышают шанс, что один slow call испортит весь response.

## Когда применять

- При выборе sync или async request path.
- При настройке autoscaling.
- При выборе cache boundary.
- При анализе p95/p99 regressions.

## Связанные материалы

- [Capacity estimation](capacity-estimation.md)
- [Caching strategy](../architecture-design/caching-strategy.md)
- [Queues and streams](../architecture-design/queues-and-streams.md)
- [Observability](../production-operations/observability.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
