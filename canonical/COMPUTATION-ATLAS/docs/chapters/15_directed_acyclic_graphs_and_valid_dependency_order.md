# Chapter 15 — Directed acyclic graphs and valid dependency order

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A directed acyclic graph (DAG) admits a topological order: every directed edge points from an earlier to a later vertex. This structure supports build systems, dataflow computation, scheduling, and dynamic programming. Kahn's algorithm tracks indegrees, repeatedly removes a zero-indegree vertex, and detects a cycle when unprocessed vertices remain. Cycles are not necessarily errors in all dynamical systems, but they invalidate an acyclic dependency interpretation unless some feedback or iterative semantics is explicitly supplied. A dependency graph also needs a completion contract. Receiving a worker result is not necessarily satisfying the prerequisite if the result has not been validated, admitted, or published.

## Formal statement, symbols, and units

Topological order π satisfies π(u)<π(v) for each edge u→v. A finite directed graph admits π iff it has no directed cycle.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

In a finite DAG there exists at least one vertex of indegree zero: otherwise following predecessor edges indefinitely repeats a vertex, creating a directed cycle. Remove a source, apply induction to the remaining DAG, and prepend it. Conversely, a directed cycle would require π(v1)<π(v2)<…<π(v1), an impossibility. The proof gives existence; a queue or heap chooses one among many valid orders.

## Reconstruction exercise with independently checkable output

Topologically sort a six-task graph and record every zero-indegree candidate at each step. Introduce a single back edge and confirm the algorithm refuses a topological order. Specify whether edges mean “must finish” or “must be independently verified”.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

One valid order does not prove optimal makespan or fair execution. The graph is a model of declared dependencies, not a complete worker-runtime guarantee.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
