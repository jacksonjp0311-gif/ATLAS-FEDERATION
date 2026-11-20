# Chapter 44 — Complexity classes P, NP and careful reductions

**Area:** Theory. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Complexity classes describe families of formal decision problems under explicit machine models and input encodings. P contains languages decided by a deterministic algorithm in polynomial time; NP contains languages with polynomial-size certificates verified in polynomial time, equivalently accepted by a nondeterministic polynomial-time machine. NP-hardness is established by suitable reductions from already-hard problems, not by a problem merely seeming difficult. A problem can be NP-hard without belonging to NP, while NP-completeness requires both NP membership and NP-hardness.

## Mathematical contract

P⊆NP. A language L is NP-complete when L∈NP and ∀K∈NP, K≤_p L. A many-one polynomial reduction f must satisfy x∈K iff f(x)∈L and compute f in polynomial time.

## Derivation and reasoning

The reduction preserves yes/no membership in both directions. Without the reverse direction, a mapping can produce misleading evidence of hardness. To show a problem is NP-complete, provide a certificate verifier with polynomial bound and a reduction from a known NP-complete problem. The still-unresolved P versus NP question must not be treated as settled by performance observations, large LLMs or heuristic solvers.

## Worked reconstruction and independent check

Encode subset sum as a decision problem, define the input length in bits, and show why an O(nW) dynamic program can be pseudopolynomial rather than polynomial in input length. Explain what a correct reduction to a different decision problem would need to preserve. Do not claim to have proved a new completeness result.

## Limitations, falsification, and invalid use

Worst-case difficulty is not the predicted cost of one ordinary input. Empirical runtime failure cannot prove NP-hardness or undecidability. Complexity class definitions alone do not specify hardware energy or online provider latency.

## Cross-domain meaning

Complexity theory constrains Computation and Agent planning, but it does not prove an AI architecture has achieved general reasoning or improved any task distribution.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [Stanford Encyclopedia of Philosophy, Computability and Complexity](https://plato.stanford.edu/entries/computability/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
