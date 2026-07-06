---
title: Patterns, Principles, and Practices of Domain-Driven Design
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2015-Scott-Patterns,%20Principles,%20and%20Practices%20of%20Domain%20Driven%20Design.pdf
type: book
category: sources
tags: [architecture, software-design, book]
added: 2026-07-06
status: ingested
---

# Patterns, Principles, and Practices of Domain-Driven Design

Scott Millett, 2015.

Большой справочник по DDD-паттернам с примерами: от стратегического дизайна до тактических реализаций и интеграций. Фокус на практическом применении и организационном масштабировании DDD.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Статус

Добавлено: 2026-07-06

## Извлечённые заметки (2026-07-06)

- [Tactical Decision Framework](../../patterns/architecture-design/tactical-decision-framework.md) — как выбирать между Entity, Value Object, Aggregate, Domain Service
- [Process-Driven Architecture](../../patterns/architecture-design/process-driven-architecture.md) — DDD + бизнес-процессы, Sagas, Process Managers
- [CQRS (Millett's tradeoffs)](../../patterns/architecture-design/cqrs.md) — практические трейд-оффы, CQRS lite, антипаттерны
- [Event-Driven Architecture Patterns](../../patterns/architecture-design/event-driven-architecture-patterns.md) — event vs command, event chains, idempotent consumers
- [DDD Organization Scaling](../../patterns/architecture-design/ddd-organization-scaling.md) — Conway's Law, team structure, domain governance
- [DDD and Microservices](../../patterns/architecture-design/ddd-microservices-and-distributed-systems.md) — BC как граница сервиса, sagas, eventual consistency
- [Legacy Integration Patterns](../../patterns/architecture-design/legacy-integration-patterns.md) — Strangler Fig, ACL implementation, CDC
- [Bounded Context Communication](../../patterns/architecture-design/bounded-context-communication.md) — Published Language, Open-Host Service, consumer-driven contracts
- [Domain Event Versioning](../../patterns/architecture-design/domain-event-versioning.md) — upcasters, schema registry, compatibility matrix

## Покрытие относительно Evans/Vernon

Millett добавляет то, что слабо освещено в существующих заметках:
- Decision-making framework для тактических паттернов
- Процессно-ориентированная архитектура (а не только структурная)
- Масштабирование DDD на организацию (governance, команды, Conway's Law)
- Практические паттерны интеграции (Strangler Fig, CDC, consumer-driven contracts)
- Коммуникация между BC (Published Language слои, OHS implementation)
- Версионирование событий и управление эволюцией схем
