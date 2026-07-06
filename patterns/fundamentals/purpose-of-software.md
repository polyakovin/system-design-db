---
title: Purpose of Software
category: patterns
tags: [code-simplicity, software-design, user-value, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Purpose of Software

## Problem

Developers and teams frequently lose sight of *why* they're building software. They optimize for technical elegance, framework purity, code coverage metrics, or personal preference — forgetting that none of these deliver direct value to users. When the purpose is unclear, every decision becomes a matter of taste rather than a tradeoff against user outcomes.

## Solution

Kanat-Alexander states a simple but radical principle: **the purpose of software is to help people**. Everything else — architecture, code quality, test coverage, performance — is secondary. They are means, not ends.

### The value equation revisited

Recall the desirability equation from [Simplicity First](simplicity-first.md):

```
D = V / E
```

`V` (Value) is defined solely by how much the software helps its users accomplish their goals. If a feature or refactor doesn't increase `V` or decrease `E`, it is waste.

### Value is behavior, not code

**The value of a system is in its behavior, not its code.** Users don't care about your clean architecture, your monad transformers, or your elegant type system. They care that the system:

1. Solves their problem.
2. Does so reliably.
3. Doesn't get in their way.

Code is a liability — a necessary cost to produce the desired behavior. Every line of code is a line that must be read, understood, debugged, and maintained. The ideal system produces maximum user value with minimum code.

### Practical implications

When making any design or implementation decision, ask:

1. **Does this help users?** If not, why are we doing it?
2. **Is this the simplest way to help users?** Complexity that doesn't serve user value is theft from future development speed.
3. **Would users notice if we removed this?** If no, it's probably accidental complexity.

### The behavior-over-code filter

Before writing code, define the desired behavior change. Before refactoring, define what user-visible improvement it enables. If you can't articulate the user benefit, don't write the code.

## Tradeoffs

- Pure user-value focus can neglect internal quality to the point where future user value becomes impossible to deliver. The art is balancing today's user value against tomorrow's ability to deliver.
- Some work (refactoring, testing infrastructure, monitoring) doesn't directly help users but is necessary to *keep* helping users at sustainable velocity.

## Related

- [Simplicity First](simplicity-first.md) — why simplicity is the path to maximizing V/E
- [System design principles](system-design-principles.md) — starting with user workflow, not technology
- [Design for change](design-for-change.md) — building systems that evolve with user needs

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013). The behavior-over-code principle is a recurring theme throughout the book.
