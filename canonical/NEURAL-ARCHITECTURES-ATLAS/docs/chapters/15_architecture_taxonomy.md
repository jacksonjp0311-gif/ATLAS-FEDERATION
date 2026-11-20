# 15 — Convolutional, recurrent and attention architecture boundaries

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Convolution shares local weights across positions; recurrence updates a state through time; self-attention forms content-conditioned mixtures over a set or sequence. None is universally best. Inductive biases, causal structure, compute topology and data determine suitability; the current code models only foundational primitives directly.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`1D valid convolution y_t=sum_{j=0..k−1} w_j x_{t+j}+b; recurrent state h_t=tanh(W_x x_t+W_h h_{t−1}+b); attention uses softmax(QK^T/sqrt(d))V.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For x=[1,2,3] and convolution kernel [2,−1], valid outputs are [0,1]. A simple recurrent state h_t=tanh(x_t+h_{t−1}), h_0=0 changes with input order. Self-attention without position cues can be equivariant under token permutations, so it has a different built-in structure.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Build small finite examples of each equation, document boundaries and hidden states, compare output length and parameter reuse. A future neural v1 expansion must supply separate tested convolution/recurrent implementations and held-out tests before claiming coverage of those families.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

CNN and RNN software interfaces are described algebraically but do not constitute a benchmarked high-level implementation in this foundational edition. Claims about accuracy, sample efficiency and scaling require a task-controlled comparison.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
