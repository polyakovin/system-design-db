---
title: Classes
category: patterns
tags: [clean-code, classes, srp, cohesion, encapsulation]
source: clean-code.md
added: 2026-07-06
---

# Classes

## Проблема

Классы обрастают ответственностями, теряют cohesion и превращаются в God Objects, в которых невозможно найти нужное поведение и которые невозможно протестировать изолированно.

## Решение

### Class organisation

- **Ordering**: public static constants → private static variables → private instance variables → public functions → private utilities (invoked by public functions). Инкапсуляция: скрывай детали.
- **Stepdown rule для классов**: публичный интерфейс говорит *что*, приватные — *как*.

### Single Responsibility Principle (SRP)

Класс должен иметь **одну причину для изменения**.

- `SuperDashboard` с 70 методами, отвечающими за UI layout, версионирование и сборку — три причины для изменения.
- Название класса должно описывать его ответственность. Если не можешь назвать без слов «Manager», «Processor», «Super» — класс делает слишком много.
- **Признак нарушения**: если описание класса содержит «and» или «or».

### Cohesion

Класс должен иметь небольшое количество instance variables, и каждый метод должен использовать большинство из них. Высокая cohesion означает, что методы и переменные класса взаимозависимы и образуют логическое целое.

- **Cohesion падает** → класс разбивается. Когда подмножество методов работает с одним подмножеством переменных — это кандидат на выделение.
- Стратегия **split**: выдели подмножество переменных и методов в новый класс. Повторяй, пока cohesion не станет высокой.

### Organising for change

- Изолируй изменяющиеся части. Класс с высокой cohesion плюс SRP устойчив к изменениям: change затрагивает только один класс.
- **Open-Closed Principle (OCP)**: класс открыт для расширения, закрыт для модификации. Достигается через абстракцию и полиморфизм.
- **Dependency Inversion Principle (DIP)**: класс зависит от абстракций, а не от конкретных деталей.

## Tradeoffs

- Много маленьких классов требует навигации. Компенсируется понятными именами и логической группировкой (пакеты, модули).
- Over-engineering через интерфейсы для всего — запах. Один интерфейс с одним implementation — перебор.

## Связанные материалы

- [Functions](functions.md)
- [Objects and Data Structures](objects-and-data-structures.md)
- [Systems](systems.md)
- [Code Smells](code-smells.md)
- [Clean Code](../../sources/books/clean-code.md)
