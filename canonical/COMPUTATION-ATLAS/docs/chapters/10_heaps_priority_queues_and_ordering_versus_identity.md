# Chapter 10 — Heaps, priority queues, and ordering versus identity

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A binary heap is an array-based complete binary tree with local parent-child ordering. Insert and delete-min run in O(log n) in the worst case; peeking at the minimum is O(1). A heap is not a sorted array, and iterating its internal storage does not produce sorted output. A priority queue supports best-first algorithms such as Dijkstra when keys are valid. Implementations without decrease-key commonly add duplicate entries and discard stale ones when popped; correctness depends on comparing the popped priority against the current best known value. Tie-breaking must be deterministic when reproducibility matters. A task scheduler also needs fairness and liveness criteria; heap order alone does not ensure that every lower-priority task eventually executes.

## Formal statement, symbols, and units

Heap invariant: parent(i)≤child(i), with parent(i)=⌊(i−1)/2⌋. Heap operations modify O(log n) ancestor/descendant levels.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A heap's local invariant implies the root is globally minimal by transitivity along parent chains. Insert restores the property by bubbling upward; delete-min replaces the root and pushes down. A stale heap entry is safe to ignore if a more recent smaller distance is already recorded. Stable tie-breaking in a scheduler requires an explicit sequence counter, not incidental memory addresses.

## Reconstruction exercise with independently checkable output

Represent the heap [1,3,2,7,5,4] as a binary tree, verify each parent-child inequality, then insert 0 and trace swaps. Compare with the priority queue used by the shortest-path reference.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not infer starvation freedom from a valid heap invariant. Priority queues model ordering, not policy fairness, progress, or correct authority boundaries for dispatched work.

## Source orientation

- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
