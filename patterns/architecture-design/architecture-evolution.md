---
title: Architecture Evolution
type: pattern
category: architecture
tags: [architecture, evolution, monolith, soa, microservices, event-driven, patterns]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# Architecture Evolution

## Core thesis

Architecture evolves, it doesn't revolutionize. Each stage solves the problems of its predecessor while introducing new ones. The architect's job is to recognize which stage the system is in and what the *next logical step* is — not to jump to the latest trend.

## The evolution chain

### 1. Monolith → Layered Architecture

**Problem:** spaghetti code with no structure.

**Solution:** [Layered Architecture](layered-architecture.md) — UI, Business Logic, Data. Simple, understandable, works for small teams.

**When it breaks:** monolithic codebase grows, changes in one module break unrelated parts, deployment becomes all-or-nothing.

### 2. Layered → SOA (Service-Oriented Architecture)

**Problem:** monolith can't scale organizationally — multiple teams step on each other.

**Solution:** extract services by business capability, communicate via ESB/SOAP/XML. Reuse through service registry.

**What SOA got right:** business-aligned decomposition, service contracts, governance.

**What SOA got wrong (per the Architect):** ESB became a bottleneck and a governance nightmare. XML/SOAP was heavy. "Reuse" was pursued at the expense of autonomy — shared services became shared bottlenecks.

### 3. SOA → Microservices

**Problem:** SOA's ESB became a single point of failure and a governance bottleneck. Services were too coarse-grained, shared databases persisted.

**Solution:** independently deployable services, each owning its data, communicating via lightweight protocols (REST/gRPC/events). No central bus, no shared database.

**The Architect's caution:** microservices are not the destination — they are a stage. The cost is distributed systems complexity: network failures, eventual consistency, debugging across services. Don't adopt microservices because they're popular; adopt them when the monolith's organizational cost exceeds the distributed systems cost.

### 4. Microservices → Event-Driven Architecture

**Problem:** synchronous chains between microservices create distributed monoliths — services coupled at runtime, cascading failures.

**Solution:** events replace synchronous calls for cross-service communication. Services publish facts, consumers react independently. See [Event-Driven Architecture Patterns](event-driven-architecture-patterns.md).

**The Architect's observation:** most systems never reach this stage — and shouldn't. Event-driven is the right answer when services need near-real-time reaction to each other's state changes. For simpler integration, REST/gRPC is sufficient.

## Evolution is not linear

The Architect emphasizes: you don't have to go through all stages. A new project can start as a modular monolith and stay that way. Evolution happens when the *pain* of the current architecture exceeds the *pain* of migrating. Migration for migration's sake is resume-driven development.

## Patterns lineage

```
Layered → SOA → Microservices → Event-Driven
  │         │         │              │
  └─ DDD ───┴─ Bounded Context ─────┘
       (Evans)   (service boundary)
```

Each stage absorbs the patterns of the previous while adding new ones. Microservices inherits SOA's business-aligned decomposition but replaces ESB with smart endpoints/dumb pipes. Event-driven inherits microservices' data ownership but replaces synchronous coupling with asynchronous events.

## When to evolve

| Current stage | Evolve when |
|---|---|
| Monolith | Deployment of any module requires full regression test. 3+ teams touching same codebase. |
| SOA | ESB is the bottleneck. Services share databases. "Reuse" has become "shared pain." |
| Microservices | Synchronous chains span 3+ services. Debugging requires running 5+ services locally. |
| Event-Driven | (Reached the asymptote — optimize, don't restructure.) |

## The Architect's rule

> "Архитектура не проект, а процесс. Она не создаётся, она выращивается." — Architecture is not a project, it's a process. It's not created, it's grown.

## Связанные материалы

- [Layered Architecture](layered-architecture.md) — the foundation
- [SOA vs Microservices](soa-vs-microservices.md) — detailed comparison
- [Event-Driven Architecture Patterns](event-driven-architecture-patterns.md) — EDA in practice
- [DDD and Microservices](ddd-microservices-and-distributed-systems.md) — bounded context as service boundary
- [Architecture as Tradeoff](architecture-as-tradeoff.md) — why each stage is a compromise
