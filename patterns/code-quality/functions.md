---
title: Functions
category: patterns
tags: [clean-code, functions, srp, side-effects, abstraction]
source: clean-code.md
added: 2026-07-06
---

# Functions

## Проблема

Большие функции с множеством уровней абстракции, побочными эффектами и смешанными ответственностями трудно тестировать, понимать и изменять.

## Решение

Функция должна делать **одно**, делать это **хорошо** и **только это**.

- **Small**: ~4 строк в идеале, редко больше 20. Каждый `if`, `else`, `while` — обычно одна строка на вызов функции.
- **Single level of abstraction**: все операторы функции должны быть на одном уровне абстракции. Не смешивай `getHtml()` (высокий уровень) с `.append('\n')` (низкий уровень) в одной функции. Stepdown rule: код читается сверху вниз как narrative, каждый уровень делегирует следующему.
- **Switch statements**: терпимы только один раз — для создания полиморфных объектов. Прячь за абстрактной фабрикой.
- **Use descriptive names**: `includeSetupAndTeardownPages` вместо `includeSetupPages`. Имя описывает что делает функция.
- **Few arguments**: 0 (niladic) — идеал, 1 (monadic), 2 (dyadic). 3 (triadic) — требует обоснования. Больше 3 — запах. Аргументы делают функцию сложнее для понимания и тестирования.
- **No flag arguments**: `render(true)` — ужасно. Флаг означает, что функция делает больше одного. Раздели на две: `renderForSuite()` и `renderForSingleTest()`.
- **No side effects**: функция обещает одно, но делает скрытое изменение (write to file, session variable). Temporal coupling скрыт.
- **Command-query separation**: функция либо **делает** (command), либо **отвечает** (query), но не оба. `set(attr, value)` → устанавливает и возвращает старое значение — нарушение.
- **Prefer exceptions to error codes**: error codes порождают вложенные `if` и заставляют вызывающего обрабатывать ошибку сразу. Выноси try/catch в отдельную функцию.
- **Don't repeat yourself (DRY)**: дублирование — корень всех зол в ПО. Каждый кусок знания должен иметь единственное представление.
- **Structured programming**: Дейкстра говорил — одна точка входа, одна точка выхода. Для малых функций это естественно: короткая функция редко нуждается в `break`, `continue`, множественных `return`.

## Tradeoffs

- Много маленьких функций означает больше indirection. Компенсируется хорошим именованием.
- Слишком агрессивное извлечение функций без смыслового разделения может создать фрагментацию.

## Связанные материалы

- [Meaningful Names](meaningful-names.md)
- [Classes](classes.md)
- [Code Smells](code-smells.md)
- [Clean Code](../../sources/books/clean-code.md)
