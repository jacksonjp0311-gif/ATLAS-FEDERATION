# 3. Thermodynamic state and the first law

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Internal energy is a state function: its change depends on initial and final thermodynamic states, not the specific path. Heat and work are process-dependent transfers, not substances stored inside matter. A closed system excludes mass crossing its boundary; open systems require mass-flow enthalpy and kinetic and potential energy terms. The choice of sign convention must be explicit. We use heat into the system as positive and work done by the system as positive. Real engines often cycle through phases where pressure, temperature and composition vary; an ideal gas approximation applies only under conditions for which its constitutive law is adequate. State changes can be represented mathematically but actual thermodynamic properties require reliable material data.

## Fundamental relationship, symbols and SI dimensions

`ΔU = Q − W (closed system); W_reversible = ∫P dV; ideal gas PV=nRT.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The first law integrates energy conservation and assigns heat and work signs. For a reversible isothermal ideal gas, U depends only on T; therefore ΔU=0, so heat received equals the work delivered. Integrating P=nRT/V between V1 and V2 gives W=nRT ln(V2/V1). This result cannot be transferred to irreversible gas expansion against a finite external pressure without modeling the actual process path.

## Reconstruct the example without external AI

Expand one mole of ideal gas reversibly from 0.01 m³ to 0.02 m³ at 300 K. Calculate work by hand using nRT ln 2, then compare with the reversible_ideal_gas_work reference. List how the calculation changes when gas deviates from ideal behavior.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A temperature reading does not determine the internal energy of arbitrary material without heat-capacity, phase and composition information. Reversible work is an upper-limit idealization for a given process, not a promise about real devices.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
