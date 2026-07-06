---
title: Legacy Integration Patterns
type: pattern
category: ddd
tags: [ddd, domain-driven-design, legacy, integration, strangler-fig, anti-corruption-layer, migration]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Legacy Integration Patterns

## Проблема

Evans' [Anti-Corruption Layer](anti-corruption-layer.md) is the canonical DDD answer to legacy integration — but Millett expands this into a practical playbook. The ACL pattern alone doesn't answer: how do you *migrate off* the legacy system? How do you run old and new side-by-side? How do you handle data synchronization during the transition?

Real legacy integration is a **multi-year migration**, not a one-off adapter build.

## The Strangler Fig pattern (Millett, Chapter 21)

Named after the vine that gradually envelops and replaces a host tree, the Strangler Fig is the migration strategy:

```
Phase 1: Legacy system is the source of truth. New system exists alongside, consuming legacy data.
Phase 2: New system takes over some features. Traffic is routed to the appropriate system.
Phase 3: New system is the source of truth. Legacy system is read-only.
Phase 4: Legacy system is decommissioned.
```

### Routing traffic during migration

Millett describes the routing layer that straddles old and new:

```
Request → [Router]
              ├── Feature X → Old System
              ├── Feature Y → New System
              └── Feature Z → Proxy to Old + Sync to New (dual-write)
```

The router is a thin layer — it doesn't translate models, it directs traffic. Translation happens in the ACL.

### Data synchronization patterns

**Dual-write (simplest, riskiest):**
```
New Order → Write to New DB → Write to Old DB → both in sync
```
Risk: if one write fails, the systems diverge. Requires compensation logic.

**Change Data Capture (CDC, preferred):**
```
Old DB → CDC (Debezium/Kafka Connect) → Event Stream → New System consumes
```
Legacy system doesn't know the new system exists. The CDC tool captures changes from the DB transaction log.

**Batch sync (for non-real-time):**
```
Nightly ETL: Old DB → Transform → New DB
```
Acceptable for reference data, configuration, or historical archives. Not for transactional data.

**Event-driven bridge:**
```
Legacy System → emits events (via adapter) → ACL → Domain Events → New System
```
Millett's preferred approach: build an event adapter on the legacy side, translate to domain events through the ACL.

## Anti-Corruption Layer implementation (Millett's detail)

Evans describes the ACL concept; Millett gives the implementation blueprint.

### ACL structure

```
[New Domain] → [ACL] → [Legacy System]
                 │
                 ├── Facade: simple interface that matches domain language
                 ├── Adapter: translates between Facade and Legacy API
                 ├── Translator: converts data structures
                 └── Service: (optional) adds domain behavior on top of translation
```

### Translator patterns

**Synchronous translator:**
```csharp
class LegacyCustomerTranslator {
    Customer Translate(LegacyCustomerRecord legacy) {
        return new Customer(
            id: new CustomerId(legacy.CUST_NO),       // rename
            name: legacy.CUST_NAME,                     // pass-through
            status: MapStatus(legacy.STATUS_CD),        // enum map
            tier: legacy.TIER?.ToDomain() ?? CustomerTier.Standard // nullable + default
        );
    }
}
```

**Asynchronous translator (for event streams):**
```
Legacy DB Change → CDC Event → Translator → Domain Event → New System
```

### ACL testing strategy (Millett)

Millett emphasizes that ACLs *must* be tested against real legacy data:

1. **Snapshot tests:** capture real legacy API responses, assert translation produces expected domain objects.
2. **Round-trip tests:** translate legacy → domain → legacy, verify no data loss.
3. **Fuzz tests:** feed the translator with nulls, unexpected values, edge cases from real legacy DB dumps.
4. **Performance tests:** ACL translation should not become the bottleneck.

### ACL anti-patterns (Millett)

1. **Leaky ACL:** legacy concepts leak through the facade. "The ACL returns `LegacyCustomerRecord` with a `getDomainObject()` method" — that's not an ACL, that's a wrapper.

2. **God Translator:** one translator class handles all 200 legacy types. Split by bounded context or aggregate.

3. **ACL with business logic:** the ACL translates data, it doesn't enforce domain rules. If the ACL starts validating "customer must have a valid email," domain logic has leaked.

4. **Skipping the ACL for "simple" integrations:** Millett warns — the simplest external API will change. Without an ACL, that change propagates everywhere the API is consumed.

## Migration metrics and go/no-go criteria (Millett)

Millett recommends tracking:

| Metric | Target |
|---|---|
| Feature parity | 100% of committed features running on new system |
| Data consistency | <0.01% divergence between old and new |
| Performance parity | New system p95 latency ≤ old system p95 |
| Rollback capability | Can revert to legacy within 1 hour |
| Bug rate | New system bugs/week ≤ old system (or declining) |

Go/no-go for cutover: all metrics green for 2+ consecutive weeks.

## Tradeoffs

**Pros:** incremental migration reduces risk, both systems run in parallel, revert possible at any point before final cutover.

**Cons:** months/years of dual-system overhead, CDC infrastructure to maintain, ACL complexity grows with legacy system surface area.

## Связанные материалы

- [Anti-Corruption Layer](anti-corruption-layer.md) — the foundational pattern
- [Bounded Context](bounded-context.md) — ACL protects context boundaries
- [Strategic Design](strategic-design.md) — ACL is a context map relationship type
- [Domain Events](domain-events.md) — event-driven bridge between old and new
- [Bounded Context Communication](bounded-context-communication.md) — published language for new system APIs
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapter 21
