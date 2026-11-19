# Investigation 11 — A numerically certified fit can still need diagnostic review

**Question:** Does reproducing a published fit prove it is a physically reliable predictor? **Origin:** computational reanalysis of 236 source-reported NIST Hahn1 copper observations transcribed in the previous Materials release.

The published seven-parameter rational function evaluated on the local checked transcription reproduces NIST's certified RSS (about 1.5324382854). That verifies a specific numerical calculation at supplied parameters. It does not independently verify the source acquisition, model adequacy, coefficient units, sample processing or measurement uncertainty.

This increment adds descriptive residual bins ordered by temperature, not by time. For eight bins, each contains a nearly equal number of observations; each reports its temperature range, mean residual and RMSE. We also report a temperature-neighbor residual correlation but explicitly **do not** label it temporal autocorrelation or evidence of instrument drift. A residual pattern can be a reason to investigate model inadequacy, not proof of a particular physical mechanism.

**Reproduce:** `python -m materials_atlas hahn-diagnostics` and `python tools/phase_diffraction_oracle.py`. The first uses the existing published-data capture; the second recomputes bin statistics using NumPy as a separate implementation. Both keep original upstream-byte acquisition and response-scale verification open.

**Further evidence needed:** original NIST data-file bytes, independent source audit, a justified response unit multiplier, test specimen identity, uncertainty budget and a predeclared external validation set. This is a useful benchmark for software correctness, not a new materials-science discovery.
