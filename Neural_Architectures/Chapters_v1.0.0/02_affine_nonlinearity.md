# 02 — Affine layers and expressive nonlinearity

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A feed-forward layer maps x to Wx+b. A network with no nonlinearities collapses to a single affine map, regardless of depth. Tanh is smooth and bounded; ReLU is piecewise linear and has an undefined classical derivative at zero, where a subgradient convention is required. Model parameter count separately from arithmetic work.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`h=tanh(W_1 x+b_1), y=w_2·h+b_2; parameter count for d inputs and h hidden units: h(d+1)+(h+1).`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For d=2,h=2, 2·(2+1)+(2+1)=9 parameters. With W1 zeros, b1 zeros, w2=[1,1], b2=0, the network always predicts 0 regardless of x; it cannot fit a varying target without changing parameters.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Use the `neural_atlas.mlp.forward` pure Python reference. Enumerate small samples and explicitly record weights, biases, activation function and target. Compare the network to the affine special case by replacing tanh with identity for analysis, not by silently changing trained data.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A nonlinear network is not automatically a universal predictor at fixed width, fixed precision and bounded data; capacity, initialization, data support and optimization determine practical behavior. Saturated tanh has near-zero derivative and can slow learning.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
