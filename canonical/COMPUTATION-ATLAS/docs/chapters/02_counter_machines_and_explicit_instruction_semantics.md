# Chapter 02 — Counter machines and explicit instruction semantics

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A two-counter machine is a small universal-style model using two nonnegative integer registers and three instruction forms: increment with branch, decrement-if-positive with branch, and halt. A formal instruction grammar makes its behavior analyzable without a general-purpose programming language. Each step is deterministic when the program counter is valid. A bounded interpreter can execute a finite prefix of any run, record the registers and program counter, and distinguish normal halting from a step-budget cutoff. This distinction prevents a simulation from presenting an undecidable judgment as an experimental finding. The mathematical model allows unbounded counters; the reference implementation uses finite machine memory, so actual runtime and overflow limitations remain separate.

## Formal statement, symbols, and units

Program P = (I_0,…,I_(m-1)); configuration C=(pc,r0,r1). Step relation C→C′. A run is C_0→C_1→… until HALT or external budget exhaustion.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

An induction on step count establishes that register values remain nonnegative, provided the initial counters are nonnegative and decrement only occurs when the selected register is positive. It does not establish that the run halts. A loop that continually increments counter zero is a valid finite program whose observed finite prefixes never halt. A budget of B steps certifies only those B steps. The words “unknown” and “non-halting” carry materially different epistemic meanings.

## Reconstruction exercise with independently checkable output

Use computation_atlas.models.counter_machine to run a halt program, a decrement program, and an increment loop. Record all outputs with program bytes and step budget. Repeat with increasing budgets; do not mislabel the persistent loop as universally non-halting solely from experiments.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The interpreter is deliberately not a secure virtual machine for arbitrary untrusted code; it accepts a tiny instruction language. Any universality statement requires the formal unbounded-counter model, not this finite Python execution.

## Source orientation

- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
