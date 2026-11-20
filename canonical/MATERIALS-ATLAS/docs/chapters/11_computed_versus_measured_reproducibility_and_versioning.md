# Chapter 11. Computed versus measured, reproducibility and versioning

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A calculation can reproduce an equation yet not validate the physics that generated its input. Store the software release, pseudopotential/basis model, functional, U parameters, convergence controls, k-point strategy, structure file, correction scheme, units and computational energy normalization. For experiments, store instrument identity, standard/edition, calibration, reference specimen, raw curve, analysis script, environmental conditions and uncertainty model.

Database revision changes can alter computed results without changing the nominal material identifier. Avoid treating a value obtained in one Materials Project release as equivalent to another without checking the correction and thermodynamic reference. The publication itself explains that compatibility across mixed functionals requires correction schemes.

The NIST materials repository notes that contributed information may not be critically reviewed. Availability and indexing are not source validation. The Atlas records original source URLs but does not mirror third-party datasets without verified rights. If raw files are absent, record that limitation explicitly. Favor stable persistent identifiers where available.

**Data comparison guard:** before computing a numerical difference, check property, method, units, temperature, direction, sample condition and origin. Contradictory values may be condition-specific rather than truly contradictory. The comparison utility uses equality of a fixed metadata list and still does not calculate significance without a covariance and coverage model.

## Reference capsules for this chapter

- **Computed entries need a reproducible pipeline** (method): Record functional, code release, structure, magnetic initialization, convergence, reference energies, and corrections.
- **Measurements need sample and machine histories** (method): Record raw curve, sample processing, geometry, machine configuration, calibration, environment and data reduction code.
- **Metadata equality precedes property subtraction** (method): Compare only quantities with compatible property, units, method, state, temperature and orientation; even then statistical inference requires joint uncertainty.
- **Data availability is not quality certification** (concept): A public repository entry is not necessarily critically reviewed; provider rights and provenance must be checked separately.

## Publisher portions used

[MP-CALC](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details) · [MP-ENERGY](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability) · [MP-RELEASE](https://docs.materialsproject.org/changes/database-versions) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system) · [NIST-REPO](https://materialsdata.nist.gov/)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
