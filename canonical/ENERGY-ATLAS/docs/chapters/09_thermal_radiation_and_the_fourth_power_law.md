# 9. Thermal radiation and the fourth-power law

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

All bodies above absolute zero exchange electromagnetic radiation. A blackbody has an ideal radiative exitance proportional to the fourth power of absolute temperature. Real surfaces have emissivity and wavelength-dependent behavior; geometry introduces view factors, multiple reflections and participating media. A simple net exchange between a gray surface and a large isothermal surrounding environment is epsilon sigma A(T_surface⁴−T_surroundings⁴). That expression is a controlled approximation, not a universal radiative transfer solution. At high temperatures radiation can dominate thermal losses, which makes a linear-temperature approximation unreliable over large differences.

## Fundamental relationship, symbols and SI dimensions

`Qdot_rad≈εσA(T_s⁴−T_env⁴), 0≤ε≤1; σ≈5.670374419×10^-8 W·m^-2·K^-4.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Stefan–Boltzmann integration of ideal blackbody radiation gives total emitted flux σT⁴. Subtracting an idealized surrounding incident flux gives a net rate. The factor ε is a gray-body approximation; a real spectral emissivity could require integration over wavelength and angles. SI defining constants make the exact derived value of sigma calculable, though the decimal representation is rounded in this code.

## Reconstruct the example without external AI

Calculate the ideal net rate from 400 K to 300 K over one square metre with emissivity one. Reverse temperatures and verify the sign changes but magnitude stays equal. Then explain why changing view factor or emissivity affects a real enclosure.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Use kelvin, not degrees Celsius, under a fourth power. A net flux estimate does not prove safe material temperatures or fire resistance.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
