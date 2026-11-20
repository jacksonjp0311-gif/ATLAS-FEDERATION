# Chapter 06 — Machine coordinates, spindle kinematics and feed conversion

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Uniform tangential speed defines the spindle relation v_c=πDn after consistent unit conversion. For z cutting edges and feed per tooth f_z, the nominal programmed linear feed is n z f_z. The relation assumes steady rotation and full engagement; it does not identify an experimentally safe feed, tooth breakage threshold, vibration limit, or heat load. Coordinate systems include machine coordinates, work offsets and tool offsets. Any transform must identify origin, handedness, axis direction and units; silent frame changes create systematic dimension errors.

## Reconstructible law, dimensional contract and assumptions

`n[rpm]=1000 v_c[m/min]/(πD[mm]); v_f=n z f_z`

Inputs/outputs: **rpm, mm/min**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

D=10 mm, v_c=100 m/min, z=4, f_z=0.05 mm produces n≈3183 rpm and feed≈637 mm/min in the ideal formula. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Using mm as metres creates a 1000× speed error. Encoder counts do not guarantee actual cutting-edge position under tool deflection. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
