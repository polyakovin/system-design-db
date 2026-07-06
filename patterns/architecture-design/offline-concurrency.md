---
title: Offline Concurrency
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, concurrency, optimistic-lock, pessimistic-lock, transactions]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Offline Concurrency

Offline concurrency — управление параллельным доступом к данным, когда бизнес-транзакция охватывает несколько запросов (edit form → save), а не укладывается в один SQL-запрос. В отличие от database-транзакций, бизнес-транзакция длится секунды или минуты.

## Pessimistic Lock (Pessimistic Offline Lock)

Блокировка строки данных на время всей бизнес-транзакции. Пока User A редактирует Order #42, User B не может его открыть на редактирование — получает ошибку.

```sql
-- Захват блокировки при открытии формы
UPDATE orders SET locked_by = 'user_A', locked_at = NOW()
WHERE id = 42 AND locked_by IS NULL;

-- Освобождение при сохранении/отмене
UPDATE orders SET locked_by = NULL, locked_at = NULL WHERE id = 42;
```

**Плюсы:** предотвращает конфликты до их возникновения, подходит когда конфликты частые и дорогие.

**Минусы:** плохо масштабируется (блокировки долгие), deadlocks, забытые блокировки (пользователь закрыл браузер), ухудшает user experience.

**Когда:** высокая вероятность конфликта, дорогой merge (юридический документ, финансовый отчёт), небольшое число пользователей.

## Optimistic Lock (Optimistic Offline Lock)

Блокировка не ставится. При сохранении проверяется, не изменил ли кто-то данные за время редактирования — через version-поле или timestamp.

```sql
-- Проверка при сохранении
UPDATE orders
SET status = 'paid', version = 3, updated_at = NOW()
WHERE id = 42 AND version = 2;  -- версия на момент открытия

-- Если rows_affected = 0 → кто-то изменил раньше → конфликт
```

**Плюсы:** не блокирует других пользователей, хорошо масштабируется, нет «забытых блокировок».

**Минусы:** конфликт обнаруживается поздно (пользователь уже потратил время на редактирование), merge/retry-логика на клиенте.

**Когда:** низкая вероятность конфликта, данные не критические для merge, много пользователей (веб-приложения).

## Implicit Lock

Фреймворк/ORM автоматически блокирует объекты, не требуя явных вызовов lock/unlock. Программист не пишет код блокировки, но должен понимать, когда она включается.

Hibernate: optimistic lock через `@Version`, включается автоматически. Pessimistic lock через `LockModeType.PESSIMISTIC_WRITE` в запросе.

**Плюсы:** меньше кода, меньше ошибок (забытая блокировка).

**Минусы:** «магия» — неочевидно, когда и что блокируется, сложнее диагностировать проблемы.

## Business Transactions vs System Transactions

| | System Transaction | Business Transaction |
|---|---|---|
| **Длительность** | Миллисекунды | Секунды — минуты |
| **Граница** | BEGIN … COMMIT | Несколько запросов + БД-транзакций |
| **Блокировка** | Pessimistic (БД-уровень) | Optimistic / Pessimistic (приложение) |
| **Atomicity** | Полная (rollback) | Частичная (компенсация) |

**Ключевой принцип:** нельзя держать БД-транзакцию открытой на время бизнес-транзакции (edit form → save). Это убивает пул соединений и производительность.

## Coarse-Grained Lock

Блокировка не одной строки, а группы связанных объектов (агрегата). Вместо блокировки каждого OrderLine отдельно — блокировка всего Order.

```sql
-- Блокировка всего агрегата, а не каждой строки
UPDATE orders SET locked_by = 'user_A' WHERE id = 42;
-- Не надо: UPDATE order_lines SET locked_by = 'user_A' WHERE order_id = 42;
```

## Связанные материалы

- [Object-Relational Patterns](object-relational-patterns.md) — Unit of Work, где живут эти блокировки
- [Session State](session-state.md) — где хранить состояние между запросами
- [Aggregates](aggregates.md) — DDD-агрегат как естественная граница блокировки
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 5, 7
