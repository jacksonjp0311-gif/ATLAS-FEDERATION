# Chapter 17 — 0/1 knapsack and pseudopolynomial behavior

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The 0/1 knapsack problem selects whole items to maximize value under a weight capacity. Its standard dynamic programming algorithm uses capacity as an array index, which is viable only for bounded nonnegative integer weights. An item is selected at most once. A fractional variant would require a different formulation, and a negative weight invalidates the usual recurrence. The table can be exact for a finite input but enormous when capacity is a large binary integer. This is an explicit example of pseudopolynomial complexity. An engineering-grade algorithm must enforce memory and work caps before allocating a table, and return a refusal rather than exhausting the host.

## Formal statement, symbols, and units

D(i,c)=max[D(i−1,c), v_i + D(i−1,c−w_i)] if w_i≤c; otherwise D(i,c)=D(i−1,c). Base D(0,c)=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The recurrence follows by partitioning feasible solutions according to inclusion of item i. If the item is included, the remaining capacity is c−w_i and prior items are the only choices; if excluded, the prior problem is unchanged. Induction on i proves the table value equals optimum for the declared finite instance. Reconstructing choices by comparing successive rows gives a witness. A separate exhaustive subset enumerator provides an independent oracle for small n.

## Reconstruction exercise with independently checkable output

For item weights [2,3,4], values [3,4,5], capacity 5, enumerate all eight subsets and verify optimum 7 using items 0 and 1. Increase capacity to a very large binary value while keeping item count small and analyze memory blowup.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A runtime cap is a host resource policy, not a proof the optimization problem is intractable. Approximation schemes and branch-and-bound should be studied separately in later editions.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
