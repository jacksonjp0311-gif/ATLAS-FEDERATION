# Measurement worked casebook

Twelve original synthetic cases. No input is an instrument observation or certificate. Every result is conditional on its stated model. Run `python tools/content_casebook.py` to reproduce. The five earlier cases remain in `tools/casebook.py`.

## unit-scale: Convert a length and its absolute uncertainty

Inputs: `{"value_mm": 25, "u_mm": 0.2, "m_per_mm": 0.001}`

- **value_m:** 0.025 m
- **u_m:** 0.0002 m

Assumptions: Exact declared scale conversion.

Limits: Not a general unit parser.

References: [quantity-value-unit](records/quantity-value-unit.md).

## temperature-offset: Convert a Celsius value but not an interval offset

Inputs: `{"value_degC": 20, "u_degC": 0.3, "interval_degC": 5}`

- **value_K:** 293.15 K
- **u_K:** 0.3 K
- **interval_K:** 5 K

Assumptions: Scale offset is exact in the stated relationship.

Limits: No instrument calibration uncertainty is invented.

References: [celsius-temperature-interval](records/celsius-temperature-interval.md).

## rounding: A specified uniform rounding model

Inputs: `{"step_mm": 0.02}`

- **u_mm:** 0.0057735026919 mm

Assumptions: Rounding to nearest step; justified uniform residual.

Limits: Truncation and other noise need their own model.

References: [quantization-assumption](records/quantization-assumption.md), [resolution-meaning](records/resolution-meaning.md).

## shared-offset: Common offset survives averaging

Inputs: `{"n": 4, "u_common_mm": 0.2, "sigma_independent_mm": 0.1}`

- **variance_mm2:** 0.0425 mm^2
- **u_mm:** 0.206155281281 mm

Assumptions: Independent common offset and independent reading noise.

Limits: A mathematical covariance model, not measured sensor behavior.

References: [correlated-mean](records/correlated-mean.md), [shared-offset-average](records/shared-offset-average.md).

## difference-covariance: Compare correlated estimates

Inputs: `{"a_mm": 12.3, "b_mm": 12.2, "var_a_mm2": 0.04, "var_b_mm2": 0.09, "cov_mm2": 0.03}`

- **difference_mm:** 0.1 mm
- **u_mm:** 0.264575131106 mm

Assumptions: Same specified measurand; covariance is supplied.

Limits: No acceptance rule or probability is inferred.

References: [measurement-difference](records/measurement-difference.md), [compatibility-rule](records/compatibility-rule.md).

## inverse-calibration: Inverse calibration with coefficient covariance

Inputs: `{"indication": 10, "intercept": 2, "slope": 4, "input_order": ["indication", "intercept", "slope"], "covariance": [[0.04, 0, 0], [0, 0.01, -0.002], [0, -0.002, 0.0025]]}`

- **estimate:** 2 input-unit
- **variance:** 0.00325 input-unit^2
- **u:** 0.057008771255 input-unit

Assumptions: Coefficient units match a declared response/input convention; linearization is adequate.

Limits: No evidence of linearity or applicable range is supplied by this arithmetic.

References: [inverse-linear-calibration](records/inverse-linear-calibration.md), [inverse-calibration-sensitivities](records/inverse-calibration-sensitivities.md).

## area-budget: First-order rectangular area budget

Inputs: `{"L_mm": 100, "W_mm": 50, "uL_mm": 0.2, "uW_mm": 0.1, "cov_mm2": 0}`

- **area_mm2:** 5000 mm^2
- **u_mm2:** 14.1421356237 mm^2

Assumptions: Declared independent inputs; first-order approximation.

Limits: Not the exact product distribution.

References: [linear-propagation](records/linear-propagation.md).

## ratio-budget: First-order ratio budget

Inputs: `{"x": 10, "y": 2, "ux": 0.1, "uy": 0.02, "cov": 0}`

- **ratio:** 5 1
- **u_ratio:** 0.0707106781187 1

Assumptions: Same input quantity kind; denominator bounded away from zero; local linearization adequate.

Limits: Not safe to generalize to near-zero denominators.

References: [linear-propagation](records/linear-propagation.md).

## nonlinear-counterexample: Finite enumeration exposes first-order failure

Inputs: `{"X_values": [-1, 0, 1], "probabilities": ["1/3", "1/3", "1/3"], "model": "Y=X^2"}`

- **exact_mean:** 0.666666666667 1
- **exact_variance:** 0.222222222222 1
- **first_order_variance:** 0 1

Assumptions: Equiprobable invented values; exact rational enumeration.

Limits: A counterexample to universal linearization, not a claim about every nonlinear problem.

References: [linearization-counterexample](records/linearization-counterexample.md).

## effective-dof: Conventional effective-degree arithmetic

Inputs: `{"variance_contributions": [1, 1], "degrees_of_freedom": [10, 10]}`

- **nu_eff:** 20 1

Assumptions: Independent components and conventional approximation conditions.

Limits: No t quantile or coverage probability has been calculated.

References: [effective-degrees-of-freedom](records/effective-degrees-of-freedom.md).

## frequency-conversion: Cyclic to angular frequency

Inputs: `{"frequency_Hz": 10}`

- **angular_rate:** 62.8318530718 rad/s

Assumptions: A defined periodic cycle.

Limits: Does not infer frequency from an experimental signal.

References: [angular-frequency-unit](records/angular-frequency-unit.md).

## report-with-k: Report the chosen factor without inventing probability

Inputs: `{"standard_uncertainty_mm": 0.224, "chosen_k": 2}`

- **expanded_mm:** 0.448 mm

Assumptions: k=2 is explicitly supplied.

Limits: No probability claim is assigned solely from k.

References: [expanded-uncertainty](records/expanded-uncertainty.md), [uncertainty-reporting](records/uncertainty-reporting.md).
