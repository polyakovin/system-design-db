# Data partitioning

## Проблема

Один storage node или logical partition перестает выдерживать load, а hot keys создают uneven utilization.

## Решение

Раздели dataset на partitions:

- range partitioning для ordered access;
- hash partitioning для равномерного распределения;
- tenant-based partitioning для isolation;
- composite keys для контролируемого routing;
- rebalancing plan до появления hard limit.

## Tradeoffs

Partitioning повышает capacity, но усложняет joins, cross-partition transactions, migrations и operational tooling.

## Рекомендации из DDIA

- Разделяй partitioning и replication: partitioning делит data по nodes, replication копирует partitions для availability и locality.
- Range partitioning сохраняет ordered scans, но может создавать hot ranges; hash partitioning лучше распределяет load, но ломает efficient range queries.
- Secondary indexes в partitioned storage требуют отдельного выбора: local indexes упрощают writes, global indexes упрощают reads, но усложняют coordination.
- Rebalancing должен перемещать ограниченный объем данных и иметь operational guardrails; полностью automatic rebalancing может усилить incident во время load spike.
- Request routing является частью дизайна partitioning: клиент, routing tier или coordination service должны находить нужный partition предсказуемо.

## Когда применять

- Dataset или write load приближается к пределам одного узла.
- Есть естественный tenant или entity boundary.
- Нужна изоляция noisy neighbors.

## Связанные материалы

- [Capacity estimation](../fundamentals/capacity-estimation.md)
- [Storage selection](storage-selection.md)
- [Cassandra](../../tools/databases/cassandra.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
