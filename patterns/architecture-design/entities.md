---
title: Entities
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, entities]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Entities

## Проблема

Некоторые объекты предметной области имеют непрерывную идентичность, которая не зависит от изменения их атрибутов. Если изменить адрес клиента, это всё тот же клиент.

## Решение

Выделить объекты, определяемые identity, а не атрибутами. Entity имеет уникальный идентификатор, который сохраняется на протяжении всего жизненного цикла, даже если все остальные поля меняются.

- **Identity:** уникальный ID (UUID, business key), неизменяемый после создания.
- **Мутабельность:** Entity может менять состояние, но identity — нет.
- **Equality:** два Entity равны, если у них одинаковый identity (а не одинаковые поля).
- **Жизненный цикл:** создаётся, изменяется, может быть удалён/архивирован.

## Когда Entity, а не Value Object

- Объект имеет собственную непрерывную идентичность в домене (человек, заказ, счёт).
- Нужно отслеживать объект во времени (история изменений состояния).
- Два объекта с одинаковыми атрибутами — это разные объекты (два клиента с одинаковым именем).

## Пример

```
class Customer:
    id: CustomerId    # identity — неизменяем
    name: str         # атрибуты — изменяемы
    email: Email      # value object внутри entity
    status: str

    def change_email(self, new_email: Email):
        self.email = new_email
```

## Типичные ошибки

- Превращать всё в Entity — многие объекты могут быть [Value Objects](value-objects.md).
- Использовать технические ID (автоинкремент БД) как часть доменной модели.
- Не различать equality по identity vs equality по состоянию.

## Связанные материалы

- [Value Objects](value-objects.md) — объекты без identity, определяемые атрибутами
- [Aggregates](aggregates.md) — Entity как aggregate root
- [Repositories](repositories.md) — хранение и поиск Entity
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — главы 5 (Entities) и 6 (Life Cycle)
