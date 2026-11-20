# 23. Electrochemical batteries and capacity versus power

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Rechargeable batteries store energy through chemical potentials and convert between electrical and chemical energy through electrochemical reactions. Their nominal capacity is often quoted in ampere-hours or watt-hours, but usable capacity depends on voltage, temperature, discharge rate, age, cell balance and allowed state-of-charge limits. Power capability depends on internal resistance, electrode kinetics, thermal management and protection electronics. A battery with high energy capacity need not provide high short-duration power, and a high-power cell need not provide large total energy. Battery management systems protect cells against overcharge, deep discharge, overcurrent and thermal events; a formula for state of charge is not a substitute for such protection.

## Fundamental relationship, symbols and SI dimensions

`E_stored≈∫V_terminal I dt within stated sign convention; nominal energy ≈ V_nominal×Ah, not exact if voltage varies.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Chemical free-energy differences drive an open-circuit cell potential, while terminal voltage differs under load because of internal losses and polarization. Coulomb counting integrates current but accumulates measurement bias and must be corrected by calibration or independent state estimates. A pack has cell-level safety limits that can bind before the nominal overall energy is exhausted.

## Reconstruct the example without external AI

A nominal 10 V, 100 Ah storage unit is often labeled 1 kWh. Explain why measuring terminal voltage under a varying load is necessary for a better energy estimate, and why 1 kWh capacity does not guarantee that a 2 kW load can be supplied for 30 minutes safely.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not use a simple energy-balance model as battery charging firmware or a safety controller. Chemistry-dependent thermal runaway risks, degradation and BMS limits require separate validated engineering.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
