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

## Millett's practical tradeoffs (2015 — Chapters 10, 14)

Vernon covers *what* CQRS is and *when* to apply it. Millett adds depth on *how* CQRS affects the development process and what teams actually struggle with.

### CQRS and team workflow

Millett's key insight: CQRS changes *how the team works*, not just the architecture:

- **Write side = deep domain expertise needed.** Developers must understand aggregates, invariants, and business rules. This is where senior domain developers focus.
- **Read side = data engineering mindset.** Developers build projections, optimize queries, denormalize data. Domain expertise is less critical — data skills matter more.
- **Natural specialization:** CQRS lets you assign people to the side that matches their skills, rather than forcing everyone to master everything.

### The "projection rebuild" acid test

Millett's litmus test for CQRS readiness: "Can you drop and rebuild every read model from scratch in under 30 minutes?" If not:
- Your projections are too tightly coupled to the write model.
- You've lost the main benefit of CQRS — disposable read models.
- Fix: make projections replayable from the event stream or write-model state.

### When CQRS hurts more than it helps (Millett's red flags)

| Red flag | Why it's a problem |
|---|---|
| Most read models mirror the write model 1:1 | You're duplicating data with no benefit — just use the write model for reads |
| Projection failures go unnoticed for hours | You've built a system that silently serves stale/corrupt data |
| Write-side operations query the read model | The write side depends on the read side — cyclical dependency, defeats the purpose |
| Every new UI screen requires a new read model | Read model explosion — each one adds maintenance, lag, and storage cost |
| Team can't explain what eventual consistency means for their feature | They don't understand the tradeoff they signed up for |

### CQRS lite — Millett's pragmatic middle ground

Millett proposes "CQRS lite" as a stepping stone:

```
Write Model: Aggregates → normalized tables (same DB)
Read Model:  SQL Views / materialized views → no separate DB yet
```

Benefits: no distributed system complexity, no eventual consistency, still get query optimization. Upgrade to full CQRS (separate DB, async projections) only when views become a bottleneck.

### CQRS without Event Sourcing

Millett emphasizes: CQRS ≠ Event Sourcing. Many teams conflate them. CQRS works fine with:
- **ORM + normalized DB on write side** — aggregate state is current-state rows, not events
- **SQL projections on read side** — views, materialized views, or denormalized tables in the same DB
- **Sync or async projections** — can be in the same transaction for simple cases

Only add Event Sourcing when you need audit trail, temporal queries, or multiple read model versions. See [Event Sourcing](event-sourcing.md) for those use cases.

### CQRS and reporting/analytics

Millett draws a boundary: CQRS read models are for **operational queries** (show this user's order history). They are NOT a replacement for:

- **Data warehouse** — cross-domain analytics, aggregations over all data
- **BI/reporting** — multi-dimensional queries, ad-hoc analysis
- **Search** — full-text search (use dedicated search engine: Elasticsearch, etc.)

The read model is optimized for known query patterns; analytics needs unknown query flexibility.

## Связанные материалы

- [Domain Events](domain-events.md) — events drive read-model updates
- [Event Sourcing](event-sourcing.md) — natural write-model for CQRS
- [Aggregates](aggregates.md) — write model is aggregates
- [Repositories](repositories.md) — write-side persistence, not used on read side
- [Strategic Design](strategic-design.md) — read models across bounded contexts
- [Tactical Decision Framework](tactical-decision-framework.md) — when to use which pattern
- [Event-Driven Architecture Patterns](event-driven-architecture-patterns.md) — events as the glue between read/write
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 4 (Architecture), глава 8 (Domain Events), глава 10 (Aggregates)
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapters 10, 14 (CQRS practical tradeoffs)
