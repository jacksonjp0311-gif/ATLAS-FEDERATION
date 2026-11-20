# Chapter 22 — Conditioning, stability, and error budgets

**Domain:** Numerics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Conditioning describes how a mathematical problem's output changes when its input changes; numerical stability describes how an algorithm's computation responds to rounding and perturbations. They must not be conflated. An ill-conditioned problem can defeat even a stable algorithm if input uncertainty dominates; an unstable algorithm can squander accuracy on a well-conditioned problem. Forward error measures distance between computed and true output, while backward error asks whether the computed result solves a nearby problem. Engineering error budgets include measurement uncertainty, model approximation, discretization, floating rounding, and stopping tolerance. These components are not necessarily independent or additive without justification.

## Formal statement, symbols, and units

Condition number κ≈(relative output perturbation)/(relative input perturbation) for sufficiently small changes. Backward stability: computed y=f(x+Δx) with small Δx.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Consider subtracting x and y where x≈y: a small relative perturbation in either operand can produce a large relative perturbation in x−y. This is conditioning of the subtraction problem, not merely a defect in one code implementation. Scaling, algebraic reformulation, exact arithmetic, and interval enclosures can mitigate different causes. A reproducible analysis specifies which error notion is being bounded and which assumptions justify a bound.

## Reconstruction exercise with independently checkable output

Compare sqrt(x+1)−sqrt(x) with the algebraically equivalent 1/(sqrt(x+1)+sqrt(x)) for large x. Use high-precision rational or decimal reference and report absolute and relative errors separately.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

A tiny residual does not automatically guarantee a tiny solution error in an ill-conditioned problem. Synthetic oracle agreement under one distribution does not certify global accuracy or physical measurements.

## Source orientation

- Python documentation, Floating-Point Arithmetic: Issues and Limitations: https://docs.python.org/3/tutorial/floatingpoint.html
- SciPy reference, optimization and root finding: https://docs.scipy.org/doc/scipy/reference/optimize.html
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
