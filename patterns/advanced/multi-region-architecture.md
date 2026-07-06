# Multi-region architecture

## Проблема

Один region может стать bottleneck, single failure domain или источником высокой latency для удаленных пользователей.

## Решение

Выбери region strategy:

- active-passive для disaster recovery;
- active-active для lower latency и higher availability;
- regional routing для locality;
- explicit data residency rules;
- tested failover и failback runbooks.

## Tradeoffs

Multi-region резко повышает complexity: replication lag, conflicts, cost, deploy coordination и [Incident response](../production-operations/incident-response.md) становятся сложнее.

## Рекомендации из DDIA

- Geo-distribution усиливает стоимость linearizability: чем больше network delay между regions, тем дороже synchronous coordination.
- Active-active writes требуют заранее выбранной conflict policy и понятного ownership для user-visible invariants.
- Для latency-sensitive flows разделяй local reads/writes и global invariants: не все данные должны пересекать region boundary синхронно.
- Derived data лучше восстанавливать из durable logs, чтобы region failover не зависел от manual reconstruction.

## Когда применять

- Есть строгие recovery targets.
- Пользователи распределены географически.
- Требуется data residency или regional isolation.

## Связанные материалы

- [Availability and reliability](../fundamentals/availability-and-reliability.md)
- [Replication strategy](../architecture-design/replication-strategy.md)
- [Incident response](../production-operations/incident-response.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
