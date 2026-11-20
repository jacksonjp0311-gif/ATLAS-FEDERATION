# Chapter 16 — Heat balances in machines, toolrooms and thermal processes

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A lumped thermal capacity C linked to ambient through thermal resistance R and heated by constant P obeys C dT/dt=P−(T−T_ambient)/R. Solve this linear ODE to obtain the exponential response with τ=RC and equilibrium T_∞=T_ambient+PR. Thermal state changes machine dimensions, material stiffness, electronics and measurement. The model is appropriate only when internal temperature gradients are negligible relative to the boundary resistance. Store energy balances, sensor uncertainty and environmental history.

## Reconstructible law, dimensional contract and assumptions

`T(t)=T_∞+[T(0)−T_∞] exp[−t/(RC)]`

Inputs/outputs: **K, W, J/K**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With T(0)=310 K, ambient 300 K, P=5 W, R=2 K/W and C=10 J/K, T is already at 310 K and remains constant. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A lumped response cannot predict tool-tip gradients, thermal deformation, flash temperatures or chemical thermal processes. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Metrology programme and measurement practice**, https://www.nist.gov/metrology. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
