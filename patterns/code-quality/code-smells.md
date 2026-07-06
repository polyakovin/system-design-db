---
title: Code Smells
category: patterns
tags: [clean-code, code-smells, refactoring, heuristics]
source: clean-code.md
added: 2026-07-06
---

# Code Smells

## Проблема

Запахи кода — поверхностные индикаторы глубинных проблем в дизайне. Игнорирование ведёт к exponential decay maintainability. Команда тратит всё больше времени на навигацию и understanding вместо delivery.

## Решение

Регулярно выявляй запахи и проводи рефакторинг. Ниже — каталог ключевых запахов из Clean Code.

### Bloaters

- **Large functions**: функция длиннее ~20 строк. Каждая функция должна делать ровно одно.
- **Large classes**: класс с >1 ответственностью. Признаки: много instance variables, название с «and», длинный список импортов.
- **Long parameter lists**: >3 аргументов. Вместо этого передавай объект, создавай parameter object.
- **Long chains of conditionals**: полиморфизм вместо switch/if-else. `switch` допустим в фабрике, которая создаёт полиморфные объекты, и только там.

### Change preventers

- **Divergent change**: один класс меняется по разным причинам (формат отчёта + бизнес-правило + схема БД). Нарушение SRP. Раздели.
- **Shotgun surgery**: маленькое изменение заставляет менять много классов. Одна ответственность размазана по системе. Собери.

### Couplers

- **Feature envy**: метод класса чаще обращается к данным другого класса. Перемести метод.
- **Inappropriate intimacy**: классы слишком много знают о внутренностях друг друга. Разбей или перестрой.
- **Message chains**: `a.getB().getC().doSomething()` — train wreck / Law of Demeter violation.
- **Middle man**: класс, который только делегирует. Если больше половины методов — pass-through, удали класс и делегируй напрямую.

### Dispensables

- **Comments**: комментарий, объясняющий плохой код. Refactor, don't document.
- **Duplicate code**: идентичный или структурно похожий код в нескольких местах. Extract method / Template Method.
- **Dead code**: unreachable код, закомментированный код. Удали.
- **Speculative generality**: код «на будущее», который сейчас не используется. Абстрактные классы с одним наследником, hooks, неиспользуемые параметры. YAGNI.
- **Data classes**: классы с только геттерами/сеттерами и без поведения. Найди поведение рядом и перемести в класс.

### Naming

- **Poor names**: однобуквенные переменные, невыразительные имена, непроизносимые имена, несогласованный словарь.

### Environment

- **Build requires more than one step**: checkout → одна команда (build/run). Builds с ручными шагами ненадёжны.
- **Tests require more than one step**: одна команда запускает все тесты. Иначе их не запускают.

### Tests

- **Insufficient tests**: тестовое покрытие не отвечает на вопрос «достаточно ли тестов для деплоя».
- **Missing edge cases**: тесты только на happy path.
- **Slow tests**: медленные тесты не запускают.

## Связанные материалы

- [Functions](functions.md)
- [Classes](classes.md)
- [Emergence](emergence.md)
- [Meaningful Names](meaningful-names.md)
- [Refactoring (2nd ed.)](../../sources/books/refactoring-second-edition.md)
- [Clean Code](../../sources/books/clean-code.md)
