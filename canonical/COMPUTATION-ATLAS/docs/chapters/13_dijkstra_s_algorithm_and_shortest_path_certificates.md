# Chapter 13 — Dijkstra’s algorithm and shortest-path certificates

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

For a graph with nonnegative edge weights, Dijkstra's algorithm maintains tentative distances from a source and extracts the smallest next distance. Once a vertex is extracted with the current minimum, nonnegative edges guarantee that no undiscovered alternative can improve its distance. A practical heap implementation may contain stale entries, discarded when their priority exceeds the current recorded value. Predecessor links provide a path witness, but a path witness alone proves only an upper bound on distance. A stronger certificate combines valid predecessor chains with inequalities across every edge. That is valuable for independent checking: a producer may be buggy, while a simple verifier can still reject an invalid distance table.

## Formal statement, symbols, and units

Relaxation: d(v)←min(d(v),d(u)+w(u,v)). Certificate: d(s)=0; each finite v has an s→v predecessor chain matching d(v), and ∀(u,v), d(v)≤d(u)+w(u,v).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Every actual s→v path supplies an upper bound on the true shortest distance. Edge inequalities imply that the proposed d(v) is no greater than any path length when telescoped along edges. A predecessor chain of equalities shows the proposed d(v) is achieved by a concrete path. Together they establish equality. For vertices claimed unreachable, closedness of the reachable set under outgoing edges must be satisfied. Negative edges invalidate Dijkstra's greedy-choice proof even when no negative cycle exists.

## Reconstruction exercise with independently checkable output

Run the four-vertex example in the casebook, record heap contents after each extraction, then deliberately alter a distance or predecessor. Confirm the independent shortest_path_certificate rejects it.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The reference verifier uses a floating tolerance: near-ties and extreme magnitudes may require exact rational arithmetic. It is not a cryptographic receipt proving how a worker obtained the answer.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- SciPy reference, sparse graph shortest paths: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
