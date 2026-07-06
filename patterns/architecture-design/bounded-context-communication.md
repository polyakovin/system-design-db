---
title: Bounded Context Communication
type: pattern
category: ddd
tags: [ddd, domain-driven-design, integration, published-language, open-host-service, bounded-context, communication]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Bounded Context Communication

## Проблема

Evans' context map identifies *what* relationships exist between bounded contexts. But how do you actually implement the communication? What protocol? What contract format? How do you evolve the contract without breaking consumers?

Millett provides the implementation detail that bridges strategic design diagrams to production code.

## Published Language — beyond the schema (Millett, Chapter 13)

A Published Language is more than a JSON schema. Millett defines it as a **shared understanding formalized as a machine-readable contract**, with four layers:

### Layer 1: Domain semantics

What do the terms mean? "An Order is a binding request to purchase specific products at agreed prices." Without this, the schema is just field names. Millett recommends a lightweight domain glossary alongside the schema.

### Layer 2: Structural contract

The schema itself: field names, types, cardinality, optionality. Formats:
- **REST:** OpenAPI 3.x (JSON Schema)
- **gRPC:** Protocol Buffers (.proto)
- **Events:** Apache Avro with schema registry
- **Async messages:** AsyncAPI

### Layer 3: Behavioural contract

What happens when you use the API? Preconditions, postconditions, error modes:
```
POST /orders
  Precondition: customer must be authenticated, order must have ≥1 line item
  Postcondition: order is created in PENDING state, OrderPlaced event is emitted
  Error modes: 400 (invalid order), 409 (duplicate order), 503 (downstream unavailable)
```

Millett: "The most common integration failure is not a schema mismatch — it's a behavioural assumption mismatch. Consumer assumes the API is idempotent; it isn't."

### Layer 4: Evolutionary contract

How the contract changes over time (see also [Domain Event Versioning](domain-event-versioning.md)):
- Deprecation policy (how many versions supported simultaneously)
- Breaking change definition
- Consumer notification mechanism (changelog, CI checks, schema compatibility gates)

## Open-Host Service — implementation patterns (Millett)

Evans defines OHS as "a protocol that gives access to your subsystem as a set of services." Millett gives the implementation blueprint:

### API-first design

The OHS API is designed for consumers, not for the implementation's convenience:

```
Implementation                    API (OHS)
─────────────                    ─────────
Internal aggregate structure  →  Consumer-shaped resources
Domain method names           →  Consumer-friendly endpoint names
DB column names              →  Meaningful field names in contract
Internal error codes          →  Consumer-actionable error messages
```

Millett's rule: "The OHS API is a product. Treat consumers as customers."

### API versioning strategy

Millett prefers URL-based versioning for REST APIs:

```
/v1/orders      — current stable
/v2/orders      — new version (in beta)
/v1/orders      — deprecated, sunset date: 2026-12-31
```

Support at most 2 active versions. Three versions = you're accumulating technical debt.

### Consumer-driven contracts

Instead of the provider defining the API and hoping consumers are happy, Millett advocates consumer-driven contracts:

1. Consumer writes tests defining what they need from the provider.
2. Provider runs consumer contract tests in CI.
3. If provider changes break a consumer contract, the CI build fails.
4. Provider and consumer negotiate the change before it ships.

This inverts the traditional provider-consumer power dynamic and prevents the most common integration failure: the provider changes something, ships it, and discovers 3 consumers are broken.

## Communication patterns matrix (Millett)

| Relationship (Context Map) | Communication | Contract | When to use |
|---|---|---|---|
| Customer–Supplier | REST/gRPC, consumer-driven | OpenAPI, Protocol Buffers | Supplier serves known consumers |
| Partnership | Shared code (lib), co-designed API | Shared repo, joint review | Teams collaborate closely |
| Shared Kernel | Shared library, version in lockstep | Shared source, CI validates both sides | Tight coordination needed |
| Conformist | Supplier's API as-is | Supplier's contract | Consumer doesn't care about model purity |
| ACL + OHS | REST/gRPC + ACL adapter | Own contract + translation layer | Protecting model from legacy/external |
| Separate Ways | No integration | N/A | Cost of integration > cost of duplication |
| Event-driven | Async events via broker | Avro + schema registry | Loose coupling, eventual consistency |

## Millett's communication anti-patterns

1. **Database integration:** BC A reads BC B's database directly. Worst possible coupling — every schema change in B silently breaks A. No contract, no versioning, no visibility.

2. **Importing domain classes:** BC A imports BC B's Java/C# domain classes as a library. Now A's model IS B's model — the context boundary doesn't exist. Use DTOs or generated clients from the contract.

3. **Leaking internal identifiers:** BC A's API exposes its internal aggregate IDs (`orderId=42`). BC B stores them. When BC A migrates its database and IDs change, BC B breaks. Use natural keys or opaque external IDs.

4. **Synchronous chains:** A → B → C synchronously. A's latency is B's latency + C's latency + network. A's availability is B's availability × C's availability. Use async events.

5. **No integration tests against the contract:** unit tests pass, integration breaks. Consumer contract tests in CI catch this.

## Tradeoffs

**Pros:** explicit contracts, consumer-aware API design, predictable evolution, reduced integration failures.

**Cons:** overhead of contract management, versioning complexity, consumer-driven contracts require organizational buy-in.

## Связанные материалы

- [Strategic Design](strategic-design.md) — context map defines relationship types
- [Bounded Context](bounded-context.md) — communication crosses context boundaries
- [Anti-Corruption Layer](anti-corruption-layer.md) — ACL often wraps an OHS
- [Domain Events](domain-events.md) — event-driven communication alternative
- [Domain Event Versioning](domain-event-versioning.md) — contract evolution for events
- [Legacy Integration Patterns](legacy-integration-patterns.md) — ACL implementation detail
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapter 13
