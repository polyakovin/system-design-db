---
title: DDD and Microservices
type: pattern
category: ddd
tags: [ddd, domain-driven-design, microservices, bounded-context, distributed-systems, eventual-consistency, sagas]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# DDD and Microservices

## Проблема

A bounded context is a model boundary. A microservice is a deployment boundary. They often align — but treating them as the same thing leads to over-splitting, distributed monoliths, and integration nightmares.

Millett (writing in 2015, when microservices were gaining traction) bridges DDD's bounded context concept with microservice architecture, and extends it to the distributed systems challenges that come with this alignment.

## Bounded Context as service boundary (Millett, Chapters 20, 24)

### When a BC should be its own service

```
One BC → One Service when:
├── Independent deployability is needed (different release cadences)
├── Independent scalability is needed (different load profiles)
├── Different technology stacks are justified (polyglot persistence)
├── Team autonomy requires it (different team owns the BC)
└── Failure isolation is critical (one BC's crash must not affect others)
```

### When multiple BCs should share a service

```
Multiple BCs → One Service when:
├── Same team owns all of them
├── Same deployment and scaling profile
├── Low complexity — splitting adds overhead without benefit
├── Early-stage project — split later when boundaries are proven
└── Tight latency requirements that async integration can't meet
```

Millett's rule: **"Deploy together what changes together. Deploy separately what changes independently."** The bounded context defines *what* changes independently; the deployment boundary follows from that.

### The distributed monolith anti-pattern

The worst outcome: BCs are separate services but coupled at runtime through synchronous calls. Every service must be deployed together, scaled together, and debugged together — but with network latency and partial failure added. This is worse than a monolith.

Millett's prevention:
1. **No synchronous chains across services:** Service A → B → C synchronously = distributed monolith. Use events.
2. **Each service owns its data:** no shared databases between services, even if they share a bounded context.
3. **Contracts over convenience:** define explicit API contracts (gRPC, OpenAPI, event schemas). Never bypass the contract "just this once."

## Distributed systems challenges (Millett, Chapter 20)

### Eventual consistency between BCs

When BC A's aggregate transitions, BC B's corresponding data becomes stale — it's updated asynchronously via events.

Millett's pragmatic approach:
1. **Acknowledge the staleness.** The UI must reflect it: "Order placed, confirmation pending" — not "Order not found."
2. **Use correlation IDs** to trace an event from producer through all consumers.
3. **Provide reconciliation endpoints** — if the consumer's projection diverges, the user (or support) can trigger a re-sync.
4. **Monitor the lag.** If event processing falls behind by >N seconds, alert. This is a business metric, not just a technical one.

### Sagas between bounded contexts

Millett extends sagas to cross-BC workflows (not just within a single BC's aggregates):

```
Saga: OrderFulfillment (spanning 4 BCs)
├── Sales BC: OrderPlaced event
├── Payment BC: PaymentAuthorized event (or PaymentFailed → compensate Sales)
├── Inventory BC: StockReserved event (or OutOfStock → compensate Payment + Sales)
└── Shipping BC: ShipmentCreated event (or ShippingFailed → escalate to human)
```

**Millett's saga rules for cross-BC coordination:**
1. Each step is a local transaction in its own BC. No distributed transactions.
2. Compensation is a business decision, not a technical rollback. Refunding a payment has business implications — it's not like rolling back a database row.
3. The saga state is persisted in one BC (the orchestrator's). Other BCs don't know they're in a saga — they just process commands and emit events.
4. Timeouts at every step. A saga that waits forever for a response is a resource leak.

### When NOT to use eventual consistency

Millett identifies cases where eventual consistency is unacceptable:

- **Financial ledger integrity:** double-entry bookkeeping requires atomicity. If you debit one account, you must credit another in the same transaction.
- **Legal/regulatory atomicity:** "both these changes happen or neither happens" is a legal requirement.
- **User experience demands:** some UIs can't tolerate a "pending" state without confusing users.

Fallback: keep those operations in one BC, in one ACID transaction. The bounded context boundary IS the consistency boundary for a reason.

### Service discovery and resilience

Millett covers the operational side briefly:

- **Service discovery:** each service registers with a registry (Consul, etcd). Consumers discover via logical name, not IP.
- **Circuit breakers:** if a downstream BC is failing, stop calling it — fail fast, fall back, or degrade gracefully.
- **Bulkheads:** isolate failure — one BC's overload shouldn't consume all thread pool resources of its caller.

## When NOT to use microservices

Millett is explicit: "If you have fewer than 3 bounded contexts, you probably don't need microservices." A modular monolith with clear package boundaries delivers most DDD benefits without distributed systems complexity.

Signs you're ready for microservices:
- 3+ independent teams
- Different deployment cadences between contexts
- Independent scaling needs (one context has 10× the load of others)
- The modular monolith's boundaries keep getting violated (teams reaching across packages)

## Связанные материалы

- [Bounded Context](bounded-context.md) — the model boundary that maps to service boundaries
- [Strategic Design](strategic-design.md) — context map relationships become service contracts
- [Domain Events](domain-events.md) — events decouple services at runtime
- [Process-Driven Architecture](process-driven-architecture.md) — sagas span multiple services
- [DDD Organization Scaling](ddd-organization-scaling.md) — team structure drives service boundaries
- [Legacy Integration Patterns](legacy-integration-patterns.md) — strangler fig for service decomposition
- [Distributed Transactions](../advanced/distributed-transactions.md) — saga implementation
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapters 20, 24
