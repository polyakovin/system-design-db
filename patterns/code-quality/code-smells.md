---
title: Code Smells
category: patterns
tags: [clean-code, code-smells, refactoring, heuristics]
source: clean-code.md, refactoring-second-edition.md
added: 2026-07-06
updated: 2026-07-06
---

# Code Smells

## Проблема

Запахи кода — поверхностные индикаторы глубинных проблем в дизайне. Игнорирование ведёт к exponential decay maintainability. Команда тратит всё больше времени на навигацию и understanding вместо delivery.

## Решение

Регулярно выявляй запахи и проводи рефакторинг. Каталог ниже объединяет запахи из Clean Code (Robert C. Martin) и Refactoring 2nd ed. (Martin Fowler).

---

## Fowler's Code Smells (Chapter 3, Refactoring 2nd ed.)

Fowler группирует запахи иначе, чем Clean Code, и многие совпадают, но есть уникальные. Здесь — полный каталог с кросс-ссылками.

### 1. Mysterious Name

Имя не раскрывает намерения. Самый распространённый и недооценённый запах. Когда не можешь придумать хорошее имя — в дизайне что-то не так.

**Fix:** Rename Function, Rename Variable, Rename Field.

**Пересечение с:** Poor names в Clean Code.

### 2. Duplicated Code

Одинаковая или структурно похожая логика в разных местах. Если видишь дубликат — ищи способ объединить.

**Fix:** Extract Function, Slide Statements, Pull Up Method (если дубликат в sibling-подклассах).

### 3. Long Function

Функция, которая делает больше, чем заявлено в названии. Код, требующий комментариев *внутри* функции для объяснения «что происходит» — признак, что пора разбивать.

**Fix:** Extract Function (99% случаев). Replace Temp with Query, Introduce Parameter Object, Decompose Conditional.

### 4. Long Parameter List

> 3–4 параметров — сигнал. Признаки: все параметры передаются вместе через цепочку вызовов, часть параметров — флаги.

**Fix:** Replace Parameter with Query, Preserve Whole Object, Introduce Parameter Object, Remove Flag Argument, Combine Functions into Class.

### 5. Large Class

Класс с >1 ответственностью. Индикаторы: много полей, длинный список импортов, дублирующийся код между полями.

**Fix:** Extract Class, Extract Superclass, Replace Type Code with Subclasses.

### 6. Global Data

Глобальные переменные особенно опасны: их может изменить кто угодно откуда угодно. В ООП: синглтоны, статические поля. Fowler считает это одним из самых опасных запахов.

**Fix:** Encapsulate Variable — обернуть глобальную переменную в функцию с контролируемым доступом. Позволяет отслеживать чтение/запись и рефакторить дальше.

### 7. Mutable Data

Изменяемые данные. Мутация в одном месте может сломать предположение в другом. Fowler выделяет отдельно от Global Data — мутабельность сама по себе проблема, даже в локальном скоупе.

**Fix:** Encapsulate Variable, Split Variable (не используй одну переменную для разных целей), Slide Statements (приблизить код, меняющий данные, к данным), Extract Function (изолировать мутацию), Separate Query from Modifier, Combine Functions into Transform (создать иммутабельную копию), Change Reference to Value.

### 8. Divergent Change

Один класс меняется по разным причинам: сегодня — формат отчёта, завтра — бизнес-правило, послезавтра — схема БД. Нарушение SRP.

**Fix:** Extract Class, Split Phase (разделить этапы обработки).

### 9. Shotgun Surgery

Маленькое изменение заставляет менять много классов. Противоположность Divergent Change. Одна ответственность размазана по системе.

**Fix:** Move Function, Move Field, Combine Functions into Class, Inline Class.

### 10. Feature Envy

Метод класса обращается к данным другого класса чаще, чем к своим. Метод хочет жить в другом месте.

**Fix:** Move Function. Иногда — Extract Function и затем Move. Исключение: паттерны Strategy, Visitor, где разделение намеренное.

### 11. Data Clumps

Группы данных, которые всегда ходят вместе: `start` + `end`, `x` + `y` + `z`. Как дети в плаще — выглядят как трое, но действуют как один.

**Fix:** Extract Class, Introduce Parameter Object, Preserve Whole Object. Проверка: удали одно поле из группы — остальные всё ещё имеют смысл? Если нет — это clump.

### 12. Primitive Obsession

Использование примитивов (строки, числа) вместо доменных типов. Телефон как `string`, деньги как `number`, ID как `string`.

**Fix:** Replace Primitive with Object, Replace Type Code with Subclasses/Strategy, Replace Data Value with Object, Introduce Parameter Object, Extract Class.

### 13. Repeated Switches

Один и тот же `switch` или цепочка `if/else` дублируется в разных местах. Добавление нового варианта требует найти и обновить все копии.

**Fix:** Replace Conditional with Polymorphism (основной). Для небольшого числа вариантов — Replace Type Code with Subclasses.

### 14. Loops

Традиционные циклы (`for`, `while`) там, где лучше подходят pipeline-операции. Fowler считает, что в современном коде `map`, `filter`, `reduce` предпочтительнее — они лучше выражают намерение.

**Replace Loop with Pipeline** — использовать коллекционные операции.

### 15. Lazy Element

