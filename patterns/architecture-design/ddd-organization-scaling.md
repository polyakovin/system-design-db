---
title: DDD Organization Scaling
type: pattern
category: ddd
tags: [ddd, domain-driven-design, governance, team-structure, conways-law, organization, scaling]
source: Patterns, Principles, and Practices of Domain-Driven Design (Scott Millett, 2015)
added: 2026-07-06
---

# DDD Organization Scaling

## Проблема

DDD works well for one team with 2–3 bounded contexts. But how do you scale it to 50 teams, 200 bounded contexts, and thousands of aggregates? Without organizational governance, bounded contexts proliferate chaotically, ubiquitous languages fracture, and context maps become stale diagrams nobody reads.

Millett addresses what Evans and Vernon touch on only briefly: **DDD at organizational scale.**

## Conway's Law and DDD (Millett, Chapter 24)

```
"Organizations which design systems are constrained to produce designs
 which are copies of the communication structures of these organizations."
                                                          — Melvin Conway, 1968
```

Millett's DDD interpretation: **bounded context boundaries will naturally mirror team boundaries.** If you fight this, you lose. If you embrace it, you get a consistent architecture.

### Inverse Conway Maneuver

Instead of letting the org chart dictate the architecture, **design the team structure to produce the desired architecture:**

1. Define target bounded contexts based on domain analysis.
2. Assign one team per bounded context.
3. Rearrange teams to match.
4. The architecture now follows naturally from team communication patterns.

Millett: "You cannot have a clean context map with messy team boundaries. Fix the organization first, or accept the architecture the organization produces."

### Team per bounded context — Millett's rules

| Rule | Rationale |
|---|---|
| One team owns exactly one bounded context | Clear ownership, no shared responsibility |
| Team size: 4–8 people (two-pizza rule) | Bounded context small enough for one team to understand deeply |
| Full-stack ownership | Team owns UI → Domain → Data for its context |
| Cross-functional within the team | No handoffs between "domain team" and "UI team" across context boundaries |
| API between teams = context boundary | Team A's public API IS the context boundary |

### When one team owns multiple contexts

Millett is pragmatic: small organizations can't afford one team per context. Two rules:

1. **Adjacent contexts only:** a team can own 2–3 tightly related contexts (Sales + Pricing). Non-adjacent contexts (Sales + HR) → split teams.
2. **No shared aggregates:** if two contexts share an aggregate, they're the same context. Either merge them or extract the shared part into a new context.

## Domain governance (Millett, Chapter 24)

### The Domain Governance Board

Millett recommends a lightweight governance structure — not a heavyweight architecture review board:

**Composition:** senior developer from each team + domain architect + product owner representative. Meets bi-weekly.

**Responsibilities:**
1. **Context boundary disputes:** Team A and Team B both want to own `Customer`. Governance board resolves.
2. **Ubiquitous language conflicts:** two teams using the same term for different concepts → rename one.
3. **New context approval:** new bounded context proposal → is it genuinely distinct? What's the context map relationship?
4. **Integration pattern selection:** API vs. events vs. shared kernel for new cross-context integration.
5. **Technical debt in domain model:** aggregates that grew too large, ACLs that leak, events that need versioning.

### The living context map

Millett insists the context map must be **living documentation** — auto-generated from code and deployment metadata, not a static Visio diagram:

```
CI Pipeline → analyze:
  ├── Package dependencies → context coupling
  ├── API schemas → integration types
  ├── Event schemas → event-driven relationships
  └── Deployment manifests → runtime topology

Output: auto-updated context map (updated on every deployment)
```

### Domain maturity model (Millett)

| Level | Characteristics | Typical org size |
|---|---|---|
| 1. Ad-hoc | No explicit contexts, one team owns everything | 1–5 devs |
| 2. Emerging | Contexts identified but boundaries are porous, models leak | 5–15 devs |
| 3. Defined | Documented context map, team per context, ACLs at boundaries | 15–50 devs |
| 4. Governed | Living context map, domain governance board, versioned contracts | 50–200 devs |
| 5. Optimising | Metrics-driven context sizing, auto-detected boundary violations | 200+ devs |

The level you need depends on organizational complexity, not on how "good" you are at DDD. A 3-person startup at Level 1 is appropriate.

### Anti-patterns in domain governance

1. **Architecture by org chart:** letting team structure dictate context boundaries without domain analysis. "The frontend team owns the frontend context, the backend team owns the backend context" — these are technical layers, not bounded contexts.

2. **Governance as gatekeeping:** every new aggregate requires board approval → teams stop modeling and start bypassing governance.

3. **Context map as artifact, not tool:** a beautiful diagram that's 6 months out of date and nobody consults. Worse than no map.

4. **Over-splitting:** 50 contexts for 20 developers. Integration overhead kills productivity. Millett: "start with fewer, larger contexts and split when the pain of staying together exceeds the pain of splitting apart."

## Tradeoffs

**Pros:** predictable architecture at scale, clear ownership, faster decision-making within context boundaries.

**Cons:** governance overhead (meetings, reviews), risk of ossification (too many rules → teams stop innovating), political resistance to domain-based team structures.

## When governance is too much

- <3 teams: governance is a conversation, not a board meeting
- Prototype/experimental projects: skip governance, distill learnings later
- Stable contexts with no integration changes: don't review what isn't changing

## Архитектор (2016): Conway's Law beyond DDD

The Architect (架构漫谈) provides a non-DDD perspective on Conway's Law, framing it as a universal architectural constraint, not a DDD-specific insight:

> "Структура команды — это архитектура. Всё остальное — детали." — Team structure IS the architecture. Everything else is details.

### The Architect's Conway corollaries

1. **You cannot out-architect your org chart.** If the organization has separate frontend and backend teams, the architecture WILL have a frontend-backend split — regardless of what bounded contexts the domain analysis suggests.

2. **Architectural problems are often organizational problems in disguise.** A service that "nobody owns" is a team structure problem, not an architecture problem. Shared databases between services are almost always the result of shared ownership or unclear boundaries between teams.

3. **Communication paths dictate coupling.** If Team A and Team B meet daily, their services will be tightly coupled — regardless of what the architecture diagram says. If they never speak, integration will be loose and documented.

4. **The Inverse Conway Maneuver is a restructuring, not a replatforming.** Before splitting the monolith, split the teams. The code will follow. Attempting the reverse (split the code, keep the teams) creates a distributed monolith.

### Where the Architect differs from Millett

Millett treats Conway's Law as a tool for DDD scaling (team per bounded context). The Architect treats it as a **diagnostic tool** for any architectural problem:

- Symptom: "Service boundaries keep getting violated."
- Millett's response: "Strengthen the bounded context, add ACLs."
- Architect's response: "Who talks to whom? The architecture is reflecting the communication patterns. Fix the communication, not the code."

## Связанные материалы

- [Bounded Context](bounded-context.md) — the atomic unit of team ownership
- [Strategic Design](strategic-design.md) — context map patterns
- [Distillation](distillation.md) — where to invest (core domain gets best team)
- [DDD and Microservices](ddd-microservices-and-distributed-systems.md) — context as service boundary
- [Bounded Context Communication](bounded-context-communication.md) — how teams integrate
- [Architecture vs Design](architecture-vs-design.md) — Conway's Law as a strategic constraint
- [Governance in Distributed Systems](governance-in-distributed-systems.md) — governing team boundaries
- [Managing Complexity](../fundamentals/managing-complexity.md) — team complexity as a source of system complexity
- [Patterns, Principles, and Practices of DDD](../../sources/books/patterns-principles-practices-ddd.md) — Chapter 24
