---
title: Domain-Driven UI
type: pattern
category: ddd
tags: [ddd, domain-driven-design, ui, presentation, task-based-ui]
source: Implementing Domain-Driven Design (Vaughn Vernon, 2013)
added: 2026-07-06
---

# Domain-Driven UI

## Проблема

UIs built directly on database tables or CRUD endpoints bypass the domain model. Users see table rows, not business concepts. Complex workflows (placing an order, approving a claim) require the UI to orchestrate business rules it shouldn't know about.

## Решение

Vernon describes a Presentation Model that reflects the domain's ubiquitous language, not the database schema. The UI is task-based — each screen represents a domain use case, not a CRUD form.

## Key concepts (Vaughan Vernon, Chapter 14)

### Presentation Model

A Presentation Model is a DTO shaped for a specific UI screen, derived from the domain's read model (CQRS) or composed from multiple aggregates:

```
Domain:               UI:
Order {               OrderView {
  id: OrderId           orderId: "ORD-123"
  customerId: CustId    customerName: "Alice"
  items: [LineItem]     itemCount: 3
  total: Money          total: "$42.00"
  status: OrderStatus   status: "Processing"
}                     }
```

The Presentation Model is dumb data. No business logic. The domain model remains the single source of business rules.

### Task-based UI

Vernon advocates structuring UIs around tasks (use cases), not entities:

| Anti-pattern (CRUD-based) | Pattern (Task-based) |
|---|---|
| "Edit Order" form with 20 fields | "Approve Order" → shows relevant data, one button |
| User must know the process | UI guides through the process |
| Direct entity editing | Commands: `ApproveOrder`, `RejectOrder`, `RequestChanges` |

Each task:
1. Loads a Presentation Model (from read model).
2. Renders the UI.
3. On submit, sends a **command** to the application layer (not an update to the entity).
4. The application service loads the aggregate, executes the domain logic, and persists.

### Composing views from multiple bounded contexts

A single UI screen often needs data from multiple BCs. Vernon describes three approaches:

1. **Composite UI (micro-frontends):** each BC owns its UI fragment. The shell composes them. Complex orchestration, but clean boundaries.
2. **API composition layer (BFF — Backend for Frontend):** a dedicated service calls multiple BC APIs, assembles the view model, returns it to the UI. Simplest for most cases.
3. **Cross-BC read model:** a dedicated read DB that aggregates data from multiple BCs via events. Powerful but adds coupling.

### Testing the UI

Vernon's approach: test the domain logic independently. UI tests verify:
- Correct Presentation Model is rendered for given domain state.
- Correct command is sent on user action.
- Edge cases: empty states, error states, loading states.

He advocates thin UI logic — the domain handles all decisions, the UI just renders and sends commands.

## Tradeoffs

**Pros:**
- UI speaks the user's language (ubiquitous language), not the database's.
- Domain logic stays in the model, testable without UI.
- Task-based UI reduces user errors — the UI enforces the process.

**Cons:**
- More development effort than CRUD scaffolding.
- Requires collaboration between UX and domain experts.
- Presentation Model maintenance — changes to domain propagate to views.

## When to apply

- Complex workflows with business rules (claims, approvals, ordering).
- Multiple UIs (web, mobile, API) sharing the same domain.
- Users benefit from guided processes rather than free-form data entry.

## When NOT to apply

- Simple CRUD applications (admin panels for configuration tables).
- Internal tools where domain complexity is minimal.
- When the team can't invest in UX design alongside domain modeling.

## Связанные материалы

- [CQRS](cqrs.md) — read models power the Presentation Model
- [Domain Events](domain-events.md) — drive read-model updates for the UI
- [Bounded Context](bounded-context.md) — composing views across contexts
- [Strategic Design](strategic-design.md) — integration for composite UIs
- [Implementing Domain-Driven Design](../../sources/books/implementing-domain-driven-design.md) — глава 14 (Application, User Interface)
