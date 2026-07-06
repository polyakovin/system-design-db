---
title: Tactical Decision Framework
type: pattern
category: ddd
tags: [ddd, domain-driven-design, tactical-design, decision-framework, aggregates, entities, value-objects]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Tactical Decision Framework

## Проблема

Developers face a recurring decision: should this concept be an Entity, a Value Object, or part of an Aggregate? Evans and Vernon describe *what* these patterns are, but Millett provides a systematic **decision framework** for *when* to use each.

Wrong choices cascade: a VO misclassified as an Entity introduces unnecessary identity tracking and repository overhead. An Entity flattened into an Aggregate creates a god object with transaction contention.

## Decision framework (Millett, Chapters 5–7)

### Step 1: Does it have a lifecycle independent of its attributes?

```
Does the object change over time while remaining "the same thing"?
├─ YES → Entity (has identity, tracked by ID)
│   └─ Does it enforce invariants spanning multiple child objects?
│       ├─ YES → This is the Aggregate Root
│       └─ NO  → Entity (standalone or child of an aggregate)
└─ NO  → Go to Step 2
```

**Entity test:** if you change every attribute and the business still considers it the same object, it's an Entity. If not, it's a Value Object.

### Step 2: Is it defined entirely by its attributes?

```
Are two objects with identical attributes interchangeable?
├─ YES → Value Object
│   └─ Does it encapsulate domain logic on those attributes?
│       ├─ YES → Rich Value Object (Money, Email, DateRange)
│       └─ NO  → Consider: is this just a primitive in disguise?
└─ NO  → Reconsider — you might have an Entity
```

**Millett's litmus test for VO:** would you ever say "give me the same Address, but with a different street"? No — you'd say "give me a different address." That's a VO. But "change the customer's name" — same customer. That's an Entity.

### Step 3: Transaction boundary test

```
Does a business rule require atomic consistency across these objects?
├─ YES → They belong in the same Aggregate
│   └─ Which object is the entry point? → That's the Aggregate Root
└─ NO  → Separate Aggregates (use eventual consistency)
```

### Step 4: Concurrency test

```
How often are these objects modified concurrently?
├─ HIGH contention on different parts → Split into separate Aggregates
│   Even if they feel related — transaction serialization will kill throughput
└─ LOW contention → Keep together for simplicity
```

Millett: "The aggregate boundary is driven by transactional consistency, not by domain taxonomy. Two concepts that 'feel' related but are modified independently should be separate aggregates."

## Tactical pattern selection matrix

| Situation | Pattern | Rationale |
|---|---|---|
| Object tracked over time (customer, order, account) | Entity | Has identity, lifecycle, mutable state |
| Object defined by its attributes (money, address, date range) | Value Object | Immutable, replaceable, no identity |
| Cluster of objects with shared invariant | Aggregate | Single consistency boundary |
| Stateless domain operation (pricing, routing, validation) | Domain Service | Doesn't belong to any one entity |
| Data access, persistence, retrieval | Repository | Abstracts storage for aggregates |
| Significant business occurrence | Domain Event | Facts that other parts react to |
| Multi-step business process spanning aggregates | Saga / Process Manager | Orchestrates long-running workflows |
| Business rule that can be evaluated independently | Specification | Boolean logic over domain objects |
| Transform/adapt external model to internal | Anti-Corruption Layer | Protects domain from external corruption |

## Common misclassification traps (Millett)

1. **"Everything is an Entity."** Many concepts have no meaningful identity — a phone number, an address, a measurement. These are VOs. Millett estimates 60–70% of domain objects should be VOs.

2. **"One aggregate per table."** Database tables ≠ aggregates. A single aggregate may span multiple tables; conversely, a table may store data for multiple aggregates.

3. **"Domain Services are where logic goes when I can't decide."** Millett warns: domain services are the fallback, not the default. If logic naturally belongs to an Entity or VO, put it there. Domain services are for operations that span multiple aggregates or are stateless by nature.

4. **"Repositories per entity."** Repositories exist ONLY for aggregate roots. Non-root entities and VOs are accessed through the root's repository.

## When to use each pattern — Millett's heuristics

**Entity:** when the business tracks this thing over time, assigns it identifiers, and distinguishes it from others even when all attributes match. Framework: "Can two of these exist with identical attributes and be different things?" If yes → Entity.

**Value Object:** when the business cares about the *value* of the thing, not which specific instance it is. Framework: "Does this concept describe, measure, or quantify something?" If yes → VO.

**Aggregate:** when a business invariant must hold across multiple objects at all times, and violating it during a concurrent operation is unacceptable. Framework: "Can this invariant be temporarily violated under any circumstance?" If the business says no → same aggregate.

**Domain Service:** when an operation doesn't naturally belong to any Entity or VO, yet is part of the ubiquitous language. Framework: "If I force this into an Entity, does it make the model unnatural?" If yes → Domain Service.

## Связанные материалы

- [Entities](entities.md) — objects with identity
- [Value Objects](value-objects.md) — objects defined by attributes
- [Aggregates](aggregates.md) — consistency boundaries
- [Domain Services](domain-services.md) — stateless domain operations
- [Bounded Context](bounded-context.md) — all tactical patterns live inside a context
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapters 5–7 (Entities, Value Objects, Aggregates)
