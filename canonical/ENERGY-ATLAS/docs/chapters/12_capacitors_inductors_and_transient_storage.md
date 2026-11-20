# 12. Capacitors, inductors, and transient storage

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Capacitors store energy in electric fields; inductors store energy in magnetic fields. Their constitutive laws connect voltage/current to changes over time. In a simple resistor-capacitor discharge, the voltage falls exponentially with time constant RC. In an inductor, an abrupt current change requires a large induced voltage according to the lumped ideal model, which can cause dangerous switching transients in real equipment. Stored field energy is not the same as delivered energy after conversion losses. Ideal linear component equations neglect parasitic resistance, dielectric absorption, leakage, saturation and breakdown. An engineering energy library must preserve the limitations of a lumped approximation.

## Fundamental relationship, symbols and SI dimensions

`E_C=½CV²; E_L=½LI²; i_C=C dv/dt; v_L=L di/dt; V_RC(t)=V0 e^(−t/RC).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For RC discharge, charge balance gives C dV/dt=−V/R. Separating variables yields exponential voltage and quadratic decay of stored energy. A real capacitor may lose usable energy through series resistance or internal leakage; applying the ideal formula beyond rated voltage can cause component failure. Energy can be conserved while being transformed into resistor heat.

## Reconstruct the example without external AI

A 1 F capacitor at 10 V stores 50 J. Through a 1 Ω resistor, one time constant is 1 second, and the remaining voltage is 10/e V. Derive how much energy has dissipated by that time.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

An RC time constant is not a battery self-discharge law. Stored energy in a capacitor can be small despite high peak power delivery; never confuse power density and energy density.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
