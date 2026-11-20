# Estimator contract 0.2.0

These are separately invoked standard-library teaching tools. Retrieval never executes them. Numbers are exact rational strings for retained calculations; input magnitude and table sizes are bounded. No model is fitted and no sample uncertainty interval is produced.

## Individual rows

`estimate FILE --nuisance-origin synthetic_oracle` accepts a JSON list,1–10000 rows, with exactly `id,a,y,e,m0,m1,x`. IDs are unique nonblank strings. Treatment is integer0/1, not bool; both arms must exist. Probabilities satisfy0<e<1. Numeric fields must be finite and within documented code bounds. `x` is one declared baseline covariate used only for a mean-balance diagnostic; it does not define a full adjustment set.

Nuisance provenance must be `known_design`, `external_predictions`, `out_of_fold`, `in_sample`, or `synthetic_oracle`. This records a caller assertion, not an authenticated fitting history. The input CLI limit is256KiB; the direct Python row limit remains10000. Exact row fields prevent accidental count weights or undisclosed extra columns.

Returns crude, outcome-regression, Horvitz–Thompson IPW, Hájek IPW and residual-form AIPW differences plus weight diagnostics. No clipping or automatic repair occurs. Invalid inputs raise `ModelError` and CLI exit2.

## Fully stipulated population

`population FILE` accepts1–128 unique named strata with exactly `name,q,e,mu0,mu1,g,m0,m1`. Positive target masses q sum exactly to1. Generating e and working g are interior probabilities; generating and working binary outcome means lie in[0,1]. This function knows the true model because it was supplied; it is not an estimator from ordinary observations.

## Missing outcomes and trend scenarios

`missing-bounds FILE` accepts objects `0` and `1`, each containing integer `total,observed,successes`, with0<=successes<=observed<=total and1<=total<=10^9. It returns counted-population bounds, not confidence intervals or a confounding correction.

Python `two_period_contrast(treated_pre,treated_post,control_pre,control_post,untreated_trend_difference=0)` returns arithmetic and a labeled sensitivity scenario. It does not validate parallel trends or implement a panel-data estimator.

## Unsupported work

Propensity fitting, cross-fitting, imputation, confidence intervals, clustered sampling, repeated unit histories, survival analysis, causal graph discovery, real-data authentication and final scientific acceptance are not implemented. The previously documented DAG and finite binary tools retain their bounds. See `models.py`, `estimation.py` and [coverage](COVERAGE_MATRIX.md).
