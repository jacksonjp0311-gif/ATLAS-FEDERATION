# Chapter 25 — Finite-state reachability and bounded model checking

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Model checking explores explicitly represented states and transitions to answer properties about a declared model. Reachability can find a concrete path witness to a goal. Exhaustive failure to find a goal establishes non-reachability only if the reachable state graph has been completely explored and the model faithfully represents the system. State explosion can make exhaustive enumeration impossible; a resource limit produces an unknown verdict, not a false property. Model checking is distinct from running a real distributed system: clock timing, nondeterministic environment input, network loss, and memory corruption may be absent from the abstraction. A preservation-grade report must identify the model boundary and whether the search was complete.

## Formal statement, symbols, and units

Reach(initial,goal) ⇔ ∃ path s0→s1→…→sk with s0=initial and goal(sk). A visited set prevents infinite re-exploration of finite graph cycles.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Breadth-first traversal discovers shortest witnesses by edge count in an unweighted finite graph. If the exploration queue empties after every legal successor has been considered, no path reaches the goal in the stated graph. If the queue remains when the budget expires, non-reachability has not been established. This is a finite exact result that does not contradict the general undecidability of arbitrary-program halting.

## Reconstruction exercise with independently checkable output

Supply states {0,1,2}, transitions 0→1 and 1→2, and a goal predicate state==2. Compare the full exploration result with one limited to a single expansion; the latter must return unknown.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not equate a bounded model checker with a universal proof engine. Unmodeled state dimensions or outside-world actions can invalidate the model-level guarantee.

## Source orientation

- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
