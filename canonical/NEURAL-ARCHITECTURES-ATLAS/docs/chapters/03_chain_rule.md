# 03 — Reverse-mode differentiation, adjoints and finite differences

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Reverse differentiation computes the gradient of a scalar loss with respect to many parameters by applying the chain rule from output to inputs. The local derivative of tanh(z) is 1−tanh(z)^2. For a squared-error target, the output adjoint is prediction−target. Analytic derivatives must be independently checked with perturbed evaluations, not against a shared derivative routine.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`L=(y−t)^2/2; δ_out=y−t; ∂L/∂w2_j=δ_out h_j; δ_hj=δ_out w2_j(1−h_j²); ∂L/∂W1_ji=δ_hj x_i.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For x=[0,0], h=[0,0], output bias b2=1, target t=0, L=1/2. The bias gradient is exactly +1 and W1,w2 gradients are zero, because the inputs and activations are zero. Decreasing b2 by 0.1 predicts 0.9 and reduces loss to 0.405.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Run `neural_atlas.mlp.loss_and_grads`. For each parameter θ, compute g_fd=[L(θ+h)−L(θ−h)]/(2h) without calling the analytic gradient formula. Check a tolerance and repeat at several h to detect truncation and cancellation; `h=1e−6` is reasonable for the constructed moderate-scale model.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A vanishing finite difference at too-small h is not proof of zero derivative; huge h causes truncation error. Discontinuities, stochastic layers and nondeterministic evaluation demand special treatment. This model is a two-layer regression network, not automatic differentiation generally.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
