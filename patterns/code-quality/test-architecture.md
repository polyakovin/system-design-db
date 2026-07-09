---
title: Test Architecture
category: patterns
tags: [testing, test-architecture, flexible-design, maintainability, port-adapter, comments, emergence]
source: multiple
added: 2026-07-10
updated: 2026-07-10
---

# Test Architecture

## Проблема

Тесты пишутся как линейные скрипты — setup → act → assert — и со временем становятся главным тормозом разработки. Они хрупкие (падают при любом рефакторинге), нечитаемые (куча бойлерплейта) и недоверительные (никто не понимает, что на самом деле тестируется). Корень проблемы — не в количестве тестов, а в их архитектуре.

Дополнительная проблема: жёсткая архитектура тестов. Когда тесты зафиксированы в одной схеме (например, «все тесты через моки» или «все тесты интеграционные»), любое изменение в production-коде требует перелопачивания всей тестовой базы. Тесты должны быть гибкими — адаптироваться под изменения, а не сопротивляться им.

## Решение

Применяй к тестовому коду те же принципы архитектуры, что и к production-коду: SRP, dependency inversion, [clean boundaries](boundaries.md), выразительные имена. Тесты — полноценная кодовая база, а не скрипты второго сорта.

Главный принцип гибкой архитектуры тестов: **тесты — это дизайн-система, а не набор скриптов**. Как и любая дизайн-система, она должна быть:

- **Адаптируемой** — изменения в одной части не ломают другую;
- **Выразительной** — назначение каждого теста ясно из его структуры;
- **Экономичной** — минимальное количество кода для максимальной уверенности (см. [Emergence](emergence.md)).

### 1. Адаптируемое разделение слоёв (Flexible Port/Adapter)

Раздели тесты на уровни не как жёсткую иерархию, а как **спектр** — от быстрых доменных тестов до медленных интеграционных. Чем ближе к домену — тем быстрее и изолированнее тест. Чем ближе к инфраструктуре — тем интеграционнее.

```
  Быстро, изолированно          Медленно, интеграционно
  ─────────────────────────────────────────────────────>
  Domain Tests → Use-Case Tests → Adapter Tests → E2E Tests
       ↑                             ↑
  Чистая логика            Проверка связки с реальным миром
```

**Domain Tests** — бизнес-правила, инварианты, value objects. Работают без БД, без сети, без DI. Один тест — одно правило. Это самые стабильные тесты: они меняются только при изменении бизнес-логики.

**Use-Case / Scenario Tests** — поведение системы в координированном сценарии. Могут использовать fake-репозитории (in-memory), но не реальную БД. Проверяют, что use case корректно оркестрирует доменные объекты.

**Adapter Tests** — инфраструктурный код: репозитории, контроллеры, сериализаторы. Проверяют, что порт (интерфейс) правильно реализован поверх реальной БД / API / файловой системы.

**E2E Tests** — самые медленные и хрупкие. Используй точечно: критический пользовательский путь, платёжные сценарии.

#### Гибкость, а не догма

Границы между слоями — не бетонная стена, а мембрана. Если в проекте нет выделенного порта (интерфейса) — не создавай его «для тестов». Вместо этого:

- Тестируй сервис напрямую с in-memory реализацией, если она легко подключается.
- Если смена БД не планируется — интеграционные тесты на реальную БД дешевле, чем абстракция с fake.

**Ключевой вопрос: «Когда этот тест сломается?»** Если ответ «при любом изменении реализации» — ты тестируешь не то. Перестрой тест на уровень выше (domain) или используй fake.

#### Пример: плохая архитектура

```python
def test_order_creation():
    # Смесь domain + инфраструктуры — хрупко
    db = connect_to_test_db()
    repo = PostgresOrderRepository(db)
    service = OrderService(repo)
    service.create_order(user_id=1, items=[...])
    rows = db.query("SELECT * FROM orders WHERE user_id=1")
    assert len(rows) == 1
```

#### Пример: гибкая архитектура

```python
# Domain test — fast, no DB, pure business logic
def test_order_limits_invariant():
    order = OrderFactory.create(with_items=[...])
    order.add_item(heavy_item)
    # Проверка инварианта домена, не инфраструктуры
    assert order.total_weight() <= Order.MAX_WEIGHT

# Use-Case test — fake repo, проверяет сценарий целиком
def test_place_order_creates_pending_shipment():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    order = service.place_order(customer_id=1, items=[...])

    saved = repo.load(order.id)
    assert saved.status == OrderStatus.PLACED
    assert saved.shipment.status == ShipmentStatus.PENDING

# Adapter test — проверяет только mapping к реальной БД
def test_postgres_order_repository_saves_and_loads():
    repo = PostgresOrderRepository(test_db)
    order = OrderFactory.create(id=OrderId("abc-123"))
    repo.save(order)
    loaded = repo.load(OrderId("abc-123"))
    assert loaded.id == order.id
    assert loaded.total() == order.total()
```

Каждый уровень независим. Можно переписать adapter на MongoDB — domain и use-case тесты не меняются.

