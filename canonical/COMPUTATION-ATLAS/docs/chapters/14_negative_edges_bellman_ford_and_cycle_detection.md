# Chapter 14 — Negative edges, Bellman–Ford, and cycle detection

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Negative edge weights arise in transformed optimization problems, potential-based graph methods, and some economic or energy accounting models. Negative edges are not by themselves a failure, but they break the greedy logic of Dijkstra. Bellman–Ford repeatedly relaxes all edges and, after |V|−1 passes, finds finite shortest paths if no negative cycle reachable from the source exists. A further successful relaxation indicates a reachable negative cycle, making shortest-path cost unbounded below for vertices reachable from that cycle. Unreachable negative cycles do not invalidate distances from a source that cannot reach them. Status codes must therefore distinguish finite distances, unreachable vertices, and reachable negative cycles.

## Formal statement, symbols, and units

After k complete passes, d(v) is no greater than the minimum path length using at most k edges. A simple finite shortest path has ≤|V|−1 edges.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If a finite minimum path contained a repeated vertex, the repeated segment would form a cycle. Removing any nonnegative cycle cannot make it worse, so a simple path of at most |V|−1 edges exists when no relevant negative cycle spoils the optimum. This supports the pass count. If relaxation remains possible after that, the path can continue to improve via a negative cycle. The proof is relative to a static graph, exact weights, and reachable subgraph.

## Reconstruction exercise with independently checkable output

Construct a source connected to a two-node negative cycle; record distances after each pass and reject a finite shortest-path claim. Move that cycle to a disconnected component and verify finite source distances remain valid.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not infer a negative cycle merely because a numerical optimization failed to converge. Floating-point comparisons and malformed graphs require separate diagnosis.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
