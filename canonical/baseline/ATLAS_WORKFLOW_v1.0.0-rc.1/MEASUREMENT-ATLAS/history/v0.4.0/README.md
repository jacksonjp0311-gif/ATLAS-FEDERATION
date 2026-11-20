# MEASUREMENT ATLAS

**Meaningful measurements need units, assumptions, uncertainty and traceable evidence.**

**Engineering checkpoint 0.4.0 · Measurement v1 acceptance pending · Active Atlas in Forge**

Measurement Atlas is the reference implementation of the shared Atlas knowledge contract. It combines bounded, source-linked metrology reference records with explicitly assumed numerical tools. It is not a calibration laboratory, complete uncertainty standard, independently reviewed corpus or verified measurement service.

## Reference knowledge

The common node contains **35 records**: twenty bounded reference records checked against specific public NIST passages, nine new source-page records, five preserved unreviewed heading-navigation packets and the original NIST source card. The new checks are assistant primary-portion checks, not independent review or experimental reproduction.

Coverage includes Type A/B evaluation, standard/combined/expanded uncertainty, first-order covariance propagation, assumed uniform/triangular bounds, certificate multipliers, reporting, systematic corrections and traceability limitations. Units/dimensional reasoning and several v1 case families still need substantive expansion.

Install the companion Forge 0.4.0 wheel for the shared reference engine:

```powershell
py -3 -m measurement_atlas reference "uncertainty of a difference" --max-bytes 32768
```

This reads this node through exactly the same `AtlasStore` used for Signal and Cymatics, not a separate search implementation. The numerical toolkit below works without Forge.

## Numerical tools

```powershell
py -3 -m measurement_atlas type-a "[10,12,14]"
py -3 -m measurement_atlas combine '{"sensitivities":[1,1],"covariance":[[4,0],[0,9]]}'
py -3 tools/casebook.py
```

Functions: uncertainty of an independent repeated-reading mean, first-order covariance propagation, explicit coverage factor multiplication, difference uncertainty, named budgets with declared harmonized output units, assumed Type B distributions, and documentation-chain checks. An `as_of` ISO date makes traceability-document checks repeatable. These checks do not certify a physical calibration or prove fitness for purpose.

## Confirmed v0.3 defect repaired

The earlier covariance checker used an absolute tolerance floor. It accepted `[[1e-12,2e-12],[2e-12,1e-12]]`, an invalid covariance matrix implying correlation 2, and returned zero uncertainty for sensitivities `[1,-1]`.

This version validates a dimensionless correlation matrix with relative tolerance and a pivoted positive-semidefinite check. That invalid example is now rejected at every tested scale. Regression tests include small/large scale, global indefiniteness, singular valid covariance, zero-variance rows, overflow and explicit assumptions. The repair does not make floating-point first-order propagation a general nonlinear solver.

## Reproducible checks

Run the unit suite with `python -m unittest discover -s tests -v`. Shared-reference tests require the Forge wheel or its `src` directory on `PYTHONPATH`; without it they explicitly skip. The combined workflow runs both suites with that dependency available.

`tools/casebook.py` produces five invented teaching examples, never laboratory observations. `tools/numerical_oracle.py` optionally uses NumPy to compare 600 seeded positive-definite covariance cases over five scales and reject five invalid cases. This is a numerical cross-check, not independent human review.

## Directory

| Path | Purpose |
| --- | --- |
| `measurement_atlas/uncertainty.py` | Explicit first-order numerical models and validation |
| `measurement_atlas/budget.py` | Declared uncertainty contributions and correlation |
| `measurement_atlas/traceability.py` | Structural documentation checks, not certification |
| `measurement_atlas/reference.py` | Thin adapter to Forge's common runtime |
| `measurement_atlas/resources/common/` | Complete executable single-node common snapshot |
| `reference/` | Readable duplicate of the same record collections |
| `evidence/primary_reference_additions.json` | Authored source-linked additions with locators |
| `docs/PRIMARY_SOURCE_REGISTER.md` | Source/check boundary and record directory |
| `docs/receipts/` | Actual regression, oracle and synthetic casebook outputs |
| `history/` and `docs/history/` | Preserved previous manifests and documentation |

`atlas_manifest.json` describes the source node and its `data/` common collections. The runtime bundle under `measurement_atlas/resources/common` is the portable single-node registry. Forge bundles the identical current Measurement records.

**Measurement remains the active work until v1.** Close declared scope/evidence gaps, demonstrate actual Bitwork and model use, freeze and run independent evaluations, and verify supported platforms before advancing. Software/contract version numbers do not imply those gates passed.
