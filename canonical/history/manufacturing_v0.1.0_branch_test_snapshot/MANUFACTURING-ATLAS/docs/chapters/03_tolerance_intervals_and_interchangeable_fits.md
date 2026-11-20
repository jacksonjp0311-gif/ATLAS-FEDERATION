# Chapter 03 — Tolerance intervals, clearance/interference, and interchangeable fits

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A manufactured dimension is not a point; it is an admissible interval. The extremal clearance for a hole and shaft comes from the smallest hole paired with the largest shaft, and the largest hole paired with the smallest shaft. Positive C_min guarantees clearance within declared bounds. Negative C_max guarantees interference. A range spanning zero is a transition fit or boundary. Tolerance choice is functional and must consider thermal behavior, roughness, measurement uncertainty, and actual geometric form. This interval reasoning is independent of probabilistic distribution assumptions.

## Reconstructible law, dimensional contract and assumptions

`C_min=H_min−S_max; C_max=H_max−S_min`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Hole [10.02,10.05] mm and shaft [9.97,9.99] mm imply guaranteed [0.03,0.08] mm diametral clearance. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A Monte Carlo estimate cannot replace a worst-case bound unless its probabilistic assumptions and risk target are explicitly accepted. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
