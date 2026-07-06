---
title: Domain Services
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, services]
source: Domain-Driven Design (Eric Evans, 2010)
added: 2026-07-06
---

# Domain Services

## Проблема

Некоторые операции предметной области не принадлежат ни одному Entity или Value Object. Попытка «впихнуть» их в Entity нарушает Single Responsibility Principle или требует искусственного владельца («кому принадлежит перевод денег между счетами?»).

## Решение

Domain Service — stateless операция, которая выполняет доменную логику, не вписывающуюся естественно в Entity/VO. Сервис ничего не хранит, только координирует объекты.

- **Stateless:** нет полей, только методы. Чистая функция от входных данных и доменных объектов.
- **Имя — часть Ubiquitous Language:** `TransferService.transfer()`, `PricingService.calculate_price()`.
- **Не путать с Application Service:** Domain Service содержит бизнес-логику; Application Service — оркестрацию (транзакции, вызов репозиториев, отправку событий).

## Когда нужен Domain Service

- Операция затрагивает несколько агрегатов (перевод денег между счетами).
- Операция не имеет естественного владельца среди Entity.
- Сложный алгоритм или бизнес-правило, которое не хочется раздувать в Entity.

## Пример

```python
class TransferService:
    """Domain service: переводит деньги между счетами."""

    def transfer(
        self,
        source: Account,
        target: Account,
        amount: Money
    ) -> None:
        if source.balance < amount:
            raise InsufficientFundsError()
        source.debit(amount)
        target.credit(amount)
```

## Антипаттерны

- **Anemic Domain Model:** вся логика в сервисах, Entity — просто DTO с геттерами/сеттерами.
- **Domain Service с состоянием:** сервис помнит что-то между вызовами.
- **Путаница с Application Service:** Domain Service — бизнес-логика, Application Service — инфраструктурная оркестрация.

## Связанные материалы

- [Entities](entities.md)
- [Aggregates](aggregates.md)
- [Layered Architecture](layered-architecture.md) — где живёт сервис
- [Domain-Driven Design](../../sources/books/domain-driven-design.md) — глава 5
