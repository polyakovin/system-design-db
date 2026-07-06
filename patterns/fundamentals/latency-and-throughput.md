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

