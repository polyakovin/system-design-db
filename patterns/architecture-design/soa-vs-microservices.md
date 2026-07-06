---
title: SOA vs Microservices
type: pattern
category: architecture
tags: [soa, microservices, architecture, comparison, tradeoffs, evolution]
source: 架构漫谈 (Architect, 2016)
added: 2026-07-06
---

# SOA vs Microservices

## Core thesis

Microservices are not a rejection of SOA — they are SOA done right, with the lessons of SOA's failures baked in. The Architect, writing in 2016 when microservices were still a hot debate, provides a balanced comparison.

## What they share

Both SOA and microservices:
- Decompose systems by business capability, not by technical layer
- Define service contracts (explicit interfaces between services)
- Aim for loose coupling between services
- Embrace polyglot persistence (each service chooses its own storage)

## What separates them

| Dimension | SOA | Microservices |
|---|---|---|
| **Integration** | ESB (Enterprise Service Bus) — smart pipes | Dumb pipes, smart endpoints (REST, gRPC, events) |
| **Communication** | SOAP/XML, heavy protocols | Lightweight: REST/JSON, gRPC, message queues |
| **Data** | Shared database or shared data model | Each service owns its database |
| **Service granularity** | Coarse-grained, business-process-level | Fine-grained, bounded-context-level |
| **Governance** | Centralized governance board, shared schemas | Decentralized, team autonomy, consumer-driven contracts |
| **Reuse** | Maximize reuse (shared services) | Minimize coupling; reuse through copy if needed |
| **Deployment** | Services deployed as a group | Each service independently deployable |
| **Team structure** | Technology-aligned (DB team, UI team) | Business-capability-aligned (full-stack team per service) |

## The Architect's analysis of SOA's failures

1. **ESB became the bottleneck.** What started as a smart integration layer became a single point of failure, a governance choke point, and a vendor lock-in vehicle.

2. **Reuse killed autonomy.** "Reuse" was sold as efficiency but delivered coordination overhead. Changing a shared service required approval from every consumer team — the opposite of agility.

3. **SOAP was too heavy.** XML schemas, WSDL, UDDI — the protocol overhead was enormous relative to the business value. Teams spent more time on WSDL than on business logic.

4. **Shared databases defeated the purpose.** Services were logically separated but physically coupled through a shared database. You couldn't change a schema without breaking downstream consumers.

5. **Governance became gatekeeping.** The centralized architecture board was supposed to ensure consistency. In practice, it became a bottleneck: every new service waited weeks for approval.

## How microservices fixed SOA

| SOA problem | Microservice solution |
|---|---|
| Centralized ESB | Dumb pipes: simple message broker, direct REST/gRPC |
| Heavy protocols | Lightweight: JSON, Protobuf, Avro |
| Shared databases | Database per service, event-driven sync |
| Centralized governance | Team autonomy + automated contract testing |
| Maximize reuse | Prefer autonomy; tolerate duplication |

## When SOA patterns still apply

The Architect doesn't discard SOA entirely. SOA patterns that remain valid:

- **Service registry/discovery** — microservices need this too
- **Service contracts** — explicit APIs, just lighter weight
- **Business-aligned decomposition** — the fundamental insight survives
- **Enterprise-wide standards** for logging, monitoring, security — some centralization is still valuable

## When to choose which

| Choose SOA-style when | Choose microservices when |
|---|---|
| Enterprise-wide coordination is a legal/compliance requirement | Team autonomy is the primary value |
| Services are managed by different vendors (SOAP contracts) | All services are built in-house |
| Existing SOA infrastructure is working and migrating would disrupt | Starting from scratch or greenfield |
| Batch/async integration is the dominant pattern | Request-response and real-time are the dominant patterns |

## The Architect's rule

> "Микросервисы — это SOA, из которого выкинули всё, что не работало, и добавили то, чему SOA научил." — Microservices are SOA with everything that didn't work stripped out, plus the lessons SOA taught.

## Связанные материалы

- [Architecture Evolution](architecture-evolution.md) — SOA as an evolution stage
- [Architecture as Tradeoff](architecture-as-tradeoff.md) — the SOA tradeoff decisions
- [DDD and Microservices](ddd-microservices-and-distributed-systems.md) — bounded context as service boundary
- [Governance in Distributed Systems](governance-in-distributed-systems.md) — governance without centralization
- [REST Architectural Style](rest-architectural-style.md) — the microservice communication default
