---
title: Session State
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, session-state, client-session, server-session, database-session]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Session State

Где хранить состояние между HTTP-запросами (корзина, прогресс формы, аутентификация) — архитектурное решение с tradeoffs по масштабируемости, надёжности и времени разработки.

## Client Session State

Сериализовать состояние и отправить клиенту — cookie, hidden field, URL query, или JWT-токен в заголовке.

```
Клиент → [запрос + состояние] → Сервер → обработка → ответ
Клиент ← [ответ + обновлённое состояние] ← Сервер
```

**Когда:** состояние небольшое (< 4KB), легко сериализуется, не содержит sensitive данных (или зашифровано), stateless-серверы (микросервисы, serverless).

**Плюсы:** серверы stateless → легко масштабировать, нет sticky sessions, переживает перезагрузку сервера.

**Минусы:** размер ограничен, клиент может подделать состояние (нужна подпись/шифрование), данные ходят туда-сюда на каждом запросе.

## Server Session State

Сервер хранит состояние в памяти, клиент получает session ID (cookie). Классический подход: `req.session.cart = [...]`, `req.session.userId = 42`.

```
Клиент → [запрос + session_id] → Сервер → находит session в memory → обработка → ответ
```

**Когда:** средний размер состояния, нужен быстрый доступ, один сервер/регион или sticky sessions.

**Плюсы:** быстро (in-memory), любые структуры данных, безопасно (клиент видит только ID).

**Минусы:** sticky sessions или репликация между серверами, состояние теряется при перезагрузке и падении сервера, память сервера.

## Database Session State

Сервер хранит состояние в БД (или Redis). Клиент получает session ID. Каждый запрос загружает и сохраняет состояние в хранилище.

```
Клиент → [запрос + session_id] → Сервер → SELECT session → обработка → UPDATE session → ответ
```

**Когда:** кластер без sticky sessions, состояние должно пережить рестарты серверов, размер состояния больше чем комфортно держать в памяти или передавать клиенту.

**Плюсы:** stateless-серверы (хранилище общее), survive рестарты, масштабируется горизонтально.

**Минусы:** latency на загрузку/сохранение на каждый запрос, нагрузка на хранилище, serialization/deserialization overhead.

## Сравнение

| Критерий | Client | Server | Database |
|---|---|---|---|
| **Масштабируемость** | Отличная | Sticky или репликация | Хорошая (общее хранилище) |
| **Latency** | Низкая (нет доп. запросов) | Низкая (in-memory) | Средняя (I/O на каждый запрос) |
| **Надёжность** | Высокая (нет состояния на сервере) | Низкая (теряется при падении) | Высокая (persist в БД) |
| **Размер данных** | < 4KB | Без ограничений | Без ограничений |
| **Безопасность** | Нужна подпись/шифрование | Только ID на клиенте | Только ID на клиенте |

## Fowler's Decision Rule

> Client Session State — лучшее решение, если данные помещаются и не секретные. Stateless архитектура упрощает всё. Server/Database Session State — fallback для данных, которые не влезают или не должны покидать сервер.

## Связанные материалы

- [Offline Concurrency](offline-concurrency.md) — optimistic/pessimistic lock при долгих сессиях
- [Distribution Patterns](distribution-patterns.md) — Remote Facade, DTO
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — глава 6
