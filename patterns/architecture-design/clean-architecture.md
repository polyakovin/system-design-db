---
title: Clean Architecture
type: pattern
category: architecture
tags: [clean-architecture, dependency-rule, use-cases, entities, hexagonal, ports-and-adapters]
source: Clean Architecture (Robert C. Martin, 2017)
added: 2026-07-06
---

# Clean Architecture

## Проблема

Фреймворки, БД и UI просачиваются в бизнес-логику. Изменение БД ломает use cases. Смена веб-фреймворка требует переписывания всего приложения. Архитектура системы говорит «Spring + Postgres + React», а не «система управления заказами».

## Решение

Clean Architecture разделяет систему на концентрические круги с жёстким правилом зависимостей.

### Концентрические круги (изнутри наружу)

```
  ┌──────────────────────────────────────┐
  │          Frameworks & Drivers        │
  │  ┌────────────────────────────────┐  │
  │  │     Interface Adapters         │  │
  │  │  ┌──────────────────────────┐  │  │
  │  │  │   Application (Use Cases)│  │  │
  │  │  │  ┌────────────────────┐  │  │  │
  │  │  │  │     Entities       │  │  │  │
  │  │  │  │  (Enterprise       │  │  │  │
  │  │  │  │   Business Rules)  │  │  │  │
  │  │  │  └────────────────────┘  │  │  │
  │  │  └──────────────────────────┘  │  │
  │  └────────────────────────────────┘  │
  └──────────────────────────────────────┘
```

- **Entities (Enterprise Business Rules)** — объекты с критически важными бизнес-правилами. Не зависят ни от чего. Могут быть классами или модулями с методами. Самые стабильные, меняются только при изменении бизнеса.
- **Use Cases (Application Business Rules)** — оркестрируют поток данных между entities и внешними адаптерами. Определяют входные/выходные порты (`InputPort`, `OutputPort`). Не знают о БД, UI, HTTP.
- **Interface Adapters** — конвертируют данные между use cases и внешним миром. Presenters, Controllers, Gateways, Repositories. Преобразуют форматы данных, но не содержат бизнес-логики.
- **Frameworks & Drivers** — внешний слой: веб-фреймворки, БД, UI-библиотеки. Код здесь должен быть минимальным «клеем».

### The Dependency Rule

**Source code dependencies must point only inward.** Ничто во внутреннем круге не знает о чём-то во внешнем. Имена внешних кругов (типы, функции, модули) не упоминаются внутри.

```
Entities ← Use Cases ← Interface Adapters ← Frameworks & Drivers
```

Пересечение границ происходит через **интерфейсы и Dependency Inversion**: внешний круг реализует интерфейс, определённый во внутреннем. Use Case определяет `OrderRepository` (интерфейс); внешний слой предоставляет `PostgresOrderRepository` (реализацию).

### Use Case Interactors

Use case — это объект с единственным методом `execute(input): output`. Он:
- Принимает входные данные через `InputPort`
- Загружает entities через репозитории
- Вызывает бизнес-методы entities
- Отправляет результат через `OutputPort` (presenter)
- Не знает, кто его вызвал: HTTP-контроллер, CLI или тест

### Screaming Architecture

Архитектура должна **кричать о предметной области**, а не о фреймворках. Первый взгляд на структуру проекта должен отвечать на вопрос «что это за система?», а не «на чём она написана?».

- *Плохо*: `controllers/`, `models/`, `views/` — кричит «это MVC».
- *Хорошо*: `orders/`, `inventory/`, `shipping/` — кричит «это система управления заказами».

Фреймворк — деталь реализации, отложи решение о фреймворке насколько возможно.

### Architecture vs Framework

Фреймворки — **плагины** к бизнес-логике, а не её основа. Хорошая архитектура позволяет:
- Отложить выбор фреймворка до момента, когда информации достаточно
- Заменить фреймворк без переписывания бизнес-логики
- Тестировать use cases без запуска фреймворка (Spring, Rails, etc.)

### Decoupled Communication

Entities и use cases **не знают о БД и UI**. Use case вызывает `OrderRepository.findById(id)`, но не знает, реализован ли репозиторий через Postgres, in-memory store или REST API.

Коммуникация между слоями происходит через простые структуры данных (DTOs, request/response models), понятные обоим слоям, но не навязывающие детали реализации.

## Tradeoffs

- **Плюсы**: независимость от фреймворков, тестируемость без инфраструктуры, замена БД/UI без изменения бизнес-логики, отложенные решения.
- **Минусы**: indirection, больше файлов/классов, overhead для простых CRUD-систем. Не применяй слепо — оцени соотношение сложности системы и цены абстракции.

## Когда применять

- Система с нетривиальной бизнес-логикой, которая переживёт несколько фреймворков/БД.
- Долгоживущие продукты, где стоимость замены инфраструктуры высока.

## Когда не применять

- Простые CRUD-приложения с минимальной бизнес-логикой.
- Прототипы, скрипты, одноразовые утилиты.

## Связанные материалы

- [SOLID Architecture Principles](solid-architecture-principles.md) — основа dependency rule
- [Architectural Boundaries](architectural-boundaries.md) — пересечение границ, плагины
- [Use Case Driven Design](use-case-driven-design.md) — use cases как ядро
- [Database as a Detail](database-as-detail.md)
- [Web as a Detail](web-as-detail.md)
- [Layered Architecture](layered-architecture.md) — DDD-взгляд на слои
- [Boundaries](../../patterns/code-quality/boundaries.md) — чистые границы с third-party кодом
- [Clean Architecture](../../sources/books/clean-architecture.md) — книга-источник
