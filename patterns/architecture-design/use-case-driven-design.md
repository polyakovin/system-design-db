---
title: Use Case Driven Design
type: pattern
category: architecture
tags: [use-cases, interactors, input-port, output-port, testing, clean-architecture]
source: Clean Architecture (Robert C. Martin, 2017)
added: 2026-07-06
---

# Use Case Driven Design

## Проблема

Бизнес-логика рассеяна по контроллерам, сервисам и DAO-объектам. Невозможно понять, что система делает, глядя на код. Невозможно протестировать бизнес-правила без поднятия БД и веб-сервера.

## Решение

### Use Case как ядро архитектуры

Use case — объект, реализующий один сценарий предметной области. Получает вход, оркестрирует entities, отправляет выход.

```
Request Model → InputPort → UseCase/Interactor → OutputPort → Response Model
```

- **Interactor** (use case) — единственный метод: `execute(InputData): OutputData`. Не зависит от доставки (HTTP, CLI, очередь).
- **Input Port** — интерфейс, который реализует interactor. Вызывающая сторона знает только этот интерфейс.
- **Output Port** — интерфейс, через который interactor отправляет результат. Реализуется presenter'ом или gateway.
- **Input/Output Data** — простые структуры (DTO), не зависящие от фреймворков. Никаких HTTP-request объектов, никаких ORM-entity.

### Как use case работает

1. Принимает request data (простые структуры).
2. Загружает business entities через репозиторий (интерфейс, определённый в слое use cases).
3. Вызывает методы entities, выполняет бизнес-правила. Entities не знают, что их вызвал use case.
4. Отправляет результат через output port (presenter).

### Пример

```python
# Входной порт (определён в слое use cases)
class PlaceOrderInput:
    customer_id: str
    items: list[OrderItem]

class PlaceOrderOutput:
    order_id: str
    total: Money
    status: str

# Интерфейсы (определены в слое use cases)
class OrderRepository(ABC):
    def save(self, order: Order) -> None: ...
    def next_id(self) -> str: ...

class PlaceOrderPresenter(ABC):
    def success(self, output: PlaceOrderOutput) -> None: ...
    def out_of_stock(self, items: list[str]) -> None: ...

# Interactor (use case)
class PlaceOrderUseCase:
    def __init__(self, repo: OrderRepository, presenter: PlaceOrderPresenter):
        self.repo = repo
        self.presenter = presenter

    def execute(self, input: PlaceOrderInput) -> None:
        order = Order.create(input.customer_id, input.items)
        # Business entity handles logic, validates stock, etc.
        self.repo.save(order)
        self.presenter.success(PlaceOrderOutput(
            order_id=order.id, total=order.total, status="placed"
        ))
```

Интерактор зависит только от интерфейсов, определённых в своём слое. Не знает о БД, HTTP, фреймворке.

### Testing Approach

Use case testing **без фреймворков и инфраструктуры**:

- **Unit-test use case interactor**: подставь fake-реализации репозитория и presenter'а. Проверь, что presenter вызван с правильными данными.
- **Boundary testing**: тестируй use case на границе — входные данные, выходные данные, сценарии ошибок.
- Бизнес-правила тестируются быстро (in-memory, без БД).
- **Fake-реализации**: `FakeOrderRepository` с `dict` вместо БД. `FakePresenter`, записывающий вызовы для assert.
- Тесты пишутся **до production-адаптеров** — ты можешь разрабатывать и проверять бизнес-логику до того, как решил, какую БД использовать.

### Delivery-agnostic

Use case не знает, кто его вызывает:
- HTTP-контроллер берёт JSON, мапит в `PlaceOrderInput`, вызывает interactor.
- CLI-команда парсит аргументы, создаёт тот же input, тот же interactor.
- Тест создаёт input напрямую — без HTTP, без CLI.

Это значит, что вся бизнес-логика тестируется без поднятия сервера.

## Tradeoffs

- Use cases отделены от контроллеров → больше файлов. Окупается при первом же переиспользовании в другом delivery-канале.
- Interactor + input/output порты — overhead для `return repo.findById(id)`. CRUD-операциям не нужен interactor — вызывай репозиторий напрямую из контроллера.

## Связанные материалы

- [Clean Architecture](clean-architecture.md) — место use cases в концентрической модели
- [Architectural Boundaries](architectural-boundaries.md) — input/output порты как границы
- [Clean Architecture](clean-architecture.md) — use cases в концентрической модели, decoupled communication
- [Web as a Detail](web-as-detail.md) — UI-независимое тестирование
- [Database as a Detail](database-as-detail.md) — БД-независимое тестирование
- [Unit Tests](../../patterns/code-quality/unit-tests.md) — F.I.R.S.T., структура тестов
- [Clean Architecture](../../sources/books/clean-architecture.md) — книга-источник, главы 22–23 (The Clean Architecture, Presenters and Humble Objects)
