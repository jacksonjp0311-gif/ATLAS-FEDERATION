# Chapter 30 — Parallelism, Amdahl’s law, and synchronization cost

**Domain:** Architecture. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Parallel computing divides work among processors, but dependencies and coordination limit speedup. Amdahl's law models fixed-size work: a fraction remains serial, and the rest can be parallelized ideally. Parallel overhead, data transfer, contention, load imbalance, and memory capacity often make real speedup smaller. Gustafson-style scaling considers larger problems as resources grow, answering a different question. Amdahl's law is not evidence that a particular distributed agent swarm will run proportionally faster. Tasks may share bottlenecks, retry failed work, contend for a provider, or duplicate efforts. Measuring total compute, wall-clock critical path, and quality separately is essential.

## Formal statement, symbols, and units

Idealized speedup S(p)=1/[(1−f)+f/p+o(p)] where f is parallelizable fraction, p workers, and o(p) is overhead expressed relative to serial baseline.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The denominator separates serial time, parallelized time, and overhead. As p→∞ and o(p)=0, speedup approaches 1/(1−f) when f<1. Even without serial work, overhead may dominate at large p. Work–span analysis gives a complementary lower bound on parallel runtime. A synchronization barrier can cause idle workers, and independent throughput is not the same as critical-path latency for one request.

## Reconstruction exercise with independently checkable output

Calculate idealized speedup for f=0.9 and p in {1,2,4,8,16}. Repeat with overhead 0.1 and show a case where more workers no longer help. Record that these are assumed parameters, not measurements from PEGASUS or any other live system.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

No benchmark speedup claim follows from the model alone. Amdahl is also not a universal law of all optimization: workload scaling and changed algorithms alter the question.

## Source orientation

- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
