# Chapter 09 — Stable sorting and comparison lower bounds

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A sorting algorithm returns values ordered by a declared key. Correctness has two parts: the output is ordered and it contains exactly the input multiset. Stability adds a third: items with equal keys preserve original relative order. Merge sort meets these properties with an O(n log n) comparison bound under appropriate ordering assumptions. Sorting algorithms differ across in-place memory use, worst-case bounds, adaptivity, and key domains. A finite certificate can check that one output is sorted and a permutation of one input; it cannot prove that the implementation behaves correctly for every future input. A custom key that violates transitivity invalidates many algorithmic proofs.

## Formal statement, symbols, and units

Permutation: multiset(output)=multiset(input). Order: ∀i<n−1, key(out_i)≤key(out_(i+1)). Stability: equal-key original indices remain in increasing order.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Merge sort's stability follows inductively if each recursively sorted half is stable and ties at merge choose the left element first. The logarithmic-depth recursion and linear merges give O(n log n). Comparison sorting must distinguish n! permutations; a binary decision tree requires height Ω(log2(n!))=Ω(n log n). Integer keys in a constrained range allow counting sort and invalidate the decision-tree premise.

## Reconstruction exercise with independently checkable output

Create tagged duplicate keys and trace the merge at each level. Check multiset preservation independently using a frequency map; verify that the order of equal-tag groups is maintained.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The certificate implemented here relies on hashable elements and Python comparison semantics. Data corruption, inconsistent comparators, locale-dependent rules, or missing input items may escape a mere sortedness check.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
