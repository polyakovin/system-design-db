---
title: Minimum Necessary Work
category: patterns
tags: [code-simplicity, yagni, less-code, simplicity, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Minimum Necessary Work

## Problem

Developers consistently overbuild: they write code for features that *might* be needed later, add abstraction layers for hypothetical use cases, and solve problems that don't exist yet. Each unnecessary line of code is a liability — it must be read, understood, tested, maintained, and debugged forever. The codebase accumulates dead weight that slows down every subsequent change.

## Solution

Kanat-Alexander's rule: **don't write code you don't need right now.** This is the principle behind YAGNI ("You Ain't Gonna Need It"), systematized into a design philosophy.

### The case for less code

- **Less code = less bugs**. Every line is a potential defect site. Fewer lines → fewer places for bugs to hide.
- **Less code = less maintenance**. When you delete code, you delete all future maintenance of that code.
- **Less code = easier understanding**. A new developer can hold a smaller codebase in their head.
- **Less code = faster changes**. Less code to read before you can safely modify.

### The simplest fix is making the problem disappear

Kanat-Alexander's most counterintuitive principle: **the best fix to a problem is often making the problem disappear entirely**, not solving it with more code.

Example: instead of adding complex retry logic with exponential backoff for a flaky third-party API, switch to a more reliable provider. The retry code was never written, never tested, never debugged, never maintained.

Apply this heuristic to every problem:

1. **Can I remove the condition that creates the problem?** (simplest)
2. **Can I solve it without new code?** (reconfigure, change a parameter, use an existing feature)
3. **Can I solve it by deleting code?** (remove the broken feature if it's low value)
4. **Only then:** write new code.

### The law of diminishing returns to complexity

Every new feature adds complexity to the *entire system*, not just to itself. The first feature is cheap — there's nothing to interact with. The 100th feature must coexist with 99 existing features, each with their own assumptions, data formats, and edge cases.

Kanat-Alexander's formulation: **each new feature makes every subsequent feature harder to add.** The marginal cost of features increases non-linearly. This means:

- Features should be evaluated not just by their own value, but by the future value they block.
- A feature that provides moderate value today but makes the next 5 features significantly harder may be a net negative.
- Removing low-value features is not regression — it's capacity recovery.

### YAGNI in practice

Before writing any code, answer:

1. **Is there a user who needs this today?** If not, don't write it.
2. **Can I achieve the same outcome with less code?** (Existing stdlib? Existing library? Simpler algorithm?)
3. **Will this code still be valuable in 6 months?** If uncertain, make it as small and isolated as possible.
4. **Can I delete existing code instead of adding new code?** Deletion is always the best refactor.

## Tradeoffs

- "Needed right now" doesn't mean "ignore architecture entirely." Some structural decisions (API contracts, data models) are hard to change later and warrant upfront thought.
- Writing less code is not the same as writing unclear code. Tricky one-liners that nobody can read violate [Design for Change](design-for-change.md).
- For shared libraries/APIs, backwards compatibility constraints mean you *do* need to think about future use — but only after the first real consumer exists.

## Related

- [Simplicity First](simplicity-first.md) — less code = simpler system = higher D (V/E)
- [Emergence](../code-quality/emergence.md) — Kent Beck's "minimal elements" rule
- [Managing complexity](managing-complexity.md) — accidental vs. essential complexity
- [Purpose of software](purpose-of-software.md) — if it doesn't help users, it doesn't belong

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013). The YAGNI principle, law of diminishing returns to complexity, and "make the problem disappear" are recurring themes in Code Simplicity.
