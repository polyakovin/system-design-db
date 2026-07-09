---
title: Design Precedes Testing
category: patterns
tags: [code-simplicity, software-design, testing, quality, kanat-alexander]
source: books/simple-elegance-of-software-design.md
added: 2026-07-06
---

# Design Precedes Testing

## Problem

The industry has internalized "write tests" as the primary quality practice. Teams invest heavily in test coverage, CI pipelines, and QA processes while neglecting design. The result: well-tested systems that are still buggy, hard to change, and expensive to maintain. Testing catches defects after they exist; it doesn't prevent them.

## Solution

Kanat-Alexander draws a sharp distinction: **testing and debugging are not the same as design, and design is primary.** Good design prevents entire categories of bugs from ever being written. Testing can only catch the bugs that slip through.

### Design prevents bugs; testing finds them

- **Design** eliminates bug *classes* — by making invalid states unrepresentable, by enforcing invariants at the type level, by simplifying control flow so edge cases are visible.
- **Testing** finds individual bug *instances* — specific inputs that produce wrong outputs. Testing is necessary but insufficient.

A system with excellent tests and poor design will have:
- Many tests (because the design doesn't prevent bugs).
- Brittle tests (because tests couple to implementation, not behavior).
- Slow development (because every change breaks tests that test the wrong thing).

A system with good design and minimal tests will have:
- Fewer bugs overall.
- Tests that verify behavior, not implementation.
- Faster development (because changes don't cascade).

### Proactive quality: design as bug prevention

Good design prevents bugs by:

1. **Making invalid states unrepresentable.** Use types, enums, and data structures where the compiler/reviewer can see that certain states are impossible.
2. **Minimizing the number of things that can change.** Fewer mutable variables → fewer states → fewer bugs.
3. **Keeping modules small.** A 50-line function has far fewer possible bugs than a 500-line function, even before testing.
4. **Explicit contracts.** Documented preconditions, postconditions, and invariants make violations visible.
5. **Simplicity.** The simplest solution has the fewest places for bugs to hide.

### The role of testing

Testing is valuable but secondary. It serves two purposes:

1. **Verification**: confirming that the design was implemented correctly.
2. **Regression protection**: ensuring that future changes don't break existing behavior.

Testing cannot replace design because testing can only find bugs in the code that was *written*. Design eliminates the bugs that would have been written in a worse design.

### Practical order of operations

When building a feature:

1. **Design** — understand the problem, choose the simplest solution, define interfaces and invariants.
2. **Implement** — write the minimum code to realize the design.
3. **Test** — verify behavior matches intent.
4. **Review** — have another person check your understanding.

Never skip step 1 because "we'll catch it in testing." Testing catches the bugs you anticipated. Design prevents the bugs you didn't anticipate.

## Tradeoffs

- Design takes time. For trivial scripts or throwaway prototypes, testing alone may be sufficient.
- Over-design (building abstractions "to prevent future bugs") becomes accidental complexity. Design for the problems you actually have.
- TDD (test-first) is not incompatible with this principle — TDD is a design *technique*, not a testing technique. Writing tests first forces you to think about behavior before implementation.

## Related

- [Simplicity First](simplicity-first.md) — simple design is the best bug prevention
- [Understanding before building](understanding-before-building.md) — understanding prevents defects
- [Defensive programming](defensive-programming.md) — protecting code from invalid inputs
- [Unit tests](../code-quality/unit-tests.md) — Clean Code testing practices
- [Test Architecture](../code-quality/test-architecture.md) — flexible test design: design quality enables test quality
- [Minimum necessary work](minimum-necessary-work.md) — less code = fewer bugs

## Source

Max Kanat-Alexander, *The Simple Elegance of Software Design* (2013). The primacy of design over testing is a core Code Simplicity principle.
