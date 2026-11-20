# Chapter 28 — Shannon entropy, information, and physical uncertainty

**Domain:** Information. **Edition:** Computation Atlas 0.1.0. **Evidence status:** original educational synthesis; bibliography checked only within declared scopes.

## Foundations and precise vocabulary

Information theory quantifies expected surprise under a declared probability distribution. Shannon entropy H measures average self-information in bits when the logarithm base is two. It does not measure truth, intelligence, understanding, meaning, or scientific evidence quality. A perfectly random source can have high entropy while carrying no useful explanatory content; a compact theorem can have few bytes while conveying profound knowledge to someone with the prerequisites. For compression, probability assumptions and code constraints matter. Empirical frequency estimates introduce sampling uncertainty that should not be hidden inside an exact-looking entropy number. A physical thermodynamic entropy is related in some settings but not interchangeable with Shannon entropy without a specific model.

## Formal statement, symbols, and units

H(X)=−Σ_i p_i log₂(p_i), with 0 log 0 defined as 0. For a fair binary distribution H=1 bit; for a certain outcome H=0.

Input is a mathematically declared object. Time and memory claims use abstract operation/space units, not measured seconds or joules unless explicitly stated.

## Explanation, proof sketch, and mathematical boundaries

Expected surprise is obtained by averaging −log₂ p_i with respect to p_i. Entropy is maximized by a uniform distribution on a finite alphabet. Jensen's inequality or constrained optimization gives the maximum bound log₂(n). It quantifies distributional uncertainty, not the epistemic confidence of a human citation or the accuracy of a classifier.

## Reconstruction exercise with independently checkable output

Compute H for [1,0], [1/2,1/2], and [1/4]*4. Then construct two messages of the same length with different semantic value, explaining why byte count alone cannot determine usefulness to future scientists.

The exercise is author-generated. Inspect and verify the mathematics independently before applying the technique to any external data or physical apparatus.

## Failure modes and counterexamples

Never use “information density” as a validated cognitive-performance measure without defining its operational units, baseline, and independent held-out tasks. Entropy estimates based on unrepresentative samples can mislead.

## Source orientation

- MIT OpenCourseWare, Mathematics for Computer Science: https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- MIT OpenCourseWare 18.S191 Introduction to Computational Thinking: https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/
- NIST Dictionary of Algorithms and Data Structures: https://www.nist.gov/publications/dictionary-algorithms-and-data-structures

These are publisher navigation and selected technical-context links, **not archival primary-source bytes**. The source-acquisition ledger lists offline gaps.
