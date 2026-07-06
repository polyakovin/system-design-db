# Design in construction

## Проблема

Разработчики часто воспринимают design как upstream-активность, выполняемую архитектором до начала кодинга. В реальности значительная часть проектных решений принимается во время construction, но без осознанной методологии эти решения ad-hoc и непоследовательны.

## Решение

McConnell выделяет **design in construction** как отдельный слой проектирования — ниже системной архитектуры, но выше построчного кодинга. Это проектирование на уровне:

- отдельных классов, модулей и подпрограмм;
- внутренних интерфейсов между компонентами;
- алгоритмов и структур данных;
- обработки ошибок в рамках одного модуля.

## Design heuristics (по McConnell)

- **Find real-world objects** — моделируй объекты предметной области.
- **Form consistent abstractions** — единый уровень абстракции внутри модуля.
- **Encapsulate implementation details** — скрывай, что может измениться.
- **Inherit when it simplifies** — наследование только когда это reduces complexity, не для «красоты иерархии».
- **Hide secrets** — information hiding как основной инструмент управления сложностью.
- **Identify areas likely to change** — изолируй нестабильные части.
- **Keep coupling loose** — минимизируй зависимости между модулями.
- **Aim for strong cohesion** — класс/модуль должен делать одну вещь.

## Design levels (по McConnell)

1. **Software system** — общая архитектура.
2. **Division into subsystems/packages** — разбиение на крупные блоки.
3. **Division into classes** — классы внутри подсистемы.
4. **Division into routines** — функции и методы.
5. **Internal routine design** — алгоритмы и control flow внутри функции.

## Tradeoffs

Хороший design-in-construction замедляет первую версию, но снижает стоимость изменений на порядок. Плохой — ускоряет v1 и создаёт compounding complexity debt.

## Связанные материалы

- [Software construction](software-construction.md)
- [Managing complexity](managing-complexity.md)
- [Working classes](working-classes.md)
- [API design](../architecture-design/api-design.md)

## Источник

Steve McConnell, *Code Complete* (2004), Chapter 5: Design in Construction.
