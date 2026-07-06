---
title: Anti-Corruption Layer
type: pattern
category: ddd
tags: [ddd, domain-driven-design, strategic-design, integration, acl]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Anti-Corruption Layer

## Проблема

Интеграция с legacy-системой или внешним сервисом приносит чужую модель в ваш домен. Если позволить чужой модели «протечь» внутрь, она исказит ваш Ubiquitous Language и сломает инварианты.

## Решение

Anti-Corruption Layer (ACL) — изолирующий слой, который транслирует чужую модель в вашу. ACL находится на границе вашего Bounded Context и действует как фасад + адаптер + транслятор.

- **Translator:** преобразует данные между чужой и своей моделью.
- **Adapter:** адаптирует интерфейс legacy-системы под интерфейсы вашего домена.
- **Façade:** скрывает сложность внешней системы за простым API.

## Структура

```
[Your Domain Model] → [ACL] → [External System / Legacy]
                       ↑
                    Translator
                    Adapter
                    Façade
```

## Когда применять

- Интеграция с legacy-системой, которую нельзя изменить.
- Внешний сервис с плохой моделью, которая не вписывается в ваш домен.
- Защита нового зелёного поля от старой грязной модели.
- Когда цена искажения доменной модели выше, чем цена поддержки ACL.

## Когда НЕ применять

- Поставщик использует тот же Ubiquitous Language (Customer–Supplier).
- Вы — Conformist и принимаете чужую модель как есть.
- Интеграция настолько простая, что ACL переусложняет.

## Tradeoffs

Плюсы: защита доменной модели, изоляция изменений внешней системы.
Минусы: дополнительный код на поддержку, может стать узким местом производительности, риск устаревания трансляции.

## Связанные материалы

- [Bounded Context](bounded-context.md)
- [Strategic Design](strategic-design.md) — anti-corruption layer в context map
- [Domain Events](domain-events.md) — ACL часто используется для трансляции событий
- [Layered Architecture](layered-architecture.md) — ACL как часть infrastructure-слоя
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 14
