---
title: Bounded Context
type: pattern
category: ddd
tags: [ddd, domain-driven-design, strategic-design, bounded-context, architecture]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Bounded Context

## Проблема

В большой системе одна и та же бизнес-сущность (Customer, Order, Product) означает разное для разных команд. Попытка создать единую каноническую модель приводит к раздутому монолиту, где каждое изменение ломает чужой код.

## Решение

Явно определить границы, внутри которых конкретная модель имеет однозначный смысл. Внутри Bounded Context действует свой [Ubiquitous Language](ubiquitous-language.md), своя модель данных и свои инварианты.

- Каждый BC владеет своим набором понятий — **один BC = одна команда** (в идеале).
- Модель вне контекста не обязана быть верной — важно, что она верна внутри.
- BC — это граница ответственности, а не граница сервиса (хотя часто совпадает с микросервисом).

## Пример

В e-commerce системе:
- **Sales BC:** `Order` — это заказ клиента с товарами, суммами и статусом оплаты.
- **Fulfillment BC:** `Order` — это задача на сборку со складскими локациями, весом и маршрутом доставки.
- **Billing BC:** `Order` — это финансовый документ с транзакциями, счетами и refund-ами.

Один и тот же термин — три разные модели. Объединение их в один `Order` класс создало бы God Object.

## Tradeoffs

Плюсы: автономия команд, независимая эволюция моделей, снижение coupling.
Минусы: дублирование данных, необходимость интеграции между BC, overhead на поддержку границ.

## Practical Context Sizing (Vaughan Vernon, Chapters 2–3)

### How to find bounded contexts

Vernon's practical techniques for identifying BC boundaries:

1. **Listen to language.** When the same word ("Customer", "Order") means different things in different conversations, you've found a context boundary. Each meaning belongs in its own BC.

2. **Business capability alignment.** Map BCs to business capabilities, not technical layers. "Catalog," "Pricing," "Shipping" are BCs; "Frontend," "Database" are not.

3. **Team topology.** One team owns one BC. If two sub-teams can't agree on a model, split the context.

4. **Start coarse, refine iteratively.** Vernon advises starting with larger contexts (5–10 for an enterprise system) and splitting them as understanding deepens. Over-splitting early creates unnecessary integration overhead.

### Sizing heuristics

- **Too big:** a single context that spans 3+ teams, or has 50+ aggregate types.
- **Too small:** a context with a single aggregate that has no business reason to exist independently (just split because you could).
- **Golden rule:** a BC is the size of one team's cognitive capacity to deeply understand the domain model.

### BC as a service boundary

Vernon notes that a BC often maps to a microservice, but he warns:
- A BC is a **model boundary**, not a deployment boundary.
- Multiple BCs can coexist in one monolith with strict package/module boundaries.
- A single BC can span multiple services if they share the same model.
- The deployment choice (monolith vs. microservice) is secondary to model integrity.

## Связанные материалы

- [Ubiquitous Language](ubiquitous-language.md) — язык привязан к контексту
- [Strategic Design](strategic-design.md) — context map: отношения между BC
- [Anti-Corruption Layer](anti-corruption-layer.md) — защита BC от чужой модели
- [Domain Events](domain-events.md) — интеграция между BC через события
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — главы 2–3 (Domains, Subdomains, Bounded Contexts)
