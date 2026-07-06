---
title: Domain-Driven Design: Tackling Complexity in the Heart of Software (领域驱动设计)
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2010-Eric-%E9%A2%86%E5%9F%9F%E9%A9%B1%E5%8A%A8%E8%AE%BE%E8%AE%A1%EF%BC%9A%E8%BD%AF%E4%BB%B6%E6%A0%B8%E5%BF%83%E5%A4%8D%E6%9D%82%E6%80%A7%E5%BA%94%E5%AF%B9%E4%B9%8B%E9%81%93.pdf
type: book
category: sources
tags: [architecture, software-design, book]
added: 2026-07-06
status: new
---

# Domain-Driven Design: Tackling Complexity in the Heart of Software (领域驱动设计)

Eric Evans, 2010.

Оригинальная DDD-книга: ubiquitous language, bounded contexts, entities, value objects, aggregates, domain events.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Извлечённые концепции

Из книги извлечены и оформлены как canonical-заметки в `patterns/architecture-design/`:

- [Ubiquitous Language](../../patterns/architecture-design/ubiquitous-language.md) — единый язык в bounded context
- [Bounded Context](../../patterns/architecture-design/bounded-context.md) — границы модели
- [Entities](../../patterns/architecture-design/entities.md) — объекты с identity
- [Value Objects](../../patterns/architecture-design/value-objects.md) — иммутабельные объекты, определённые атрибутами
- [Aggregates](../../patterns/architecture-design/aggregates.md) — кластеры Entity + VO с root и инвариантами
- [Repositories](../../patterns/architecture-design/repositories.md) — абстракция хранения агрегатов
- [Domain Services](../../patterns/architecture-design/domain-services.md) — stateless доменные операции
- [Domain Events](../../patterns/architecture-design/domain-events.md) — события предметной области
- [Strategic Design](../../patterns/architecture-design/strategic-design.md) — context map и отношения между BC
- [Anti-Corruption Layer](../../patterns/architecture-design/anti-corruption-layer.md) — защита модели
- [Layered Architecture](../../patterns/architecture-design/layered-architecture.md) — слои: UI, Application, Domain, Infrastructure
- [Supple Design](../../patterns/architecture-design/supple-design.md) — intention-revealing interfaces, side-effect-free functions
- [Distillation](../../patterns/architecture-design/distillation.md) — core domain vs generic vs supporting
- [Large-Scale Structure](../../patterns/architecture-design/large-scale-structure.md) — system metaphors, evolving order

## Статус

Добавлено: 2026-07-06
