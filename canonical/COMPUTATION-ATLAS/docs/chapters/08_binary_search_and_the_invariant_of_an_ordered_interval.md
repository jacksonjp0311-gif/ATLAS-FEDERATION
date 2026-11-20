# Chapter 08 — Binary search and the invariant of an ordered interval

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Binary search locates a target in a sorted sequence or identifies an insertion boundary. The sortedness assumption is essential; on unsorted input the same code may return a plausible but wrong answer without warning. A lower-bound implementation maintains a half-open candidate interval [lo,hi) whose elements could still contain the first key >= target. At each step, the midpoint splits the candidate interval into two pieces. Because one piece is discarded, the interval size decreases and termination follows from a nonnegative integer rank function. Duplicate keys expose the difference between “an occurrence” and “the first occurrence”. An empty array is a valid case when returning an insertion index.

## Formal statement, symbols, and units

Invariant: ∀i<lo, a_i<target; ∀i≥hi, a_i≥target. Variant: hi−lo decreases on each loop. At exit lo=hi is the insertion point.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Initially lo=0 and hi=n, so both quantified statements are vacuously true. If a_mid<target, all entries before and including mid are below target by sortedness, so lo becomes mid+1. Otherwise all entries from mid onward are at least target, so hi becomes mid. Each update preserves both conditions and decreases the interval length. The combination of induction and rank decrease proves correctness and termination for sorted finite arrays.

## Reconstruction exercise with independently checkable output

Run computation_atlas.models.lower_bound on [1,1,2,2,4] for 0,1,2,3,5. At every iteration, write the two invariant partitions. Then violate sortedness and observe that the guarantee no longer applies.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never treat a few passing lookup tests as proof that a caller supplied sorted data. Sortedness can be checked in O(n) or maintained by a trusted upstream process; that cost belongs in the system specification.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
