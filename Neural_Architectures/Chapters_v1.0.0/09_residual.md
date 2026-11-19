# 09 — Residual pathways, composition and Jacobian structure

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A residual layer computes an identity-carried signal plus a learned correction. Its Jacobian is I+J_F where differentiable. This creates a direct gradient pathway but does not by itself prove numerical stability or stable training; depth, normalization, initialization and spectrum matter.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`y=x+F(x); J_y=I+J_F. In 1D if F(x)=ax, dy/dx=1+a.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For x=3 and F(x)=−0.1x, output is 2.7 and the derivative is 0.9. If F(x)=−x, the residual output vanishes and derivative is 0; therefore “residual means gradients cannot vanish” is false.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Reconstruct residual addition as a shape-preserving operation, evaluate a finite difference of F(x)+x, compare to 1+F'(x). For multidimensional systems compare Jacobian-vector products with small perturbations. Explicitly record any projection used when feature widths differ.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A residual skip is not an unconditional safety net; badly scaled residual branches, incompatible shapes and hidden state dependence can still fail. The provided standalone models do not simulate the deep-residual image classification experiments from the bibliography.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `HE2016`: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
