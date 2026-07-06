---
title: Design for Change
category: patterns
tags: [code-simplicity, software-design, change, maintenance, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Design for Change

## Problem

Software requirements change — always. Business pivots, users discover new needs, platforms evolve, dependencies break. Systems designed for a frozen set of requirements become brittle: each change requires touching code in dozens of places, and the risk of regression grows with every release.

The opposite failure is over-engineering: building a "flexible" system with plugin architectures, configuration files for every constant, and abstraction layers for hypothetical future use cases. The flexibility is never used, but the complexity remains permanently.

## Solution

Kanat-Alexander's principle: **design for change, but without over-engineering.** Accept that change is inevitable and build systems that accommodate it, but only for changes that are *likely*, not every change that is *possible*.

### The three horizons of change

1. **Changes you know are coming** — design for these explicitly. If you know there will be more payment providers, isolate the payment interface now.
2. **Changes that are plausible** — keep options open without committing. Use simple abstractions (functions, interfaces) rather than heavyweight frameworks (plugin systems, rule engines).
3. **Changes that are speculative** — ignore them. YAGNI. The cost of building for a change that never materializes exceeds the cost of adapting when it actually arrives.

### Information hiding for change

The core technique: **hide the parts that are likely to change behind a stable interface.** This is Parnas's information hiding applied pragmatically:

- Identify which decisions are volatile (storage backend, external API, UI framework).
- Encapsulate each volatile decision behind a narrow, stable interface.
- The interface should expose *what* the system needs, not *how* it's implemented.

### Design for maintenance

**Code is read 10 times more often than it is written.** (Kanat-Alexander cites this ratio; Robert C. Martin estimates it even higher.) This means:

- **Readability is the primary design constraint**, not write-time convenience, not cleverness, not brevity.
- Every time you save 5 minutes writing clever code, you cost the team 50 minutes of reading it across its lifetime.
- Naming, structure, and clarity are not cosmetic — they are the primary determinants of maintenance cost.
- The best code reads like a clear explanation of what the system does.

### Practical checklist

Before merging code, ask:

1. **Can a new team member understand this without help?** If not, restructure or add clarifying comments.
2. **Will this break if [likely change X] happens?** If yes, isolate that dependency now.
3. **Did I build flexibility for a use case that doesn't exist?** If yes, remove it.
4. **Is this code harder to read than it needs to be?** If yes, simplify.

## Tradeoffs

- Designing for change adds a small upfront cost that pays back over the system's lifetime. For throwaway prototypes, skip it.
- Knowing *which* changes are likely requires domain experience. When uncertain, favor simplicity — simple code is easier to change regardless of direction.
- Readability vs. performance: in hot paths, a well-commented complex algorithm beats a slow simple one. Profile before optimizing.

## Related

- [Simplicity First](simplicity-first.md) — simple systems are easier to change
- [Managing complexity](managing-complexity.md) — complexity as the enemy of change
- [System design principles](system-design-principles.md) — evolvability as a quality attribute
- [Clean Architecture](../architecture-design/clean-architecture.md) — dependency rule and plugin architecture

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013). The "design for change" and "code read 10x more than written" principles are core themes.
