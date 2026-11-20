# Future response uncertainty includes new observation variation

**Record:** `prediction-versus-mean` · **Type:** method · **Origin:** source_reported

A fitted mean response and a single future response can have the same point estimate but different uncertainty. For an independent new response, prediction variance includes both fitted-mean variance and residual response variance.

## Declared relation

```text
s_prediction^2 = s_mean^2 + s_residual^2
```

## Source and inspected portion

[Mean response and single-response prediction uncertainty](https://www.itl.nist.gov/div898/handbook/pmd/section5/pmd512.htm) · §4.5.1.2 Uncertainties Do Differ and Standard Deviation of Prediction

## Assumptions

- The new response is independent of the fitting data and follows the same response-error variance model.

## Limitations

- This is model-based uncertainty, not a complete metrological budget.
- Prediction SD by itself is not a confidence or coverage interval.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
