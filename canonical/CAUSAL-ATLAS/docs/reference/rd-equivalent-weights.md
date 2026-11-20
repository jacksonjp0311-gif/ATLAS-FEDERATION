# Local-line intercept weights may be negative

The derived intercept weights sum to one and have zero weighted scaled-score sum. Negative equivalent weights are reported, not silently removed.

**Record:** `causal-atlas:rd-equivalent-weights`  
**Exact revision:** `35e1f4c924e297f0f284f3bbc0e3f5628c8bde4999c4050f28c427548e886e6a`  
**Origin:** `authored_derivation`

## Equation

`ell_i=w_i*(S2-S1*u_i)/(S0*S2-S1^2)`

## Assumptions and limits

- Kernel-weight ESS is not independent inferential sample size.

## Source and locator

Original derivation/example; see the local locator.

docs/chapters/11_regression_discontinuity.md; causal_atlas/quasi.py:_fit_side

No independent scientific review or empirical validation is claimed.
