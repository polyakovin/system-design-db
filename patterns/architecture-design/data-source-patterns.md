---
title: Data Source Patterns
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, data-source, table-data-gateway, row-data-gateway, data-mapper]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Data Source Patterns

Три паттерна организации доступа к данным в Data Source Layer. Различаются гранулярностью и coupling между бизнес-логикой и схемой БД.

## Table Data Gateway

Один объект на таблицу. Инкапсулирует SQL-запросы к одной таблице (иногда с JOIN'ами). Возвращает простые структуры данных — DataSet, массивы, словари, DTO. Не возвращает domain-объекты.

```csharp
// Table Data Gateway — SQL на таблицу, возвращает RecordSet/DTO
class OrdersGateway {
    public DataSet FindByCustomerId(int customerId) {
        return db.Query("SELECT * FROM orders WHERE customer_id = ?", customerId);
    }
    public DataSet FindPending() {
        return db.Query("SELECT * FROM orders WHERE status = 'pending'");
    }
    public void UpdateStatus(int orderId, string status) {
        db.Execute("UPDATE orders SET status = ? WHERE id = ?", status, orderId);
    }
}
```

**Когда:** Transaction Script или Table Module — логика оперирует RecordSet'ами. Простой код, нет объектно-реляционного impedance mismatch.

**Плюсы:** простой интерфейс, легко тестировать (подмена gateway), естественно для процедурного кода.

**Минусы:** возвращает сырые данные (не domain-объекты), логика SQL размазана по gateway, нет identity map.

## Row Data Gateway

Один объект = одна строка таблицы. Объект содержит данные строки + CRUD-операции для этой строки. Похож на Active Record, но **без бизнес-логики** — только доступ к данным.

```ruby
# Row Data Gateway — объект = строка, только CRUD, без бизнес-логики
class OrderRow
  attr_accessor :id, :customer_id, :status, :total

  def self.find(id)
    row = db.execute("SELECT * FROM orders WHERE id = ?", id)
    OrderRow.new(row) if row
  end

  def insert
    db.execute("INSERT INTO orders (...) VALUES (?)", ...)
    @id = db.last_insert_id
  end

  def update
    db.execute("UPDATE orders SET ... WHERE id = ?", @id)
  end
end
```

**Когда:** Transaction Script, нужен объектный интерфейс к данным. Популярен в Ruby (DataMapper) и раннем Java (JDBC RowSet).

**Отличие от Active Record:** Row Data Gateway — **только доступ к данным**. Active Record добавляет бизнес-логику в тот же объект. Это вопрос coupling: если логика отдельно — Row Data Gateway, если в объекте — Active Record.

## Data Mapper

Слой-посредник между объектной моделью и реляционной БД. Переносит данные между объектами и таблицами, сохраняя их независимыми. Ни объекты не знают о БД, ни БД — об объектах.

```python
# Data Mapper — объекты и БД независимы
class Order:
    def __init__(self, id: int, status: str, total: Money):
        self.id = id
        self.status = status
        self.total = total
    # Никакого SQL, никакой ORM

class OrderMapper:
    def find(self, order_id: int) -> Optional[Order]:
        row = db.execute("SELECT * FROM orders WHERE id = ?", order_id)
        return Order(row['id'], row['status'], Money(row['total'])) if row else None

    def save(self, order: Order) -> None:
        db.execute("UPDATE orders SET status=?, total=? WHERE id=?",
                   order.status, order.total.amount, order.id)
```

**Когда:** Domain Model. Объекты чистые, без инфраструктурных зависимостей. ORM типа Hibernate, Entity Framework, SQLAlchemy реализуют Data Mapper (с разной степенью прозрачности).

**Плюсы:** полное разделение модели и БД, объекты тестируются без БД, схема БД может эволюционировать независимо.

**Минусы:** самый сложный из трёх, требует mapping-кода (ручного или ORM-конфигурации), overhead для простых случаев.

## Сравнение

| Критерий | Table Data Gateway | Row Data Gateway | Data Mapper |
|---|---|---|---|
| **Гранулярность** | Таблица | Строка | Объект → таблица(ы) |
| **Возвращает** | RecordSet/DTO | Row-объект с полями | Domain-объекты |
| **Бизнес-логика** | Отдельно | Отдельно | В domain-объектах |
| **Coupling** | Оба слоя видят схему БД | Row-объект знает БД | Объекты не знают о БД |
| **Парный паттерн** | Transaction Script / Table Module | Transaction Script | Domain Model |
| **Сложность реализации** | Низкая | Средняя | Высокая |

## Связанные материалы

- [Domain Model vs Transaction Script](domain-model-vs-transaction-script.md) — выбирай Data Mapper для Domain Model
- [Table Module vs Active Record](table-module-vs-active-record.md)
- [Object-Relational Patterns](object-relational-patterns.md) — Unit of Work, Identity Map, Lazy Load
- [Repositories](repositories.md) — DDD-эволюция Data Mapper
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 10, 11, 12
