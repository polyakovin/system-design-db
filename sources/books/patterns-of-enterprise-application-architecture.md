---
title: Patterns of Enterprise Application Architecture (企业应用架构模式)
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2006-Martin%20Fowler-%E4%BC%81%E4%B8%9A%E5%BA%94%E7%94%A8%E6%9E%B6%E6%9E%84%E6%A8%A1%E5%BC%8F.pdf
type: book
category: sources
tags: [architecture, software-design, book, fowler]
added: 2026-07-06
status: processed
---

# Patterns of Enterprise Application Architecture (企业应用架构模式)

Martin Fowler, 2002.

Каталог архитектурных паттернов для корпоративных приложений: слои, domain logic, data source, object-relational mapping, web presentation, concurrency, session state.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Разобранные концепции

### Domain Logic
- [Domain Model vs Transaction Script](../patterns/architecture-design/domain-model-vs-transaction-script.md) — когда использовать объектную модель, а когда процедурные скрипты
- [Table Module vs Active Record](../patterns/architecture-design/table-module-vs-active-record.md) — промежуточные паттерны между Transaction Script и Domain Model

### Data Source
- [Data Source Patterns](../patterns/architecture-design/data-source-patterns.md) — Table Data Gateway, Row Data Gateway, Data Mapper
- [Object-Relational Patterns](../patterns/architecture-design/object-relational-patterns.md) — Unit of Work, Identity Map, Lazy Load

### Presentation
- [MVC Pattern Decomposition](../patterns/architecture-design/mvc-pattern-decomposition.md) — MVC, MVP, MVVM, Presentation Model
- [Page Controller vs Front Controller](../patterns/architecture-design/page-controller-vs-front-controller.md) — два способа диспетчеризации запросов
- [Application Controller](../patterns/architecture-design/application-controller.md) — централизованное управление навигацией и flow

### Architecture
- [Layered Architecture](../patterns/architecture-design/layered-architecture.md) — PEAA-версия классической трёхуровневой архитектуры (Presentation, Domain, Data Source)

### Distribution & State
- [Session State](../patterns/architecture-design/session-state.md) — Client, Server, Database-backed session
- [Distribution Patterns](../patterns/architecture-design/distribution-patterns.md) — Remote Facade, Data Transfer Object

### Concurrency
- [Offline Concurrency](../patterns/architecture-design/offline-concurrency.md) — pessimistic/optimistic lock, implicit lock, business vs system transactions

## Статус

Добавлено: 2026-07-06
Обработано: 2026-07-06 — 11 концепций перенесены в patterns/architecture-design/
