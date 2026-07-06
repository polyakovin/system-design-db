---
title: Process-Driven Architecture
type: pattern
category: ddd
tags: [ddd, domain-driven-design, business-process, workflow, process-manager, saga, architecture]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# Process-Driven Architecture

## Проблема

Traditional DDD focuses on structural domain models (entities, aggregates, value objects), but real business value comes from **processes**: Order-to-Cash, Hire-to-Retire, Claim-to-Settlement. These processes span multiple aggregates, bounded contexts, and time — often hours or days. A purely structural model misses the orchestration layer.

Millett argues that DDD's tactical patterns answer "what is the domain?" but not "how does the domain flow?" Process-driven architecture bridges this gap.

## Core idea (Millett, Chapter 22)

Align software architecture with business processes, not just business structure. The process is a first-class architectural concept — not an afterthought glued on top of aggregates.

```
Business Process (end-to-end)
    │
    ├── Step 1: Aggregate A transitions → emits Event A
    ├── Step 2: Saga reacts to Event A → commands Aggregate B
    ├── Step 3: Aggregate B transitions → emits Event B
    ├── Step 4: Process Manager waits for Events A+B+C → triggers next phase
    └── ... 
```

## Process patterns

### 1. Process Manager (long-running workflow)

A Process Manager is a state machine that tracks progress across multiple aggregates and bounded contexts. Unlike a simple event handler, it maintains its own state: "we're on step 3 of 7, waiting for PaymentConfirmed event."

```
ProcessManager {
    processId: ProcessId,
    currentState: "AwaitingPayment" | "AwaitingShipment" | "Completed",
    correlationId: OrderId,
    timeout: DateTime,
    completedSteps: [Step],
    pendingSteps: [Step]
}
```

**Key characteristics (Millett):**
- Persistent state — survives restarts and failures
- Handles timeouts — if a step doesn't complete within SLA, escalate or compensate
- Idempotent — replays must not double-execute
- Human tasks supported — some steps require manual approval, not fully automated

### 2. Saga (distributed transaction through compensation)

When a process spans multiple aggregates and any step can fail, use a saga: a sequence of local transactions, each with a compensating action.

```
Saga: PlaceOrder
├── ReserveInventory()     → compensate: ReleaseInventory()
├── ChargePayment()        → compensate: RefundPayment()
└── ConfirmOrder()         → compensate: CancelOrder()
```

Millett distinguishes:
- **Choreographed saga:** each service emits events, others react. No central coordinator. Simpler, but harder to understand end-to-end flow.
- **Orchestrated saga:** a central Process Manager commands each step. More visible, single point of coordination — but also single point of failure.

### 3. Routing slip

A message carries the list of remaining steps. Each service executes its step and forwards the message to the next. Millett notes this is useful for pipelines where the sequence is known at initiation (e.g., document approval workflow).

## Mapping business processes to architecture

Millett's 4-step method:

### 1. Event Storming the process

Map the process as a sequence of domain events: `OrderPlaced → PaymentAuthorized → InventoryReserved → OrderShipped → OrderDelivered`. Each event represents a meaningful business state transition — not a technical event.

### 2. Identify aggregates and commands

For each event: which aggregate produces it? Which command triggers it?

```
Command: PlaceOrder → Aggregate: Order → Event: OrderPlaced
Command: AuthorizePayment → Aggregate: Payment → Event: PaymentAuthorized
```

### 3. Identify process boundaries (policies)

Which events trigger the next step? These are **policies**: reactive rules like "when OrderPlaced, authorize payment."

Policies are the glue between aggregates — they belong to the domain, not infrastructure. Millett: "A policy is a domain concept that says: when X happens, do Y."

### 4. Design for failure and time

Every process step can fail, and every wait can time out. Design the process model to handle:
- **Retry:** transient failures (network blip, lock timeout)
- **Compensate:** business failures (out of stock, payment declined)
- **Escalate:** timeout failures (step didn't complete in N hours → notify human)
- **Idempotency:** duplicate events must not advance the process twice

## Process-Driven vs. Aggregate-Driven

Millett's key insight: aggregates model *state*, processes model *change over time*. Both are necessary.

| Aspect | Aggregate-Driven | Process-Driven |
|---|---|---|
| Focus | Structural consistency | Temporal flow |
| Primary concern | Invariants at a point in time | Correctness across time |
| Unit of design | Aggregate boundary | Process step |
| Failure handling | Transaction rollback | Compensation + retry |
| Testing | State assertions | Sequence assertions |

## Tradeoffs

**Pros:**
- Process becomes explicit, testable, and visible — not scattered across event handlers
- Long-running workflows become first-class domain objects with persistent state
- Timeouts, retries, and compensation are built into the model, not bolted on

**Cons:**
- Additional complexity: Process Manager is another domain concept to maintain
- Can over-formalize simple flows — not every 3-step sequence needs a state machine
- Requires team to think temporally, not just structurally

## When NOT to use

- Simple CRUD with no multi-step business processes
- Synchronous request-response flows with no time dimension
- When the process is already well-served by a workflow engine (Camunda, Temporal) — don't rebuild in domain code

## Связанные материалы

- [Aggregates](aggregates.md) — processes orchestrate aggregates
- [Domain Events](domain-events.md) — events mark process steps
- [CQRS](cqrs.md) — commands drive processes, queries show progress
- [Event Sourcing](event-sourcing.md) — event stream IS the process audit trail
- [Strategic Design](strategic-design.md) — processes span bounded contexts
- [Distributed Transactions](../../advanced/distributed-transactions.md) — saga implementation details
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapter 22 (Process-Driven Architecture)
