---
title: 架构漫谈 (Chatting About Architecture)
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2016-%E6%9E%B6%E6%9E%84%E5%B8%88-%E6%9E%B6%E6%9E%84%E6%BC%AB%E8%B0%88.pdf
type: book
category: sources
tags: [architecture, software-design, book]
added: 2026-07-06
status: ingested
---

# 架构漫谈 (Chatting About Architecture)

架构师 (Architect), 2016.

Китайские эссе по архитектуре: эволюция архитектур, микросервисы, SOA, REST, анализ trade-off, governance, архитектурный долг.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Статус

Добавлено: 2026-07-06
Ingested: 2026-07-06

## Извлечённые заметки (2026-07-06)

- [Architecture Evolution](../../patterns/architecture-design/architecture-evolution.md) — монолит → SOA → микросервисы → Event-Driven, эволюция не революция
- [Architecture as Tradeoff](../../patterns/architecture-design/architecture-as-tradeoff.md) — непрерывный компромисс, нет идеальной архитектуры
- [REST Architectural Style](../../patterns/architecture-design/rest-architectural-style.md) — resource-oriented, stateless, uniform interface, HATEOAS
- [SOA vs Microservices](../../patterns/architecture-design/soa-vs-microservices.md) — различия, когда что выбирать, уроки SOA
- [API Design](../../patterns/architecture-design/api-design.md) — версионирование, backward compatibility, evolvability
- [Governance in Distributed Systems](../../patterns/architecture-design/governance-in-distributed-systems.md) — децентрализованное управление, fitness functions
- [Architectural Debt](../../patterns/architecture-design/architectural-debt.md) — архитектурные долги vs code-level debt
- [Architecture vs Design](../../patterns/architecture-design/architecture-vs-design.md) — стратегические vs тактические решения

### Дополнения к существующим заметкам

- [Managing Complexity](../../patterns/fundamentals/managing-complexity.md) — сложность от бизнеса и структуры команды
- [DDD Organization Scaling](../../patterns/architecture-design/ddd-organization-scaling.md) — Conway's Law как диагностический инструмент

## Покрытие относительно существующих источников

The Architect добавляет независимый взгляд на темы, слабо освещённые в Evans/Vernon/Millett/McConnell:
- Эволюция архитектур как непрерывный процесс (а не DDD-centric view)
- REST как архитектурный стиль (ограничения, свойства, when to use)
- SOA vs Microservices — детальный сравнительный анализ
- API design — practical versioning, backward compatibility, evolvability
- Governance — децентрализованный подход, fitness functions
- Architectural debt — отличие от code-level debt, почему сложнее pay off
- Architecture vs Design — стратегические vs тактические решения
