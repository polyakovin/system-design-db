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

### Clean Architecture (Robert C. Martin)

Паттерны из книги "Clean Architecture" (2017) — концентрические круги, dependency rule, компонентный дизайн.

- [Clean Architecture](architecture-design/clean-architecture.md) — концентрические круги, Dependency Rule, screaming architecture, архитектура vs фреймворк.
- [SOLID Architecture Principles](architecture-design/solid-architecture-principles.md) — SRP/OCP/LSP/ISP/DIP на уровне компонентов и сервисов.
- [Component Cohesion and Coupling](architecture-design/component-cohesion-coupling.md) — REP/CCP/CRP (cohesion) и ADP/SDP/SAP (coupling), метрики устойчивости.
- [Architectural Boundaries](architecture-design/architectural-boundaries.md) — boundary crossing, plugin architecture, presenters, Humble Object.
- [Use Case Driven Design](architecture-design/use-case-driven-design.md) — use cases как оркестраторы, input/output порты, тестирование без фреймворков.
- [Database as a Detail](architecture-design/database-as-detail.md) — БД как деталь, модель данных определяет схему, не наоборот.
- [Web as a Detail](architecture-design/web-as-detail.md) — веб как I/O устройство, UI-независимые use cases, presenter + ViewModel.

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

#### Practical DDD (Vaughn Vernon, 2013)

Дополнения из "Implementing Domain-Driven Design" — практическая реализация, детали инфраструктуры и новые паттерны.

- [CQRS](architecture-design/cqrs.md) — разделение command и query моделей, tradeoffs
- [Event Sourcing](architecture-design/event-sourcing.md) — event store, перестройка состояния, snapshots
- [Domain-Driven UI](architecture-design/domain-driven-ui.md) — task-based UI, presentation model
- [Testing DDD](architecture-design/testing-ddd.md) — тестирование агрегатов, событий, use cases

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

### Enterprise Application Architecture (Martin Fowler, 2002)

Паттерны из книги "Patterns of Enterprise Application Architecture" — domain logic, data source, web presentation, concurrency, distribution.

- [Domain Model vs Transaction Script](architecture-design/domain-model-vs-transaction-script.md) — выбор способа организации бизнес-логики
- [Table Module vs Active Record](architecture-design/table-module-vs-active-record.md) — альтернативы Domain Model средней сложности
- [Data Source Patterns](architecture-design/data-source-patterns.md) — Table Data Gateway, Row Data Gateway, Data Mapper
- [Object-Relational Patterns](architecture-design/object-relational-patterns.md) — Unit of Work, Identity Map, Lazy Load
- [MVC Pattern Decomposition](architecture-design/mvc-pattern-decomposition.md) — MVC, MVP, MVVM, Presentation Model
- [Page Controller vs Front Controller](architecture-design/page-controller-vs-front-controller.md) — два подхода к обработке запросов
- [Application Controller](architecture-design/application-controller.md) — централизованная логика навигации и flow
- [Session State](architecture-design/session-state.md) — Client, Server, Database-backed сессии
- [Distribution Patterns](architecture-design/distribution-patterns.md) — Remote Facade, Data Transfer Object
- [Offline Concurrency](architecture-design/offline-concurrency.md) — pessimistic/optimistic lock, бизнес-транзакции

## Learning path

1. Прочитать [System design principles](fundamentals/system-design-principles.md), чтобы договориться о языке.
2. Сделать rough numbers через [Capacity estimation](fundamentals/capacity-estimation.md).
3. Разобрать latency, availability и consistency через fundamentals.
4. Выбрать storage, traffic и async blocks через architecture-design.
5. Добавить observability, deployment и incident workflow.
6. Только после этого рассматривать advanced-паттерны.

## Формат заметок

Паттерны описываются по схеме: проблема, решение, tradeoffs, когда применять, когда не применять, связанные материалы.

