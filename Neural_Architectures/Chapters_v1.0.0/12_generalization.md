# 12 — Dataset partitions, uncertainty and evaluation discipline

**ATLAS FORGE — Neural Architectures original 30-domain priority 13 — scoped v1.0.0**

## Reconstructible question and engineering assumptions

Training loss measures fit to the training sample; independent validation estimates performance on another sample drawn under assumptions. Hold-out data must not be used iteratively to select unlimited hypotheses. Leakage, distribution shift, calibration and rare-event behavior require independent evidence and statistical uncertainty.

The input domain is finite, explicitly shaped and dimensionless unless physical units are provided. Array shape is part of the specification; negative dimensions, nonfinite input and incompatible axes must be rejected, never silently coerced. Software repeatability is a necessary but insufficient condition for scientific validity.

## Governing mathematics and derivation

`Mean squared error MSE=(1/n)sum_i(y_i−ŷ_i)². For independent bounded Bernoulli accuracy indicators, Hoeffding gives P(|p̂−p|≥ε)≤2exp(−2nε²) under i.i.d. assumptions.`

A correct derivation specifies which parameters are independent, which dimensions are reduced, and which operations are approximated. When a real-valued algebraic identity is implemented with IEEE floating point, report relative/absolute tolerances and record any exceptional input domain. The identities here are general mathematical knowledge, not a new scientific discovery by Atlas.

## Fully worked constructed investigation

For n=100 and ε=0.1, Hoeffding upper bound is 2exp(−2)=~0.2707; this is not a meaningful guarantee under non-independent samples. A model that memorizes 100 training examples can have zero training error and arbitrarily poor error on a shifted population.

For independent reconstruction, write each intermediate vector or scalar, verify signs and axis order, and compare with a second method rather than only checking a return code. Numbers above are constructed pedagogical examples; they are not measured production-model performance.

## Offline executable or pencil-and-paper procedure

Define explicit train/validation/test splits before inspecting outcome. Log data source rights, creation dates, preprocessing revision, random seeds, metrics and number of model selections. Re-run on a truly held-out sample and preserve negative results.

Where the reference module does not implement the entire feature described, treat the equation and the constructed investigation as a specification and record the implementation gap. Never mark an unexecuted benchmark as passed. Preserve seeds and input values as an exact reproducibility receipt.

## Negative cases, limits and uncertainty

Software oracle agreement confirms a calculation, not learning effectiveness. Evaluation conclusions must not be projected to a live offline AI without a model-specific pretraining and deployment assessment.

An important negative control is a plausible but incorrect shortcut: applying a learned metric to uncalibrated logits, conflating floating-point consistency with physical accuracy, or inferring production readiness from toy arrays. Any future release must preserve negative examples and error cases instead of excluding them to increase test pass counts.

## Source provenance and cross-domain reconstruction

Bibliographic key `GOODFELLOW2016`: https://www.deeplearningbook.org/. This is an official/author-associated pointer subject to exact edition and claim-level verification; no publisher original file bytes are included.

Exact cross-domain dependencies are recorded in the Atlas common relationship data (Computation algorithmic semantics; Mathematics/Physics numerical methods; Computer Architecture memory models; Measurement evidence). The primary scientific status is **offline bounded mathematical content**, not authenticated original-source evidence, physical AI build validation or expert peer review.
