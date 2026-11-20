# MEASUREMENT ATLAS

**A reusable reference for what a measurement means, how uncertainty is calculated, and what a result does not establish.**

## Version 1.0.0 release candidate 1

The candidate contains 141 common records, eight foundational chapters, practical supplements, declared numerical methods, reproducible examples and a published-data calculation. It is not final v1 acceptance, an independently reviewed metrology service or a calibration laboratory.

## Read the reference

[Reference guide](docs/REFERENCE_GUIDE.md) · [V1 scope](docs/V1_RELEASE_SCOPE.md) · [Source register](docs/PRIMARY_SOURCE_REGISTER.md) · [Coverage gaps](docs/COVERAGE_MATRIX.md)

| Topic | Entry point |
|---|---|
| Units, dimensions and quantity kinds | [Bounded conversion API](docs/UNIT_CONVERSIONS.md) |
| Repeated readings and uncertainty budgets | [Models](docs/UNCERTAINTY_MODELS.md) and [budgets](docs/UNCERTAINTY_BUDGETS.md) |
| Coverage and inverse calibration | [Coverage methods](docs/COVERAGE_METHODS.md) |
| Calibration information and later use | [Certificate interpretation](docs/CERTIFICATE_INTERPRETATION.md) |
| Conditional probabilities and decision rules | [Decision models](docs/CONFORMITY_DECISIONS.md) |
| Published observations and discrepancies | [Pontius analysis](docs/PUBLISHED_CALIBRATION_CASE.md) and [inverse interval replay](docs/INVERSE_INTERVAL_REPLAY.md) |
| Remaining acceptance evidence | [Review handoff](docs/V1_REVIEW_HANDOFF.md) and [release audit](docs/RELEASE_AUDIT_v1.0.0-rc.1.md) |

## Use the tools

```python
from measurement_atlas import convert_quantity, normal_conformance

result = convert_quantity(20, "degC", "K", quantity_kind="temperature", uncertainty=0.2)
context = normal_conformance(0.95, 0.1, lower=0, upper=1, unit="mm",
    quantity_kind="length", model_basis="Synthetic declared normal knowledge model")
```

Numerical functions use the Python standard library. Reference search uses the companion Forge wheel so the node does not fork its own retrieval engine. Source and wheel layouts share the same version-pinned record view.

```powershell
py -3 -m measurement_atlas reference "calibration uncertainty"
py -3 -m measurement_atlas published-case
py -3 -m measurement_atlas inverse-interval
py -3 -m measurement_atlas certificate-review --input examples/synthetic_certificate.json
py -3 tools/practical_casebook.py
```

An incomplete certificate review is an explicitly reported result, not a process failure. A successful calculation does not establish the model assumptions. Guard-band decisions are outcomes under a declared rule, not proofs of conformity.

## Reproduce and review

Run the complete workflow from the workspace root; it supplies both source paths for tests. Optional NumPy, SciPy and mpmath checks are separate numerical comparisons, never human review. Every original Pontius observation and previous discrepancy remains preserved. Synthetic certificate fixtures and publisher illustrations are not newly measured data.

The final gate remains closed for review/freeze, source/evidence completion, live Bitwork and actual model use, independent held-out evaluation and supported-platform confirmation. No other Atlas domain starts as a side effect of this candidate.
