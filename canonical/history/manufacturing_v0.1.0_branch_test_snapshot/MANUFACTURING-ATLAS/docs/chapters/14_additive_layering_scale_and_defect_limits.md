# Chapter 14 — Additive layers, geometric error accumulation and qualification

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

In the simplest layered fabrication model, nominal height equals the number of deposited layers multiplied by nominal layer thickness, with a bounded systematic scale error. This geometric relation does not predict melt-pool dynamics, residual stress, porosity, anisotropy, surface finish or material strength. Additive process qualification requires characterized feedstock, machine state, in-process sensor quality, postprocessing and destructive or nondestructive evaluation as appropriate. Measure dimension and material quality separately. Machine setpoints cannot be transferred uncritically across systems.

## Reconstructible law, dimensional contract and assumptions

`H=N_layers h(1+ε_scale)`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For 100 layers of 0.2 mm each and a 1% hypothetical scale error, expected height is 20.2 mm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

The layer-height calculation cannot certify load-bearing performance or quality of a laser-melted part. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Measurement Science for Additive Manufacturing Program**, https://www.nist.gov/programs-projects/measurement-science-additive-manufacturing-program. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
