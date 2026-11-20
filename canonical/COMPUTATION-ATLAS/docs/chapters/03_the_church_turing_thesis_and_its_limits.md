# Chapter 03 — The Church–Turing thesis and its limits

**Domain:** Foundations. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The Church–Turing thesis relates an informal idea—an effective procedure—to formal mathematical computability. Several formal systems, including Turing machines and lambda calculus, identify the same class of computable functions. Their equivalence is a mathematical result; the interpretation of every intuitively effective process is a thesis rather than an ordinary theorem about a previously formalized concept. This thesis is not the claim that every physical event can be efficiently simulated on today's computers, nor that all imaginable physical processes obey a particular digital implementation. Conflating computability with speed, parallelism, or physical determinism produces misleading forecasts. A human reconstructing the field needs three separate questions: can a function be computed in principle; what resources does it require; and can a particular physical system realize it?

## Formal statement, symbols, and units

Computable(f) means there exists a finite effective program P such that, for every x in dom(f), P(x) returns f(x) in finitely many steps. Cost(P,x) is a separate function.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

There are countably many finite programs but uncountably many mathematical functions from natural numbers to bits. Thus some such functions have no finite program representation. That counting argument is not an explicit method for identifying a specific uncomputable function; diagonal constructions provide one. The equivalence of formalisms does not erase assumptions about encodings, memory, or effectivity. A finite register machine's physical execution is bounded even if its mathematical semantics admit unbounded storage.

## Reconstruction exercise with independently checkable output

Write definitions of effective computation and polynomial-time computation in separate boxes. Construct a diagonal countability argument for binary functions, then compare it with the explicit self-reference proof in the next chapter.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Reject claims that a large GPU, quantum hardware, neural model, or novel encoding automatically escapes undecidability. New architectures can change resource requirements without deciding every arbitrary program's halting behavior.

## Source orientation

- Stanford Encyclopedia of Philosophy, The Church-Turing Thesis: https://plato.stanford.edu/entries/church-turing/
- Stanford Encyclopedia of Philosophy, Computability and Complexity: https://plato.stanford.edu/entries/computability/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
