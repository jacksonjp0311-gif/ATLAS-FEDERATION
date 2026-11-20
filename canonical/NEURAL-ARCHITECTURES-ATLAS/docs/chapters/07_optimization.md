# 07 — SGD descent, step-size limits and reproducibility

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Optimization attempts to minimize an objective by updating parameters in the negative gradient direction. For a local differentiable scalar loss, a sufficiently small step tends to decrease loss when the gradient is nonzero; this does not guarantee progress under arbitrary learning rates, nonconvex landscapes, data noise or finite precision.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`θ_{k+1}=θ_k−η∇L(θ_k); for scalar L(θ)=θ²/2, θ_{k+1}=(1−η)θ_k, stable strict decay for 0<η<2.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

With θ=2 and η=0.25, the scalar quadratic objective goes from L=2 to L=1.125. At η=2 it oscillates without objective reduction, while η=3 magnifies the magnitude. This serves as a negative control independent of the two-layer network.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Run `sgd_step` on the same deterministic sample with documented weights and small η, compare before/after loss, and independently inspect one-dimensional quadratic steps. For real experiments, freeze the train/validation split, RNG seeds, optimizer state, precision and dataset rights.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A decrease on one training example is not generalization. Mini-batch order, momentum, weight decay and adaptive optimizers are not implemented here; report them as missing features, not as implied by a successful SGD test.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
