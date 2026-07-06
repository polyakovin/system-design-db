---
title: Application Controller
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, application-controller, flow-logic, navigation]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Application Controller

**Проблема:** логика навигации и потока экранов (wizard, multi-step form, onboarding) размазана по контроллерам отдельных страниц. Каждый контроллер знает, «куда идти дальше», и изменения flow требуют правок в нескольких местах.

**Решение:** Application Controller — централизованный объект, управляющий flow экранов и навигацией. Контроллеры страниц спрашивают у него, какой экран показывать следующим, вместо того чтобы содержать эту логику внутри себя.

```
Пользователь → Page Controller → Application Controller → next view
                                         ↑
                            flow logic: правила перехода,
                            условия, состояние wizard
```

## Структура

Application Controller содержит:
- **Состояние flow:** на каком шаге пользователь, что уже заполнено.
- **Правила перехода:** при каких условиях переходить на следующий экран.
- **Обработку команд:** какие действия доступны на каждом шаге.

```python
class CheckoutController:
    def __init__(self, app_controller: ApplicationController):
        self.flow = app_controller

    def handle_step(self, request):
        step = request.session.get("step", "shipping")
        if request.method == "POST":
            # Делегируем решение о следующем шаге Application Controller
            next_step = self.flow.get_next_step(step, request.POST)
            request.session["step"] = next_step
            return redirect(next_step)
        return render(f"checkout/{step}.html")

class ApplicationController:
    def get_next_step(self, current_step: str, data: dict) -> str:
        flows = {
            "shipping": lambda d: "payment" if d.get("address_valid") else "shipping",
            "payment":  lambda d: "review" if d.get("payment_ok") else "payment",
            "review":   lambda _: "confirmation",
        }
        handler = flows.get(current_step)
        return handler(data) if handler else current_step
```

## Когда применять

- Многошаговые формы (wizards, checkout, onboarding).
- Flow с ветвлениями (в зависимости от ответов пользователя — разные следующие экраны).
- Одинаковые правила навигации используются несколькими Page Controller'ами.
- Нужна централизованная обработка ошибок и retry flow.

## Когда не применять

- Простые CRUD (одна страница — одна операция, нет flow между страницами).
- Навигация простая и не меняется (links, меню).
- Single Page Application (SPA) — навигация на клиенте, Application Controller на фронтенде.

## Tradeoffs

**Плюсы:** flow-логика в одном месте, легко менять правила навигации, переиспользование между экранами, тестируется отдельно от UI.

**Минусы:** дополнительный слой, абстракция ради абстракции при простом flow, на SPA логика всё равно дублируется на клиенте для быстрой навигации.

## Связка с контроллерами

| Паттерн | Кто решает навигацию |
|---|---|
| **Page Controller без Application Controller** | Сам Page Controller (логика внутри) |
| **Page Controller + Application Controller** | Application Controller централизованно |
| **Front Controller** | Front Controller может содержать навигацию сам или делегировать Application Controller |

## Связанные материалы

- [Page Controller vs Front Controller](page-controller-vs-front-controller.md)
- [MVC Pattern Decomposition](mvc-pattern-decomposition.md)
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — глава 14
