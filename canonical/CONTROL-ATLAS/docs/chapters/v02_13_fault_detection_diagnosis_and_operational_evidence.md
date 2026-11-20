# 13. Fault detection, diagnosis and operational evidence

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Fault detection asks whether observed behavior deviates from a declared normal model. Fault isolation asks what mechanism caused the deviation. They are not the same task. A residual spike may reflect a stuck valve, instrument drift, changed input, material changes, calibration error or a shifted operating point. A high-dimensional model may predict a change without identifying the responsible physical component.

For a linear predictor, a residual `e[k]=y[k]−yhat[k]` can be examined across time, inputs and environmental conditions. Correlation and periodic structure in residuals can reveal unmodeled dynamics, but not all patterns are component-specific. Positive predictive power in an authored simulation is not evidence of real fault detection on independently measured equipment.

A defensible diagnostic plan preserves the timestamps of commands, measurements, maintenance, product batches and alarms; sensor and controller versions; model training and validation windows; the operating range; confounders; and a controlled comparison to a baseline or alternate sensor. Do not treat a changed software version as causal proof that software created a physical defect without controlled evidence.

This Atlas has no actual industrial fault dataset, no deployed fault detector and no authority to actuate or bypass safeguards. Manufacturing Atlas will cover physical process diagnosis, while Causal Atlas handles experimental attribution. Control Atlas holds dynamic-model reasoning and the measurement/observability conditions required to make a claim meaningful.

**Publisher/documentation scope:** [MATH-ID](https://www.mathworks.com/help/ident/gs/system-identification-workflow.html) · [MATH-ID-QUALITY](https://www.mathworks.com/help/ident/gs/about-system-identification.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
