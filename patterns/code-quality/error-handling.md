---
title: Error Handling
category: patterns
tags: [clean-code, error-handling, exceptions, special-case-pattern]
source: clean-code.md
added: 2026-07-06
---

# Error Handling

## Проблема

Обработка ошибок, размазанная по коду, скрывает бизнес-логику. Коды ошибок создают вложенные `if`, заставляют обрабатывать ошибку немедленно и поощряют игнорирование.

## Решение

### Exceptions over error codes

- Бросай исключения вместо возврата кодов ошибок. Вызывающий код остаётся чистым; обработка ошибок отделяется от happy path.
- **Try/catch blocks**: выноси в отдельную функцию. Первое, что делает функция с try/catch — `try`. Ничего до него.
- **Unchecked exceptions**: checked exceptions нарушают Open/Closed Principle: изменение в низкоуровневом коде заставляет менять сигнатуры всей цепочки вызовов.

### Context with exceptions

- Каждое исключение должно нести достаточно контекста: что пошло не так, где, при каких данных.
- Создавай informative error messages, логируй вместе с исключением.
- Классифицируй исключения по тому, как вызывающий может на них ответить (retryable, fatal, validation).

### Don't return null

- Возврат `null` — один символ, который требует проверки в каждом caller.
- Возвращай empty collection, empty Optional, или бросай исключение.
- **Не передавай null** в аргументах: в большинстве языков это runtime surprise. Запрети на уровне код-ревью.

### Special Case Pattern

Создай класс или объект, инкапсулирующий особое поведение. Вместо проверки на `null` или специальный код, вызывающий работает с объектом единообразно.

- Пример: `NullEmployee` (с именем «N/A», зарплатой 0) вместо `null` check.
- `try { expenses = employee.getExpenses(); }` — код читается чисто; обработка особого случая внутри `NullEmployee`.

### Wrapping third-party APIs

Оборачивай сторонние API в тонкий слой, который:
- Переводит их исключения в исключения твоего домена.
- Позволяет заменить библиотеку без изменения бизнес-логики.
- Даёт единую точку для тестирования (mock один wrapper, не всю библиотеку).

## Tradeoffs

- Too many exception types создают свой шум. Группируй по смыслу для вызывающих (transient vs permanent), а не по источнику.
- Special case pattern — overhead для одного вызова, окупается при повторном использовании.

## Связанные материалы

- [Functions](functions.md)
- [Boundaries](boundaries.md)
- [Unit Tests](unit-tests.md)
- [Clean Code](../../sources/books/clean-code.md)
