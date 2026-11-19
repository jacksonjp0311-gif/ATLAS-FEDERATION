# Chapter 07 — Material-removal rate, specific cutting energy and power accounting

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

For a rectangular approximation of engaged material, removing a slice of axial depth a_p and radial width a_e across feed distance v_f per minute yields Q=v_f a_p a_e. The ideal specific-cutting-force approximation converts k_c in N/mm² and Q in mm³/min into watts by dividing by 60,000. Input motor electrical power must exceed cutting power when efficiency is below unity, and other losses contribute. Specific force depends on material, tool geometry, chip thickness and wear. This is an accounting model, not measured cutting conditions.

## Reconstructible law, dimensional contract and assumptions

`Q=v_f a_p a_e; P_cut=k_c Q/60000`

Inputs/outputs: **mm³/min, W**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With a 6,366 mm³/min rate and k_c=1,500 N/mm², the ideal power estimate is about 159 W before drive and auxiliary losses. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A single k_c constant cannot predict chatter, tool fracture, burrs, heat damage, machine bearing loads or unsafe conditions. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
