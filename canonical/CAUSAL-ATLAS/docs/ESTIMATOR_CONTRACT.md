# Estimator contract 0.3.0

These are separately invoked standard-library teaching tools. Retrieval never executes them. Numbers are exact rational strings for retained calculations; input magnitude and table sizes are bounded. Nuisance models are not fitted. The new RD tool fits only explicitly bounded local lines; no sampling uncertainty interval is produced.

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

## Instrumental variables and supplied contrasts

`wald FILE` requires `y_z0`, `y_z1`, `d_z0`, `d_z1`, `minimum_first_stage`, and `data_origin`. Supplied treatment means must be probabilities. The ratio is `(y_z1-y_z0)/(d_z1-d_z0)`. If the absolute denominator is at or below the caller's nonnegative guard, the result is `unresolved_first_stage`, not infinity or an invented effect. A numerical guard is not a statistical weak-instrument test. No population-wide interpretation, standard error, sample-size information or instrument validity is inferred.

`iv-population FILE` takes 1–64 fully stipulated types with exactly `name,mass,d0,d1,y0,y1,direct_z`. Masses must be positive and sum exactly to one; treatment potentials are literal integer 0/1, not booleans. Outcomes may be general bounded numbers. The model is `Y(d,z)=y0+(y1-y0)*d+direct_z*z`. Using the same type distribution in both instrument arms stipulates independence. Its reported treatment effects are known-model outputs, not observational estimates.

`iv-sensitivity FILE` requires `reduced_form`, `first_stage`, `direct_lower`, `direct_upper`, `minimum_first_stage`, `data_origin`. It varies the supplied additive direct contribution in `reduced_form=theta*first_stage+direct_contribution`. The returned scenario bounds are not confidence intervals or universal partial-identification bounds.

## Local regression-discontinuity teaching fits

`rd FILE` takes `rows`, `cutoff`, `bandwidth`, `kernel`, `data_origin`. Each of 1–512 rows has exactly `id,x,y`. IDs are unique. The bandwidth is positive and kernel is `triangular` or `uniform`. Both use the strict open window `abs(x-cutoff)<bandwidth`; the cutoff is assigned to the right. Rows exactly at either bandwidth boundary are excluded. All supplied rows, including excluded rows, must be syntactically valid.

Each side requires at least three positive-weight rows and two distinct scores for this implementation. This is a numerical support requirement, **not** a sufficient sample size for reliable inference. The line is fit with exact rational normal equations in `u=(x-cutoff)/bandwidth`. The output includes each side's intercept, slope per score unit, weighted residual sum of squares, support counts, nearest gap, kernel-weight ESS and equivalent intercept weights. Equivalent weights can be negative; none is clipped. The estimated jump is the right intercept minus the left. The support diagnostics do not prove continuity or rule out sorting and other interventions.

`fuzzy-rd FILE` additionally requires literal binary `d` in every row and `minimum_first_stage`. Outcome and treatment fits use identical rows, bandwidth and kernel. The ratio is guarded as above. Local linear treatment predictions outside [0,1] are flagged, not silently clipped; this possible linear-fit behavior does not authorize treating a bad design as valid.

`rd-bandwidths FILE` replaces `bandwidth` with 1–12 distinct positive `bandwidths`. Every requested window is reported, including windows lacking required support. No bandwidth is automatically selected.

For the new tools, `data_origin` must be `synthetic_constructed`, `operator_supplied`, or `published_transcription`. The label is a caller assertion, not an authenticated provenance chain. New numeric inputs have absolute magnitude at most 10^12 and rational denominator bit length at most 128. CLI input remains limited to 256 KiB. The utilities are bounded teaching implementations, not optimized large-data estimators. Normal input validation errors are explicit exceptions and CLI exit 2. A computable but unsupported causal interpretation is retained as a scoped numerical result, not called a scientifically verified answer.

Neither RD branch computes robust bias-corrected inference, clustered errors, a density test or an IV confidence set. Those remain explicit coverage gaps. Source lookup never executes these tools.

## V1 bounded additional methods

The separately invoked `causal_atlas.advanced` module provides exact arithmetic for supplied binary potential-outcome models, with explicit identifiers and limitations. It does not learn nuisance probabilities, identify observational causal effects, or supply full sampling uncertainty.

| CLI | Function | Interpretation boundary |
|---|---|---|
| `longitudinal` | `longitudinal_gformula` | Fixed two-decision model with one binary intermediate covariate |
| `staggered-did` | `staggered_group_time` | Descriptive cohort-time comparisons; no full estimator or variance |
| `mediation` | `mediation_interventional` | Stochastic mediator distribution contrast, not natural direct effect |
| `interference` | `cluster_interference` | Fully supplied two-unit assignment outcomes |
| `transport` | `transport_strata` | Supplied stratum response functions and support check |
| `binomial-interval` | `independent_binary_contrast` | Conditional approximate descriptive interval, not causal inference |
| `ucb-admissions` | `berkeley_admissions` | Historical observational aggregates; no identified intervention

All tools reject malformed arguments and return explicit scoped status. Users must specify the data-generating assumptions independently. See the casebook and numbered chapters.
