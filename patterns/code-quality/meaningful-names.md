---
title: Meaningful Names
category: patterns
tags: [clean-code, naming, readability]
source: clean-code.md
added: 2026-07-06
---

# Meaningful Names

## Проблема

Плохие имена создают постоянное когнитивное трение: разработчик вынужден держать в голове mapping между символом и его смыслом. Имя `d` или `theList` не отвечает на вопрос «зачем это здесь».

## Решение

Имя должно отвечать на три вопроса: **почему** существует, **что** делает, **как** используется.

- **Reveal intent**: `elapsedTimeInDays` вместо `d`. Имя должно раскрывать намерение без необходимости читать реализацию.
- **Avoid disinformation**: не называй группу аккаунтов `accountList` если это не `List`; не используй `O` и `l` в именах переменных. Избегай слов с устоявшимся значением (например `hp` для «hip» когда все читают как «horsepower»).
- **Make meaningful distinctions**: `a1`, `a2`, `a3` — не различие. `Product` vs `ProductInfo` vs `ProductData` — шум. Различие должно быть семантическим.
- **Use pronounceable names**: `generationTimestamp` вместо `genymdhms`. Программирование — социальная деятельность.
- **Use searchable names**: имя из одной буквы допустимо только как локальная переменная внутри короткого метода. Константы (`MAX_CLASSES_PER_STUDENT`) вместо magic numbers.
- **Avoid mental mapping**: читатель не должен переводить `r` в «полное имя с адресом».
- **Class names**: nouns (`Customer`, `Account`). Избегай `Manager`, `Processor`, `Data`, `Info`.
- **Method names**: verbs (`postPayment`, `deletePage`). Accessors, mutators, predicates: `get`, `set`, `is`.
- **One word per concept**: `fetch`, `retrieve`, `get` для одного и того же действия — путаница. Выбери одно слово на концепт.
- **Use solution/problem domain names**: solution domain (алгоритмы, паттерны, CS-термины) понятны программистам; problem domain — когда нет solution domain имени.
- **Add meaningful context**: `addrState` вместо `state`. Но не добавляй избыточный контекст (`GasStationDeluxe`-приложение не нуждается в префиксе `GSD` для каждого класса).

## Tradeoffs

- Длинные имена повышают читаемость ценой verbosity при написании (editor autocomplete нивелирует).
- Слишком специфичные имена хрупки при изменении domain model.

## Когда применять

Всегда. Это самый дешёвый способ улучшить codebase.

## Связанные материалы

- [Functions](functions.md)
- [Clean Code](../../sources/books/clean-code.md)
