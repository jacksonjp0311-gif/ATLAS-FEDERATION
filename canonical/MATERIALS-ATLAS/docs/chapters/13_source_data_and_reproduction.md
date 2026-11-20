# Chapter 13 — An experimental dataset is not its fitted equation

**Question:** What does it mean to reproduce a material-property analysis when the original experiment cannot be repeated?

This chapter adds a concrete distinction between (1) a physical specimen measurement, (2) a published observation table, (3) a numerical reconstruction of a published analysis, and (4) use of a model for a new specimen. These are different evidence levels and cannot be upgraded by increasing the number of software tests. The Materials Atlas uses NIST's 236-point Hahn1 copper thermal expansion example to show this distinction. The original NIST study is credited to Thomas Hahn (1979) and the Handbook and StRD pages describe one study, not independent measurement campaigns.

## Reproduction boundary

Our source report identifies the predictor as temperature in kelvin and the response as a coefficient of thermal expansion. NIST's displayed table does **not** assign a clear physical unit or scale to the response. The Atlas therefore stores the original numeric response with `response_scale_unresolved` and refuses to calculate a physical length change from it. In particular, the values 16–21 must not be silently relabeled `10^-6 K^-1`, even if that interpretation seems chemically plausible. Property semantics must come from a checked source, not inference.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## What remains before material qualification

Obtain verified original source bytes or independent publisher confirmation of the values, documentary response units, instrument/method metadata, uncertainty, specimen purity, grain history, and independent scientific review. NIST notes a lower-quality quadratic/quadratic rational model can produce structured residuals even when plotted data look close; model fit is not model adequacy. A new copper lot may behave differently from this experiment, and an equation calibrated only in the published range must not be extrapolated.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.