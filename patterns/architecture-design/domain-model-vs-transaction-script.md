---
title: Domain Model vs Transaction Script
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, domain-logic, transaction-script, domain-model]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Domain Model vs Transaction Script

Выбор способа организации бизнес-логики — фундаментальное архитектурное решение. Fowler выделяет три паттерна: **Transaction Script**, **Domain Model** и **Table Module**.

## Transaction Script

Бизнес-логика организована по процедурам — одна процедура на каждый use case (Create Order, Process Payment). Скрипт читает данные из БД, обрабатывает, сохраняет. Простая последовательная логика без объектов.

```python
# Transaction Script — процедурный подход
def process_payment(order_id: int, amount: float) -> None:
    with db.transaction():
        order = db.execute("SELECT * FROM orders WHERE id = ?", order_id)
        if order["status"] != "pending":
            raise ValueError("Order not pending")
        if order["total"] != amount:
            raise ValueError("Amount mismatch")
        db.execute("UPDATE orders SET status = 'paid' WHERE id = ?", order_id)
        db.execute("INSERT INTO payments (order_id, amount) VALUES (?, ?)", order_id, amount)
```

**Когда применять:** простая логика, немного use cases, CRUD-приложения, команда привыкла к процедурному стилю.

**Когда не применять:** сложные бизнес-правила, много условной логики, пересекающиеся сценарии — Transaction Script дублируется.

## Domain Model

Бизнес-логика живёт в объектах, отражающих предметную область. Объекты (Entities, Value Objects) инкапсулируют данные и поведение. Use case оркестрирует объекты, но логика внутри них.

```python
# Domain Model — объектный подход
class Order:
    def __init__(self, id: OrderId, status: str, total: Money):
        self.id = id
        self.status = status
        self.total = total

    def process_payment(self, amount: Money) -> Payment:
        if self.status != "pending":
            raise ValueError("Order not pending")
        if self.total != amount:
            raise ValueError("Amount mismatch")
        self.status = "paid"
        return Payment(self.id, amount)
```

**Когда применять:** сложные бизнес-правила, много сущностей с поведением, пересекающиеся use cases, долгоживущий проект с частыми изменениями логики.

**Когда не применять:** простые CRUD-приложения — overhead создания объектной модели не оправдан. Fowler: «Не используй Domain Model если твоя логика проста — Transaction Script достаточно.»

## Tradeoffs

| Критерий | Transaction Script | Domain Model |
|---|---|---|
| **Сложность старта** | Низкая — пара функций | Высокая — нужна модель |
| **Масштабирование сложности** | Экспоненциальный рост дублирования | Линейный рост — логика в одном месте |
| **Тестируемость** | Интеграционные тесты с БД | Модульные тесты без БД |
| **Рефакторинг** | Размазанная логика → сложно | Локализованная логика → легче |
| **Производительность** | Прямые SQL-запросы → быстро | ORM overhead, N+1 traps |

## Fowler's Rule of Thumb

> Если логика умещается в 3-5 экранов кода и не имеет сложных правил — Transaction Script. Если правил больше, они меняются, и есть пересечения между use cases — Domain Model.

## Связанные материалы

- [Table Module vs Active Record](table-module-vs-active-record.md) — альтернативные паттерны domain-логики
- [Layered Architecture](layered-architecture.md) — Domain Layer, где живёт эта логика
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 2-4
