# Defensive programming

## Проблема

Код, который предполагает корректные входные данные и идеальную среду выполнения, ломается непредсказуемо при первом же неожиданном input. Ошибки проявляются далеко от источника, и отладка становится дорогой.

## Решение

**Defensive programming** — практика написания кода, который защищает себя от некорректных данных и состояний, делая ошибки явными и близкими к источнику.

## Ключевые техники

### Assertions

- Используй assertions для проверки инвариантов — условий, которые всегда должны быть истинны.
- Assertions документируют предположения в коде и ловят ошибки на earliest possible stage.
- Отключай assertions в production только для performance-critical paths; для остального — пусть падают явно.

### Error handling

- Выбирай стратегию обработки ошибок осознанно: возврат к neutral value, substitution of next valid data, возврат того же что и в прошлый раз, substitution of closest valid value, logging, error code, или shutdown.
- Обрабатывай ошибки на том уровне, где есть контекст для принятия решения.
- Не подавляй ошибки молча — каждый caught exception должен либо обрабатываться, либо пробрасываться осмысленно.

### Exceptions

- Используй исключения для truly exceptional conditions, не для control flow.
- Лови исключения на уровне, где можешь meaningful recover.
- Не игнорируй пустые catch-блоки — это скрытые баги.

### Barricades

- McConnell предлагает «barricade» паттерн: внешние данные валидируются на границе системы, внутренний код работает с чистыми, проверенными данными.
- Аналогия: шлюз на входе в чистую комнату.

## Tradeoffs

- Defensive code = больше строк, но меньше времени в отладке.
- Слишком много assertions в performance-critical коде — overhead; есть смысл отключать в production.

## Связь с системным дизайном

Defensive programming — это реализация принципа fail-fast на уровне отдельного модуля. На системном уровне тот же принцип проявляется в circuit breakers, input validation на API gateway и graceful degradation.

## Связанные материалы

- [Managing complexity](managing-complexity.md)
- [Debugging](debugging.md)
- [Code quality](code-quality.md)

## Источник

Steve McConnell, *Code Complete* (2004), Chapter 8: Defensive Programming.
