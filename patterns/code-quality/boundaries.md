---
title: Boundaries
category: patterns
tags: [clean-code, boundaries, third-party, learning-tests, adapters]
source: clean-code.md
added: 2026-07-06
---

# Boundaries

## Проблема

Сторонний код (frameworks, libraries) проникает в доменную логику, создавая tight coupling. Смена библиотеки или обновление версии ломает систему каскадно.

## Решение

### Clean boundaries

- **Thin wrappers over third-party code**: предоставляй интерфейс в терминах твоего домена. `Map<String, Sensor>` → класс `Sensors` с `getById(id)`. Скрываешь тип коллекции, управляешь generics в одном месте.
- Граница должна быть тонкой и тестируемой. Код, который напрямую зависит от third-party API, не должен быть размазан по проекту.
- **Adapters**: реализуй dependency inversion — бизнес-логика зависит от интерфейса, а adapter зависит от third-party библиотеки и реализует этот интерфейс.

### Learning tests

Прежде чем использовать стороннюю библиотеку в production:
- Напиши маленькие тесты, проверяющие твоё понимание API.
- Это документирует ожидаемое поведение.
- При обновлении версии библиотеки learning tests сразу покажут, что изменилось (breaking API, новое поведение).
- Learning tests бесплатны: ты всё равно пишешь exploratory code, чтобы понять библиотеку.

### Using code that doesn't exist yet

- Создай интерфейс для отсутствующего компонента. Работай с фасадом, который ты контролируешь.
- Когда компонент готов, напиши adapter.
- `Fake`-реализация интерфейса даёт возможность работать и тестировать без ожидания.

## Tradeoffs

- Wrapper — overhead написания. Окупается при первом же обновлении библиотеки или смене реализации.
- Слишком толстые wrappers становятся новым source of coupling.

## Связанные материалы

- [Error Handling](error-handling.md)
- [Objects and Data Structures](objects-and-data-structures.md)
- [Clean Code](../../sources/books/clean-code.md)
