# 6. Heat capacity, calorimetry, and phase change

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Heating a body requires knowing what its material is, which phase it occupies, and how heat capacity varies with temperature. The approximation Q=mcΔT is useful only where specific heat c is approximately constant and no phase transition occurs. During melting or boiling, latent heat can absorb energy with little temperature change at specified pressure, so a thermometer alone does not measure heat input. Thermochemical databases preserve standard enthalpy, entropy, heat capacities and phase-transition data, but those values depend on pressure, purity and measurement methods. A reconstruction-ready atlas must record source, reference state and uncertainty for every numeric property before using it in an engineering prediction.

## Fundamental relationship, symbols and SI dimensions

`Q≈mc_pΔT at constant pressure when c_p is constant; Q_phase=mL; generally Δh=∫c_p(T)dT + phase terms.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Integrating temperature-dependent heat capacity gives the correct enthalpy change for a single phase under suitable conditions. A simple constant-c calculation is a local approximation to that integral. For a heating curve across a phase boundary, divide the path into sensible-heat and latent-heat intervals. The first law ensures total energy accounting, but the material model determines how input energy changes temperature and phase.

## Reconstruct the example without external AI

Take 1 kg of a hypothetical solid with c=500 J/kg/K, heated by 10 K; compute 5 kJ. Now introduce a phase change with latent heat 50 kJ/kg and explain why adding 50 kJ may not increase temperature.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A material property quoted without source, composition, temperature and pressure is not universally valid. Do not extrapolate a heat-capacity table into chemically reactive or high-pressure regimes without evidence.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
