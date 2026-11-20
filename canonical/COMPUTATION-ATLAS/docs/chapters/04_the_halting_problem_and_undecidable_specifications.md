# Chapter 04 — The halting problem and undecidable specifications

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The halting problem asks for an algorithm that correctly determines for every program and input whether execution eventually stops. A diagonal proof shows no such total algorithm exists under a universal computation model. This is not a warning that no practical termination checker can ever help. Static analyzers may prove termination for important restricted programs; runtime budgets may stop runaway execution; proof assistants may verify a supplied well-founded ranking function. What fails is a universal complete decision procedure for arbitrary programs. This distinction guides how to describe software test outcomes and AI agent recovery: “not shown to terminate”, “terminated under bound B”, “proved terminating for a restricted model”, and “observed not to finish” are different evidence states.

## Formal statement, symbols, and units

Assume H(P,x) decides halting. Define D(P): if H(P,P) says halt then loop, else halt. Evaluate D(D) to obtain a contradiction.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The proof uses self-reference: if H predicts that D halts on its own description, D is defined to loop; if H predicts a loop, D halts. This contradicts H's assumed correctness. Note what the proof does not say: that every individual termination property is unprovable, or that real bounded systems cannot be exhaustively searched. For a finite transition system with a finite complete state enumeration, reachable loops can be checked. The class of arbitrary programs is strictly larger than the finite models under inspection.

## Reconstruction exercise with independently checkable output

Document a restricted finite loop with states {0,1,2}, exhaust reachable transitions, then compare the finite proof with a budgeted counter-machine run. Use the tool output “unknown_budget_exhausted” when the budget is insufficient.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never describe a timeout as proof of undecidability or nontermination. The finite-state model checker in this archive establishes properties only inside a supplied complete model, not arbitrary Python programs.

## Source orientation

- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
