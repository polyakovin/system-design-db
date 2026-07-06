---
title: Object-Relational Patterns
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, unit-of-work, identity-map, lazy-load, orm]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Object-Relational Patterns

Три паттерна, решающие проблемы объектно-реляционного отображения: согласованность изменений (Unit of Work), дублирование объектов (Identity Map) и производительность загрузки (Lazy Load).

## Unit of Work

**Проблема:** бизнес-операция изменяет несколько объектов, но сохранять их по-одному нельзя — получится несогласованное состояние при ошибке или параллельном доступе. Отслеживание того, что изменилось в рамках одной транзакции, размазывается по коду.

**Решение:** Unit of Work отслеживает все объекты, затронутые бизнес-транзакцией, и сохраняет их одним скоординированным коммитом. Хранит списки: new, dirty, deleted объектов.

```python
class UnitOfWork:
    def __init__(self):
        self._new: List[object] = []
        self._dirty: List[object] = []
        self._deleted: List[object] = []

    def register_new(self, obj): self._new.append(obj)
    def register_dirty(self, obj): self._dirty.append(obj)
    def register_deleted(self, obj): self._deleted.append(obj)

    def commit(self):
        # Порядок важен: insert → update → delete
        for obj in self._new: mapper.insert(obj)
        for obj in self._dirty: mapper.update(obj)
        for obj in self._deleted: mapper.delete(obj)
        self._new.clear(); self._dirty.clear(); self._deleted.clear()
```

**Ключевая идея:** объекты не сохраняют себя сами. Они регистрируются в UoW, а UoW решает порядок и batch-операции при commit.

**Когда применять:** Domain Model с Data Mapper, сложные бизнес-транзакции с несколькими объектами, нужна atomicity изменений.

**Когда не применять:** Transaction Script с Table Data Gateway (сохранение явное и последовательное), Active Record (объект сам знает, как сохраниться).

## Identity Map

**Проблема:** если дважды загрузить один и тот же объект из БД в рамках одной сессии, получится два разных экземпляра. Изменения в одном не отразятся на другом → баги, inconsistent reads.

**Решение:** Identity Map — кэш в памяти, который гарантирует, что каждый объект загружается из БД ровно один раз за сессию. Повторный запрос возвращает тот же экземпляр.

```python
class IdentityMap:
    def __init__(self):
        self._objects: Dict[Type, Dict[int, object]] = {}

    def get(self, cls, id) -> Optional[object]:
        return self._objects.get(cls, {}).get(id)

    def put(self, obj, id):
        cls = type(obj)
        if cls not in self._objects:
            self._objects[cls] = {}
        self._objects[cls][id] = obj
```

**Ключевой контракт:** «в пределах сессии — один объект на одну строку БД». ORM (Hibernate, Entity Framework) реализуют Identity Map как Session/Context.

**Когда применять:** всегда, когда несколько операций в одной сессии могут обращаться к одному объекту.

**Tradeoff:** память — Identity Map хранит все загруженные объекты. Для batch-обработки (миллионы строк) нужен stateless-режим (stateless session в Hibernate).

## Lazy Load

**Проблема:** загрузка объекта с его графом зависимостей (Order → OrderLines → Products → Categories) приводит к загрузке всей БД. N+1 запросов или гигантский JOIN.

**Решение:** Lazy Load откладывает загрузку связанных объектов до первого обращения к ним. Объект содержит прокси/заглушку, которая делает запрос при первом вызове getter'а.

Реализации:
- **Lazy Initialization:** поле = null → при доступе загружаем. Простейший вариант.
- **Virtual Proxy:** объект-заглушка того же типа, при первом вызове метода загружает реальный объект.
- **Value Holder:** объект-обёртка с методом `getValue()`, загружающая данные при вызове.
- **Ghost:** объект с ID, но без данных. При первом доступе к полю загружает всё остальное.

```python
class Order:
    def __init__(self, id: int, customer_loader):
        self.id = id
        self._customer_loader = customer_loader  # callable
        self._customer = None  # lazy field

    @property
    def customer(self):
        if self._customer is None:
            self._customer = self._customer_loader(self.id)
        return self._customer
```

**Когда применять:** графы объектов с глубокими связями, где не всегда нужны все связанные данные.

**Опасность:** `LazyInitializationException` (Hibernate) при обращении к lazy-полю вне транзакции/сессии. Решение: eager fetch для данных, которые точно нужны, open session in view (анти-паттерн), или explicit fetch в application-слое.

## Связка паттернов в ORM

Типичный ORM-стек: **Data Mapper + Unit of Work + Identity Map + Lazy Load.** Unit of Work и Identity Map — session-scoped (одна бизнес-транзакция). Lazy Load — per-object. Data Mapper — singleton.

## Связанные материалы

- [Data Source Patterns](data-source-patterns.md)
- [Repositories](repositories.md) — DDD-версия абстракции над Data Mapper
- [Offline Concurrency](offline-concurrency.md) — pessimistic/optimistic lock над Unit of Work
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 11, 12, 13, 14
