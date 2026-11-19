# 13 — Memory, arithmetic intensity and latency accounting

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Compute and storage constraints matter for offline neural systems. Distinguish parameter storage, activations, score matrices and optimizer states. The dominant term depends on architecture, batch, sequence length and precision; a single “model size” metric is incomplete.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`For one dense layer: parameters=d_in*d_out+d_out, bytes≈parameters*b; for attention score matrix: T² elements per batch and head; standard dense attention arithmetic O(T² d_k+T² d_v).`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For T=1024, one head scores 1,048,576 entries; at fp32, ~4 MiB for scores alone. For T=2048, the score element count quadruples to 4,194,304. An int8 embedding with 64,000 entries would be 64,000 bytes ideally, but may require scales and alignment.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Compute parameter and activation estimates analytically and compare with actual measured process RSS on the target runtime when available. State precision and whether a backend materializes scores or streams blocks. Log memory ceilings, OOM failures and expected accuracy changes before altering quantization.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

Big-O is asymptotic complexity, not an exact latency model. Python list overhead dominates this pedagogical runtime. It does not establish achievable tokens/s, FLOPS, I/O energy or thermal behavior on a specific machine.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `VASWANI2017`: https://papers.neurips.cc/paper/7181-attention-is-all-you-need. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
