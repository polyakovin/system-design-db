---
title: Distribution Patterns
type: pattern
category: enterprise-architecture
tags: [patterns-of-enterprise-application-architecture, fowler, remote-facade, data-transfer-object, dto, distributed-systems]
source: Patterns of Enterprise Application Architecture (Martin Fowler, 2002)
added: 2026-07-06
---

# Distribution Patterns

При распределённой архитектуре (клиент-сервер, микросервисы) вызов методов через сеть имеет принципиально другую стоимость, чем локальный вызов. Два паттерна решают эту проблему.

## Data Transfer Object (DTO)

**Проблема:** при распределённой архитектуре каждый вызов метода — сетевой запрос. Вызвать `order.getCustomer().getName().getAddress()` — это 4 round-trip. Локально бесплатно, через сеть — сотни миллисекунд.

**Решение:** собрать все нужные данные в один объект и передать за один round-trip.

```java
// Без DTO — 3 сетевых вызова
Order order = remoteService.getOrder(id);
Customer customer = order.getCustomer();      // сетевой вызов
Address address = customer.getAddress();       // сетевой вызов

// С DTO — 1 сетевой вызов
OrderDTO dto = remoteService.getOrderDTO(id);
System.out.println(dto.customerName + " lives at " + dto.customerAddress);
```

**Ключевые свойства DTO:**
- Сериализуемый (JSON, XML, Protobuf) — передаётся по сети.
- Плоский или почти плоский — минимум вложенных графов.
- Не содержит логики — только данные (поля + getter/setter).
- Assembles данные из нескольких domain-объектов.

**Когда:** любой вызов через сеть (REST, RPC, message), где нужна агрегация данных из нескольких объектов.

**Когда не:** локальные вызовы (DTO — лишняя абстракция), или когда клиенту нужен ровно один простой объект.

## Remote Facade

**Проблема:** domain-модель имеет fine-grained интерфейс (много мелких методов). Клиенту через сеть нужны coarse-grained операции — одна операция = один бизнес-результат.

**Решение:** Remote Facade — coarse-grained фасад поверх fine-grained domain-модели для удалённых клиентов.

```java
// Domain model — fine-grained
order.setStatus("paid");
order.setPaidDate(now);
paymentGateway.process(order);
ledger.record(order);

// Remote Facade — coarse-grained
class OrderServiceFacade {
    public OrderResultDTO processPayment(PaymentRequestDTO request) {
        // Одна операция → весь бизнес-сценарий
        Order order = orderRepo.get(request.orderId);
        order.processPayment(request.amount);   // domain logic
        orderRepo.save(order);
        return OrderResultDTO.from(order);
    }
}
```

**Когда:** domain-модель используется удалённо (микросервисы, клиент-сервер), один use case затрагивает несколько domain-объектов.

**Когда не:** монолит (все вызовы локальные), простые CRUD-сервисы.

## Сочетание Remote Facade + DTO

Remote Facade определяет границу coarse-grained операций. DTO — формат данных, которыми они обмениваются. Стандартная связка:

> Remote Facade + DTO = coarse-grained API с агрегированными данными за один round-trip.

В REST: Remote Facade — это ресурс (endpoint), DTO — это JSON-тело ответа.

## Первое правило распределённых объектов (Fowler)

> Don't distribute your objects. Если можно не распределять — не распределяй. Распределение — не бесплатная абстракция, это архитектурное решение с реальной стоимостью (latency, serialization, versioning, partial failure).

## Связанные материалы

- [Session State](session-state.md)
- [Page Controller vs Front Controller](page-controller-vs-front-controller.md)
- [MVC Pattern Decomposition](mvc-pattern-decomposition.md)
- [Patterns of Enterprise Application Architecture](../../sources/books/patterns-of-enterprise-application-architecture.md) — главы 15, 16
