---
title: Value Objects
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, value-objects]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Value Objects

## Проблема

Многие понятия в домене не имеют собственной идентичности, а описывают свойства других объектов. Адрес, сумма денег, дата, цвет — если адрес изменился, это не «тот же адрес с новыми полями», это другой адрес.

## Решение

Value Object — иммутабельный объект, полностью определяемый своими атрибутами. Равенство — по значению всех полей. Замена — только целиком.

- **Иммутабельность:** после создания не меняется. Изменение = создание нового VO.
- **Equality по значению:** два VO равны, если все их поля равны.
- **Side-effect-free:** методы возвращают новый VO, не меняя существующий.
- **Самодокументирование:** VO несёт доменный смысл (Email, а не `str`; Money, а не `Decimal`).

## Когда Value Object, а не Entity

- Объект не имеет собственной непрерывной идентичности.
- Замена объекта не меняет смысла — если у двух заказов одинаковый адрес доставки, это эквивалентные адреса.
- Объект описывает свойство, а не действующее лицо.

## Пример

```python
@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def add(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)
```

## Типичные ошибки

- Делать VO мутабельным — теряется predictability.
- Использовать примитивы вместо VO (primitive obsession: `str` вместо `Email`).
- Добавлять identity полю — тогда он становится Entity.

## Связанные материалы

- [Entities](entities.md) — объекты с identity
- [Aggregates](aggregates.md) — VO внутри агрегата
- [Supple Design](supple-design.md) — side-effect-free functions
- [Domain-Driven Design](../../sources/books/domain-driven-design.md)