### 2. Гибкие фикстуры: Builders, Factories, Object Mothers

Когда у агрегата десяток обязательных полей, каждый тест начинает с громоздкого конструктора. Тест становится нечитаемым, а добавление нового поля ломает все тесты сразу.

**Плохо:** прямой вызов конструктора в каждом тесте.

```java
Order order = new Order(
    new OrderId("123"),
    new CustomerId("456"),
    LocalDateTime.now(),
    OrderStatus.DRAFT,
    List.of(new OrderLine("SKU-1", 2, Money.of(100))),
    Address.empty()
);
```

**Гибкий подход:** выбирай инструмент под задачу.

| Инструмент | Когда использовать |
|---|---|
| **Test Data Builder** | Объект сложный (>5 полей), большинство полей — разумные умолчания |
| **Factory Method** | Нужна вариативность: `createDraftOrder()`, `createConfirmedOrder()` |
| **Object Mother** | Один и тот же «типовой» объект используется в десятках тестов |
| **Inline Construction** | Объект простой (2–3 поля), тест один |

```java
// Builder — гибкие умолчания, переопределяешь только нужное
Order order = OrderBuilder.defaultOrder()
    .withId("123")
    .withLine("SKU-1", 2, 100)
    .build();

// Factory — именованные варианты, читается как DSL
Order draft = OrderFactory.draftForCustomer("123");
Order confirmed = OrderFactory.confirmedWithLines("123", lines);

// Object Mother — константы-образцы
Order sample = SampleOrders.standardWithTwoLines();
```

Каждый подход решает свою проблему. Если проект маленький — inline достаточно. Builder окупается, когда тестов > 30 и конструктор меняется хотя бы раз.

См. также: [Supple Design](../architecture-design/supple-design.md) — intention-revealing interfaces, standalone classes.

### 3. Коммуникация через код: комментарии + имена + структура

Тестовый код — первичная документация системы (см. [Emergence](emergence.md)). Хороший тест читается как спецификация. Гибкая архитектура тестов использует **все три инструмента** коммуникации, выбирая уместный:

#### Имена: Given-When-Then как контракт

Лучший «комментарий» для теста — его имя. Используй структуру, которая раскрывает намерение:

```python
def test_givenOrderOverThreshold_whenShippingCalculated_thenFreeShipping():
    # ...
```

Или вложенный describe/it стиль (pytest, vitest, JUnit 5):

```python
class TestShipping:
    def test_free_shipping_over_100(self):
        ...
    def test_standard_shipping_under_100(self):
        ...
```

#### Структура: Arrange-Act-Assert как шаблон

Трёхчастная структура (или Given-When-Then) — минимальный шаблон. Не добавляй в тест ничего вне этих секций. Если секция становится большой — вынеси в helper.

```python
def test_cancel_confirmed_order():
    # Arrange
    order = OrderBuilder.default().withStatus(CONFIRMED).build()
    service = OrderService(InMemoryOrderRepository())

    # Act
    result = service.cancel(order.id)

    # Assert
    assert result.status == CANCELLED
```

#### Комментарии: только «почему»

Комментарий в тесте оправдан, когда он объясняет **причину**, неочевидную из кода.

| Тип | Пример | Зачем |
|-----|--------|-------|
| **Why, not what** | `# Vendor API rounds to 2 decimals — we must match` | Объясняет внешнее ограничение |
| **Spec reference** | `# Implements ACID-07: partial refund must not exceed original` | Связь с требованиями |
| **Known limitation** | `# Skipping edge case X — see ticket T-42` | Честность о coverage |
| **Performance note** | `# This test takes > 30s. Only run on CI.` | Предупреждение последствий |
| **Intent of complex setup** | `# Creating order with weight=101 to trigger freight check` | Почему именно эти данные |

**Что НЕ нужно комментировать:**

- Очевидное — `assert result == 5` не требует `# Assert the result is 5`
- Историю — `# Added by Ivan` (VCS хранит историю)
- Закомментированный код — удаляй его
- Нарратив — `# Now we create the user...` (тест должен читаться без подсказок)

См. также: [Comments](comments.md) — общие принципы хороших и плохих комментариев.

### 4. Проверка поведения, а не реализации

Vernon's advice: **fake, don't mock**. Тест с моками проверяет *как* вызван метод, а не *что* получилось. Это coupling к реализации — тест падает при рефакторинге, даже когда поведение верное.

**Mock (хрупкий):** проверяет вызовы.

```python
repo = Mock(OrderRepository)
service = OrderService(repo)
service.place_order(...)
repo.save.assert_called_once_with(order_matcher)
```

**Fake (гибкий):** проверяет состояние.

```python
repo = InMemoryOrderRepository()
service = OrderService(repo)
service.place_order(...)
saved = repo.load(order_id)
assert saved.status == OrderStatus.PLACED
```

Но и здесь гибкость: **иногда mock — правильный выбор**.

- Когда fake сложнее mocked-вызова (например, внешний HTTP-клиент).
- Когда реальная реализация имеет побочные эффекты вне твоего контроля.
- Для «глупых» объектов (логгер, метрики) — mock дешевле и читаемее fake.

