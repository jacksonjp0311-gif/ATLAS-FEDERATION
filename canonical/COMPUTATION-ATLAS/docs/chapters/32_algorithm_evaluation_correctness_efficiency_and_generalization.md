# Chapter 32 — Algorithm evaluation: correctness, efficiency, and generalization

**Domain:** Methodology. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

An algorithm should be evaluated against its stated contract, not a convenient benchmark alone. Unit tests check examples and boundary cases; property-based tests examine invariants on many generated inputs; independent oracles use a mathematically or implementationally separate route; differential tests compare systems; formal proofs establish quantified results under assumptions. These forms of evidence have different strengths. Randomized trial counts do not automatically measure independence: two algorithms could share the same bug, and a large number of correlated trials can exaggerate certainty. A benchmark specification should include input generator, distribution, seeds, environment, hardware, compiler versions, numerical tolerances, and expected outputs before results are observed.

## Formal statement, symbols, and units

Observed failure rate = failures/eligible_trials, with eligibility and denominator defined in advance. Property for sorting: sorted(out) ∧ multiset(out)=multiset(in).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The logical quantifiers differ: a test asserts ∀x in a finite checked set, property(x); universal correctness requires ∀x in the declared domain. An independent oracle increases confidence but does not change the quantifier unless it is itself a proof checker with verified soundness. A benchmark also needs honest selection: a method chosen after seeing held-out task results is no longer evaluated under a sealed holdout.

## Reconstruction exercise with independently checkable output

Generate 100 seeded random graphs, test dijkstra against an independent Bellman–Ford implementation, and record any disagreement with the exact graph. Include adversarial disconnected graphs, tie weights, and very large weights. Keep the oracle separate from production code.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not equate 10,000 passing synthetic tests with field validation, cross-architecture reproducibility, or scientific peer review. Test logs are evidence of execution, not of the truth of all source claims.

## Source orientation

- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- SciPy reference, sparse graph shortest paths: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.dijkstra.html

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
