---
title: Implementing Domain-Driven Design
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2013-Vaughn-Implementing%20Domain%20Driven%20Design.pdf
type: book
category: sources
tags: [architecture, software-design, book, ddd, domain-driven-design]
added: 2026-07-06
status: processed
---

# Implementing Domain-Driven Design

Vaughn Vernon, 2013.

Практическое руководство по реализации DDD: стратегический и тактический дизайн, event sourcing, CQRS, интеграция bounded contexts, тестирование.

## Covered topics

- **Domains and Subdomains** (Ch 2–3): identifying core domain, supporting subdomains, generic subdomains
- **Strategic Design** (Ch 3): practical context mapping, sizing bounded contexts
- **Architecture** (Ch 4): layered architecture, ports and adapters, CQRS
- **Entities, Value Objects** (Ch 5–6): implementation patterns, identity generation, immutability
- **Domain Services** (Ch 7): stateless operations, when to use vs aggregate methods
- **Domain Events** (Ch 8): event model, publishing infrastructure, event store, outbox pattern
- **Modules** (Ch 9): packaging by domain concept, not by technical layer
- **Aggregates** (Ch 10): Vernon's 4 rules, consistency boundaries, reference by identity
- **Factories** (Ch 11): factory method vs standalone factory, producing valid aggregates
- **Repositories** (Ch 12): ORM vs hand-rolled, lazy vs eager, event-sourced repositories
- **Integrating Bounded Contexts** (Ch 13): RPC, REST, messaging, published language, separate ways
- **Application and UI** (Ch 14): application services, task-based UI, presentation model, testing

## Unpacked into

- [Aggregates](../../patterns/architecture-design/aggregates.md) — Vernon's 4 rules added
- [Bounded Context](../../patterns/architecture-design/bounded-context.md) — practical context sizing
- [CQRS](../../patterns/architecture-design/cqrs.md) — new note
- [Domain Events](../../patterns/architecture-design/domain-events.md) — implementation details added
- [Domain-Driven UI](../../patterns/architecture-design/domain-driven-ui.md) — new note
- [Event Sourcing](../../patterns/architecture-design/event-sourcing.md) — new note
- [Repositories](../../patterns/architecture-design/repositories.md) — implementation patterns added
- [Strategic Design](../../patterns/architecture-design/strategic-design.md) — practical integration patterns added
- [Testing DDD](../../patterns/architecture-design/testing-ddd.md) — new note

## Status

Добавлено: 2026-07-06. Обработано: 2026-07-06.
