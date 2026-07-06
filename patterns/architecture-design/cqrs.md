---
title: CQRS
type: pattern
category: ddd
tags: [ddd, domain-driven-design, cqrs, command-query-separation, read-model, write-model]
source: Implementing Domain-Driven Design (Vaughn Vernon, 2013)
added: 2026-07-06
---

# CQRS (Command Query Responsibility Segregation)

## Проблема

A single domain model serves both commands (writes) and queries (reads). This forces trade-offs: the model is optimised for neither. Write operations need business logic, invariants, and consistency. Read operations need fast, denormalised data shaped for the UI. One model can't excel at both.

## Решение

Split the system into two models:

- **Command model (write side):** processes commands, enforces invariants, emits events. Uses the full domain model (aggregates, entities, value objects).
- **Query model (read side):** serves pre-computed, denormalised views optimised for specific UI screens. No business logic — just data projection.

```
Command → [Write Model] → Events → [Projections] → Read Model → Query
                ↓                         ↓
           Event Store            Materialised Views (SQL, NoSQL, cache)
```

## Key concepts (Vaughan Vernon, Chapters 4, 8, 10)

### Command side

- Commands are imperative: `PlaceOrder`, `CancelOrder`, `ShipProduct`.
- An application service loads the aggregate, calls its method, saves events.
- The aggregate produces domain events — these drive the read-model updates.
- **One aggregate per transaction.** Vernon: "don't try to update two aggregates in one command."

### Query side

- Queries are simple data fetches: "give me the order summary for customer X."
- Queries bypass the domain model entirely — they hit denormalised read tables or a dedicated read database.
- Read models are disposable: if you change the projection logic, drop and rebuild from events.
- No repositories on the read side — use thin data access objects (DAOs) or raw SQL.

### Synchronisation: eventual consistency

The read model is updated asynchronously after the write transaction commits. This means:
- **Stale reads are normal.** The UI must handle the fact that a just-placed order may not appear immediately.
- **Vernon's pattern:** write side returns the event/confirmation, UI polls or subscribes to the read model.

### Vernon's tradeoff decision framework

| Factor | Use CQRS | Don't use CQRS |
|---|---|---|
| Read/write shape divergence | Queries return very different shapes from commands | All reads return aggregates as-is |
| Number of read models | 3+ distinct read models needed | Single canonical read model |
| Query complexity | Multi-join, cross-aggregate queries | Simple by-ID lookups |
| Team structure | Separate teams for read/write sides | One team owns everything |
| Write throughput | High write load, reads must not slow writes | Low traffic, no contention |

### Practical implementation approaches

**1. Same DB, different tables (simplest):**
- Write to normalised aggregate tables.
- Update denormalised read tables in the same transaction or via outbox.
- Good starting point — no distributed system complexity.

**2. Separate DBs with event-driven sync (Vernon's preferred):**
- Write side: event store or normalised DB.
- Read side: dedicated read DB (PostgreSQL with different indexes, Elasticsearch, Redis).
- Event-driven projector updates the read DB asynchronously.
- Full separation: scale independently, optimise each DB for its workload.

**3. Materialised views (DB-level):**
- PostgreSQL materialised views, MongoDB change streams.
- Less application code, but limited control.

### Don't over-split

Vernon warns: CQRS is not "split every aggregate into read/write." Start simple:

1. Build the write model with aggregates.
2. Use repositories for reads until query needs outgrow the aggregate shape.
3. Add read models one at a time, per use case.
4. Only then consider separate databases.

## Tradeoffs

**Pros:**
- Each model optimised for its task: rich domain for writes, fast denormalised for reads.
- Write performance improves — no complex joins on the write path.
- Read models can be rebuilt from events at any time.
- Enables independent scaling and technology choice per side.

**Cons:**
- Eventual consistency — harder to reason about, harder to test.
- Duplication: same data exists in write and read models.
- Operational complexity: two databases, projection failures, lag monitoring.
- Premature CQRS adds complexity without benefit.

## When NOT to apply

- Simple CRUD applications where read == write shape.
- Low traffic — a single model with smart indexing suffices.
- Team is new to DDD — master aggregates and repositories first.

## Связанные материалы

- [Domain Events](domain-events.md) — events drive read-model updates
- [Event Sourcing](event-sourcing.md) — natural write-model for CQRS
- [Aggregates](aggregates.md) — write model is aggregates
- [Repositories](repositories.md) — write-side persistence, not used on read side
- [Strategic Design](strategic-design.md) — read models across bounded contexts
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 4 (Architecture), глава 8 (Domain Events), глава 10 (Aggregates)
