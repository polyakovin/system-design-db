---
title: Understanding Before Building
category: patterns
tags: [code-simplicity, software-design, understanding, debugging, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Understanding Before Building

## Problem

Developers routinely start coding before they fully understand the problem. They skim a ticket, form a quick mental model, and begin implementing — only to discover halfway through that their model was incomplete, the requirements were ambiguous, or the underlying system behaves differently than assumed. This produces rework, bugs, and designs that solve the wrong problem.

## Solution

Kanat-Alexander's principle: **you cannot build a good system without understanding the problem first.** Understanding is not a preliminary step you rush through — it is the foundation of all good design.

### The understanding obligation

Before writing a single line of code, you must understand:

1. **What problem** the user actually has (not what they *asked for*).
2. **Why** the current system doesn't solve it (if modifying existing code).
3. **How** the relevant parts of the system currently work — trace the real flow, don't assume.
4. **What will change** — which parts are stable, which are volatile.

### Defects are failures of understanding

Kanat-Alexander's most provocative claim: **bugs are not caused by carelessness or inattention — they are caused by not understanding the system.** If you truly understood every line of code, every interaction, and every edge case, you would not introduce defects.

This reframes debugging from "find the typo" to "find the gap in my mental model." When a bug appears:

1. Don't blame yourself for being careless.
2. Ask: *what did I not understand about this system?*
3. Fix the understanding first, then the code.

### The understanding loop

Good design follows a cycle:

```
Understand → Design → Implement → Learn → (repeat)
```

Skipping "Understand" produces designs that look correct on the surface but crumble under real-world conditions. Skipping "Learn" (post-implementation reflection) means the same misunderstandings recur.

### Practical heuristics

- **Read the code you're modifying.** Trace every caller, every callee, every data path. Don't guess.
- **Talk to users.** Their description of the problem is more valuable than their proposed solution.
- **Draw the flow.** If you can't diagram the data/control flow, you don't understand it yet.
- **Explain it to someone.** If you can't explain the problem and solution clearly, you haven't understood it.

## Tradeoffs

- Deep understanding takes time upfront. For trivial changes, the cost may exceed the benefit.
- Understanding can become analysis paralysis. The goal is *sufficient* understanding, not perfect omniscience.
- Some understanding only emerges from building. Prototyping is a valid way to learn — but treat the prototype as throwaway research, not production code.

## Related

- [Debugging](debugging.md) — McConnell's scientific debugging method; complements Kanat-Alexander's "defects as understanding gaps"
- [Design in construction](design-in-construction.md) — design decisions during implementation
- [Simplicity First](simplicity-first.md) — understanding reduces accidental complexity
- [Minimum necessary work](minimum-necessary-work.md) — don't code what you don't understand

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013). The "defects are failures of understanding" thesis is a central pillar of Code Simplicity.
