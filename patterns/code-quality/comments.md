---
title: Comments
category: patterns
tags: [clean-code, comments, documentation, self-documenting-code]
source: clean-code.md
added: 2026-07-06
---

# Comments

## Проблема

Комментарии компенсируют нашу неспособность выразить намерение в коде. Они рождаются из неудачного кода и со временем лгут — код эволюционирует, комментарий остаётся.

## Решение

**Код — единственный надёжный источник истины.** Пиши код, который не требует объяснений.

### Хорошие комментарии

- **Legal**: `// Copyright (C) 2026 ...`
- **Informative**: `// Returns an instance of Responder being tested` — но лучше через имя метода.
- **Explanation of intent**: `// We sort by zip because the vendor's spec requires it`. Почему, а не что.
- **Clarification**: `// a < b (lexicographic comparison)` — когда код неочевиден из-за внешних ограничений.
- **Warning of consequences**: `// This test takes > 30s. Only run on CI.`
- **TODO**: но не оставляй их навечно — регулярно чисти.
- **Amplification**: выделение важности того, что иначе выглядит незначительным `// The trim is critical here—the API sends trailing spaces`.
- **Javadocs in public APIs**: документирование контракта, а не реализации.

### Плохие комментарии

- **Redundant**: `// increment i` над `i++`. Шум.
- **Misleading**: комментарий говорит не то, что код делает.
- **Mandated**: требование «комментировать каждую функцию / переменную» порождает мусор.
- **Journal**: `// 2026-07-06 — Bob changed ...`. Для этого есть VCS.
- **Noise**: `/** Default constructor. */`.
- **Position markers**: `// Actions //////////////////////` — шум.
- **Closing brace comments**: `} // while` — если блок настолько большой, что это нужно, разбей его.
- **Attribution**: `// Added by Rick` — VCS знает.
- **Commented-out code**: шум и неуверенность. Кто прочитает и решится удалить? Удаляй.
- **HTML comments**: Javadoc с HTML — нечитаемо в редакторе.
- **Nonlocal information**: комментарий описывает что-то не в этом месте.
- **Too much information**: эссе об RFC, когда нужна одна строчка контекста.

## Tradeoffs

- Полный отказ от комментариев тоже вреден: intent-documenting comments незаменимы.
- Перекос в сторону комментариев вместо рефакторинга — главный риск.

## Связанные материалы

- [Meaningful Names](meaningful-names.md)
- [Functions](functions.md)
- [Clean Code](../../sources/books/clean-code.md)
