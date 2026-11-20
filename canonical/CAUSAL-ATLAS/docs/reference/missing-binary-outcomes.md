# Unknown binary outcomes produce bounds, not zeros

Within completely counted groups, missing binary values bound risk between successes/total and (successes+missing)/total.

**Record:** `causal-atlas:missing-binary-outcomes`  
**Revision:** `c73fb0785917b760bac1f14af3bf0c72aaacdb57abfb9b1e72ca2192a654810c`  
**Evidence type:** original_arithmetic_with_source_context

## Conditions

- Binary outcome and known denominator

## Limitations

- Bounds do not account for sampling variation or treatment confounding

## Primary source scope

[Causal Inference What If author resource page](https://miguelhernan.org/whatifbook) — Original arithmetic derived; book includes selection/censoring scope

**Equation:** `s/n <= risk <= (s+n-o)/n`

This source-linked record is not independently scientifically reviewed.
