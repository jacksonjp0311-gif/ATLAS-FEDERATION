# Chapter 50 — Type systems, specifications and proof-carrying software

**Area:** Formal Methods. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Type systems classify program expressions and may rule out certain invalid operations before runtime. Contracts and refinements strengthen that classification with preconditions, postconditions and invariants. A type checker usually proves a restricted property about syntax under a formal semantics; it does not prove that the algorithm meets a human's intended specification, that a compiler implements the language correctly, or that an external tool has permission to perform its action. Proof-carrying software separates an executable artifact from a checkable evidence object, with the consumer verifying a stated property under a small trusted checking base.

## Mathematical contract

Judgment Γ⊢e:τ means expression e has type τ in environment Γ. Hoare triple {P} C {Q} claims that if P holds and command C terminates normally, Q holds, under the command semantics and environmental assumptions.

## Derivation and reasoning

A sound typing rule is justified by preservation of well-typed execution and progress or an explicit stuck-state classification, relative to a formal language. Hoare logic uses inference rules to derive correctness properties; a checked proof remains conditional on the rule semantics. A program may be well-typed and still compute the wrong tax, wrongly classify a scientific state, or leak information through an authorized but unsafe API.

## Worked reconstruction and independent check

Take expression 1+2 and derive its integer type using an addition rule. Try true+2 and show why the rule rejects it, rather than coercing values silently. For a simple counting loop write an invariant and a decreasing rank, then separate termination evidence from postcondition correctness. Describe what a proof checker must trust and how a human could reconstruct the derivation.

## Limitations, falsification, and invalid use

This edition presents proof obligations and finite examples, not a certified general-purpose compiler, theorem prover, or formal verification of the full ATLAS runtime. Source code and proof text are independently auditable, but a formal kernel has not been trusted or reviewed.

## Cross-domain meaning

Agent evidence receipts may eventually carry proof objects, but those require explicit semantics and a host-owned verifier before operational use.

## Source orientation and recoverability

- [MIT OpenCourseWare, Mathematics for Computer Science](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) — original publisher bytes unavailable in this package.
- [Stanford Encyclopedia of Philosophy, Computability and Complexity](https://plato.stanford.edu/entries/computability/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
