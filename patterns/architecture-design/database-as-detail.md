---
title: Database as a Detail
type: pattern
category: architecture
tags: [database, detail, orm, repository, data-model, clean-architecture]
source: Clean Architecture (Robert C. Martin, 2017)
added: 2026-07-06
---

# Database as a Detail

## Проблема

База данных диктует модель данных приложения. Таблицы = entities, JOIN'ы = бизнес-правила, миграции = изменения архитектуры. Смена БД = переписывание всего. ORM просачивается в домен — аннотации `@Entity`, `@Column` на бизнес-классах.

## Решение

**База данных — деталь.** Модель данных определяется архитектурой, а не БД-схемой.

### Data Model drives Database, not vice versa

- Структуры данных определяются бизнес-потребностями (use cases, entities), а не нормализацией или ORM-конвенциями.
- БД-схема — отражение модели данных, адаптированное под конкретную СУБД. Схема подстраивается под модель, а не наоборот.
- Entities в доменном слое — plain objects без аннотаций ORM. Никаких `@Entity`, `@Table`, `@Column`.

### Repository как граница

Repository — интерфейс, определённый в слое use cases. Реализация — во внешнем слое:

```
UseCase → OrderRepository (interface) ← PostgresOrderRepository
```

- Use case вызывает `orderRepo.save(order)` — не знает, Postgres это или in-memory.
- Переход на MongoDB: новая реализация интерфейса — и всё. Use cases не меняются.
- Уровень изоляции, схема партицирования, индексы — детали в infrastructure-слое, невидимые бизнес-логике.

### ORM — инструмент, не архитектура

ORM не должен диктовать модель данных. Бизнес-объекты не должны знать об ORM.

- **Gateway pattern**: ORM используется внутри репозитория. Entities — plain classes. Репозиторий мапит между ORM-entity и business-entity на границе.
- Если ORM просочился в use cases (ленивая загрузка, flush, транзакции на уровне бизнес-логики) — архитектура нарушена.

### Почему БД — деталь

- БД — технология доступа к данным. Данные важны, способ хранения — нет.
- СУБД выбирается под нефункциональные требования (latency, throughput, durability), а не под структуру данных.
- Бизнес-правила живут дольше БД. БД меняют (с Postgres на Cassandra, с SQL на файлы), бизнес-логика остаётся.

## Tradeoffs

- Репозиторий с маппингом добавляет код. Для простых CRUD — перебор.
- Полный отказ от возможностей СУБД (специфичные индексы, stored procedures) в пользу абстракции может дать просадку производительности.
- На практике не каждая смена БД безболезненна — гарантии транзакций, модель консистентности различаются. Repository защищает код, но не данные.

## Связанные материалы

- [Clean Architecture](clean-architecture.md) — БД как внешний круг
- [Architectural Boundaries](architectural-boundaries.md) — репозиторий как boundary crossing
- [Use Case Driven Design](use-case-driven-design.md) — use cases с репозиторием
- [Web as a Detail](web-as-detail.md) — симметричная идея для UI
- [Repositories](repositories.md) — DDD-репозиторий
- [Storage Selection](storage-selection.md) — выбор хранилища
- [Clean Architecture](../../sources/books/clean-architecture.md) — книга-источник, глава 27 (Services: Great and Small) и 30 (Database is a Detail)
