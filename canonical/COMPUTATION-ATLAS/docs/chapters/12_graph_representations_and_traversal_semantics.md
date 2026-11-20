# Chapter 12 — Graph representations and traversal semantics

**Domain:** Algorithms. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A graph consists of vertices and edges; a directed graph distinguishes ordered pairs. Adjacency lists use space proportional to vertices and edges, while adjacency matrices use quadratic space in the vertex count. Breadth-first search explores unweighted graphs in increasing number of edges from the source. Depth-first search follows branches and supports component analysis, topological ordering, and cycle detection. Edge direction, multigraph conventions, self-loops, and duplicate edges must be declared. An unreachable vertex is a mathematical result only relative to the given graph snapshot. In a distributed system whose graph changes during analysis, that snapshot may already be stale. The representation matters because a missing vertex key in an adjacency dictionary can silently remove edges if the implementation does not validate the whole node set.

## Formal statement, symbols, and units

Adjacency-list traversal work O(|V|+|E|), provided each node and edge is processed O(1) times. Unweighted distance dist(v)=number of edges on shortest source–v path.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

BFS maintains a FIFO frontier. All vertices at distance k are dequeued before those first discovered at distance k+1. Induction on layer k establishes that the first assigned distance is minimal. DFS uses a stack and does not generally discover minimum-length routes. Strongly connected components require checking reachability in both directions; treating a directed edge as undirected changes the problem.

## Reconstruction exercise with independently checkable output

Represent the same four-node graph as an adjacency list and matrix, enumerate edges, then execute BFS by hand and compare the cost of checking a missing edge in each representation.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A path found by DFS is not generally the shortest path. Declaring a graph with omitted vertices, mixed edge directions, or inconsistent weights invalidates downstream guarantees.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- Pat Morin, Open Data Structures: https://www.opendatastructures.org/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
