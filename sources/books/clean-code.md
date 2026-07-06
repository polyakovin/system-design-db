---
title: Clean Code
url: https://github.com/rocky-191/Awesome-CS-Books/raw/master/SoftwareEngineering/Architecture/2008-Martin-Clean%20Code.pdf
type: book
category: sources
tags: [architecture, software-design, book]
added: 2026-07-06
status: new
---

# Clean Code

Robert C. Martin, 2008.

Принципы написания читаемого и поддерживаемого кода: именование, функции, комментарии, форматирование, обработка ошибок.

Источник: [Awesome-CS-Books / Architecture](https://github.com/rocky-191/Awesome-CS-Books/tree/master/SoftwareEngineering/Architecture)

## Извлечённые концепции

Все концепции разнесены в `patterns/code-quality/`:

- [Meaningful names](../../patterns/code-quality/meaningful-names.md) — правила именования: intent, no disinformation, searchability, pronounceable, one word per concept.
- [Functions](../../patterns/code-quality/functions.md) — малые функции, single level of abstraction, no side effects, command-query separation, few arguments.
- [Comments](../../patterns/code-quality/comments.md) — хорошие (intent, legal, warning) vs плохие (redundant, journal, commented-out code) комментарии.
- [Formatting](../../patterns/code-quality/formatting.md) — newspaper metaphor, вертикальное/горизонтальное форматирование, team rules, индентация.
- [Objects and data structures](../../patterns/code-quality/objects-and-data-structures.md) — data/object anti-symmetry, Law of Demeter, train wreck avoidance, DTO vs Active Record.
- [Error handling](../../patterns/code-quality/error-handling.md) — exceptions over error codes, special case pattern, don't return/pass null, wrapping third-party APIs.
- [Boundaries](../../patterns/code-quality/boundaries.md) — thin wrappers, learning tests, адаптеры для отсутствующего кода.
- [Unit tests](../../patterns/code-quality/unit-tests.md) — F.I.R.S.T. принципы, three laws of TDD, Build-Operate-Check, single concept per test.
- [Classes](../../patterns/code-quality/classes.md) — SRP, cohesion, class organisation, organising for change (OCP, DIP).
- [Systems](../../patterns/code-quality/systems.md) — separation of main, dependency injection, cross-cutting concerns (AOP), scaling up без BDUF.
- [Emergence](../../patterns/code-quality/emergence.md) — правила простого дизайна Kent Beck: runs tests, no duplication, expresses intent, minimal.
- [Code smells](../../patterns/code-quality/code-smells.md) — bloaters, change preventers, couplers, dispensables, naming, environment, tests.

## Статус

Добавлено: 2026-07-06
Распаковано: 2026-07-06
