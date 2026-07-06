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

## Kanat-Alexander: The law of diminishing returns to complexity

Each new feature adds complexity to the *entire system*, not just to itself. Feature #1 is cheap — nothing to interact with. Feature #100 must coexist with 99 existing features, each with their own assumptions, data formats, and edge cases. The marginal cost of features increases non-linearly.

Practical consequence: evaluate features not just by their own value, but by the future value they block. A feature that provides moderate value today but makes the next 5 features significantly harder may be a net negative. Removing low-value features is capacity recovery, not regression.

See also: [Minimum necessary work](minimum-necessary-work.md).

## Связанные материалы

- [System design principles](system-design-principles.md)
- [Design in construction](design-in-construction.md)
- [Working classes](working-classes.md)
- [Refactoring](refactoring.md)
- [Simplicity First](simplicity-first.md) — Kanat-Alexander's core thesis on simplicity
- [Minimum necessary work](minimum-necessary-work.md) — YAGNI and diminishing returns to complexity

## Архитектор (2016): сложность от бизнеса и команды

The Architect (架构漫谈) adds a dimension McConnell doesn't fully explore: **complexity originates not just from code, but from the business domain and the team structure.**

### Essential complexity = business complexity + team complexity

The Architect argues that essential complexity has two components:

1. **Business complexity:** the inherent intricacy of the domain. A tax calculation engine is complex because tax law is complex. No amount of clean code eliminates that — it only makes it manageable.

2. **Team complexity:** the communication overhead produced by the team structure. As teams grow, communication paths grow as O(n²). This complexity leaks into the architecture — more teams → more integration points → more coordination → more accidental complexity arising from the org chart.

### The Architect's implication

You can't simplify the business domain (that's the value you're paid for). But you can design the team structure and system boundaries to minimize the *cross-product* of business complexity × team complexity. This is why Conway's Law matters: if team boundaries don't match domain boundaries, the architecture will fight both the business complexity and the team complexity simultaneously.

### Practical consequence

When a system feels "too complex," the Architect asks two questions before touching the code:

1. **Is this complexity truly in the business, or did we invent it?** (Is it essential or accidental?)
2. **Is our team structure amplifying the complexity?** (Would different team boundaries simplify the system?)

Often the answer to #2 is yes — and no amount of refactoring fixes a team structure problem.

## Источник

Steve McConnell, *Code Complete* (2004), Chapters 5–6, 34.
Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013) — law of diminishing returns to complexity.
架构师, *架构漫谈* (2016) — complexity from business and team structure.
