# Chapter 26 — Inductive invariants and loop correctness

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

An invariant is a property of system states preserved by every allowed transition. An inductive invariant requires initialization and step preservation. It is a sufficient proof principle: if the invariant holds initially and no transition leaves it, every reachable state satisfies it. A proposed invariant may fail induction because it is too weak even when the target safety property is true; strengthening is often needed. In an explicitly finite universe, a checker can enumerate transitions and validate an invariant. If a successor leaves the declared universe, rejecting the model is more honest than silently ignoring the transition. The specific set of transitions must be preserved for later auditors to reproduce the proof.

## Formal statement, symbols, and units

Initialization P(s0); consecution ∀s,t: P(s)∧T(s,t) ⇒ P(t). Then ∀ reachable s, P(s).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Prove by induction on trace length. The base case follows from initialization. For any length-k trace ending in a P-state, the transition property ensures the successor also satisfies P, establishing length k+1. This logical skeleton is broadly useful in algorithms, protocol design, and control. The finite checker performs a universal check only over *its supplied state universe*. The relation to the physical system is an independent modeling obligation.

## Reconstruction exercise with independently checkable output

For states 0–3 and transition s→min(s+1,3), prove 0≤s≤3 inductive. Replace the property with s==0 and identify the one-step counterexample. Explain why a true but noninductive property may require auxiliary state.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Unit tests of typical transitions are not inductive proofs. Neither proof scripts nor hashes authenticate the source of the model unless independently controlled.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
