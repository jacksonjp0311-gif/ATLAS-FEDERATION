# 04 — Probability normalization, log-sum-exp and stable cross entropy

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Raw neural logits are unbounded scores. Softmax converts a finite vector into strictly positive probabilities over unmasked entries; zero probabilities are allowed only for masked entries. Subtract the maximum logit before exponentiating to prevent overflow; log-sum-exp and negative log likelihood should be implemented without naive exponentials.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`p_i=exp(z_i−m)/sum_j exp(z_j−m), m=max(z); logsumexp(z)=m+log(sum_j exp(z_j−m)); CE(z,y)=logsumexp(z)−z_y.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For z=[1000,1000], naive exp(1000) overflows, while stable probabilities are exactly [1/2,1/2]. The cross entropy for either class is log(2)≈0.693147. Masking [True,False] sets the second weight to zero and leaves one.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Evaluate `stable_softmax` and `logsumexp` on huge common offsets and compare the two-element probability to independently computed 1/(1+exp(z2−z1)) for bounded differences; assert row sum≈1, exact zeros on masked entries, and rejection of an all-false mask.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

An all-masked row does not define a probability distribution. Softmax likelihood is not calibration, truthfulness or a probabilistic uncertainty estimate for unseen data. Large negative scores can underflow to zero in floating point without changing the ideal real-number definition.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
