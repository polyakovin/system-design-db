# Code quality

## Проблема

Code quality — термин, который все поддерживают, но редко определяют operationally. Без конкретных критериев quality остаётся subjective и не улучшается системно.

## Решение

McConnell определяет качество кода через measurable характеристики и процессы их обеспечения.

## Характеристики quality code

- **Readability** — код читается как хорошо написанная проза; другой разработчик понимает intent за минуты, а не часы.
- **Maintainability** — изменения в одной части не ломают другие; архитектура поддерживает evolvability.
- **Simplicity** — код не сложнее, чем требует задача; complexity вводится только когда benefits доказаны.
- **Correctness** — код работает на всех defined inputs; edge cases обработаны.
- **Testability** — код спроектирован так, что его behaviour можно проверить автоматически.

## Практики обеспечения качества

### Code review

- Формальные inspections (Fagan-style) находят до 60% дефектов — эффективнее тестирования.
- Review должен проверять: корректность, читаемость, соответствие стандартам, обработку ошибок, performance traps.
- Автор и ревьюер — разные роли; review не должен быть «смотри, что я написал».

### Coding standards

- Стандарты снижают cognitive load при чтении чужого кода.
- Должны охватывать: naming, форматирование, commenting conventions, error-handling patterns, complexity limits.
- Стандарт, который не enforced, — не стандарт.

### Testing during construction

- Unit-тесты пишутся параллельно с кодом, не после.
- Integration-тесты проверяют контракты между модулями.
- Test cases должны покрывать: nominal path, boundary conditions, error paths, concurrency если применимо.

## Техники повышения качества

- **Table-driven methods** — заменяют сложную логику на lookup-таблицы.
- **Structured programming** — последовательность, выбор, итерация как base primitives; избегай goto.
- **Control-flow complexity metrics** — измеряй cyclomatic complexity; >10 — кандидат на рефакторинг.

## Связанные материалы

- [Software construction](software-construction.md)
- [Defensive programming](defensive-programming.md)
- [Refactoring](refactoring.md)
- [Managing complexity](managing-complexity.md)

## Источник

Steve McConnell, *Code Complete* (2004), Chapters 6–7, 16–17, 23–24.
