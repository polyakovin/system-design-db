# Capacity estimation

## Проблема

Без rough numbers невозможно понять, где bottleneck: CPU, disk, network, memory, database connections, queue lag или third-party dependency.

## Решение

Оцени порядок величин до выбора архитектуры:

- daily active users и peak concurrency;
- read/write ratio;
- average и peak QPS;
- payload size и bandwidth;
- storage growth per day;
- retention period;
- cache hit expectations;
- fanout на downstream calls.

## Алгоритм

1. Запиши пользовательский workflow.
2. Переведи workflow в операции.
3. Раздели average и peak.
4. Умножь traffic на payload size.
5. Оцени storage growth и retention.
6. Найди самый дорогой путь: write amplification, fanout или hot partition.

## Tradeoffs

Capacity estimate не должен быть точным прогнозом. Его задача — показать порядок величин и заставить явно назвать риски.

## Рекомендации из DDIA

- Load должен описываться параметрами, которые управляют архитектурой: requests per second, read/write ratio, fanout, payload size, cardinality keys, hot spots.
- Performance описывай через response-time distribution и throughput, а не single average.
- Для scaling strategy сначала найди limiting resource: CPU, disk seek, disk bandwidth, memory, network, locks, connection pools или partition hot spot.
- Отдельно оцени write amplification: secondary indexes, replication, change streams, cache invalidation и analytics pipelines могут умножать один user write.

## Связанные материалы

- [Latency and throughput](latency-and-throughput.md)
- [Data partitioning](../architecture-design/data-partitioning.md)
- [Queues and streams](../architecture-design/queues-and-streams.md)
- [Rate limiting](../architecture-design/rate-limiting.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
