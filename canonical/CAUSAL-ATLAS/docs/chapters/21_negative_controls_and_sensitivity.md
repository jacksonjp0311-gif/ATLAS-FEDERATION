# 21. Negative controls and sensitivity analyses: try to falsify your explanation

In observational work, the central problem is often not computing the adjustment but determining whether its assumptions could be wrong. A negative control is an exposure or outcome chosen to make certain confounding, measurement, selection or analytic biases visible. It does not guarantee that an undetected bias is absent, and an unsuitable control can falsely reassure an analyst.

## Choose a control with a clear exclusion rationale

A negative-control outcome should plausibly share some bias mechanisms with the outcome of interest while, under a substantive theory, not being causally affected by the proposed intervention. A negative-control exposure should plausibly share drivers of treatment assignment while not causally affecting the primary outcome. A genuine control requires explicit timing, selection and measurement conditions. A nonzero association can reveal trouble, but a zero association cannot prove a no-confounding assumption unless strong additional completeness assumptions justify that interpretation.

For a mechanical change purportedly lowering a product defect caused by pressure instability, a reasonable investigative question might be whether another quality measure that should not be affected by the pressure mechanism nevertheless shifts after the change. That is an example of how to frame a candidate negative control, not a verdict that the candidate is actually valid. Shared sensor recalibration or a line-wide software update might change both outcomes and destroy the proposed exclusion assumption.

## Sensitivity with explicit alternative models

A useful analysis reports how the estimate changes under plausible deviations from an identifying condition. The existing Atlas includes finite examples of an instrumental-variable exclusion violation, missing-outcome bounds, and difference-in-differences trend deviations. Each takes a declared sensitivity parameter and reveals the result; none estimates the parameter's true value. Sensitivity should explore practical ranges informed by domain knowledge, not only values close to zero.

If one unmeasured cause can plausibly change both assignment and outcome, document how strong its relationships would need to be to alter the decision. Negative-control and sensitivity methods have different assumptions; they should be chosen according to the bias mechanism, not as decorative robustness checks. Use multiple credible analyses with genuinely different failure modes rather than repeated variants of the same biased model.

## Evidence decision protocol

Record which biases each diagnostic could detect, what is expected under a valid design, whether thresholds were prespecified, every result (including inconvenient ones), and remaining blind spots. A failed control may call for redesign instead of a larger sample or more sophisticated estimator. If the available data do not distinguish two plausible explanations, report that lack of identification as a research result.

**Reference:** Lipsitch, Tchetgen Tchetgen and Cohen (2010), [*Negative Controls: A Tool for Detecting Confounding and Bias in Observational Studies*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/), abstract and paper's distinction between exposure and outcome controls. This local library does not implement a general negative-control bias-calibration estimator.
