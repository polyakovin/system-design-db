---
title: Architecture as Continuous Tradeoff
type: pattern
category: architecture
tags: [architecture, tradeoffs, decision-making, compromise, quality-attributes]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# Architecture as Continuous Tradeoff

## Core thesis

There is no ideal architecture. Every architectural decision is a compromise between competing forces. The architect's job is not to find the "right" answer — it's to make the tradeoff explicit and choose the least-bad option for the current context.

## The tradeoff mindset

The Architect identifies the fallacy of "best practice" thinking: a practice that worked at Google doesn't automatically work for a 5-person startup. Context is everything. A decision that was correct last year may be wrong today — architecture is continuous, not a one-time event.

## Key tradeoff dimensions

### 1. Consistency vs Availability (CAP)

The classic: in a partition, you can have consistency or availability, not both. The Architect's contribution: **this is a business decision, not a technical one.** The architect must translate: "if the network splits, do users see stale data or an error?" → the product owner decides, the architect implements.

### 2. Performance vs Maintainability

Fast code is often complex code. Simple code is often slow code. The Architect's rule: optimize for maintainability first. 90% of the code is not on the hot path. Profile, then optimize only what matters.

### 3. Flexibility vs Simplicity

Abstractions add flexibility but also complexity. Every indirection layer is a future debugging session. The Architect: "add flexibility when you have two concrete examples of why you need it, not one hypothetical."

### 4. Autonomy vs Consistency

Microservices give team autonomy — each team owns its stack, deploys independently, moves fast. The cost: no single source of truth, data duplication, eventual consistency. The tradeoff is organizational, not technical: do you value team speed more than data consistency?

### 5. Reuse vs Autonomy (the SOA lesson)

SOA pursued reuse — shared services, shared schemas, shared everything. The result: changing a shared service required coordination across 5 teams. Microservices learned the lesson: autonomy over reuse. Duplicate a little to avoid coupling a lot.

## The Architect's decision framework

For every architectural decision, make these explicit:

1. **What are we optimizing for?** (Latency? Throughput? Time-to-market? Cost? Team autonomy?)
2. **What are we sacrificing?** (Every optimization has a cost. Name it.)
3. **When does this decision expire?** (Under what conditions should we revisit this?)
4. **Who is affected?** (Which teams, which users, which SLAs?)

## Anti-patterns in architectural decisions

1. **Gold-plating:** optimizing for a scale you'll never reach. "We need to handle 1M QPS" — when current traffic is 100 QPS.
2. **Resume-driven architecture:** choosing technology because it's trendy, not because it solves a real problem.
3. **Analysis paralysis:** spending months evaluating options when any of the top 3 would work. Pick one, document the tradeoff, move on.
4. **No tradeoff documentation:** the team doesn't know *why* a decision was made. When context changes, they can't tell if the decision should change too.

## The Architect's rule

> "Каждое архитектурное решение — это выбор между двумя плохими вариантами и одним очень плохим. Задача архитектора — выбрать наименее плохой." — Every architectural decision is a choice between two bad options and one very bad one. The architect's job is to pick the least bad.

## Связанные материалы

- [Architecture Evolution](architecture-evolution.md) — tradeoffs drive evolution
- [SOA vs Microservices](soa-vs-microservices.md) — a specific tradeoff analysis
- [Architecture vs Design](architecture-vs-design.md) — levels of tradeoff decisions
- [System design principles](../fundamentals/system-design-principles.md) — keeping constraints and tradeoffs in focus
