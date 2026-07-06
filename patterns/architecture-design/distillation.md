---
title: Distillation
type: pattern
category: ddd
tags: [ddd, domain-driven-design, strategic-design, distillation, core-domain]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Distillation

## Проблема

Не все части системы одинаково важны для бизнеса, но команда тратит равные усилия на всё. Результат: core domain недоразвит, generic-части переинвестированы.

## Решение

Distillation — процесс отделения Core Domain от остальных частей и фокусировка усилий на самом важном.

## Три типа поддоменов

### Core Domain
То, что отличает бизнес от конкурентов. Сложные, уникальные бизнес-правила. Здесь нужны лучшие разработчики и максимальные инвестиции. Строится in-house — это не купить.

**Пример:** алгоритм ценообразования для страховой компании, matching engine для биржи.

### Supporting Subdomain
Поддерживает core domain, но не даёт конкурентного преимущества. Сложность умеренная, бизнес-специфичная. Можно разрабатывать in-house или отдать на аутсорс.

**Пример:** внутренний документооборот, onboarding сотрудников.

### Generic Subdomain
Стандартная функциональность, не уникальная для бизнеса. Используй готовое решение (SaaS, open-source) или купи. Не трать усилия на разработку.

**Пример:** аутентификация, биллинг (Stripe), email-рассылки.

## Процесс Distillation

1. Выдели Core Domain — спроси: «Если мы это уберём, бизнес умрёт?»
2. Для Generic — найди готовое решение.
3. Для Supporting — реши: build vs buy vs outsource.
4. Инвестируй лучших людей в Core Domain.

## Tradeoffs

Плюсы: оптимальное распределение ресурсов, фокус на конкурентном преимуществе.
Минусы: сложность классификации (поддомен может мигрировать со временем), политические сложности («почему моя часть — не core?»).

## Связанные материалы

- [Strategic Design](strategic-design.md) — context map показывает отношения между поддоменами
- [Bounded Context](bounded-context.md) — BC vs Subdomain: BC — пространство модели, Subdomain — пространство проблемы
- [Aggregates](aggregates.md) — core domain обычно содержит самые сложные агрегаты
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 15 (Distillation)
- [Learning Domain-Driven Design](../../sources/books/learning-domain-driven-design.md) — глава 1 (Analyzing Business Domains)
