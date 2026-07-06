---
title: Simplicity First
category: patterns
tags: [code-simplicity, software-design, simplicity, complexity, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Simplicity First

## Problem

Software systems grow in complexity over time. Every feature, dependency, and abstraction adds cognitive load. The natural tendency is to add more — more code, more layers, more patterns — without asking whether the addition *reduces* or *increases* the system's total complexity. Eventually, the accumulated accidental complexity overwhelms the team: changes become slow, bugs multiply, and nobody fully understands the system.

## Solution

Max Kanat-Alexander's central thesis: **simplicity is the fundamental goal of software design**, not a nice-to-have or an afterthought. Every design decision should be evaluated against one question: does this make the system simpler or more complex?

### Core equation

Kanat-Alexander defines a system's desirability (`D`) as:

```
D = V / E
```

Where:
- `V` (Value) — how much the system helps users achieve their goals.
- `E` (Effort) — the total cost of building, maintaining, and changing the system over its lifetime.

Maximizing `D` means either increasing `V` (more user value) or decreasing `E` (less complexity). In practice, decreasing `E` is usually the higher-leverage move.

### Simplicity is not minimalism

Simplicity doesn't mean "fewest lines of code" or "no features." It means:

- **No unnecessary complexity**: every abstraction, pattern, and dependency must justify its existence.
- **Understandable**: a new team member can comprehend a module without reading the entire codebase.
- **Changeable**: the design accommodates future changes without requiring cascading rewrites.

### The simplicity heuristic

When making any design decision, ask:

1. Does this reduce the total number of concepts in the system?
2. Can I explain this to another developer in one sentence?
3. If I remove this, what breaks — and is that breakage acceptable?

If the answer to #1 is "no", you're adding complexity. Justify it explicitly.

## Tradeoffs

- Simplicity slows down feature delivery in weeks 1-4, saves months in years 2-5.
- Over-simplifying can produce "too generic" code that handles cases that never occur — this is accidental complexity in disguise.
- The simplest solution is often not the most performant. Profile first, optimize only where data shows it matters.

## When NOT to simplify

- Security: never simplify away defense-in-depth.
- Data integrity: never skip validation or transaction boundaries.
- Regulatory requirements: compliance is essential complexity, not accidental.

## Related

- [Managing complexity](managing-complexity.md) — McConnell's take on essential vs. accidental complexity
- [Code quality](code-quality.md) — simplicity as a code quality dimension
- [Emergence](../code-quality/emergence.md) — Kent Beck's rules of simple design
- [Purpose of software](purpose-of-software.md) — why simplicity matters: user value

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013), also known as *Code Simplicity*.
