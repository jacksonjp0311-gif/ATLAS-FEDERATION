# Reproduce a published load-cell calibration

**Measurement Atlas 0.6.0 · James Paul Jackson research program · 12 November 2026**

## What is reproduced

NIST's Pontius case provides 40 load/deflection observations from two increasing-load runs, each at 20 load levels. The Atlas reproduces a straight-line fit, a quadratic fit, replicate-based lack-of-fit calculations and a bounded inverse example. The quadratic results match 11 values from the NIST StRD certified numerical reference. Six comparisons to the handbook's displayed numbers exceed their stated rounding precision; see [the retained discrepancy register](SOURCE_DISCREPANCIES.md).

This is a computational reanalysis of published experimental values. It is not an independent repetition of the load-cell experiment, a new measurement dataset, a calibration certificate or an independently reviewed study.

## Data and capture

The decimal tokens are stored in [observations.json](../measurement_atlas/resources/pontius/observations.json), in original order. [Capture metadata](../measurement_atlas/resources/pontius/capture.json) records provenance, missing information, rights review and the local SHA-256. Data were inspected in both the [publisher data file](https://www.itl.nist.gov/div898/handbook/datasets/PONTIUS.DAT) and [HTML table](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd611.htm), and compared with the [StRD data display](https://itl.nist.gov/div898/strd/lls/data/LINKS/DATA/Pontius.dat). These are three presentations of one source dataset, not independent experiments.

Direct byte download was unavailable in the build runtime. Therefore this is a **checked transcription**, not an upstream-byte snapshot. The original file hash is explicitly null. No physical units, dates, instrument serial or traceability certificate were invented. The load unit and deflection unit remain unspecified as in the inspected case. No inference of newtons, kilograms, volts or SI traceability is permitted.

Attribution and terms are in [NOTICE.md](../measurement_atlas/resources/pontius/NOTICE.md). Only this attributed numeric capture is included; linked publications are not mirrored.

## Reproduction

```powershell
py -3 -m measurement_atlas published-case
py -3 tools/published_case_oracle.py
```

The first command needs only the standard library. The optional second command uses NumPy least squares as a separate numerical implementation; it reports `not_run` rather than claiming success when NumPy is missing. A successful first command returns `passed_with_source_discrepancies`, not a claim that every publisher display agrees.

## Models and diagnostics

The response model is `D = b0 + b1 L + b2 L^2 + error`, with the quadratic term absent for the straight line. The implementation centers/scales L and uses 60-digit Decimal arithmetic for the tiny normal system. It supports degree one or two only and is not a general high-degree solver. Regression assumes fixed reference loads and independent, equal-variance response errors. A complete uncertainty budget can require reference-load uncertainty, environmental effects, drift and other components that this case cannot establish.

| Quantity | Straight line | Quadratic |
|---|---:|---:|
| Residual standard deviation | 0.00217127259606 | 0.000205177424076 |
| Residual degrees of freedom | 38 | 37 |
| R-squared | 0.999988519115 | 0.999999900179 |
| Replicate lack-of-fit F | 214.746923654 | 0.81072390031 |

The [source design warning](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd611.htm) remains central: two ordered increasing-load runs cannot cleanly identify drift. The [lack-of-fit definition](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd446.htm) requires replicates; the statistic does not establish every model assumption. A high R-squared is not a guarantee of acceptable calibration.

## Inversion and prediction

The publisher's hypothetical deflection 1.239722 gives an in-range recomputed load of about 1705105.57 source units. The distant quadratic root is excluded. The illustration is not a 41st measured observation. The software refuses nonmonotone inverse ranges and extrapolation.

Fitted-mean and future-observation prediction standard deviations are separate. An independent future observation includes residual variance in addition to mean-estimation variance, following [NIST §4.5.1.2](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm). The package does not label those standard deviations as 95% intervals. The handbook's interval endpoints are retained as documentary reference only; this release does not claim to reproduce them.

## What remains before scientific v1

Original byte archival capture, complete unit and traceability documentation, broader metrological cases, certificate/specification interpretation, independent human review, coverage and decision-risk validation, Windows execution and the deferred Bitwork/AI evaluation remain open. One numerical reproduction does not close those gates.
