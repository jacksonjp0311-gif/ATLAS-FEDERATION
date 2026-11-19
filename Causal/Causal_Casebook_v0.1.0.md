# Seven reproducible causal teaching checks

Every value here is synthetic. No laboratory, manufacturing or patient measurements were collected. A calculation is not an established causal effect.

## Confounding and adjustment

For a stipulated graph U → A, U → Y, A → Y, the empty adjustment set fails the ordinary back-door check; conditioning on U passes. This is conditional on the stipulated graph including the relevant causes. It does not measure U or validate that graph.

## Collider selection

For A → C ← Y and C → D, the unconditioned A–Y path is blocked. Conditioning on C or D opens that path. No causal magnitude is inferred from the graph.

## A synthetic reversal

Two strata have untreated outcome rates 0.1 and 0.7, and treated rates 0.2 and 0.8. The target population has equal stratum weights. Direct standardization therefore gives untreated risk 0.4, treated risk 0.5 and difference +0.1.

The synthetic observed table places 90 treated cases in the low-rate stratum and 10 in the high-rate stratum; controls have the reverse composition. Their event counts are 18/90, 8/10, 1/10 and 63/90 respectively. The crude difference is 0.26 − 0.64 = −0.38. Supplied propensity scores 0.9 and 0.1 yield normalized IPW risks 0.5 and 0.4, matching the standardized target.

These are deliberately constructed frequencies. The sign reversal illustrates population mixing; it does not demonstrate that any real treatment harms or helps anyone.

## Explicit failures

Zero/one propensity scores are rejected rather than clipped. Directed cycles are rejected because the implemented graph contract is a DAG. The seven executable checks comprise two back-door cases, one collider case, standardized reversal, same-table IPW, zero-support rejection, and cycle rejection.

Run `python -m causal_atlas casebook`. Separate exhaustive active-path enumeration cross-checks the moralization implementation on 64 four-node ordered DAGs and all 1,536 endpoint/conditioning combinations. This comparison is authored numerical/algorithmic checking, not independent review.
