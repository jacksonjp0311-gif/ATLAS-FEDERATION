# Investigation 10. A changing residual is not proof of a faulty component

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

Suppose a dynamic model predicts a stable process, but the measured output drifts after a software release. A residual increase may reflect a controller bug, a sensor calibration change, a different material lot, altered temperature, physical wear, unmodeled load, or timestamps being shifted by the logging pipeline. The residual is evidence of disagreement with the model, not a unique root cause.

A discriminating investigation would retain command and measurement time series across runs, controller and machine versions, maintenance/calibration logs, operating and environmental conditions, and a controlled rollback plan. Causal Atlas provides study-design principles for attributing intervention effects. Measurement Atlas provides uncertainty and calibration concepts. Control Atlas retains the dynamic explanation without conflating these domains.

**Source:** MathWorks System Identification documentation (model validation and residual analysis). **Refusal:** this package cannot diagnose a specific real machine or infer an equipment repair from a synthetic residual.
