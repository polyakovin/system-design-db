---
title: MVC Pattern Decomposition
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, mvc, model-view-controller, mvp, mvvm, presentation-model]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# MVC Pattern Decomposition

Семейство паттернов для организации Presentation Layer. Все решают одну задачу: отделить бизнес-логику от отображения, чтобы их можно было изменять независимо.

## Model View Controller (MVC)

Классический MVC (Smalltalk, 1979).

```
       ┌──────────┐
       │   Model   │ ← данные и бизнес-логика
       └─────┬─────┘
             │ notifies (Observer)
      ┌──────┴──────┐
      │    View     │ ← отображение, слушает Model
      └──────┬──────┘
             │ user input
      ┌──────┴──────┐
      │ Controller  │ ← обрабатывает ввод, меняет Model
      └─────────────┘
```

- **Model:** данные, бизнес-логика, state. Не знает о View и Controller.
- **View:** отображает Model, подписывается на изменения Model (Observer pattern).
- **Controller:** обрабатывает пользовательский ввод (клики, нажатия), изменяет Model. Не содержит логики отображения.

**Ключевое:** разделение View и Controller: View — только вывод, Controller — только ввод. Observer связывает Model → View (при изменении Model View обновляется автоматически).

**Web MVC (Fowler's adaptation):**

В вебе Observer не работает (HTTP — request/response, нет постоянного соединения). Поэтому web-MVC вырождается:

```
Request → Controller → Model → View (render)
```

Controller получает запрос, дёргает Model, передаёт данные в View для рендеринга. View больше не подписывается на Model — данные передаются явно.

## Model View Presenter (MVP)

Эволюция MVC для UI с rich widget'ами (Windows Forms, Swing, GWT).

```
       ┌──────────┐
       │   Model   │
       └─────┬─────┘
             │
       ┌─────┴──────────┐
       │   Presenter     │ ← вся логика: и ввода, и отображения
       └─────┬───────────┘
             │ interface (IView)
       ┌─────┴─────┐
       │    View    │ ← пассивная: только рендеринг, делегирует всё Presenter'у
       └───────────┘
```

- **Presenter:** вся презентационная логика (что показать, как реагировать на ввод). Не зависит от конкретного UI-фреймворка — общается с View через интерфейс `IView`.
- **View:** пассивная — только отрисовка. Presenter говорит View: «покажи это», «включи кнопку». View сообщает Presenter: «пользователь кликнул сюда».

**Отличие от MVC:** Presenter содержит и логику ввода, и логику отображения (что контроллер, что view-логика в одном месте). View полностью пассивна — максимум data binding.

**Supervising Controller:** вариант MVP, где View берёт на себя простой data binding, а Presenter — только сложную логику.

## Model View ViewModel (MVVM)

Эволюция MVP для платформ с мощным data binding (WPF, Silverlight, современные JS-фреймворки: Vue, Angular).

```
Model ↔ ViewModel ↔ View (data binding)
```

- **ViewModel:** Model, адаптированная для конкретного View. Содержит свойства, команды, computed values. **Не знает о View** — только данные и поведение, к которым View биндится.
- **View:** декларативное описание UI + data binding к ViewModel. Минимум кода.

**Отличие от MVP:** ViewModel не знает о View (нет IView-интерфейса). View привязывается к ViewModel через декларативный data binding.

## Presentation Model (Fowler)

То же, что MVVM, но под другим названием. Fowler описал в 2004, Microsoft популяризовала как MVVM в 2005. Presentation Model = ViewModel.

## Сравнение

| | Model View Controller | Model View Presenter | Model View ViewModel |
|---|---|---|---|
| **View знает о модели?** | Да (Observer) | Нет (через Presenter) | Нет (через ViewModel) |
| **Presenter/VM знает о View?** | Контроллер знает | Да (через IView) | Нет (только data) |
| **Data binding** | Нет (ручное обновление) | Частично (Supervising) | Основной механизм |
| **Тестируемость логики** | Средняя | Высокая (IView mock) | Высокая (нет View) |
| **Где применяется** | Web (Rails, Django, Spring MVC) | Desktop (WinForms, GWT) | Desktop + SPA (Vue, Angular, WPF) |

## Fowler's Summary

> Цель всех этих паттернов одна: отделить бизнес-логику от UI. Разница в том, кто кого знает и как организован data flow. Выбор определяется UI-технологией: Observer в десктопе → MVC, data binding → MVVM, пассивный View → MVP.

## Связанные материалы

- [Application Controller](application-controller.md)
- [Page Controller vs Front Controller](page-controller-vs-front-controller.md)
- [Distribution Patterns](distribution-patterns.md) — Remote Facade, DTO
- [Domain-Driven UI](domain-driven-ui.md) — task-based UI на основе DDD
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — глава 14
