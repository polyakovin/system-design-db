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

### Domain-Driven Design (DDD)

Паттерны из книги Eric Evans "Domain-Driven Design" (2010) — стратегический и тактический дизайн.

- [Ubiquitous Language](architecture-design/ubiquitous-language.md) — единый язык команды и кода
- [Bounded Context](architecture-design/bounded-context.md) — границы модели
- [Entities](architecture-design/entities.md) — объекты с непрерывной identity
- [Value Objects](architecture-design/value-objects.md) — иммутабельные объекты, определённые атрибутами
- [Aggregates](architecture-design/aggregates.md) — кластеры Entity + VO с root и инвариантами
- [Repositories](architecture-design/repositories.md) — абстракция хранения агрегатов
- [Domain Services](architecture-design/domain-services.md) — stateless доменные операции
- [Domain Events](architecture-design/domain-events.md) — события предметной области
- [Strategic Design](architecture-design/strategic-design.md) — context map, отношения между BC
- [Anti-Corruption Layer](architecture-design/anti-corruption-layer.md) — защита модели от внешних систем
- [Layered Architecture](architecture-design/layered-architecture.md) — слои: UI, Application, Domain, Infrastructure
- [Supple Design](architecture-design/supple-design.md) — intention-revealing interfaces, side-effect-free functions
- [Distillation](architecture-design/distillation.md) — core domain vs generic vs supporting
- [Large-Scale Structure](architecture-design/large-scale-structure.md) — system metaphors, evolving order

## Production & Operations

Жизнь системы после запуска: наблюдаемость, релизы и восстановление.

- [Observability](production-operations/observability.md) — metrics, logs, traces и actionable dashboards.
- [Deployment strategy](production-operations/deployment-strategy.md) — rolling, blue-green, canary и rollback.
- [Incident response](production-operations/incident-response.md) — detection, triage, mitigation и postmortem.

## Advanced

Продвинутые решения, которые нужны не каждой системе, но сильно влияют на архитектуру при росте масштаба.

- [Distributed transactions](advanced/distributed-transactions.md) — coordination, sagas и transactional outbox.
- [Multi-region architecture](advanced/multi-region-architecture.md) — geo-replication, failover и data residency.

## Code Quality

Практики написания чистого, поддерживаемого кода — от именования до рефакторинга.

- [Meaningful names](code-quality/meaningful-names.md) — правила именования: intent, no disinformation, searchability.
- [Functions](code-quality/functions.md) — малые функции, single level of abstraction, no side effects, CQS.
- [Comments](code-quality/comments.md) — хорошие и плохие комментарии, код как документация.
- [Formatting](code-quality/formatting.md) — вертикальное и горизонтальное форматирование, командные правила.
- [Objects and data structures](code-quality/objects-and-data-structures.md) — Law of Demeter, data/object anti-symmetry.
- [Error handling](code-quality/error-handling.md) — exceptions over error codes, special case pattern.
- [Boundaries](code-quality/boundaries.md) — чистые границы с third-party кодом, learning tests.
- [Unit tests](code-quality/unit-tests.md) — F.I.R.S.T., three laws of TDD, clean test structure.
- [Classes](code-quality/classes.md) — организация классов, cohesion, SRP.
- [Systems](code-quality/systems.md) — separation of main, dependency injection, scaling up.
- [Emergence](code-quality/emergence.md) — правила простого дизайна (Kent Beck): tests, no duplication, intent, minimal.
- [Code smells](code-quality/code-smells.md) — каталог запахов: bloaters, change preventers, couplers, dispensables.

## Learning path

1. Прочитать [System design principles](fundamentals/system-design-principles.md), чтобы договориться о языке.
2. Сделать rough numbers через [Capacity estimation](fundamentals/capacity-estimation.md).
3. Разобрать latency, availability и consistency через fundamentals.
4. Выбрать storage, traffic и async blocks через architecture-design.
5. Добавить observability, deployment и incident workflow.
6. Только после этого рассматривать advanced-паттерны.

## Формат заметок

Паттерны описываются по схеме: проблема, решение, tradeoffs, когда применять, когда не применять, связанные материалы.

