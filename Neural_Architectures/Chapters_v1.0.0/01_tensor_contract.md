# 01 — Tensor shape, storage and numerical semantics

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A tensor is a finite rectangular collection with axis-labelled shape; the array [batch, sequence, feature] has different meaning from [batch, feature, sequence]. An operation is invalid if the agreed contraction dimensions disagree. Values are floating-point approximations; counts and dimensions are dimensionless, and FLOP approximations assume a particular multiply-add convention.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`C_ij = sum_{k=1..K} A_ik B_kj; A in R^{M×K}, B in R^{K×N}, C in R^{M×N}; cost ≈ 2MKN floating-point operations.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

A=[[1,2],[3,4]], B=[[5,6],[7,8]], so C=[[19,22],[43,50]]. For M=2,K=2,N=2, 8 products and 4 additions are made by this naive algorithm; the commonly quoted 2MKN counts a multiply plus addition per inner term and is a convention.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Use `neural_atlas.mathcore.matmul` and compare all entries for small integer matrices against exact rational arithmetic (`fractions.Fraction`) in the separate oracle. Reject ragged matrices, booleans, mismatched inner dimensions, NaN and Inf. Save the axis interpretation alongside data.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

Swapping the sequence and feature axes can be shape-compatible yet semantically wrong when their sizes coincide. Floating-point matrix multiplication is not exactly associative. The stdlib implementation stores the full result and does not model cache, BLAS, GPUs or memory alignment.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
