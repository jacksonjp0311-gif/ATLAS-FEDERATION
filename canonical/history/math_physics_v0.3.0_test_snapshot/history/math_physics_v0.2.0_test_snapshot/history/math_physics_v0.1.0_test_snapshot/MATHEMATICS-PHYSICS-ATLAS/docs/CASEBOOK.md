# Mathematics & Physics v0.1.0 — Original Constructed Casebook

**Evidence label:** 22 project-authored finite examples. These are not experimentally measured physics or an AI performance benchmark. Reproduce with `python -m math_physics_atlas` and independent arithmetic.

## Case 01: Exact rational 2x2 solution

**Domain:** Unique square linear system. **Passed original program check:** True.

```json
{
  "solution_fractions": [
    "2",
    "1"
  ],
  "solution_floats": [
    2.0,
    1.0
  ],
  "exact_residual_zero": true,
  "scope": "unique square rational linear system, not general overdetermined fitting"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 02: Matrix multiplication

**Domain:** Linear maps only; input dimensions matter. **Passed original program check:** True.

```json
[
  [
    11.0
  ]
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 03: Orthogonal projection

**Domain:** Euclidean inner product. **Passed original program check:** True.

```json
{
  "projected": [
    3.0,
    0.0
  ],
  "perpendicular_residual": [
    0.0,
    4.0
  ],
  "coefficient": 3.0,
  "orthogonality_residual": 0.0
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 04: Least squares straight line

**Domain:** Full column rank, normal equations only. **Passed original program check:** True.

```json
{
  "parameters": [
    1.0,
    2.0
  ],
  "squared_residual": 0.0,
  "normal_equation_residual": [
    0.0,
    0.0
  ],
  "limitations": [
    "Normal equations square the condition number; use stable QR/SVD on real data",
    "No physical model or independent fitted dataset verified"
  ]
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 05: Polynomial derivative

**Domain:** Power rule for polynomials. **Passed original program check:** True.

```json
[
  3.0,
  8.0
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 06: Central finite difference

**Domain:** Discretization and rounding error. **Passed original program check:** True.

```json
4.000000000004
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 07: Exact polynomial integral

**Domain:** Antiderivative formula. **Passed original program check:** True.

```json
9.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 08: Simpson cubic integral

**Domain:** Uniform even intervals; polynomials of degree up to three. **Passed original program check:** True.

```json
4.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 09: Exponential ODE

**Domain:** Constant coefficient scalar ODE. **Passed original program check:** True.

```json
0.7357588823428847
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 10: RK4 ODE convergence

**Domain:** Finite step stability not proven for arbitrary ODEs. **Passed original program check:** True.

```json
{
  "numerical_y": 0.6065306597142194,
  "analytic_reference": 0.6065306597126334,
  "steps": 100,
  "scope": "scalar linear yprime=ay+b with constant a,b, no general ODE guarantees"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 11: Parseval DFT identity

**Domain:** Finite discrete transform with specified normalization. **Passed original program check:** True.

```json
{
  "time_energy": 2.0,
  "frequency_energy": 2.0,
  "scope": "Parseval energy, unnormalized forward DFT, no physical sampling or aliasing assessment"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 12: One bit entropy

**Domain:** Shannon discrete probabilities, not physical disorder. **Passed original program check:** True.

```json
1.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 13: Bayesian evidence update

**Domain:** User-chosen likelihoods, no true outcome inference. **Passed original program check:** True.

```json
{
  "posterior_H1": 0.9,
  "evidence_probability": 0.5,
  "scope": "chosen prior and likelihood, not real event validation"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 14: Binomial count

**Domain:** Independent identical Bernoulli trials. **Passed original program check:** True.

```json
0.5
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 15: Stable softmax

**Domain:** Probability transform, not calibrated model confidence. **Passed original program check:** True.

```json
[
  0.5,
  0.5
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 16: Quadratic gradient descent

**Domain:** Strongly convex strictly diagonal dominant Hessian. **Passed original program check:** True.

```json
{
  "solution": [
    1.0,
    2.0
  ],
  "objective": -5.0,
  "gradient_norm": 0.0,
  "scope": "strictly diagonally dominant symmetric positive quadratic only; other objectives need separate solvers"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 17: Constant acceleration kinematics

**Domain:** One dimensional classical motion. **Passed original program check:** True.

```json
{
  "position_m": 12.0,
  "velocity_m_s": 7.0,
  "scope": "one-dimensional constant acceleration in chosen inertial frame; no air drag or relativistic correction"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 18: Spring potential energy

**Domain:** Lossless linear spring within elastic range. **Passed original program check:** True.

```json
{
  "energy_J": 0.5,
  "angular_frequency_rad_s": 2.0,
  "scope": "ideal linear lossless spring, no forced/driven dynamics, validated material stress or safety"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 19: RC exponential decay

**Domain:** Ideal components, no hardware approval. **Passed original program check:** True.

```json
{
  "voltage_V": 3.6787944117144233,
  "time_constant_s": 1.0,
  "scope": "ideal RC discharge, lumped model, no actual wiring/voltage safety approval"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 20: Photon energy

**Domain:** Vacuum photon, not a measured absorption spectrum. **Passed original program check:** True.

```json
{
  "energy_J": 3.972891714297857e-19,
  "energy_eV": 2.479683968664005,
  "scope": "single photon in vacuum; not a particular material absorption spectrum"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 21: Quantum Born probabilities

**Domain:** Abstract normalized two-level state. **Passed original program check:** True.

```json
{
  "probabilities": [
    0.5,
    0.5
  ],
  "original_norm_squared": 2.0,
  "scope": "finite dimensional pure state Born rule, no claim of quantum computer or measurement"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 22: Product uncertainty

**Domain:** Linear error propagation with zero covariance. **Passed original program check:** True.

```json
{
  "value": 6.0,
  "standard_uncertainty": 0.5,
  "scope": "first-order uncertainty approximation with caller supplied covariance, no calibrated measurements"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

