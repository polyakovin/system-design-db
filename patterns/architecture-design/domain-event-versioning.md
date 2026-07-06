---
title: Domain Event Versioning
type: pattern
category: ddd
tags: [ddd, domain-driven-design, events, versioning, schema-evolution, compatibility]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Domain Event Versioning

## Проблема

Domain events evolve. Fields are added, renamed, split, or deprecated. Multiple versions of the same event coexist in production — old events in the event store, new events being produced, consumers on different deployment schedules. Without a versioning strategy, schema changes break consumers and corrupt event stores.

Millett treats event versioning as a **first-class architectural concern**, not an implementation detail.

## Core principles (Millett, Chapter 12)

1. **Events are immutable facts.** You cannot rewrite history — old events stay as they are.
2. **Consumers evolve independently.** Producers cannot force all consumers to upgrade simultaneously.
3. **The event schema is a contract.** Breaking the contract breaks consumers.

## Versioning strategies

### Strategy 1: Always-add, never-remove (weakest)

New fields are optional, old fields remain. Consumers ignore unknown fields.

```
OrderPlaced v1: { orderId, customerId, total }
OrderPlaced v2: { orderId, customerId, total, currency, itemCount }  // added: optional
```

**Pros:** simplest, no consumer breakage.
**Cons:** schema grows indefinitely. Deprecated fields accumulate forever. No way to rename — `customer` can't become `buyer` without a new field + keeping the old one.

**Millett's verdict:** good starting point, unsustainable for systems with >2–3 years of evolution.

### Strategy 2: Upcasters (intermediate)

Transform old event schemas to new ones at read time. The event store holds the original; consumers always see the latest version.

```csharp
class OrderPlacedUpcaster {
    OrderPlacedV2 Upcast(OrderPlacedV1 v1) => new OrderPlacedV2(
        orderId: v1.orderId,
        customerId: v1.customerId,
        total: v1.total,
        currency: "USD",           // default for old events
        itemCount: v1.items.Count  // computed from old schema
    );
}
```

Upcasters are registered in the event store's deserialization pipeline:
```
Event Store → Upcaster(v1→v2) → Upcaster(v2→v3) → Consumer sees v3
```

**Pros:** consumers see a single schema. Old events are never modified. New consumers don't need to know history.
**Cons:** upcaster chain can grow long. Upcaster logic must be tested with real old events. Wrong upcaster = silently corrupted data.

### Strategy 3: Schema registry with consumer-driven contracts (strongest)

Each event carries a schema version. Consumers declare which versions they accept. The broker (or event store) enforces compatibility.

```
Registry:
  OrderPlaced v1 (2019): schema, compatibility rules
  OrderPlaced v2 (2021): schema, backward-compatible with v1
  OrderPlaced v3 (2023): schema, backward-compatible with v2

Consumer A: "I accept v2+"
Consumer B: "I accept v1+"
```

Millett recommends running a **schema compatibility checker** in CI:

```
Producer commits new schema → CI checks:
  ├─ Is it backward-compatible? (can old consumers read it?)
  ├─ Is it forward-compatible? (can new consumers read old events?)
  └─ Fail build if breaking change detected
```

### Strategy 4: Double-write during transition (tactical)

When renaming a field (`customerId` → `buyerId`), emit both versions during the transition period:

```
OrderPlaced v2: { buyerId, ... }          // new consumers read this
OrderPlaced v1: { customerId, ... }        // old consumers still need this
                    ↑
            Producer emits both for N weeks → then retires v1
```

Millett calls this "evolutionary schema migration" — the safest, most expensive strategy. Use only for breaking changes on critical events.

## Compatibility matrix

| Change | Backward-compatible? | Strategy |
|---|---|---|
| Add optional field | ✅ Yes | Always-add |
| Add required field | ❌ No | Upcaster (provide default) or new event type |
| Remove field | ❌ No | Keep field, mark deprecated |
| Rename field | ❌ No | Add new field + keep old, transition via upcaster |
| Change field type (int→string) | ❌ No | New field with new name + upcaster |
| Split field (name→firstName+lastName) | ❌ No | Add new fields, upcaster for old |
| Merge fields (firstName+lastName→name) | ❌ No | Upcaster on read, keep old fields for old consumers |
| Change enum value | Sometimes | Add new value, never remove old values |

## Millett's versioning governance rules

1. **Semantic versioning for events:** MAJOR.MINOR. MAJOR = breaking change (requires consumer update). MINOR = backward-compatible addition.

2. **Deprecation window:** deprecate old fields/schemas with a documented sunset date. Millett recommends 3–6 months for internal events, 12+ months for external/published events.

3. **Monitor version usage:** track which consumers use which event versions. You cannot safely retire a version until zero consumers use it.

4. **Test with production event dumps:** use a sample of real old events in CI to verify upcasters don't corrupt real-world data.

5. **Event store schema validation:** the event store should reject events that don't match any known schema. Fail fast — don't let schema violations accumulate.

## Event Store considerations

Millett distinguishes versioning for the event store vs. versioning for message brokers:

- **Event store (persistence):** events are immutable. Old versions exist forever. Upcasters at read time. Focus: can all events ever written be deserialized correctly?
- **Message broker (integration):** events are transient. Consumers see current version. Focus: can all current consumers process the latest event?

## Tradeoffs

**Pros:** predictable evolution, no consumer surprises, audit trail maintains integrity.

**Cons:** operational overhead (schema registry, compatibility checks), upcaster chains become technical debt, deprecation windows mean carrying legacy fields for months.

## When to invest heavily

- Events are the primary integration mechanism between teams
- Multiple consumers on different release cadences
- Event store is the system of record (event sourcing)

## When a light touch suffices

- Events are internal to one team's bounded context
- Single consumer, co-deployed with producer
- Event store is not the primary source of truth

## Связанные материалы

- [Domain Events](domain-events.md) — event structure and publishing
- [Event Sourcing](event-sourcing.md) — event store as source of truth
- [Event-Driven Architecture Patterns](event-driven-architecture-patterns.md) — practical EDA patterns
- [Bounded Context Communication](bounded-context-communication.md) — published language as versioned contract
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapter 12
