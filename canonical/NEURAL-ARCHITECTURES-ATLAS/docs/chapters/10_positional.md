# 10 — Position encoding, symmetry and causal order

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Self-attention without positional features is permutation equivariant when its tokens are permuted consistently (ignoring masks and external labels). Sequential tasks therefore need an order signal, for example learned or sinusoidal positional vectors. Causal masks impose direction but do not encode absolute position by themselves.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`PE(pos,2i)=sin(pos/10000^{2i/d}), PE(pos,2i+1)=cos(pos/10000^{2i/d}); d must be even to form complete sine/cosine pairs in this convention.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

At position 0, every sine coordinate equals zero and every cosine coordinate equals one. At position 1 for the first pair, values are [sin(1),cos(1)]; these are dimensionless and reproducible using math.sin/cos.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Enumerate positions 0,1,2 with a fixed even width. Check deterministic replay, finite outputs, and PE(0) pattern. When using another encoding scheme, version it explicitly; do not silently confuse absolute, relative and rotary embeddings.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

Sinusoidal encoding alone does not prove a model understands arithmetic order, long-context extrapolation or a physical time series. Large positions lose floating-point phase resolution, and a periodic encoding can alias.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `VASWANI2017`: https://papers.neurips.cc/paper/7181-attention-is-all-you-need. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
