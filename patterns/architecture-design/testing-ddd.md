---
title: Testing DDD
type: pattern
category: ddd
tags: [ddd, domain-driven-design, testing, aggregates, domain-events, specifications]
source: Implementing Domain-Driven Design (Vaughn Vernon, 2013)
added: 2026-07-06
---

# Testing DDD

## Проблема

DDD models are rich with business rules, invariants, and domain events. Testing them through the UI or integration tests is slow, brittle, and misses edge cases. The domain model must be testable in isolation.

## Key concepts (Vaughan Vernon, Chapter 14 + throughout)

### Testing aggregates

Vernon's approach: test aggregates as isolated units — no database, no repositories, no message brokers.

```java
@Test
public void orderCannotExceedCreditLimit() {
    Customer customer = new Customer(id, new CreditLimit(Money.of(1000)));
    assertThrows(CreditLimitExceeded.class, () -> {
        customer.placeOrder(orderId, Money.of(1200));
    });
}
```

Key principles:
- **Test invariants aggressively:** every if-statement in an aggregate method deserves a test.
- **Test the full lifecycle:** create → transition through states → verify invariants at each transition.
- **Use test builders (not mocks):** create valid aggregate instances with a builder/factory. Vernon prefers real value objects over mocking them.
- **Fake, don't mock:** use in-memory repository implementations instead of mocking `OrderRepository`. Fakes verify behaviour while mocks verify implementation details.

### Testing domain events

Vernon describes two levels:

1. **Event production:** does the aggregate emit the right event at the right time?
```java
Order order = Order.place(orderId, customerId, items);
List<DomainEvent> events = order.flushEvents();
assertThat(events).containsExactly(instanceOf(OrderPlaced.class));
```

2. **Event handling:** does the event handler react correctly?
```java
OrderPlaced event = new OrderPlaced(orderId, ...);
handler.handle(event);
assertThat(inventoryRepo.get(productId).reserved()).isEqualTo(5);
```

### Testing application services (use cases)

Application services orchestrate: load aggregate → call method → persist → publish events. Vernon tests them with fakes:

```java
@Test
public void placeOrder_success() {
    OrderRepository repo = new InMemoryOrderRepository();
    OrderService service = new OrderService(repo, new FakeEventPublisher());

    service.placeOrder(new PlaceOrderCommand(orderId, customerId, items));

    Order saved = repo.get(orderId);
    assertThat(saved.status()).isEqualTo(OrderStatus.PLACED);
}
```

The fake event publisher records events in a list — verify they were published in the right order.

### Testing specifications and policies

Specifications (rules engines) and policies (reactions to events) should be tested as standalone domain services:

```java
@Test
public void shippingPolicy_ordersOver100_freeShipping() {
    ShippingPolicy policy = new FreeShippingOver(100);
    assertTrue(policy.isSatisfiedBy(orderOfValue(150)));
    assertFalse(policy.isSatisfiedBy(orderOfValue(50)));
}
```

### Testing saga / process managers

Vernon discusses long-running processes that react to multiple events. Test them as state machines:

1. Send event → verify state transition.
2. Send sequence of events → verify final state.
3. Send events out of order → verify idempotent handling.

### What NOT to test

Vernon cautions against:
- **Testing ORM mappings:** test the repository integration separately, not inside aggregate tests.
- **Testing framework plumbing:** controllers, DI wiring, HTTP routing — these are infrastructure, not domain.
- **Every possible event order:** test known sequences + edge cases; combinatorial explosion is not worth it.

## Testing pyramid for DDD

```
      /\
     /Ｅ2Ｅ\          Few: end-to-end (happy path)
    /──────\
   /Integration\     Some: repository + real DB, event publishing
  /────────────\
 /  Unit (Domain)\   Most: aggregates, value objects, domain services
/────────────────\
```

Vernon's rule: 80%+ of tests should be fast domain unit tests. Integration tests cover repository implementations and event publishing. E2E tests cover the critical user journeys only.

## Tradeoffs

**Pros:**
- Domain tests are fast (milliseconds) — run on every save.
- Catches business logic bugs, not just technical bugs.
- Tests serve as documentation of the ubiquitous language.

**Cons:**
- Requires discipline to write testable aggregates (no hidden infrastructure dependencies).
- Test builders add maintenance overhead.
- Not all teams are comfortable with "fake, don't mock" style.

## Связанные материалы

- [Aggregates](aggregates.md) — primary test subject
- [Domain Events](domain-events.md) — event production/handling tests
- [Repositories](repositories.md) — fake implementations for testing
- [Domain Services](domain-services.md) — testing stateless domain operations
- [CQRS](cqrs.md) — testing read-model projections
- [Event Sourcing](event-sourcing.md) — replay-based testing
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 14 (Application), examples throughout
