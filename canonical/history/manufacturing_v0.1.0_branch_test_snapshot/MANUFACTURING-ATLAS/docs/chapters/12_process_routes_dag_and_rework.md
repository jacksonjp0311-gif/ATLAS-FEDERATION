# Chapter 12 — Process plans, dependency DAGs, checkpoints and rework

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A part can be represented by a directed acyclic graph of operations. Each operation consumes a defined material state and produces a revised state plus evidence, e.g., datum established, surface measured, heat treatment completed. A topological order exists only without cycles. The longest dependency chain gives a lower bound on completion time if unlimited parallel resources are available. Real machines and workers create resource contention, queues, setups, rework and maintenance, so an unconstrained critical path is not a production schedule. Keep the process route reproducible and version controlled.

## Reconstructible law, dimensional contract and assumptions

`finish(v)=duration(v)+max_(u predecessor v) finish(u)`

Inputs/outputs: **min**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

If preparation takes 3 min, dependent machining takes 5 min, independent measurement 7 min, and joining takes 2 min after both, earliest completion is 10 min assuming no shared resource. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A shortest theoretical lead time ignores equipment capacity, logistics, inspection rejection and process yield. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Additive Manufacturing Data Integration and Recommended Practice**, https://www.nist.gov/publications/additive-manufacturing-data-integration-and-recommended-practice. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
