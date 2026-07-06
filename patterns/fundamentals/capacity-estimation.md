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

## Связанные материалы

- [Latency and throughput](latency-and-throughput.md)
- [Data partitioning](../architecture-design/data-partitioning.md)
- [Queues and streams](../architecture-design/queues-and-streams.md)
- [Rate limiting](../architecture-design/rate-limiting.md)

