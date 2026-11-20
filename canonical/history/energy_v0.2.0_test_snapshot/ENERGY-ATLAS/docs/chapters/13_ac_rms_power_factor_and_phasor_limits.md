# 13. AC, RMS, power factor, and phasor limits

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Alternating current and voltage vary with time. Under sinusoidal steady-state conditions, RMS amplitudes relate to equivalent resistive heating, and phase difference determines real and reactive power. Apparent power is measured in volt-amperes, real power in watts, and reactive power in vars. A power factor of 0.8 means only part of apparent power contributes to average active transfer under the defined sinusoidal model; it does not automatically measure motor mechanical efficiency. Inductive and capacitive loads exchange field energy with the source. Nonsinusoidal waveforms contain harmonics, making simple single-angle formulas insufficient. The direction of reactive power and whether current leads or lags must be declared.

## Fundamental relationship, symbols and SI dimensions

`Single-phase sinusoidal: S=V_rms I_rms; P=S cosφ; Q=S sinφ; P²+Q²=S².`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The average of v(t)i(t) over one sinusoidal period gives Vrms Irms cosφ after product-to-sum identities remove a zero-mean double-frequency term. The quadrature component is convention-dependent, so a signed Q requires a stated reactive reference. Three-phase balanced systems sum the three phase powers and simplify to sqrt(3) Vline Iline pf; this fails for arbitrary unbalanced conditions.

## Reconstruct the example without external AI

A 230 V RMS circuit draws 10 A at power factor 0.8. Compute apparent power 2300 VA, real power 1840 W and |reactive| 1380 var. Describe what additional waveforms are needed for a distorted electronic load.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not use a phase-angle power factor formula to estimate harmonic-rich loads without additional analysis. A high pf is not equivalent to high energy efficiency or improved power-system reliability.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
