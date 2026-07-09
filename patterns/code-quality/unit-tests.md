---
title: Unit Tests
category: patterns
tags: [clean-code, testing, tdd, first, quality]
source: clean-code.md
added: 2026-07-06
---

# Unit Tests

## Проблема

Плохие тесты замедляют разработку: они хрупкие, нечитаемые и недоверительные. Команда начинает их игнорировать или отключать.

## Решение

Тестовый код так же важен, как production код. Тесты — это страховка изменений.

### Three Laws of TDD

1. Не пиши production код, пока нет failing unit test.
2. Не пиши больше теста, чем нужно для failure (not compiling — failure).
3. Не пиши больше production кода, чем нужно для прохождения failing test.

Цикл: ~30 секунд на итерацию. Микро-циклы создают покрытие и уверенность.

### Clean tests — читаемость

- **Build-Operate-Check** (Arrange-Act-Assert): три чётких блока. Разделяй пустыми строками.
- **Один концепт на тест**: не смешивай в одном тесте несколько сценариев.
- **Single assert per test**: один assert заставляет думать об одном поведении. `given/when/then` на уровне имени теста.
- **Given-When-Then**: имя теста как narrative. `makeSingleWithdrawal_whenBalanceIsSufficient_reducesBalanceAndDispatchesEvent`.

### F.I.R.S.T. принципы

| Принцип | Значение |
|---|---|
| **F**ast | Тесты должны проходить быстро. Медленные тесты не запускаются. |
| **I**ndependent | Тесты не зависят друг от друга. Порядок выполнения не важен. |
| **R**epeatable | В любом окружении: локально, CI, без сети. |
| **S**elf-validating | Тест либо pass, либо fail. Не требует ручной проверки вывода. |
| **T**imely | Тесты пишутся до production кода (TDD) или сразу после. |

### Структура тестов

- **Single concept per test**: `testAddMonths()` а не `testDateFunctions()`.
- Избегай long setup через factory methods и test builders.
- Don't test trivial code (getters, setters). Но тестируй всё, что может сломаться.

## Tradeoffs

- 100% coverage не самоцель. Тестируй то, что может пойти не так.
- Слишком много моков → сигнал о плохом дизайне (нарушение SRP, tight coupling).

## Связанные материалы

- [Functions](functions.md)
- [Error Handling](error-handling.md)
- [Emergence](emergence.md)
- [Test Architecture](test-architecture.md) — flexible test layers, builders, fakes, expressive assertions
- [Clean Code](../../sources/books/clean-code.md)
