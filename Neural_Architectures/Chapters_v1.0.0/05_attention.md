# 05 — Scaled dot-product attention, dimensions and leakage constraints

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A query compares to all keys; each score is normalized and used to form a convex mixture of value vectors. A causal mask prevents a position i from incorporating values at positions j>i in a single layer. Scaling by sqrt(d_k) controls the growth of dot products when coordinates are roughly independent and order-one variance; it is not an exact universal variance theorem.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`Attention(Q,K,V)=softmax(Q K^T/sqrt(d_k)+mask)V; Q∈R^{T×d_k}, K∈R^{S×d_k}, V∈R^{S×d_v}.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For Q=[[0,0]], K=[[1,0],[-1,0]], V=[[2,4],[6,8]], both logits are 0, weights [1/2,1/2], output [4,6]. Under a two-token causal mask, the first output is exactly its first value regardless of the second value.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Use `neural_atlas.attention.attention`, explicitly inspect the score matrix and each probability row. Alter a future value while holding the query, keys and earlier values fixed; under causal masking the first output must not change. Compare against the analytic equal-score case.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A correct causal mask in one module does not ensure an entire model or dataset is leakage-free: positional encodings, training labels, caches and retrieval inputs can leak future information. This implementation is single-head, batchless and uses quadratic score storage.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `VASWANI2017`: https://papers.neurips.cc/paper/7181-attention-is-all-you-need. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
