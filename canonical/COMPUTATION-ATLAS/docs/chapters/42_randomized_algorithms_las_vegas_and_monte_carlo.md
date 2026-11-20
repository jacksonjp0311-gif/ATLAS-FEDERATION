# Chapter 42 — Randomized algorithms, Las Vegas and Monte Carlo

**Area:** Probability. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Randomization can affect runtime, output correctness, or both. A Las Vegas algorithm always returns a correct result when it terminates, but runtime can vary randomly. A Monte Carlo algorithm has bounded or controlled runtime and may return an incorrect result with a quantified probability under its probability model. Randomized pivot selection, sampling, primality tests and hash tables illustrate different uses. A pseudorandom generator with a fixed seed helps reproduce software tests but does not turn correlated or adversarial outputs into independent unbiased samples.

## Mathematical contract

For independent indicator errors E_i with P(E_i)≤p, repeating a valid independent test k times can reduce joint error to ≤p^k under independent trials. Without independence, this multiplication is unjustified.

## Derivation and reasoning

A probability bound is conditional on the algorithm's distributional assumptions. If an adversary can predict the generator seed, or if random events share hidden state, repeated outcomes may be correlated. A randomized algorithm still needs a specification of success, failure and the random-variable distribution. Correctness proofs for Monte Carlo methods usually bound error over random choices, not over every sequence of choices.

## Worked reconstruction and independent check

Construct a randomized selection process with a declared probability of a bad pivot and repeat using a fixed seed. Distinguish observed failure frequency from a theoretical bound and include the seed, generator algorithm and test inputs. Compare two independent generators only if their statistical independence is justified.

## Limitations, falsification, and invalid use

A stochastic language model's different prompts or temperature settings do not automatically produce independent benchmark tasks or evaluators. Randomized tests support software confidence, not an empirical proof of agent generalization.

## Cross-domain meaning

Agent Atlas can use randomized evaluations later, but the benchmark's sampling and outcome authority must be independently established.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare, Mathematics for Computer Science](https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
