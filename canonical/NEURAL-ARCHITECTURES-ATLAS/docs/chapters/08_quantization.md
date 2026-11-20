# 08 — Signed symmetric int8 quantization and error propagation

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Post-training quantization maps real values to a finite signed codebook with a scale; using [-127,127] maintains symmetry and reserves −128 unused. Quantization replaces information with approximation. For unclipped values in the calibrated range, nearest-integer rounding yields reconstruction error at most half a scale unit.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`s=max_i |x_i|/127 (if peak>0); q_i=clip(round(x_i/s),−127,127); x̂_i=s q_i; |x_i−x̂_i|≤s/2 for in-calibration inputs.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

With x=[−9,0,9], s=9/127, q=[−127,0,127], exact reconstruction follows. For x=0.2 under s=9/127, its code is approximately 3 and dequantization is about 0.2126, a small but nonzero error.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Use `quantize_int8` and `dequantize` with the same calibration vector; assert the half-step bound for hundreds of random finite vectors. Separately test an out-of-calibration input using the old scale to reveal clipping and distinguish that error from the half-step guarantee.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

This is scalar per-tensor symmetric int8 only; it is not GPTQ, NF4, blockwise group quantization, calibration for an entire transformer, or proof of model accuracy retention. Round-to-even and nonfinite input handling are implementation conventions.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
