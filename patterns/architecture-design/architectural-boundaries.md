---
title: Architectural Boundaries
type: pattern
category: architecture
tags: [boundaries, boundary-crossing, plugin-architecture, presenters, humble-object, adapters]
source: Clean Architecture (Robert C. Martin, 2017)
added: 2026-07-06
---

# Architectural Boundaries

## Проблема

Как разным слоям архитектуры взаимодействовать, не нарушая правило зависимостей? Как пересекать границу от use case к presenter, от интерактора к БД, сохраняя внутренний круг в неведении о внешнем?

## Решение

### Boundary Crossing через Dependency Inversion

Граница пересекается через **интерфейс**, определённый во внутреннем круге. Внешний круг реализует этот интерфейс.

```
  UseCase (внутренний круг)
     │ определяет
     ▼
  OrderRepository (interface)
     ▲
     │ реализует
  PostgresOrderRepository (внешний круг)
```

На уровне исходного кода: `import` идёт только от внешнего круга к внутреннему. Use case не импортирует класс БД.

### Plugin Architecture

Clean Architecture — это плагин-архитектура. Внешние слои — плагины к ядру:

- **DB — плагин** к use cases. Замени Postgres на MongoDB без изменения бизнес-логики.
- **Web UI — плагин**. Веб, CLI и настольное приложение могут использовать одни и те же use cases.
- **Тесты — плагин**. Тесты имитируют внешний слой и тестируют use cases напрямую.

Плагин подключается через интерфейс (API ядра) и не требует модификации ядра. Это архитектурный OCP в действии.

### Presenters и Humble Object Pattern

Presenter — это adapter, который преобразует выход use case в формат, пригодный для отображения.

**Humble Object Pattern**: отдели поведение от труднопроверяемого окружения.
- Behaviour (легко тестируемо): форматирование данных в ViewModel.
- Humble Object (трудно тестируемо): GUI, HTTP-handler, БД-драйвер.

Presenter содержит поведение (создаёт ViewModel — структуры с `String itemName`, `boolean isHighlighted`). View — humble object, который только отображает готовую ViewModel. Presenter тестируется юнит-тестами без GUI.

```
UseCase → OutputPort (interface) → Presenter → ViewModel → View (dumb)
```

### Partial Boundaries

Полноценная граница (интерфейс + реализация + раздельные компоненты) — дорого. Для более лёгких случаев:

- **Strategy pattern**: интерфейс определён, но реализация в том же компоненте. Границу можно «затвердить» позже.
- **Facade pattern**: один класс-фасад перед группой сервисов. Use case зависит от фасада, а не от десятка сервисов.
- **Пропустить последний шаг**: интерфейс и реализация в одном компоненте, но с чётким разделением по пакетам. Если граница понадобится — выделить в отдельный компонент.

### Уровни границ

Границы бывают разной силы:
- **Deployment boundary**: компоненты — отдельные jar/dll/gem.
- **Process boundary**: компоненты — отдельные процессы (локальные вызовы).
- **Service boundary**: компоненты — отдельные сервисы (сетевые вызовы).

Чем дальше граница, тем больше цена latency, сериализации, failure modes. Не строй service boundary там, где достаточно deployment boundary.

## Tradeoffs

- Границы имеют стоимость: создание интерфейсов, разделение на компоненты, overhead коммуникации.
- Решение «нарисовать границу сейчас» vs «подождать, пока она понадобится» — центральный архитектурный компромисс. YAGNI говорит ждать; риск — граница обойдётся дороже потом.
- Partial boundaries — прагматичный компромисс.

## Связанные материалы

- [Clean Architecture](clean-architecture.md) — полная картина
- [SOLID Architecture Principles](solid-architecture-principles.md) — DIP как механизм пересечения границ
- [Use Case Driven Design](use-case-driven-design.md) — как use cases определяют границы
- [Database as a Detail](database-as-detail.md) — БД как плагин
- [Web as a Detail](web-as-detail.md) — UI как плагин
- [Boundaries](../../patterns/code-quality/boundaries.md) — границы с third-party кодом
- [Clean Architecture](../../sources/books/clean-architecture.md) — книга-источник, Part V (Architecture)
