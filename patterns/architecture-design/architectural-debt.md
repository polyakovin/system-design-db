---
title: Architectural Debt
type: pattern
category: architecture
tags: [technical-debt, architectural-debt, architecture, tradeoffs, evolution, refactoring]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# Architectural Debt

## Core thesis

Technical debt at the architecture level is fundamentally different — and more dangerous — than code-level debt. Code debt can be refactored within a module. Architectural debt spans modules, teams, and contracts. The Architect argues that architectural debt is the most expensive form of technical debt because paying it off requires coordination across organizational boundaries.

## Architectural debt vs code-level debt

| | Code-level debt | Architectural debt |
|---|---|---|
| **Scope** | Single module, class, or function | Cross-module, cross-service, cross-team |
| **Example** | Duplicated validation logic | Wrong service boundaries, shared database between services |
| **Fix cost** | Hours to days | Weeks to months, requires coordination |
| **Detection** | Static analysis, code review | Architecture review, production incidents |
| **Who fixes it** | Individual developer | Multiple teams, architectural initiative |
| **Impact of delay** | Local degradation | Systemic fragility, cascading failures |

## Sources of architectural debt

### 1. Wrong boundaries

The most common architectural debt. A bounded context is split at the wrong place. Two concepts that always change together are in separate services — every change requires coordinated deployments. Or unrelated concepts are in the same service — changes to one break the other.

### 2. Missing abstractions

The team avoided creating an abstraction "because YAGNI." Now 5 services have duplicated the same logic with slight variations. Each variation is a bug surface.

### 3. Wrong communication patterns

Services communicate synchronously when events would be better (or vice versa). The synchronous chain has grown to 4 services — a failure in one cascades to all. Fixing this requires changing the integration pattern across all participants.

### 4. Shared persistence

Multiple services writing to the same database. Schema changes break downstream consumers. This is the architectural equivalent of global mutable state.

### 5. Missing observability

No distributed tracing, inconsistent logging, no standard metrics. When something fails in production, debugging requires SSH-ing into 5 services and grepping logs. The debt is not visible until the first major incident — then it's a crisis.

## Why architectural debt is harder to pay off

1. **Coordination cost.** Code debt: one developer, one afternoon. Architectural debt: 3 teams, 2 sprints, 1 migration plan.

2. **No safe refactoring.** Code refactoring has compiler/type-checker safety net. Architectural refactoring has no such safety net — you're changing contracts between services.

3. **Business resistance.** "The system works. Why spend 2 months rewriting it?" Architectural debt's impact is diffuse (hard to quantify in dollars), while the fix cost is concrete and high.

4. **Compounding interest.** Architectural debt, unlike code debt, compounds. Wrong boundaries → more coupling → harder to change → more wrong decisions → more debt.

## The Architect's approach to architectural debt

### 1. Make it visible

Maintain an architectural debt registry — a living document of known architectural shortcomings:
- What is the debt? (Concrete: "Payment and Shipping share a database")
- What is the impact? (Concrete: "Schema changes in Payment require Shipping team coordination")
- What is the trigger for paying it off? ("When we add a 3rd service to this database")
- What is the fix? ("Extract Payment data to its own database, sync via events")

### 2. Pay off opportunistically

Don't schedule "architectural debt sprints." Pay off architectural debt when you're already touching that part of the system:
- Adding a feature that touches the shared database → extract it now.
- New service needs to talk to the synchronous chain → break the chain now.

### 3. Prevent new debt

Architectural fitness functions (see [Governance in Distributed Systems](governance-in-distributed-systems.md)) that block PRs introducing known architectural anti-patterns: "no new service may connect to a shared database," "no synchronous chain >3 services."

### 4. Accept some debt

The Architect is pragmatic: not all architectural debt must be paid. If the system is being replaced in 6 months, don't refactor it. If the debt is in a stable, low-change area, the interest may never come due. Debt in high-change core domains must be paid aggressively; debt in stable supporting domains can be tolerated.

## The Architect's rule

> "Архитектурный долг — это не просто 'грязный код'. Это структурные решения, которые сегодня экономят время, а завтра берут проценты координацией, инцидентами и упущенными возможностями." — Architectural debt is not just "dirty code." It's structural decisions that save time today and charge interest tomorrow in the form of coordination, incidents, and missed opportunities.

## Связанные материалы

- [Architecture as Tradeoff](architecture-as-tradeoff.md) — every architectural decision can create debt
- [Architecture Evolution](architecture-evolution.md) — evolution often means paying off architectural debt
- [Governance in Distributed Systems](governance-in-distributed-systems.md) — preventing new architectural debt
- [Architecture vs Design](architecture-vs-design.md) — architectural decisions have higher debt cost
