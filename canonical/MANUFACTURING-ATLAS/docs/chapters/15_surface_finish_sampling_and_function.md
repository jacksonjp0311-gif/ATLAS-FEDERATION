# Chapter 15 — Surface texture, sampling limits, contact function and roughness

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Surface texture influences contact, friction, lubrication, leakage and electrical interconnect behavior. A discrete absolute-deviation calculation summarizes a profile sample relative to a fitted mean. It is not a complete realization of an official surface-roughness standard: filtering, evaluation length, probe radius, sampling spacing, directionality and spatial form all matter. Flatness and roughness are different measurements. Use explicitly stated bandwidth and instrument condition before comparing reported Ra values. Reconstruction requires both an algorithm and an independent measurement method.

## Reconstructible law, dimensional contract and assumptions

`R_a,discrete=(1/N)Σ|z_i−z̄|`

Inputs/outputs: **m**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For samples [0,+1 µm,−1 µm], the simple mean-removed average absolute height is 2/3 µm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A low Ra does not establish surface flatness, low fatigue crack risk, electrical cleanliness or seal compatibility. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
