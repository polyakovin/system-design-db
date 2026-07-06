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

## Связанные материалы

- [Ubiquitous Language](ubiquitous-language.md) — язык привязан к контексту
- [Strategic Design](strategic-design.md) — context map: отношения между BC
- [Anti-Corruption Layer](anti-corruption-layer.md) — защита BC от чужой модели
- [Domain Events](domain-events.md) — интеграция между BC через события
