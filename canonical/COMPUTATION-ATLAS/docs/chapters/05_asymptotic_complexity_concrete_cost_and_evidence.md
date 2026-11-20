# Chapter 05 — Asymptotic complexity, concrete cost, and evidence

**Domain:** Complexity. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Algorithm analysis distinguishes input-size growth from empirical wall-clock measurements. Worst-case, average-case, amortized, and smoothed complexity answer different questions. O(g(n)) is an eventual asymptotic upper bound, not a claim that every run takes g(n) seconds. Omega and Theta express lower and tight asymptotic bounds. Constants and cache effects matter enormously for realistic inputs; the asymptotic notation intentionally abstracts some of them away. A faithful report states the computational model, the variable n, input distribution assumptions, and memory accounting. Counting comparisons is not the same as counting CPU cycles, energy, branch misses, or external I/O. A finite timing chart can falsify some models but cannot prove an asymptotic theorem for all n.

## Formal statement, symbols, and units

T(n) ∈ O(g(n)) iff ∃c>0,n0∀n≥n0: T(n)≤c g(n). For Θ(g), require both asymptotic upper and lower bounds.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

For a loop performing n operations, construct a step-count bound with chosen primitive costs. To show a divide-and-conquer recurrence, account separately for the branch work and merge work, not just recursion depth. Distinguish complexity of the *problem* (best algorithm known, lower bounds) from complexity of a *particular implementation*. An NP-complete problem can have fast solutions for special instances; the worst-case label does not predict a particular input's runtime.

## Reconstruction exercise with independently checkable output

Count primitive comparisons for merge sort on increasing n and compare with n log2(n). Record hardware, interpreter, implementation, and random seed for any timings. Provide both a mathematical upper-bound argument and empirical measurements without conflating them.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Beware benchmark extrapolation across architectures, claiming practical speed from Big O alone, and mislabeling pseudopolynomial algorithms as polynomial in input bit-length.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
