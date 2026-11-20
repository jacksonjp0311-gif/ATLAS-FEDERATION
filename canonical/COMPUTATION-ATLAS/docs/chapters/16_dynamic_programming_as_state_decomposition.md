# Chapter 16 — Dynamic programming as state decomposition

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Dynamic programming solves problems with overlapping subproblems and a valid optimal-substructure relation. The designer selects a state representation and recurrence, defines base cases, and decides whether to memoize recursively or fill a table iteratively. The dominant danger is a wrong state: a short table cannot represent a hidden dependency that the recurrence actually needs. A state must contain all information relevant to future decisions. Dynamic programming is not an optimization oracle and does not make hard problems polynomial in input *bit length*. Storage can sometimes be compressed when only previous rows are required, but recovering an optimal action sequence may require parent pointers or recomputation.

## Formal statement, symbols, and units

Bellman principle: V(s)=opt_a {r(s,a)+V(T(s,a))} under a declared acyclic/finite-horizon dependency relation. State and transition design determine correctness.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Prove a recurrence by dividing optimal solutions according to a final or first decision. If every feasible solution falls in exactly one case and the recurrence considers all cases without allowing invalid combinations, induction on state order establishes optimality. For a tabulated 0/1 knapsack, the final item is either excluded or included, which motivates two alternatives. For some domains, decisions are history-dependent unless that history is encoded in the state.

## Reconstruction exercise with independently checkable output

Write a three-item knapsack table with capacities zero through five, trace the include/exclude transition, and reconstruct selected item indices. Explain why the value table alone cannot be applied to a divisible-item problem without changing the recurrence.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Beware hidden state, circular recurrences without a convergence theorem, accidental use of an item more than once, and declaring O(nW) polynomial in the input length when W is encoded in binary.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
