# Chapter 09 — Lead screws, step resolution, backlash and positioning uncertainty

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

An ideal screw translates one pitch p for each turn. Dividing that rotation into N command steps gives a nominal increment p/N. Backlash is path-dependent deadband: after direction reversal the mechanism may not move until play is taken up. Without state and calibration, a symmetric interval around the ideal command is a conservative representation, not a predicted actual position. Encoder position on the motor side may not capture tool-end motion or structural compliance. Validation requires an external position reference, reversal tests and temperature control.

## Reconstructible law, dimensional contract and assumptions

`Δx=p/N_steps; x∈[x_cmd−b−Δx/2,x_cmd+b+Δx/2]`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Ten commanded turns at 1 mm/turn with 0.02 mm backlash and 200 steps/turn yield an ideal 10 mm and a conservative reachability band of ±0.0225 mm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A 0.005 mm microstep is not proof of ±0.005 mm absolute positioning accuracy. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
