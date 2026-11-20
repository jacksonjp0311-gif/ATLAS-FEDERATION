# Measurement content coverage

The eight question families below are an explicit bounded scope, not a completeness score for metrology. Evidence maturity remains separate from software readiness.

| Family | Current coverage | Still required |
|---|---|---|
| Measurand and terminology | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/01_measurand_and_terms.md) | Independent review and domain-specific measurand examples |
| Units and quantity meaning | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/02_units_and_dimensions.md) | Bounded unit parser, explicit quantity-kind checks and temperature handling now implemented; arbitrary expressions and a universal ontology remain out of scope |
| Repeated readings and dependence | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/03_repeat_readings.md) | Real time-series evidence and independence/model diagnostics |
| Type B and resolution | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/04_type_b_and_resolution.md) | Structured operator-entered certificate/specification tools are implemented; authentic certificate access and independent interpretation remain missing |
| Budgets and nonlinear models | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/05_budgets_and_nonlinearity.md) | General nonlinear propagation and real-model validation |
| Calibration and traceability | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/06_calibration_and_traceability.md) | An attributed 40-reading case is now numerically reproduced; original bytes, certificate/traceability records, physical units, broader datasets and independent physical reproduction remain missing |
| Comparison and coverage | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/07_comparison_and_coverage.md) | Conditional t/independent-component methods and a synthetic coverage stress test are now implemented; conditional normal probability and explicit guard-band models are added; actual-distribution validation, independent review and application-specific decision rules remain open |
| Reporting and reproducible reuse | [assistant_curated_reference_and_synthetic_examples](../docs/chapters/08_reporting_and_reuse.md) | Independent report review and supported-platform checks |

All families have source-linked material; none is marked independently reviewed. Navigation is deferred, not waived. G6/G7 remain open and no next domain is authorized.
