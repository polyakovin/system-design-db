# Replication strategy

## Проблема

Single copy of data создает risk of loss и downtime. Несколько copies создают вопросы lag, conflicts и failover.

## Решение

Определи replication role:

- read replicas для scaling reads;
- synchronous replication для stronger durability;
- asynchronous replication для lower latency;
- leader election и failover policy;
- lag monitoring и user-visible consistency rules.

## Tradeoffs

Синхронная запись повышает durability, но добавляет coordination. Асинхронная запись быстрее, но требует handling для lag и stale reads.

## Рекомендации из DDIA

- Сначала назови цель replication: high availability, disconnected operation, latency, read scalability или durability.
- Для asynchronous replicas явно опиши user-visible guarantees: read-your-writes, monotonic reads и consistent prefix reads.
- Multi-leader replication требует conflict resolution policy до запуска, а не после первого concurrent write.
- Leaderless replication и quorum reads/writes не снимают всех anomalies: учитывай stale replicas, sloppy quorum, hinted handoff и concurrent writes.
- Replication lag должен быть product-level signal, если users могут читать stale data после write.

## Когда применять

- Stateful component критичен для workflow.
- Read traffic намного больше write traffic.
- Нужно снизить recovery time.

## Связанные материалы

- [Availability and reliability](../fundamentals/availability-and-reliability.md)
- [Consistency models](../fundamentals/consistency-models.md)
- [Multi-region architecture](../advanced/multi-region-architecture.md)
- [Designing Data-Intensive Applications](../../sources/books/designing-data-intensive-applications.md)
