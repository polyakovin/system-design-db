# Patterns — hierarchy

Раздел описывает системный дизайн по слоям: базовые принципы, архитектурные решения, production-эксплуатация и продвинутые tradeoffs. Начинай с fundamentals, затем переходи к решениям и операционным практикам.

## Fundamentals

С чего начать: нагрузка, надежность, задержки, согласованность и базовая декомпозиция.

- [System design principles](fundamentals/system-design-principles.md) — как держать задачу, constraints и tradeoffs в одном фокусе.
- [Capacity estimation](fundamentals/capacity-estimation.md) — порядок величин для трафика, storage, bandwidth и QPS.
- [Latency and throughput](fundamentals/latency-and-throughput.md) — различие между скоростью ответа и пропускной способностью.
- [Availability and reliability](fundamentals/availability-and-reliability.md) — SLO, redundancy, recovery и graceful failure.
- [Consistency models](fundamentals/consistency-models.md) — freshness, coordination, conflicts и user-visible guarantees.

## Architecture & Design

Архитектурные блоки, которые чаще всего становятся основой production-систем.

- [API design](architecture-design/api-design.md) — контракты, backward compatibility, pagination и idempotency.
- [Load balancing](architecture-design/load-balancing.md) — распределение трафика, health checks и failover.
- [Caching strategy](architecture-design/caching-strategy.md) — cache-aside, TTL, invalidation и hot keys.
- [Storage selection](architecture-design/storage-selection.md) — выбор primary store, индексов и read models.
- [Data partitioning](architecture-design/data-partitioning.md) — sharding, routing и rebalancing.
- [Replication strategy](architecture-design/replication-strategy.md) — replicas, lag, failover и read consistency.
- [Queues and streams](architecture-design/queues-and-streams.md) — async processing, ordering и consumer groups.
- [Rate limiting](architecture-design/rate-limiting.md) — защита shared resources и fair usage.

## Production & Operations

Жизнь системы после запуска: наблюдаемость, релизы и восстановление.

- [Observability](production-operations/observability.md) — metrics, logs, traces и actionable dashboards.
- [Deployment strategy](production-operations/deployment-strategy.md) — rolling, blue-green, canary и rollback.
- [Incident response](production-operations/incident-response.md) — detection, triage, mitigation и postmortem.

## Advanced

Продвинутые решения, которые нужны не каждой системе, но сильно влияют на архитектуру при росте масштаба.

- [Distributed transactions](advanced/distributed-transactions.md) — coordination, sagas и transactional outbox.
- [Multi-region architecture](advanced/multi-region-architecture.md) — geo-replication, failover и data residency.

## Learning path

1. Прочитать [System design principles](fundamentals/system-design-principles.md), чтобы договориться о языке.
2. Сделать rough numbers через [Capacity estimation](fundamentals/capacity-estimation.md).
3. Разобрать latency, availability и consistency через fundamentals.
4. Выбрать storage, traffic и async blocks через architecture-design.
5. Добавить observability, deployment и incident workflow.
6. Только после этого рассматривать advanced-паттерны.

## Формат заметок

Паттерны описываются по схеме: проблема, решение, tradeoffs, когда применять, когда не применять, связанные материалы.

