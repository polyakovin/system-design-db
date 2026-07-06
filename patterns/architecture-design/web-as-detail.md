---
title: Web as a Detail
type: pattern
category: architecture
tags: [web, ui, detail, io-device, presenters, clean-architecture]
source: Clean Architecture (Robert C. Martin, 2017)
added: 2026-07-06
---

# Web as a Detail

## Проблема

Веб-фреймворк диктует архитектуру приложения. Контроллеры содержат бизнес-логику. Use cases завязаны на HTTP-request/response объекты. Смена фронтенд-технологии или добавление CLI требует переписывания бизнес-логики.

## Решение

**Веб — это I/O устройство, деталь.** Бизнес-логика не знает о вебе.

### UI-независимые use cases

Use case получает входные данные в простых структурах, не в `HttpServletRequest`. Контроллер только извлекает данные из HTTP и передаёт в use case:

```
HTTP Request → Controller (извлекает данные) → PlaceOrderInput → UseCase
```

- Контроллер — тонкий, без бизнес-логики: парсинг, валидация формата, вызов use case.
- Use case не знает, откуда пришёл запрос: HTTP, CLI, очередь сообщений, тест.
- Добавление CLI к существующему веб-приложению = новый контроллер, тот же use case.

### Presenter: отделение логики отображения от UI

Presenter готовит ViewModel для View. View — humble object, тупой рендеринг:

```
UseCase → OutputPort(interface) → Presenter → ViewModel → View (React, HTML, CLI)
```

- **ViewModel**: структуры данных, готовые к отображению (`String dateFormatted`, `boolean isDisabled`, `List<MenuItem>`). Никакой логики.
- **Presenter**: принимает OutputData use case, создаёт ViewModel. Тестируется без браузера.
- **View**: получает ViewModel и рендерит. Может быть React-компонентом, HTML-шаблоном, CLI-форматтером. Содержит ноль бизнес-логики.

### Фронтенд как плагин

Веб-интерфейс — плагин к ядру. Замени React на Vue, добавь мобильное приложение, CLI — core (use cases) не меняется.

Фреймворки (Spring MVC, Rails, Express) — в самом внешнем круге. Код в них — тонкая обёртка.

### Тестирование без веба

- Use cases тестируются без HTTP-сервера: подставь fake-презентер, проверь ViewModel.
- Presenter тестируется как unit: входные данные → assert на ViewModel.
- View тестируется отдельно: snapshot-тесты, компонентные тесты — без бизнес-правил.

## Tradeoffs

- Presenter + ViewModel — дополнительный слой для систем, где UI логика тривиальна.
- Full separation UI от бизнес-логики требует дисциплины; в маленьких проектах проще вызвать `orderService.placeOrder()` прямо из контроллера.
- SPA с толстым клиентом требует дублирования валидации на клиенте и сервере — это нормально, два разных trust boundary.

## Связанные материалы

- [Clean Architecture](clean-architecture.md) — UI как внешний круг
- [Architectural Boundaries](architectural-boundaries.md) — presenters как adapter
- [Use Case Driven Design](use-case-driven-design.md) — UI-независимые interactors
- [Database as a Detail](database-as-detail.md) — симметричная идея для БД
- [Layered Architecture](layered-architecture.md) — DDD-слои (Presentation layer)
- [Clean Architecture](../../sources/books/clean-architecture.md) — книга-источник, главы 23, 31
