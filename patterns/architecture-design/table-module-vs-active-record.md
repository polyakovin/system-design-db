---
title: Table Module vs Active Record
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, domain-logic, table-module, active-record]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Table Module vs Active Record

Два паттерна middleware-сложности: проще Domain Model, мощнее Transaction Script. Оба привязаны к реляционной модели данных, но по-разному.

## Table Module

Один объект на таблицу БД. Объект содержит **всю бизнес-логику для всех строк таблицы**. Это не одна строка — это вся таблица как модуль.

```csharp
// Table Module — один объект на таблицу, работает с RecordSet'ами
class OrdersTable {
    public DataSet GetAllPending() { /* SELECT * FROM orders WHERE status='pending' */ }
    public void ProcessPayment(int orderId, decimal amount) {
        // бизнес-логика поверх DataSet
    }
    public decimal CalculateTotalForCustomer(int customerId) { /* агрегация */ }
}
```

**Ключевая идея:** Table Module работает с RecordSet/Dataset — структурами данных, а не с отдельными объектами. Хорошо ложится на .NET DataSet, ADO.NET.

**Когда применять:** логика средней сложности, таблицы — естественная единица организации, платформа хорошо поддерживает RecordSet (C#, VB.NET), мало зависимостей между таблицами.

**Когда не применять:** сложные связи между объектами, глубокое объектное моделирование.

## Active Record

Объект = строка в таблице. Объект содержит **и данные, и доступ к БД, и бизнес-логику**. Знает, как сохранить и загрузить себя.

```ruby
# Active Record — объект = строка, сам себя сохраняет
class Order < ActiveRecord::Base
  validates :status, presence: true

  def process_payment(amount)
    raise "Not pending" unless status == "pending"
    raise "Amount mismatch" unless total == amount
    update!(status: "paid")
    Payment.create!(order_id: id, amount: amount)
  end
end
```

**Ключевая идея:** объект инкапсулирует данные строки + CRUD-операции + бизнес-логику. Ruby on Rails, Laravel Eloquent, Yii — классические примеры.

**Когда применять:** структура объекта близка к структуре таблицы (одна строка — один объект), простые или средние бизнес-правила, фреймворк с готовым AR (Rails, Laravel).

**Когда не применять:** сложные связи между объектами (несколько таблиц на объект), сложные бизнес-правила не укладываются в CRUD.

## Сравнение

| Критерий | Table Module | Active Record |
|---|---|---|
| **Гранулярность** | Таблица | Строка |
| **Данные** | RecordSet/Dataset | Объект со свойствами |
| **БД-доступ** | В модуле (ручной SQL) | В объекте (ORM) |
| **Связи** | JOIN'ы в SQL, ручная сборка | belongs_to, has_many |
| **Платформы** | .NET, ADO.NET | Rails, Laravel, Hibernate (базовый) |
| **Миграция к Domain Model** | Сложнее — логика на таблицах | Легче — объекты уже есть |

## Fowler's Decision Tree (упрощённо)

```
Сложная логика? ──→ Domain Model
Средняя логика?
  ├── Объекты близки к таблицам? ──→ Active Record
  └── Удобно оперировать таблицами? ──→ Table Module
Простая логика? ──→ Transaction Script
```

## Связанные материалы

- [Domain Model vs Transaction Script](domain-model-vs-transaction-script.md)
- [Data Source Patterns](data-source-patterns.md) — Table Data Gateway, Row Data Gateway, Data Mapper
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 2, 3, 4
