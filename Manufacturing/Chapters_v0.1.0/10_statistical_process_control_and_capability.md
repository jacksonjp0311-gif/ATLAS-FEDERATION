# Chapter 10 — Control charts, capability indices and nonstationarity

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A stable process in a defined state can be characterized by the population-like distribution of an inspection characteristic. Three-sigma control limits are used to signal potential special causes, not to assert that all products are conforming. Cp compares specification width with six estimated process standard deviations; Cpk penalizes a displaced mean. These indices have meaning only given process stability, measurement-system adequacy, a justified distribution model and representative data. Treat unstable or distribution-unassessed inputs as unqualified, not as bad-looking capability numbers.

## Reconstructible law, dimensional contract and assumptions

`Cp=(USL−LSL)/(6σ); Cpk=min(USL−μ, μ−LSL)/(3σ)`

Inputs/outputs: **dimensionless**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With limits 9 and 11, mean 10, σ=0.2, both Cp and Cpk equal about 1.667 conditional on documented assumptions. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A high Cpk from six handpicked measurements is not evidence of production capability or acceptable safety risk. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Metrology programme and measurement practice**, https://www.nist.gov/metrology. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.