**Контрактное тестирование** — мост между fake и реальной реализацией. Напиши один набор тестов контракта (interface contract) и прогони его и на fake, и на реальном адаптере. Если поведение расходится — тесты упадут на обеих реализациях.

```python
# Contract test — выполняется и для InMemoryOrderRepository, и для PostgresOrderRepository
class OrderRepositoryContract:
    def test_save_and_load_by_id(self, repo):
        order = OrderFactory.create()
        repo.save(order)
        loaded = repo.load(order.id)
        assert loaded.id == order.id
        assert loaded.total() == order.total()
```

### 5. Изоляция через свежие фикстуры, не через shared state

Переиспользование состояния через `@BeforeClass` / `setUpClass` создаёт неявные зависимости между тестами. Тесты перестают быть независимыми — порядок выполнения влияет на результат.

**Вместо этого:** создавай свежий fixture на каждый тест. Но не копируй setup-код — фабрикуй через builders и helper methods.

```python
# Вредно: shared state
class TestOrderService:
    order: Order  # set once in setUpClass

    def test_cancel(self):
        self.order.cancel()
        assert self.order.status == CANCELLED

    def test_approve(self):
        # FAILS! order уже cancelled
        self.order.approve()
```

```python
# Хорошо: fresh fixture per test
class TestOrderService:
    def _create_order(self, **overrides) -> Order:
        return OrderBuilder.default().withFields(**overrides).build()

    def test_cancel(self):
        order = self._create_order()
        order.cancel()
        assert order.status == CANCELLED

    def test_approve(self):
        order = self._create_order(status=DRAFT)
        order.approve()
        assert order.status == APPROVED
```

**Исключение:** неизменяемые конфигурационные данные (список стран, enum values, константы). Их можно вынести в shared fixtures — они не меняются между тестами и не создают зависимостей.

### 6. Ассерты как спецификация

Плохой assert скрывает проблему. Хороший assert — specificity и readability.

**Плохо:**
```python
assert result is not None
assert len(result) == 3
assert result[0].name == "Alice"
```

**Хорошо:**
```python
assert result == [
    User(name="Alice", role="admin"),
    User(name="Bob", role="user"),
    User(name="Charlie", role="user"),
]
```

**Гибкий подход:** используй custom matchers/assertion helpers, когда:

- Сравнение сложное (вложенные структуры, игнорирование полей);
- Failure message должен быть информативным («expected X but got Y» вместо «False is not True»);
- Одна и та же проверка повторяется в нескольких тестах.

```python
assert_that(result).containsExactly(
    hasField("name", "Alice"),
    hasField("role", "admin"),
)
```

## Tradeoffs

| Практика | Плюсы | Минусы | Когда выбирать |
|----------|-------|--------|----------------|
| Port/Adapter test layers | Изоляция domain от инфраструктуры; тесты не падают при смене БД | Больше файлов; нужно проектировать порты заранее | Проект живёт >6 месяцев, планируется смена БД/API |
| Flexible fixture strategy | Нет over-engineering для маленьких проектов; читаемые тесты | Нужно понимать, когда какой инструмент выбрать | Всегда — как spectrum, не как binary choice |
| Fakes with contract tests | Тесты не ломаются при рефакторинге; проверяют поведение | Fake может расходиться с реализацией; overhead написания | Domain и use-case слои; adapter слои через contract tests |
| Fresh fixture per test | Полная изоляция; детерминизм | Больше объектов создаётся (но тесты — не production) | Всегда для тестов, проверяющих разное состояние |
| Expressive assertions | Понятный failure message; самодокументируемость | Дополнительные helper-классы | Для сложной бизнес-логики; для повторяющихся проверок |

## When NOT to Apply

- **Скрипты и прототипы:** если код живёт меньше недели, архитектура тестов — over-engineering. Достаточно линейных скриптов.
- **Legacy code:** сначала characterization tests (Golden Master), потом рефакторинг. Не пытайся «архитектурировать» тесты legacy — сначала сделай их зелёными.
- **Pure data transformations:** для функций вида `A → B` без побочных эффектов достаточно простых parametrized tests. Builders и порты тут избыточны.
- **Tiny projects (<500 LOC):** хорошие имена и AAA-структура — уже достаточно. Полноценная test architecture начинается, когда тестов становится больше, чем production-кода.

## Связанные материалы

- [Unit tests](unit-tests.md) — F.I.R.S.T., clean test structure
- [Testing DDD](../architecture-design/testing-ddd.md) — domain testing patterns, fakes
- [Refactoring and testing](refactoring-and-testing.md) — self-testing code prerequisite
- [Design precedes testing](../fundamentals/design-precedes-testing.md) — design is primary
- [Supple Design](../architecture-design/supple-design.md) — standalone classes, intention-revealing interfaces
- [Systems](systems.md) — separation of main, dependency injection
- [Boundaries](boundaries.md) — clean boundaries, learning tests
- [Comments](comments.md) — good vs bad comments
- [Emergence](emergence.md) — simple design: tests, no duplication, intent, minimal