Класс или функция, которые существуют «на всякий случай», но не несут реальной ценности. Функция в одну строку с очевидным телом, класс-обёртка без логики.

**Fix:** Inline Function, Inline Class, Collapse Hierarchy.

### 16. Speculative Generality

Код «на будущее»: абстрактный класс с одним наследником, параметры, которые никогда не используются, хуки для будущих фич. YAGNI.

**Fix:** Inline Function, Inline Class, Collapse Hierarchy, Remove Dead Code, Change Function Declaration (убрать лишние параметры).

### 17. Temporary Field

Поле класса, которое устанавливается только при определённых обстоятельствах, а в остальное время пустое или с дефолтным значением. Читатель кода ожидает, что поля несут данные всегда.

**Fix:** Extract Class (вынести «спящие» поля и код, который с ними работает, в отдельный класс), Introduce Special Case (заменить null на специальный объект).

### 18. Message Chains

`a.getB().getC().getD().doSomething()` — клиент связан со структурой навигации. Проблема: изменение промежуточных отношений ломает клиента.

**Fix:** Hide Delegate. Иногда — Extract Function + Move Function (создать метод там, где нужен результат).

### 19. Middle Man

Класс, который ничего не делает, кроме делегирования. Если половина методов — pass-through, класс бесполезен.

**Fix:** Remove Middle Man. Если Middle Man добавляет полезное поведение, оставить.

### 20. Inappropriate Intimacy

Два класса слишком много знают о внутренностях друг друга. Би-дирекциональные ссылки, доступ к приватным полям.

**Fix:** Move Function, Move Field, Change Bidirectional Association to Unidirectional, Replace Subclass with Delegate, Replace Superclass with Delegate.

### 21. Alternative Classes with Different Interfaces

Два класса делают одно и то же, но имеют разные сигнатуры методов. Симптом: дублирование логики с разным API.

**Fix:** Change Function Declaration, Move Function, Extract Superclass (до тех пор, пока протоколы не совпадут).

### 22. Data Class

Классы с геттерами/сеттерами и без поведения. Чистые контейнеры данных. Поведение размазано по клиентам.

**Fix:** Encapsulate Record, Remove Setting Method, Move Function (найти клиентов, которые работают с этими данными, и переместить логику в Data Class), Extract Function + Move.

### 23. Refused Bequest

Подкласс наследует методы/поля, которые ему не нужны. Нарушение LSP — подкласс не является полноценным наследником, он только использует часть.

**Fix:** Replace Subclass with Delegate (создать отдельный класс и делегировать), Replace Superclass with Delegate, Push Down Method/Field.

### 24. Comments

Комментарий, объясняющий *что* делает код (а не *почему*). Код должен быть самодокументируемым. Комментарий — признак того, что код не смог выразить намерение.

**Fix:** Extract Function, Change Function Declaration, Introduce Assertion. «Когда чувствуешь потребность написать комментарий, сначала попробуй переписать код так, чтобы комментарий стал лишним» — Fowler.

---

## Clean Code Smells (Martin)

Дополнительные запахи из Clean Code, не вошедшие в каталог Fowler:

### Bloaters (раздувание)

- **Large functions**: функция длиннее ~20 строк. Каждая функция должна делать ровно одно.
- **Large classes**: класс с >1 ответственностью. Признаки: много instance variables, название с «and», длинный список импортов.
- **Long parameter lists**: >3 аргументов. Вместо этого передавай объект, создавай parameter object.
- **Long chains of conditionals**: полиморфизм вместо switch/if-else. `switch` допустим в фабрике, которая создаёт полиморфные объекты, и только там.

### Dispensables (ненужное)

- **Duplicate code**: идентичный или структурно похожий код в нескольких местах. Extract method / Template Method.
- **Dead code**: unreachable код, закомментированный код. Удали.
- **Speculative generality**: код «на будущее», который сейчас не используется. Абстрактные классы с одним наследником, hooks, неиспользуемые параметры. YAGNI.

### Naming

- **Poor names**: однобуквенные переменные, невыразительные имена, непроизносимые имена, несогласованный словарь.

### Environment

- **Build requires more than one step**: checkout → одна команда (build/run). Builds с ручными шагами ненадёжны.
- **Tests require more than one step**: одна команда запускает все тесты. Иначе их не запускают.

### Tests

- **Insufficient tests**: тестовое покрытие не отвечает на вопрос «достаточно ли тестов для деплоя».
- **Missing edge cases**: тесты только на happy path.
- **Slow tests**: медленные тесты не запускают.

## Tradeoffs

- Запах — не баг, а индикатор. Не каждый запах требует немедленного действия.
- Некоторые запахи — временные компромиссы (deadline, отсутствие тестов).
- Контекст решает: Middle Man плох, пока не оказывается, что он изолирует клиента от нестабильного внешнего API.

## Связанные материалы

- [Functions](functions.md)
- [Classes](classes.md)
- [Emergence](emergence.md)
- [Meaningful Names](meaningful-names.md)
- [Refactoring](../fundamentals/refactoring.md)
- [Refactoring catalog](refactoring-catalog.md)
- [Refactoring and testing](refactoring-and-testing.md)
- [Refactoring (2nd ed.)](../../sources/books/refactoring-second-edition.md)
- [Clean Code](../../sources/books/clean-code.md)
