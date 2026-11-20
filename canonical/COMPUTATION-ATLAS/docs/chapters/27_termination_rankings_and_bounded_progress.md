# Chapter 27 — Termination rankings and bounded progress

**Domain:** Verification. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A ranking function maps nonterminal states to a well-founded set and decreases on every transition. A natural-number rank that strictly decreases cannot decrease forever, proving termination when each transition follows the model and no stuck nonterminal state is allowed. A ranking proof is stronger than observing that many runs stop, but it is conditional on complete state and transition descriptions. Real applications may use lexicographic ranks, multisets, ordinals, or fairness assumptions. An agent's “determination” or intent cannot replace these progress conditions. Distinguish a proof that every step reduces a rank from a scheduler promise that steps will eventually be executed.

## Formal statement, symbols, and units

Rank ρ:S→ℕ with ρ(s′)<ρ(s) for every transition from nonterminal s. No infinite descending chain exists in ℕ.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

If an infinite execution existed, its ranks would form an infinite strictly descending sequence of nonnegative integers, impossible by well-ordering. A finite checker may validate an applicant's rank function over all declared transitions. But the proof applies only if transition selection actually follows the model and all nonterminal states can take a step; otherwise deadlock may prevent the intended terminal condition. Progress and safety are distinct classes of property.

## Reconstruction exercise with independently checkable output

Model a countdown 4→3→2→1→0 using rank ρ(s)=s. Prove each transition decreases. Add a self-loop at 2 and observe the checker refutes the rank. Compare that refutation with mere step-budget exhaustion.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not claim a retry policy guarantees completion when retries can cycle, external side effects are uncertain, or the environment does not eventually respond.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
