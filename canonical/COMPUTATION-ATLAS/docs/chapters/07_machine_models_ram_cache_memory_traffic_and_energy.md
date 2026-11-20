# Chapter 07 — Machine models: RAM, cache, memory traffic, and energy

**Domain:** Architecture. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The random-access machine model treats certain operations as unit cost. Real machines fetch memory through a hierarchy: registers, caches, main memory, storage, and sometimes remote nodes. Locality—spatial and temporal—can dominate performance. External-memory algorithms count block transfers; work–span models describe available parallelism; roofline-style models compare arithmetic throughput to memory bandwidth. No single model is universally correct. A survivor reconstructing a computational result should know whether reported complexity measures primitive operations, bits, cache misses, wall-clock time, monetary cost, or joules. The size of a bit representation matters when arbitrary-precision arithmetic is used. A constant-time step for an unbounded integer is an abstraction, not a literal hardware fact.

## Formal statement, symbols, and units

Work W = total primitive operations; span S = longest dependency chain; ideal time on p processors T_p ≥ max(W/p,S). Data movement often adds a separate constraint.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If two algorithms have identical O(n) arithmetic work but one streams sequentially while the other randomly accesses a large table, cache-miss behavior can diverge. Use this to resist interpreting time measurements as universal computational superiority. The effective hardware model changes with accelerators and memory pressure; the logical answer may be invariant while latency and energy are not.

## Reconstruction exercise with independently checkable output

Compare sequential and strided memory traversal in an explicitly described environment. Repeat multiple times, record temperature and load, and treat observations as local performance results. Work out a simple work–span DAG by hand without measuring hardware.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

No physical energy-efficiency claim can be inferred from count of Python-level operations alone. Bitwork-style geometric representations later require hardware and workload-level evidence rather than rhetorical savings.

## Source orientation

- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
