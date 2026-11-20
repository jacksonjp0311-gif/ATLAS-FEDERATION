# Chapter 23 — Bisection and proof of root existence

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

The bisection algorithm brackets a root of a continuous real-valued function when endpoint values have opposite signs. Each iteration evaluates the midpoint and retains a half-interval whose endpoints still straddle zero. The intermediate value theorem supplies existence, while shrinking interval length supplies a location bound. Without continuity the sign change can be caused by a jump discontinuity without any root, so the continuity assumption must be explicit. A finite implementation can test signs and width, but it cannot generally prove that an arbitrary caller-supplied function is continuous. A bracket can be more defensible than a single estimate because it communicates residual uncertainty.

## Formal statement, symbols, and units

After k ideal iterations, width(b_k−a_k)=(b_0−a_0)/2^k. Under continuity and opposite signs, ∃r∈[a_k,b_k] with f(r)=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The proof proceeds by induction: the initial bracket satisfies the sign condition, and because midpoint is between endpoints, one of the two halves continues to have opposite endpoint signs. Interval width halves each step, so the midpoint estimate converges to a root under the stated assumptions. Finite precision may stall midpoint movement, so production implementations must detect that case. Newton-type methods may converge faster locally but need derivative information and stronger hypotheses.

## Reconstruction exercise with independently checkable output

Bracket sqrt(2) between 1 and 2 and halve until the width is under 10^-8. Independently square the endpoints and verify they straddle 2. Then attempt a discontinuous sign function and record why the continuity requirement refuses a proof.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

The reference asks callers to confirm continuity; that declaration is not independently certified. NaN evaluations, endpoint errors, and untrusted function side effects remain outside this controlled educational model.

## Source orientation

- SciPy reference, scipy.optimize.bisect: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html
- SciPy reference, optimization and root finding: https://docs.scipy.org/doc/scipy/reference/optimize.html
- MIT 6.006 Introduction to Algorithms, Fall 2011: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
