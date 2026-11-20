# Chapter 36 — Minimum spanning forests and Kruskal’s algorithm

**Area:** Algorithms. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

A spanning forest connects each connected component of an undirected weighted graph without cycles. A minimum spanning forest minimizes total selected edge weight over all such forests. Kruskal's algorithm considers edges in nondecreasing order, accepting an edge precisely when it joins previously separate components. DSU makes that component test efficient. Negative finite edge weights are allowed in this undirected objective, unlike Dijkstra's shortest paths. Self-loops cannot improve connectivity and are excluded.

## Mathematical contract

Find forest F minimizing Σ_(e∈F) w(e), subject to F acyclic and connecting every original connected component. Repeatedly accept minimum not-yet-considered edge joining distinct DSU components.

## Derivation and reasoning

The cut property gives the greedy argument: if an edge is lightest across a cut respected by the current forest, some optimum forest contains it. Exchanging the edge with one crossing the same cut preserves a spanning forest without increasing cost. An accepted edge never creates a cycle because its endpoints are in separate DSU classes. When no edges remain, every original component is connected.

## Worked reconstruction and independent check

On vertices 0–3 with edges (0,1,1), (1,2,2), (0,2,5), (2,3,1), the algorithm accepts indices 0,3,1 and reports total weight 4. A separate NetworkX oracle computes the same forest weight on randomized inputs, including disconnected graphs.

## Limitations, falsification, and invalid use

This proof concerns exact graph edges and fixed costs. It does not choose shortest paths, minimize maximum end-to-end delay, or resolve hidden energy, temporal, geographical or authorization constraints. Weight ties can produce multiple correct forests.

## Cross-domain meaning

Spanning trees provide inexpensive connectivity abstractions for distributed architectures, but a reliable network protocol also requires failure handling and temporal semantics.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
