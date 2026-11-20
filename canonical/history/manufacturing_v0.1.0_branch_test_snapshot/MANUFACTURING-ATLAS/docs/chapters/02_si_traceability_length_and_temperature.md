# Chapter 02 — SI length and temperature traceability in precision production

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A reported length is conditional on a measurement system and temperature. In a homogeneous first-order material model, length increases proportionally to the temperature difference and the coefficient of thermal expansion. Derive the approximation by integrating dL/L=α dT for approximately constant α, then truncating exp(αΔT) after its first term. Record instrument calibration, uncertainty, reference environment, repeatability, resolution, operator and date. Traceability attaches to a measurement result through a documented chain; it does not magically attach to a machine merely because its instrument has a calibration label.

## Reconstructible law, dimensional contract and assumptions

`L(T) ≈ L(T_ref)[1+α(T−T_ref)]`

Inputs/outputs: **m, K, K^-1**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

One metre of material with α=12×10^-6 K^-1 changes by approximately 0.24 mm over 20 K under the linear approximation. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Unknown coefficient α, gradients or residual stress can dominate the simple calculation; a predicted growth is not a measured correction. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST metrological traceability frequently asked questions**, https://www.nist.gov/metrology/metrological-traceability. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
