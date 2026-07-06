# Debugging

## Проблема

Большинство разработчиков отлаживают ad-hoc: добавляют print-ы, меняют что-то наугад, пробуют ещё. Без системного подхода отладка затягивается, а root cause остаётся не найденным — фиксится симптом.

## Решение

McConnell предлагает **научный метод отладки**: systematic hypothesis testing вместо random trial-and-error.

## Процесс отладки по McConnell

### 1. Стабилизируй ошибку

- Сделай баг воспроизводимым.
- Если не воспроизводится — это вероятно race condition, memory corruption или environment-specific.
- Сужение условий воспроизведения — уже половина решения.

### 2. Локализуй источник

- Сузь область поиска: бинарный поиск по коду (отключи половину системы).
- Используй assertions для проверки предположений о состоянии.
- Пойми data flow: откуда пришли некорректные данные и где они испортились.

### 3. Сформулируй гипотезу

- Что именно вызывает ошибку?
- Гипотеза должна быть specific и falsifiable: «если X — причина, то изменение Y должно исправить поведение».

### 4. Проверь гипотезу

- Сделай одно минимальное изменение.
- Проверь: баг ушёл ИЛИ поведение изменилось предсказуемо.
- Если гипотеза не подтвердилась — сформулируй новую, не гадай.

### 5. Исправь root cause, не симптом

- Пойми, *почему* код оказался в некорректном состоянии.
- Добавь защиту от повторения: assertion, тест, валидацию.

### 6. Проверь fix

- Убедись, что оригинальный баг исправлен.
- Проверь, что fix не сломал связанную функциональность.
- Подумай: есть ли похожие баги в соседнем коде?

## Инструменты и техники

- **Assertions** — проверка инвариантов во время выполнения.
- **Logging/tracing** — запись потока исполнения (не print для однократного использования).
- **Debugger** — stepping, breakpoints, watch expressions.
- **Binary search debugging** — отключение/включение частей системы для локализации.
- **Rubber duck debugging** — объяснение проблемы вслух другому (или утке).

## Kanat-Alexander: Defects are failures of understanding

Kanat-Alexander reframes debugging more fundamentally than McConnell's scientific method: **bugs are not caused by carelessness or inattention — they are caused by not understanding the system.** If you truly understood every line of code, every interaction, and every edge case, you would not introduce defects.

When a bug appears, the root cause is always a gap in your mental model. Fix the understanding first, then the code. This complements McConnell's method: McConnell gives the *process* for finding the gap; Kanat-Alexander identifies *why* the gap exists.

See also: [Understanding before building](understanding-before-building.md).

## Психология отладки

- Не вини компьютер — баг в твоём коде (или в твоём понимании чужого кода).
- Не отрицай: «этого не может быть». Если происходит — значит, может.
- Отладка — навык, который тренируется. С опытом приходит интуиция о том, где искать.

## Связанные материалы

- [Defensive programming](defensive-programming.md)
- [Code quality](code-quality.md)
- [Managing complexity](managing-complexity.md)
- [Understanding before building](understanding-before-building.md) — Kanat-Alexander on defects as understanding gaps

## Источник

Steve McConnell, *Code Complete* (2004), Chapter 23: Debugging.
Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013) — defects as failures of understanding.
