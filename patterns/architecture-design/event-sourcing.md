---
title: Event Sourcing
type: pattern
category: ddd
tags: [ddd, domain-driven-design, event-sourcing, cqrs, event-store, persistence]
source: Implementing Domain-Driven Design (Vaughn Vernon, 2013)
added: 2026-07-06
---

# Event Sourcing

## Проблема

Traditional persistence stores only the current state. History of *how* state was reached is lost. Audit, debugging, temporal queries, and rebuilding state for new read models all require the full sequence of changes — not just the final snapshot.

## Решение

Instead of storing current state, store the sequence of domain events that produced it. The event stream IS the source of truth. Current state is a projection (left fold) over the event stream.

```
Event Stream:  [Event1, Event2, Event3, ...]
                    ↓ replay / fold
Current State:  Aggregate.replay(events) → current snapshot
```

## Key concepts (Vaughan Vernon, Chapters 8, 10)

### Event store

Vernon defines an event store as an append-only log of events, partitioned by aggregate ID (stream). Operations:

- `append(aggregateId, events, expectedVersion)` — optimistic concurrency check via version number
- `load(aggregateId)` — returns full event stream for an aggregate
- `loadAfter(aggregateId, version)` — returns events after a given version (for catch-up subscriptions)

Vernon recommends the event store also serve as a message bus: subscribers (projections, process managers) poll the store for new events.

### Rebuilding state from events

```java
public class Order {
    public static Order replay(List<DomainEvent> events) {
        Order order = new Order(); // blank slate
        for (DomainEvent e : events) {
            order.apply(e);  // mutate in-memory, no side effects
        }
        return order;
    }

    private void apply(OrderPlaced e) {
        this.id = e.orderId;
        this.status = OrderStatus.PLACED;
    }
}
```

Every `apply()` method is deterministic — same events, same state. No external calls, no random values.

### Snapshots

Replaying thousands of events per aggregate on every load is slow. Vernon introduces snapshots:

- Periodically serialize the aggregate's current state + its current version.
- On load: find the latest snapshot, then replay only events with version > snapshot version.
- Snapshot interval is a per-aggregate policy (e.g., every 50 events or based on event count).

Trade-off: snapshots trade storage space and complexity for load performance. Not needed for aggregates with short event streams (< ~200 events).

### Versioning events

Events evolve. Vernon describes three strategies:

1. **Always-add, never-remove:** new fields are optional, old consumers ignore them. Weakest contract.
2. **Upcasters:** transform old event schemas to new on read. `OrderPlacedV1 → OrderPlacedV2` via an upcaster registered in the event store.
3. **Schema registry:** store the event schema version alongside the event, let consumers decide.

## Tradeoffs

**Pros:**
- Complete audit trail — every state change is a persisted event.
- Temporal queries — "what was the order state on Tuesday?"
- Rebuild any read model from events without touching the write model.
- Natural fit with event-driven architecture and CQRS.

**Cons:**
- Complexity: event versioning, snapshot management, replay infrastructure.
- Eventual consistency between write and read models.
- Deleting data: GDPR right-to-erasure requires cryptographic erasure or event rewriting — non-trivial.
- Larger storage: events + snapshots > current-state-only tables.

## When to apply

- Audit is a core business requirement (finance, healthcare).
- Multiple read models are needed (CQRS).
- Domain logic is complex and history matters (collaborative editing, workflows).
- You need temporal/bi-temporal queries.

## When NOT to apply

- Simple CRUD applications — event sourcing is overkill.
- High write-throughput with long event streams and no snapshots (replay cost).
- Team lacks operational experience with event-driven systems.

## Связанные материалы

- [Domain Events](domain-events.md) — events are the atoms of event sourcing
- [Aggregates](aggregates.md) — event-sourced aggregates
- [CQRS](cqrs.md) — natural pairing: event sourcing on write, query models on read
- [Repositories](repositories.md) — event-sourced repositories append/load events
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 8 (Domain Events), Appendix A (Aggregates and Event Sourcing)
