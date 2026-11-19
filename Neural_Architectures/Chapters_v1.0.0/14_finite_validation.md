# 14 — Independent oracles, differential testing and numerical failure cases

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

A scientific software reference needs multiple independent evidence channels. Exact rational matrix products test algebra; finite differences test gradients; independent logistic formulas check two-way softmax; invariants test causal masking; test datasets and negative examples expose failure boundaries.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`For smooth scalar f, g_fd=[f(θ+h)−f(θ−h)]/(2h) = f'(θ)+O(h²) in exact arithmetic; real floating-point cancellation increases error as h→0.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

At f(θ)=θ²/2 and θ=2, derivative is 2. With h=0.001, centered difference gives exactly 2 in ideal arithmetic. A too-small h near machine precision can yield a misleading 0 from subtraction of almost equal floating numbers.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Run `python -m unittest discover -s tests` plus `python evidence/independent_oracle.py` offline. Save actual seed, trial count, exact test outputs, Python interpreter version, failed cases and hash of implementation source. Keep initial and repaired failing traces instead of discarding them.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

A finite oracle cannot prove correctness on an unbounded floating domain. Different correct implementations can disagree near ill-conditioned problems; tolerances must be justified in units and precision and not tuned to make a failing test pass.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
