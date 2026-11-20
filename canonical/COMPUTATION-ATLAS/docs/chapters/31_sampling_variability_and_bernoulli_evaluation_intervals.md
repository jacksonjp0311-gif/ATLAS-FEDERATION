# Chapter 31 — Sampling variability and Bernoulli evaluation intervals

**Domain:** Statistics. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

A binary test outcome provides one Bernoulli observation only after a clear success criterion, sampling design, and task scope are fixed. A sample proportion is not automatically an estimate of general AI performance or scientific truth. Confidence intervals describe repeated-sampling procedures under declared assumptions. Wilson score intervals often behave better than naïve normal intervals near zero or one successes, but neither removes sampling bias, dependence between tasks, evaluator leakage, or measurement error. Paired experimental designs control task difficulty when comparing two agents or algorithms; independent Bernoulli proportions are inappropriate if the same tasks are used with correlated outcomes. Reporting both denominator and missing trials is essential.

## Formal statement, symbols, and units

p̂=k/n. Wilson center=(p̂+z²/(2n))/(1+z²/n); half-width=[z/(1+z²/n)]√(p̂(1−p̂)/n+z²/(4n²)).

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

The Wilson interval comes from inverting an approximate score test. Its advertised coverage depends on independent and identically distributed Bernoulli trials and the confidence-level convention encoded in z. The formula is an interval estimator, not a guarantee that a specific unknown probability is inside the computed range. Random seeds, task versions, grader rules, and exclusions must be logged before interpreting the numbers.

## Reconstruction exercise with independently checkable output

Compute the Wilson interval for 7 successes in 10 attempts and compare with 70 in 100. Hold the observed proportion fixed and observe that uncertainty decreases with larger n under independence assumptions.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Do not score repeated trials on the same contaminated task as independent evidence of broad generalization; do not report success rate when failures or missing labels were excluded without declaration.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
