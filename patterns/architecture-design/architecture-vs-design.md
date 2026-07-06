---
title: Architecture vs Design
type: pattern
category: architecture
tags: [architecture, design, abstraction, strategy, tactics, decision-making]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# Architecture vs Design

## Core thesis

Architecture and design are not the same thing — they operate at different levels of abstraction and have different change characteristics. The Architect distinguishes them by *what changes when* and *who can make the decision.*

## The difference

| | Architecture | Design |
|---|---|---|
| **Scope** | System-wide, cross-module, cross-service | Within a module, within a service |
| **Change frequency** | Hard to change, should change rarely | Easy to change, expected to evolve |
| **Who decides** | Architect/senior team (with input) | Individual developer or pair |
| **Time horizon** | Years (the system's lifetime) | Weeks to months (the feature's lifetime) |
| **Example decisions** | Microservices vs monolith, sync vs async communication, database per service vs shared | Class hierarchy, function decomposition, algorithm choice |
| **Cost of wrong decision** | System rewrite or migration | Local refactoring |
| **Reversibility** | Low — expensive to reverse | High — cheap to reverse |

## The Architect's litmus test

To determine whether a decision is architecture or design, ask:

1. **Can one developer reverse this decision without coordinating with other teams?** If yes → design. If no → architecture.

2. **Will this decision still matter in 2 years?** If no → design. If yes → architecture.

3. **If we get this wrong, is the fix a refactoring or a migration?** If refactoring → design. If migration → architecture.

## Strategic vs tactical decisions

The Architect borrows from military strategy:

- **Strategic decisions (architecture):** where to fight, with what resources, under what constraints. "We fight as independent squads (microservices), not as a single battalion (monolith)."

- **Tactical decisions (design):** how to execute a specific engagement. "We use a hash map for this cache, not a tree."

Strategic decisions constrain tactical decisions. If architecture says "services communicate via events," design cannot choose "synchronous REST call" for cross-service communication. But within a service, design has full freedom.

## Why the distinction matters

### 1. Decision-making velocity

Architectural decisions need broader input and more deliberation. Design decisions should be fast and local. If every design decision goes through an architecture review, velocity dies. If architectural decisions are made by a single developer without consultation, the system drifts into incoherence.

### 2. Reversibility determines process

The Architect's principle: **the harder a decision is to reverse, the more deliberation it deserves.** Architectural decisions are hard to reverse → they deserve explicit tradeoff analysis, RFCs, and recorded rationale. Design decisions are easy to reverse → make the call, ship it, reverse if wrong.

### 3. Architecture enables design

Good architecture creates space for design freedom. If the architecture says "all services communicate via a message broker," design within each service is unconstrained — choose any language, framework, or pattern that works with the broker. Bad architecture micromanages design: "all services must use Spring Boot with this exact library version."

## The spectrum, not a binary

The Architect acknowledges the boundary is fuzzy. A decision about database schema is design within a service but architectural when multiple services share the database. The key is not to classify perfectly but to apply the right level of process to each decision.

## Anti-patterns

1. **Everything is architecture:** every class name goes through architecture review. Velocity zero.

2. **Nothing is architecture:** no architectural decisions are made consciously. The system evolves by accident into a big ball of mud.

3. **Architecture by framework:** "Spring Boot decided the architecture for us." The framework is a design choice; the architecture is how components relate — the framework doesn't dictate that.

4. **Design leaking into architecture:** a tactical decision ("let's use this ORM") becomes architectural when all services are forced to use it.

## The Architect's rule

> "Архитектура определяет что нельзя. Дизайн определяет что можно." — Architecture defines what you cannot do. Design defines what you can do.

## Связанные материалы

- [Architecture as Tradeoff](architecture-as-tradeoff.md) — architectural decisions are tradeoffs
- [Architecture Evolution](architecture-evolution.md) — architectural decisions shape evolution
- [Architectural Debt](architectural-debt.md) — wrong architectural decisions create the hardest debt
- [Tactical Decision Framework](tactical-decision-framework.md) — design-level decisions in DDD
