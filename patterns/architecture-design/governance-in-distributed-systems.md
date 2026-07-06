---
title: Governance in Distributed Systems
type: pattern
category: architecture
tags: [governance, distributed-systems, microservices, decentralization, contracts, evolution]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# Governance in Distributed Systems

## Core thesis

Centralized governance doesn't scale to distributed systems. The Architect argues that governance in a distributed world must be **automated, decentralized, and contract-driven** — not board-meeting-driven. The key shift: from *pre-approval* (review before you build) to *post-validation* (build, then verify compliance automatically).

## The governance paradox

Distributed systems (microservices) promise team autonomy. But without governance, you get:
- Inconsistent APIs (REST, gRPC, GraphQL, and SOAP all in one system)
- Duplicated effort (3 teams build the same auth service)
- Incompatible data models (different meanings for "Customer" across services)
- Unmonitored technical debt (each team's debt is invisible to others)

The Architect's answer: governance through automation, not meetings.

## From centralized to decentralized governance

| Centralized (SOA-era) | Decentralized (post-SOA) |
|---|---|
| Architecture Review Board approves every new service | Automated contract validation in CI/CD |
| Shared canonical data model (enterprise-wide) | Per-service data model with explicit translation at boundaries |
| Governance meetings every week | Governance as code: linting rules, contract tests, schema registries |
| Manual compliance audits | Automated policy checks in deployment pipeline |
| "You must use this ESB" | "Your service must expose health, metrics, and a versioned contract" |

## Governance mechanisms

### 1. Contract-driven governance

Every service exposes a machine-readable contract (OpenAPI, Protobuf, AsyncAPI for events). The CI pipeline validates:
- No breaking changes to existing endpoints (unless explicitly versioned)
- All required fields are documented
- Error responses follow the standard format
- Deprecation headers are present for sunsetting endpoints

Tooling: schema registry, contract testing (Pact), automated diff on pull requests.

### 2. Fitness functions

The Architect borrows this concept: automated tests that verify architectural qualities, not just functional correctness.

```
Fitness function examples:
├── "No service has >5 synchronous dependencies" (coupling check)
├── "All services have a /health endpoint returning within 200ms" (resilience check)
├── "No service exposes its database port outside its pod" (security check)
└── "All event schemas are backward-compatible with the last 3 versions" (evolution check)
```

These run in CI. A PR that violates a fitness function fails — no human gatekeeper needed.

### 3. The shared nothing, governed everything approach

- **Shared nothing:** no shared databases, no shared libraries that force coordinated upgrades, no shared deployment pipelines.
- **Governed everything:** standardized observability (metrics format, trace propagation), standardized contracts (schema registry), standardized deployment manifests.

The Architect: "standardize the seams, not the insides."

### 4. Lightweight RFC process

For cross-cutting decisions (new communication protocol, new database technology), the Architect recommends an RFC process:

1. Anyone can propose an RFC.
2. RFC is public, comment period is time-boxed (1-2 weeks).
3. Decision is made by the affected teams, not a central board.
4. RFC is archived — future teams can understand *why* a decision was made.

This replaces the Architecture Review Board with a self-service process.

## Governance anti-patterns

1. **Governance as permission:** "you can't deploy until the board approves." Teams work around governance instead of with it.

2. **Governance as documentation:** a 50-page architecture document nobody reads. Governance must be executable (automated checks), not readable (PDFs).

3. **Governance without teeth:** fitness functions that fail but don't block deployment. People ignore yellow warnings.

4. **One-size-fits-all:** the same governance rules for a critical payments service and an internal dashboard. Risk-tiered governance: critical services get stricter rules.

## The Architect's rule

> "Управление в распределённых системах — это не запреты, а автоматические проверки. Не 'нельзя', а 'система не пропустит'." — Governance in distributed systems is not prohibitions, it's automated checks. Not "you can't," but "the system won't let you."

## Связанные материалы

- [SOA vs Microservices](soa-vs-microservices.md) — governance as a key differentiator
- [API Design](api-design.md) — contract evolution that governance enforces
- [Architecture as Tradeoff](architecture-as-tradeoff.md) — governance itself is a tradeoff (autonomy vs consistency)
- [DDD Organization Scaling](ddd-organization-scaling.md) — domain governance from a DDD perspective
