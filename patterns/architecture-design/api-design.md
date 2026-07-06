---
title: API Design
type: pattern
category: architecture
tags: [api, design, versioning, backward-compatibility, evolvability, contracts]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# API Design

## Core thesis

An API is a contract between the provider and its consumers. Breaking that contract breaks consumers. The Architect's focus: API design is not about pretty URLs — it's about managing evolution without breaking trust.

## API as a contract

The Architect frames API design as an economic problem: changing the API has a cost proportional to the number of consumers. When you have one consumer (your own frontend), breaking changes are cheap. When you have 100 external consumers, every change is a negotiation.

Key principle: **design for the consumers you'll have in 2 years, not the ones you have today.**

## Versioning

### URL versioning (`/v1/orders`, `/v2/orders`)

- **Pros:** explicit, simple to understand, easy to route to different backends.
- **Cons:** URL proliferation, breaks REST's "one resource, one URL" principle. If `/v2/orders/123` returns the same logical order as `/v1/orders/123`, REST is violated — same resource, different URLs.

### Header/Content-Type versioning (`Accept: application/vnd.company.order-v2+json`)

- **Pros:** one URL per resource, follows REST semantics.
- **Cons:** harder to test (curl needs custom headers), harder to route, less visible in logs.

### Query parameter versioning (`/orders?version=2`)

- **Pros:** easy to test, visible in URLs.
- **Cons:** pollutes the resource's identity, breaks caching (different `?version` → different cache key).

### The Architect's recommendation

URL versioning for public APIs (simplicity wins). Content-Type versioning for internal service-to-service APIs (follows REST, internal consumers can handle the complexity).

## Backward compatibility rules

The Architect's hierarchy of safe changes:

| Change | Safe? | Notes |
|---|---|---|
| Add a new endpoint | ✅ | New consumers can use it; old consumers ignore it |
| Add an optional field to response | ✅ | Old consumers ignore unknown fields |
| Add an optional field to request | ✅ | Old consumers don't send it; server uses default |
| Change field type (string → int) | ❌ | Breaks every consumer that parses the field |
| Remove a field from response | ❌ | Consumers relying on it break |
| Rename a field | ❌ | Same as remove + add; breaks all consumers |
| Change endpoint semantics | ❌ | `/orders` now creates invoices — even if URL is the same |
| Change error response format | ❌ | Consumers' error handlers break |

Rule: **never remove, only add.** Deprecate fields and endpoints with a sunset period (HTTP `Deprecation` and `Sunset` headers), then remove only after all known consumers have migrated.

## Evolvability patterns

### 1. The Tolerant Reader

Consumers must ignore unknown fields. This is the single most important rule for API evolvability. If consumers break on new fields, the provider can never add anything.

### 2. Expand/Contract for breaking changes

1. **Expand:** deploy new version side-by-side with old. New consumers use v2. Old consumers still on v1.
2. **Migrate:** move consumers to v2 over time.
3. **Contract:** when no consumers remain on v1, remove it.

### 3. API deprecation headers

```
Deprecation: true
Sunset: Sat, 31 Dec 2026 23:59:59 GMT
Link: </v2/orders>; rel="successor-version"
```

### 4. Semantic versioning is not enough

Version numbers don't communicate *what* changed. The Architect: pair version bumps with changelogs that describe the *impact* on consumers, not just the technical change. "Field `total` changed from int to float" — consumer impact: "if you do integer comparison on `total`, you'll get false negatives on decimal values."

## Anti-patterns

1. **Versioning everything:** creating `/v2` with one new field and no breaking changes. Version for breaking changes only — new fields in existing endpoints don't need a new version.

2. **"Just this once" exceptions:** bypassing the API contract for one consumer ("they're internal, it's fine"). The exception becomes the new contract. Next consumer sees it and assumes it's the API.

3. **No deprecation policy:** removing endpoints without notice. External consumers build businesses on your API — breaking them without warning is a business decision, not a technical one.

4. **API modeled on database schema:** exposing table structures, internal IDs, and join relationships. The API is a *façade* — it should hide the internal model.

## The Architect's rule

> "API — это обещание. Каждое нарушение обещания подрывает доверие. Восстановить доверие сложнее, чем исправить код." — An API is a promise. Every broken promise erodes trust. Restoring trust is harder than fixing code.

## Связанные материалы

- [REST Architectural Style](rest-architectural-style.md) — the style that most APIs follow
- [Architecture as Tradeoff](architecture-as-tradeoff.md) — API design is a series of tradeoffs
- [Governance in Distributed Systems](governance-in-distributed-systems.md) — governing API evolution
