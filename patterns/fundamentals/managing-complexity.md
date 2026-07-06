# Managing complexity

## Проблема

Софт растёт, и с каждым новым требованием код становится сложнее. Без активного управления complexity, система достигает точки, где любое изменение ломает несвязанные части. Это основная причина, по которой проекты «замедляются до смерти».

## Решение

McConnell утверждает: **управление сложностью — главный технический императив разработки**. Каждое решение должно оцениваться через призму: снижает ли оно complexity или добавляет?

## Источники complexity

- **Essential complexity** — сложность, inherent в задаче. Неустранима.
- **Accidental complexity** — сложность, привнесённая решением: плохие абстракции, over-engineering, leaky abstractions, несвязный код.

Задача разработчика — минимизировать accidental complexity при сохранении essential.

## Практики снижения complexity

### На уровне кода

- **Single responsibility**: один класс/функция — одна причина для изменения.
- **Information hiding**: скрывай decisions, которые могут измениться, за стабильным интерфейсом.
- **Low coupling, high cohesion**: модули должны знать минимум друг о друге и быть internally focused.
- **Consistent abstraction level**: не смешивай высокоуровневую бизнес-логику с низкоуровневыми деталями в одной функции.

### На уровне архитектуры

- Разделяй систему на подсистемы с minimal interfaces.
- Минимизируй количество связей между подсистемами — каждая связь = потенциальный cascading failure.
- Используй layered architecture для ограничения направления зависимостей.

### McConnell's complexity litmus test

Каждый раз, когда добавляешь код, спроси:
1. Упрощает ли это систему в целом?
2. Можно ли решить задачу без добавления нового кода?
3. Понимаю ли я все consequences этого изменения?

## Tradeoffs

- Борьба с complexity замедляет delivery в краткосрочной перспективе, но это инвестиция: каждый час, потраченный на упрощение сейчас, экономит дни отладки потом.
- Слишком агрессивное упрощение (premature abstraction) само становится accidental complexity.

## Связь с системным дизайном

Complexity management — сквозная тема: в системном дизайне это проявляется в выборе bounded contexts, microservice boundaries, API surface area и layered architecture. Принцип един: минимизируй то, что нужно держать в голове одновременно.

## Связанные материалы

- [System design principles](system-design-principles.md)
- [Design in construction](design-in-construction.md)
- [Working classes](working-classes.md)
- [Refactoring](refactoring.md)

## Источник

Steve McConnell, *Code Complete* (2004), Chapters 5–6, 34.
