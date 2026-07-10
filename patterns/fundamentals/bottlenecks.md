# Bottlenecks

## Проблема

Любая система имеет узкое место, которое ограничивает общую производительность. Без понимания bottleneck'а оптимизация даёт случайные результаты: ускорение не bottleneck'а не улучшает system throughput.

## Решение

Систематический подход к идентификации:

1. **Measure first** — собирай latency, throughput, utilisation по всем компонентам.
2. **Find the slowest link** — компонент с наибольшей utilisation или latency, который стоит на critical path.
3. **Determine the nature** — contention (ожидание shared ресурса) или coherency (координация между узлами).
4. **Fix, re-measure** — устрани bottleneck, проверь, что throughput вырос, затем ищи следующий.

## Типичные bottlenecks

| Категория | Примеры |
|---|---|
| CPU | Single-threaded обработчик, serialisation point |
| Memory | Нехватка heap, cache thrashing |
| Disk I/O | Slow storage, много random writes |
| Network | Bandwidth лимит, tail latency на downstream |
| Database | Lock contention, slow query, replication lag |
| Coordination | Consensus overhead, distributed lock |

## Когда применять

- При падении throughput под нагрузкой.
- При росте tail latency выше SLO.
- При планировании capacity.

## Связанные материалы

- [Identifying Bottlenecks with USL](../performance-and-scalability/identifying-bottlenecks.md)
- [Contention (α coefficient)](../performance-and-scalability/contention.md)
- [Coherency (β coefficient)](../performance-and-scalability/coherency.md)
- [Latency and throughput](latency-and-throughput.md)
- [Capacity estimation](capacity-estimation.md)
