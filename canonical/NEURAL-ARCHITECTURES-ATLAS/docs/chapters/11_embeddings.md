# 11 — Token embedding lookup, padding and representation boundaries

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A token ID is a discrete index; an embedding table maps it to a vector by lookup. The lookup is not semantically meaningful without learned or specified weights. Padding must be treated consistently in attention masks and loss targets to avoid mixing artificial tokens with evidence.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`E∈R^{V×d}; embedding(token_i)=E[token_i,:]; embedding parameter count Vd; attention score memory O(T²) per head.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

A 1000-token vocabulary with 64-dimensional embeddings stores 64,000 real parameters. At 4 bytes per fp32 weight, raw embedding weights require 256,000 bytes, excluding metadata and runtime allocations. A 128×128 score matrix stores 16,384 weights or 65,536 bytes at fp32 per head.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Use a small exact table, e.g. token 0→[1,0] and token 1→[0,1], and verify lookup and out-of-range failure. Record ID scheme, unknown-token policy, special-token semantics, tokenizer version, padding mask and corpus provenance as part of reproducible inference.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

Embedding indices cannot be mixed between tokenizer revisions. The cost figures are ideal arithmetic arrays and exclude Python object overhead, gradients, optimizer states, activations and cache. Language semantics are not supplied by an embedding table alone.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
