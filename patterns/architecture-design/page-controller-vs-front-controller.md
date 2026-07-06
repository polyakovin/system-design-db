---
title: Page Controller vs Front Controller
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, page-controller, front-controller, mvc, web]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Page Controller vs Front Controller

Два способа организовать обработку HTTP-запросов на сервере. Различаются местом и способом диспетчеризации.

## Page Controller

Каждая страница (URL) имеет свой контроллер. Один файл на страницу: `/orders/new` → `NewOrderController`, `/orders/list` → `ListOrdersController`.

```
GET /orders/new    → NewOrderController    → new_order.html
GET /orders/42     → ShowOrderController   → show_order.html
POST /orders       → CreateOrderController → redirect /orders/42
```

**Реализация:** ASP.NET Web Forms, старые PHP-приложения (один файл на страницу), CGI.

**Когда:** сайт с небольшим числом страниц, каждая страница уникальна, простая навигация, нет общей логики обработки запросов.

**Плюсы:** прямой mapping URL → код, легко понять, легко отлаживать, каждый контроллер независим.

**Минусы:** дублирование общей логики (parse request, error handling, auth) в каждом контроллере, сложно добавить cross-cutting behaviour.

## Front Controller

Все запросы проходят через единую точку входа, которая диспетчеризует их на handler'ы. Роутер внутри Front Controller'а определяет, какой handler вызвать.

```
GET  /orders/new    ─┐
GET  /orders/42     ─┤
POST /orders        ─┼→ Front Controller → Router → OrderHandler.new() / show() / create()
GET  /users/profile ─┘
```

**Реализация:** Spring DispatcherServlet, Laravel routing, Express.js middleware, Django URL dispatcher.

**Когда:** много страниц, нужна общая логика пред- и пост-обработки (auth, logging, CORS), pluggable handlers, REST API.

**Плюсы:** общая логика в одном месте (middleware, interceptors), единое конфигурирование, легко добавлять поведение глобально.

**Минусы:** сложнее отладка (запрос проходит через цепочку), overhead для простых случаев, «магия» route matching.

## Сравнение

| Критерий | Page Controller | Front Controller |
|---|---|---|
| **Точка входа** | Много (по одной на страницу) | Одна |
| **Cross-cutting logic** | Дублируется | Централизована (middleware) |
| **Mapping URL → handler** | Структура файлов = URL | Router config (regex, annotations) |
| **Простота понимания** | Высокая | Средняя (цепочка обработки) |
| **Гибкость** | Низкая | Высокая |
| **Современный выбор** | Почти не используется | Де-факто стандарт |

## Base Controller Pattern

Промежуточное решение: общий базовый класс для Page Controller'ов, куда выносится общая логика. ASP.NET MVC Controller, Spring @Controller — по сути Front Controller, но с удобным базовым классом для handler'ов.

## Связанные материалы

- [Application Controller](application-controller.md) — централизованная логика навигации
- [MVC Pattern Decomposition](mvc-pattern-decomposition.md)
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — глава 14
