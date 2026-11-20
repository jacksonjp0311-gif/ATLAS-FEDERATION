# 64. Uncertainty covariance and reliable scientific conclusions

**Theme:** Experimental metrology · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

The numerical precision of a formula is not the uncertainty of the physical measurement. Every instrument result has calibration, sampling and model uncertainty, and those errors may be correlated. When a derived quantity is computed from multiple measurements, the propagation of uncertainties must account for covariance rather than assuming independence. For product z=ab, a first-order propagation includes a cross term. This enables future humans and AI systems to distinguish a physically meaningful improvement from one caused by correlated sensor drift, changed reference standards, or arbitrary rounding.

## Governing relationship and dimensional conventions

`For z=ab: u_z²≈b²u_a²+a²u_b²+2ab Cov(a,b), under local linear approximation and valid input covariance.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

A Taylor expansion of f(a,b) around the measured means gives perturbation delta z≈(partial f/partial a)delta a+(partial f/partial b)delta b. Taking variance produces the sum of squared derivative terms plus the covariance cross term. For multiplication the derivatives are b and a. A covariance matrix must be positive semidefinite, which in the two-variable case requires |cov|≤u_a u_b. The code explicitly rejects inconsistent covariances instead of returning an invented uncertainty.

## Original worked investigation

Take hypothetical a=2±0.1 and b=3±0.2 with covariance zero. Compute z=6 and u_z=sqrt((3×0.1)²+(2×0.2)²)=0.5. Then add a positive covariance 0.015 and compare. Treat the numbers as mathematical fixtures, not calibrated meter observations.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

First-order propagation can fail for nonlinear models, skewed distributions and large relative error. Incomplete provenance of input calibration makes any statistical conclusion provisional.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement)
- [NIST/CODATA 2022 recommended constants, 2025 paper](https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
