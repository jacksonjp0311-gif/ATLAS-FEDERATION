# Chapter 01 — Computation is a rule-governed transformation

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A computation is a sequence of state transformations carried out according to an effective, finite description of rules. Separating the program, the state, and the environment clarifies what an algorithm actually promises. A finite machine may possess unbounded mathematical storage in its model, while any physical computer has finite memory, finite energy, and a failure-prone clock. The input specification determines what is represented: bit strings, integers, rational numbers, measured reals, or structured graphs. The output specification determines what counts as a result, including error, refusal, and nontermination. A program executable on a laptop is not thereby a proof of the function it computes; its semantics, preconditions, and adversarial cases must be examined. The same observed output may arise from different internal programs. A constructive representation requires state, instruction syntax, transition rules, and a stopping condition. The Computation Atlas treats all those elements as evidence fields, not optional implementation details.

## Formal statement, symbols, and units

Transition: s_(t+1)=delta(s_t,i_t). Partial function: f:X ⇀ Y. A total algorithm returns an output for every input in its declared domain.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

A deterministic interpreter supplies a transition relation and can reproduce a finite trace. To infer a universal property from a finite trace is a quantifier error: “these cases stopped” does not entail “all cases stop”. An encoding must be injective if exact reconstruction is expected; otherwise two distinct states might share a representation. Machine specifications also expose the resource model: what constitutes one step, one memory cell, and one cost unit? Different models can preserve computability but change practical performance.

## Reconstruction exercise with independently checkable output

Write a three-state deterministic machine, list each state and outgoing transition, then execute the initial state by hand. Confirm that the interpreter follows the same steps. Change the input encoding while preserving the decoded meaning and check whether the output remains invariant.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not confuse successful execution, decidability, feasibility, correctness, and performance. A program can halt and return the wrong answer. A correct algorithm can require impractical time. Two finite observations cannot decide a universal termination property.

## Source orientation

- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures
- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
