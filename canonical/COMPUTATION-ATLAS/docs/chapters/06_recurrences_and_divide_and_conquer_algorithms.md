# Chapter 06 — Recurrences and divide-and-conquer algorithms

**Domain:** Complexity. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Divide and conquer reduces a problem to smaller subproblems, solves them, and combines the answers. A recurrence records the cost structure. Binary search discards half the candidate interval at each step; merge sort splits the input in two and merges ordered halves. Recurrences need base cases and a definition of how n is measured. Uneven splitting, data movement, and allocation can change practical cost without overturning the high-level proof. An algorithm's return-value invariant should be stated independently of its recurrence: a quickly terminating wrong sort is not saved by having T(n)=O(n log n). For stable sorting, merge equal-key elements from the left half before the right half.

## Formal statement, symbols, and units

T_merge(n)=2T(n/2)+Θ(n) ⇒ Θ(n log n). T_binary(n)=T(⌊n/2⌋)+Θ(1) ⇒ Θ(log n).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The merge sort recurrence follows because the two halves recursively sort and merging scans each element a bounded number of times. At recursion level k, all subproblems together contain at most n elements; O(log n) levels yield O(n log n). The usual lower-bound argument for comparison sorting assumes arbitrary keys and a decision-tree model. Specialized integer sorting changes the model and may outperform comparison bounds under additional constraints.

## Reconstruction exercise with independently checkable output

Construct a merge-tree trace for eight distinct and repeated keys, listing comparisons at each level. Verify left-biased equal-key merging preserves original order. Compare recurrence predictions with measured comparisons, not machine time alone.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not apply comparison lower bounds to counting sort or assume the Master Theorem covers every recurrence without checking its regularity requirements.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
