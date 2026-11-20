# Chapter 05 — Calibration models, bias, repeatability and residual uncertainty

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A linear calibration line is a regression model, not a certificate. Derive b=Σ(x−x̄)(y−ȳ)/Σ(x−x̄)² and a=ȳ−b x̄. Evaluate residual variation with sample count n−2 and inspect residual versus input. Calibration does not necessarily improve the sensor until a correction is applied and verified. Nonlinear drift, hysteresis, misalignment, thermal dependence, and reference uncertainty are additional error mechanisms not represented in ordinary least squares. A calibration chain may carry uncertainty even when fitted residuals vanish.

## Reconstructible law, dimensional contract and assumptions

`y_indicated=a+b x_reference+ε`

Inputs/outputs: **indication / reference units**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Reference values 0,1,2,3 and indications 1,3,5,7 fit b=2, a=1 with zero constructed residual. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Perfect fitted points do not prove an instrument is traceable or accurate away from the calibration range. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST metrological traceability frequently asked questions**, https://www.nist.gov/metrology/metrological-traceability. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
