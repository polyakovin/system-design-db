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

## Когда применять

- Dataset или write load приближается к пределам одного узла.
- Есть естественный tenant или entity boundary.
- Нужна изоляция noisy neighbors.

## Связанные материалы

- [Capacity estimation](../fundamentals/capacity-estimation.md)
- [Storage selection](storage-selection.md)
- [Cassandra](../../tools/databases/cassandra.md)

