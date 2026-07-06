---
title: Clean Architecture: A Craftsman's Guide
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2017-Martin%20Fowler-Clean%20Architecture%20A%20Craftsman's%20Guide.pdf
type: book
category: sources
tags: [architecture, software-design, book]
added: 2026-07-06
status: new
---

# Clean Architecture: A Craftsman's Guide

Robert C. Martin, 2017.

Универсальные правила архитектуры: разделение ответственности через концентрические круги, правило зависимостей, компонентные принципы кохезии и coupling, границы и плагин-архитектура.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Извлечённые концепции

Все концепции разнесены в `patterns/architecture-design/`:

- [Clean Architecture](../../patterns/architecture-design/clean-architecture.md) — концентрические круги (Entities → Use Cases → Adapters → Frameworks), Dependency Rule, screaming architecture, архитектура vs фреймворк.
- [SOLID Architecture Principles](../../patterns/architecture-design/solid-architecture-principles.md) — SRP на уровне компонентов, OCP и плагин-архитектура, LSP для сервисов/API, ISP для зависимостей данных, DIP как фундамент.
- [Component Cohesion and Coupling](../../patterns/architecture-design/component-cohesion-coupling.md) — REP, CCP, CRP (принципы кохезии) + ADP, SDP, SAP (принципы coupling), метрики Instability/Abstractness, Main Sequence.
- [Architectural Boundaries](../../patterns/architecture-design/architectural-boundaries.md) — boundary crossing через DIP, plugin architecture, presenters и Humble Object pattern, partial boundaries.
- [Use Case Driven Design](../../patterns/architecture-design/use-case-driven-design.md) — use cases как оркестратор бизнес-логики, input/output порты, тестирование без фреймворков, delivery-agnostic интеракторы.
- [Database as a Detail](../../patterns/architecture-design/database-as-detail.md) — модель данных определяет БД, а не наоборот; repository как граница; ORM как инструмент, не архитектура.
- [Web as a Detail](../../patterns/architecture-design/web-as-detail.md) — веб как I/O устройство; UI-независимые use cases; presenter + ViewModel разделение.

## Статус

Добавлено: 2026-07-06
Распаковано: 2026-07-06
