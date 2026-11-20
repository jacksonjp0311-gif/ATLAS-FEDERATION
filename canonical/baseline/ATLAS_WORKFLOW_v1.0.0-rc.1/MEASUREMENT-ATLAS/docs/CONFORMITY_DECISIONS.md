# Conditional probabilities and stated decision rules

This module implements scalar mathematical models described in [JCGM 106:2012](https://www.bipm.org/en/doi/10.59161/JCGM106-2012), not accreditation or regulatory certification. See sections 7.1–7.4 for the probability model and 8.1–8.3 for acceptance rules.

A normal conformance calculation requires an explicit normal state-of-knowledge assumption. It integrates probability within the supplied limits. A standard uncertainty alone does not establish this distribution. Item-specific probability is kept separate from process-wide risk, which the module does not calculate.

`normal_conformance` returns the probability and its assumptions, with no automatic accept/reject decision. `guard_band_decision` separately applies a named inward-band rule and inclusive endpoints. Failing that rule is not proof of actual nonconformity. Selecting a rule and justifying its risks remain external decisions.

```python
from measurement_atlas.decisions import normal_conformance, guard_band_decision

context = normal_conformance(
    0.95, 0.10, lower=0, upper=1, unit="mm", quantity_kind="length",
    model_basis="Synthetic example: declared normal knowledge distribution")
decision = guard_band_decision(
    0.95, lower=0, upper=1, guard_width=0.10,
    rule_id="synthetic-inward-rule", unit="mm", quantity_kind="length")
```

These values are synthetic. The source examples in `evaluations/practical_targets.json` are publisher illustrations; they are not additional laboratory observations. `python tools/practical_casebook.py` reports each target, tolerance and result separately. Its tests are authored and visible, not a secret held-out benchmark.

Numerical restrictions: finite scalar inputs, positive uncertainty, increasing finite limits or a declared one-sided limit, and a nonnegative guard width leaving a positive-width acceptance interval. Extreme floating-point tails may underflow. Unsupported distributions, multivariate decisions, global risks and legal applicability are outside this implementation.
