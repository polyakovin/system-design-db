---
title: Layered Architecture
type: pattern
category: ddd
tags: [ddd, domain-driven-design, architecture, layered-architecture, hexagonal-architecture]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Layered Architecture

## Проблема

Без явного разделения ответственности доменная логика рассеивается по UI-обработчикам, SQL-запросам и контроллерам. Изменение бизнес-правила требует правок в десятке файлов.

## Решение

Layered Architecture изолирует домен от инфраструктуры. Каждый слой зависит только от слоёв ниже. Домен — центр, инфраструктура — периферия.

## Слои (сверху вниз)

### User Interface (Presentation)
Взаимодействие с пользователем: HTTP контроллеры, CLI, веб-страницы. Не содержит бизнес-логики — только отображение и ввод.

### Application Layer
Оркестрация use cases. Координирует доменные объекты, транзакции, вызов репозиториев. **Не содержит доменной логики.** Типичный житель: `CreateOrderHandler`, `ApproveInvoiceUseCase`.

### Domain Layer
Сердце системы. Содержит [Entities](entities.md), [Value Objects](value-objects.md), [Aggregates](aggregates.md), [Domain Services](domain-services.md), [Domain Events](domain-events.md). **Не зависит ни от одного внешнего слоя.** Ноль зависимостей от БД, HTTP, UI.

### Infrastructure Layer
Реализация технических деталей: БД, message brokers, HTTP-клиенты, файловые системы. Реализует интерфейсы, определённые в domain-слое.

## Dependency Rule

```
UI → Application → Domain ← Infrastructure
                        ↑
                   (interfaces)
```

Infrastructure реализует Domain interfaces — инверсия зависимостей.

## Эволюция: от Layered к Hexagonal (Ports & Adapters)

Evans описывает классическую слоёную архитектуру, но современный DDD чаще использует Ports & Adapters:
- **Ports:** интерфейсы в domain-слое (Repository, EventBus).
- **Adapters:** реализации в infrastructure-слое (PostgresOrderRepository, RabbitMQEventBus).

## Tradeoffs

Плюсы: изоляция домена, тестируемость, замена инфраструктуры без изменения логики.
Минусы: boilerplate, indirection, overhead для простых CRUD-систем.

## PEAA: классическая трёхуровневая архитектура (Fowler, 2002)

Fowler описывает более простую версию — три слоя вместо четырёх:

1. **Presentation Layer** — UI, отображение данных, обработка пользовательского ввода. Не содержит бизнес-логики.
2. **Domain Layer** — бизнес-логика. Может быть реализована через [Domain Model](domain-model-vs-transaction-script.md), [Transaction Script](domain-model-vs-transaction-script.md), [Table Module](table-module-vs-active-record.md).
3. **Data Source Layer** — доступ к БД, файлам, внешним системам. Паттерны: [Table Data Gateway, Row Data Gateway, Data Mapper](data-source-patterns.md).

Ключевое правило: слой зависит только от слоя ниже. Presentation → Domain → Data Source. Domain не знает о Presentation, Data Source не знает о Domain.

Отличие от DDD-версии: нет отдельного Application Layer — оркестрация либо в Presentation (для простых случаев), либо в Domain (через Domain Model).

## Связанные материалы

- [Entities](entities.md) — живут в domain-слое
- [Repositories](repositories.md) — интерфейс в domain, реализация в infrastructure
- [Domain Services](domain-services.md)
- [Anti-Corruption Layer](anti-corruption-layer.md) — часть infrastructure-слоя
- [Domain Model vs Transaction Script](domain-model-vs-transaction-script.md) — выбор реализации domain-слоя
- [Data Source Patterns](data-source-patterns.md) — паттерны data source layer
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 4 (Isolating the Domain)
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 4 (Architecture)
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — глава 1 (Layering)
