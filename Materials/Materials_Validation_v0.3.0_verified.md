# Materials Atlas 0.3.0 evidence and validation audit

**Status:** tested content development release, *not* independent materials science review or final v1. All thirty domain content libraries must precede new routing and desktop transfer.

## Findings and new methods

- **Symmetric regular solution:** Gibbs mixing with constant omega; analytic spinodal and bracketed equilibrium binodal, three phase-state classifications, mole-basis lever fractions, model refusals. Not a measured binary phase diagram or CALPHAD assessment.
- **Cubic indexed diffraction:** supplied (hkl), 2θ and uncertainty, declared Bragg first order, weighted lattice parameter, random-angle versus common wavelength uncertainty, chi-square diagnostic. Does not identify phase, fit diffraction peaks or correct systematic instrument offset.
- **NIST Hahn1:** descriptive residual analysis of the 236 source-reported observations already transcribed in v0.2. The physical response type is known from NIST, the numeric unit scale is not independently authenticated; no physical strain prediction or instrument traceability is asserted.

## Executed results

- Forge 188, Measurement 218, Causal 233, Materials 98: **737 automated tests passed**, no skips. Cross-node source closure and common-context checks passed. Repeated after ZIP extraction separately in release audit.
- SciPy direct energy-minimization phase boundary comparison: **90 cases**, largest absolute binodal discrepancy 7.75e-09 in mole fraction.
- NumPy vectorized peak uncertainty agreement: **960 scalar checks**. NumPy residual-bin comparison: **eight bins**.
- Prior 1,440 advanced and 1,200 foundational numerical comparisons rerun and passed; NIST Hahn1 two fitted algorithms and certified RSS check passed.
- Isolated wheel install and import check passed after correcting a *harness-only* expected count: the standalone Materials wheel contains one 112-record Materials node, not the full five-node index. The full collection has 766 records.
- All 89 earlier Materials record revisions unchanged; prior 19 chapters, eight investigations, baseline and other nodes preserved. Routing files unchanged.

## Scientific limits

The only source-reported physical observations reused remain the attributed NIST Hahn1 published numbers from the checked transcription; no new authentic experimental records or original NIST-byte hash obtained here. No independent scientific review, real-material phase diagram, XRD profile, apparatus calibration, Windows execution, live Bitwork run, held-out retrieval/AI answer validation or full Materials v1 acceptance occurred. Source access is explicitly partial where applicable; IUPAC direct fetch returned 403 after a search excerpt.

## Reproduce

```sh
python tools/check_collection.py --out receipts/materials-0.3-local-unique
PYTHONPATH=MATERIALS-ATLAS python -m materials_atlas expanded-cases
PYTHONPATH=MATERIALS-ATLAS python MATERIALS-ATLAS/tools/phase_diffraction_oracle.py
PYTHONPATH=MATERIALS-ATLAS python MATERIALS-ATLAS/tools/advanced_numeric_oracle.py
PYTHONPATH=MATERIALS-ATLAS python MATERIALS-ATLAS/tools/numerical_oracle.py
```

Output receipts and sources are included. A successful test run is not scientific certification. Do not manufacture additional acceptance flags.
