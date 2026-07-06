---
title: Emergence
category: patterns
tags: [clean-code, simple-design, kent-beck, refactoring]
source: clean-code.md
added: 2026-07-06
---

# Emergence

## Проблема

Сложность системы растёт нелинейно, если каждый добавляет код без оглядки на дизайн. Команда тонет в дублировании и невыразительном коде.

## Решение

### Правила простого дизайна (Kent Beck)

Дизайн «достаточно хорош», когда он, в порядке приоритета:

1. **Runs all the tests** — тесты проходят. Без тестов невозможно верифицировать, что система работает. Тесты дают уверенность для рефакторинга.
2. **No duplication** — отсутствует дублирование кода, знаний, концепций. Дублирование — основной враг хорошо спроектированной системы.
3. **Expresses intent** — код выражает намерение программиста. Имена, размеры функций, структура классов — всё передаёт «почему».
4. **Minimal elements** — минимизирует количество классов и методов. Не добавляй инфраструктуру, которая не нужна сейчас. YAGNI.

### Running all the tests

Система, которую нельзя проверить — её нельзя верифицировать, значит, нельзя менять. Высокая тестируемость ведёт к хорошему дизайну (SRP, DIP).

### No duplication

Дублирование — не только одинаковые строки. Семантическое дублирование: два куска кода, решающих одну и ту же проблему разными способами.

- **Template Method** — избавляет от структурного дублирования (same algorithm, different steps).
- **Extract method** дешёв и почти всегда окупается.

### Expressing intent

- Хорошие имена: что делает, зачем, как.
- Маленькие функции и классы — легче назвать, описать, протестировать.
- Стандартные паттерны сообщают о дизайне через имена (`Command`, `Visitor`).
- Хорошо написанные тесты — первичная документация.

### Minimal

- «Всё можно сделать проще, чем кажется». Старайся сократить число элементов.
- После избавления от дублирования и выражения намерения посмотри, что можно удалить.
- Правило: любой код, который не нужен прямо сейчас — удали.

## Kanat-Alexander: YAGNI systematized

Kent Beck's "minimal elements" rule is the seed. Kanat-Alexander develops it into a full design philosophy:

- **Don't write code you don't need right now.** Unnecessary code = future bugs + future maintenance + future confusion.
- **The simplest fix is making the problem disappear.** Before writing code for a fix, ask: can I remove the condition that creates the problem? Can I solve it by deleting code? Only write new code as a last resort.
- **The law of diminishing returns to complexity.** Each new feature makes every subsequent feature harder to add. Evaluate features by the future value they block, not just their own value.

See also: [Minimum necessary work](../fundamentals/minimum-necessary-work.md).

## Tradeoffs

- Minimal ≠ преждевременная оптимизация. Не жертвуй читаемостью ради на один класс меньше.
- Правила в порядке приоритета: дублирование хуже, чем «лишний» класс.

## Связанные материалы

- [Unit Tests](unit-tests.md)
- [Functions](functions.md)
- [Code Smells](code-smells.md)
- [Clean Code](../../sources/books/clean-code.md)
- [Minimum necessary work](../fundamentals/minimum-necessary-work.md) — YAGNI and simplicity from Code Simplicity
