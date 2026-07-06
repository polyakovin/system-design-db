---
title: Event-Driven Architecture Patterns
type: pattern
category: ddd
tags: [ddd, domain-driven-design, eda, event-driven, messaging, patterns]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Event-Driven Architecture Patterns

## Проблема

Evans and Vernon cover Domain Events and Event Sourcing, but Millett goes further into practical **event-driven architecture (EDA)** patterns that go beyond persistence. How do you design event schemas? When do you use commands vs. events? How do you handle ordering, deduplication, and event chains in production?

## Millett's EDA patterns

### 1. Event vs. Command

A recurring confusion: "should I send a command or an event?"

| | Command | Event |
|---|---|---|
| Intent | Request something to happen | State that something happened |
| Naming | Imperative: `PlaceOrder` | Past tense: `OrderPlaced` |
| Ownership | Consumer decides to accept/reject | Producer owns the fact — it happened |
| Rejection | Consumer can reject (validation) | Cannot be rejected — it's a fact |
| Addressing | Point-to-point (specific handler) | Broadcast (any subscriber can listen) |

Millett's rule: **use commands for intent, events for facts.** If the receiver has a choice, it's a command. If it's a fait accompli, it's an event.

### 2. Event-Carried State Transfer

How much data should an event carry? Millett describes the spectrum:

- **Fat events (full state):** consumer gets everything it needs without calling back. Decouples at runtime, but couples on schema — any field change breaks consumers.
- **Thin events (ID only):** `OrderPlaced(orderId)`. Consumer calls back for details. Loose schema coupling, tight runtime coupling — consumer can't function without producer's API.
- **Hybrid (Millett's default):** carry the data consumers *always* need (identity + key attributes), let them call back for the rest. `OrderPlaced(orderId, customerId, total, itemCount)`.

### 3. Event notification vs. Event-Carried State Transfer vs. Event Sourcing

Millett distinguishes three levels:

| Pattern | Event carries | Consumer action | Use case |
|---|---|---|---|
| Event Notification | Minimal (ID + timestamp) | Call back to producer | Fine when producer API is always available |
| Event-Carried State Transfer | Full snapshot of changed data | No callback needed | Cross-BC integration, disconnected systems |
| Event Sourcing | State delta / full event | Replay to rebuild state | Audit, temporal queries, multiple read models |

### 4. Event chain patterns

Events rarely exist in isolation. Millett documents common event chains:

**Fan-out:** one event triggers multiple independent handlers.
```
OrderPlaced → [InventoryReserver, PaymentProcessor, EmailSender]
```

**Chain (pipeline):** each handler produces the next event.
```
OrderPlaced → OrderValidated → PaymentAuthorized → OrderConfirmed
```

**Aggregation:** multiple events combine to trigger one action.
```
(PaymentAuthorized + InventoryReserved) → OrderConfirmed
```

**Dead-letter chain:** events that fail repeatedly go to a dead-letter queue for manual inspection.

### 5. Ordering guarantees

Millett is pragmatic about ordering:

- **Within an aggregate stream:** events MUST be ordered. If `OrderShipped` arrives before `OrderPlaced`, the consumer's state is corrupted. Use partition key = aggregate ID.
- **Across aggregates:** ordering is NOT guaranteed and SHOULD NOT be assumed. Design consumers to handle out-of-order arrival.
- **Causality:** if event B depends on event A, encode this explicitly (correlation ID, causation ID) rather than relying on delivery order.

### 6. Idempotent consumers — Millett's approach

Every event consumer MUST be idempotent. Millett's pattern:

```csharp
public void Handle(OrderPlaced @event) {
    if (_processedEvents.Contains(@event.EventId))
        return; // already processed

    // ... process ...

    _processedEvents.Mark(@event.EventId); // in same transaction
}
```

Store processed event IDs in the same database as the consumer's state — a single transaction guarantees exactly-once processing.

### 7. Event versioning and schema evolution

See [Domain Event Versioning](domain-event-versioning.md) for Millett's full treatment.

## When to use EDA vs. Request-Response

Millett's decision matrix:

| Factor | Event-Driven | Request-Response (REST/gRPC) |
|---|---|---|
| Coupling tolerance | Loose coupling preferred | Tight coupling acceptable |
| Latency requirements | Seconds-to-minutes acceptable | Milliseconds required |
| Failure mode | Consumer can be temporarily unavailable | Consumer must be available now |
| Data flow | One-to-many (broadcast) | One-to-one (point-to-point) |
| Complexity budget | Team can handle eventual consistency | Team needs simple mental model |

Millett's advice: start with request-response for intra-BC communication, use events for cross-BC integration. Don't default to events for everything.

## Anti-patterns (Millett)

1. **Event as RPC:** using events where a synchronous call would suffice. "Just fire an event and hope" — leads to untraceable failures and debugging hell.

2. **Event soup:** hundreds of fine-grained events with no schema governance. Consumers drown in noise. Group related events into a bounded set.

3. **Event sourcing everything:** using event sourcing where current-state persistence would be simpler. Millett: "Event sourcing is a specialised tool for audit-heavy, multi-read-model scenarios. It is not the default persistence strategy."

## Связанные материалы

- [Domain Events](domain-events.md) — the foundational event concept
- [Event Sourcing](event-sourcing.md) — events as persistence
- [CQRS](cqrs.md) — events feeding read models
- [Domain Event Versioning](domain-event-versioning.md) — schema evolution
- [Process-Driven Architecture](process-driven-architecture.md) — events as process steps
- [Bounded Context Communication](bounded-context-communication.md) — events across BCs
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapters 11–14
