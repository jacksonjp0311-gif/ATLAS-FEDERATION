# Chapter 45 — Approximation algorithms and objective guarantees

**Area:** Optimization. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

For difficult optimization problems, an algorithm may provide a feasible solution with a provable quality ratio, even when exact optimum is expensive to compute. An approximation guarantee compares objective values to the best possible solution under a specified problem instance class. It is distinct from a heuristic benchmark: an average observed score over examples is not a worst-case approximation proof. Some approximation schemes become computationally impractical as the desired accuracy increases, so the dependence on ε must be stated.

## Mathematical contract

For nonnegative minimization cost, ρ-approximation means ALG(I)≤ρ·OPT(I), ρ≥1. For maximization, ALG(I)≥OPT(I)/ρ. A PTAS has polynomial input-time for each fixed ε>0, but may grow rapidly as ε→0.

## Derivation and reasoning

The greedy set-cover algorithm can be analyzed by charging each newly covered element a portion of the selected set's cost. Comparing these charges to an optimal set cover leads to a logarithmic performance factor. The proof depends on set coverage and cost assumptions; translating arbitrary scheduling or memory retrieval into set cover requires an explicit reduction and a correct objective. A ratio against a nonoptimal baseline is not an approximation guarantee.

## Worked reconstruction and independent check

Construct a four-element set-cover example and enumerate all feasible covers. Compare the greedy cover to exact optimum and identify whether the guarantee holds for the declared cost model. Explain why a case with an impressive ratio does not establish the theorem for all inputs.

## Limitations, falsification, and invalid use

No universal approximation ratio is claimed for Bitwork routing, source retrieval or agent collaboration. Even a proven approximation algorithm can produce unsafe choices if the mathematical objective excludes a real-world constraint.

## Cross-domain meaning

The future router can use approximate search once its evidence-loss and cost objectives are explicitly defined and independently evaluated.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT 6.006 Introduction to Algorithms, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
