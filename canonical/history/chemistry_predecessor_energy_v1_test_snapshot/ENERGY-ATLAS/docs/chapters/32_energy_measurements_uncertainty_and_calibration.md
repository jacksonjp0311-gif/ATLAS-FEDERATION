# 32. Energy measurements, uncertainty, and calibration

**Area:** Metrology. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A scientific energy measurement begins by defining the measurand: electrical energy delivered to a load, chemical energy content of fuel, net heat transfer, or whole-facility electricity. Instruments have calibration uncertainty, resolution, drift, bandwidth, phase error and sampling limits. Measuring voltage and current separately does not always recover instantaneous real power, particularly with phase shift or distorted waveforms; a proper power analyzer integrates their product with synchronized sampling. Measurement uncertainties can be correlated, making simple independent-root-sum-of-squares formulas inadequate. A reconstructible result preserves device, calibration record, measurement interval, reference conditions and uncertainty propagation.

## Fundamental relationship, symbols and SI dimensions

`E≈Σ_i (P_i+P_(i+1))/2 × Δt_i for trapezoidal interpolation; u_y²≈Σ_i(∂f/∂x_i)²u_i² plus covariance terms.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Trapezoidal integration is exact for linear power variation between samples, but real transients between measurement points can be missed. Error propagation follows first-order linearization of the measurement model around estimates; it is not automatically valid for large nonlinear or non-Gaussian uncertainty. A robust study includes a second measurement method or known calibration source where possible.

## Reconstruct the example without external AI

Integrate three synthetic samples (t=0,10,20 s; P=10,10,20 W), giving 250 J by trapezoidal rule. Describe a pulse between samples that this calculation would completely miss. State an appropriate sampling or anti-aliasing plan.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A numerical result with many decimal places does not prove high physical accuracy. Calibration and timing traceability determine the defensible significant figures.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
