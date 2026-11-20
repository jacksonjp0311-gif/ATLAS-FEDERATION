# 26. Thermal, gravitational, mechanical, and pumped storage

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Electricity can be stored indirectly as gravitational potential, kinetic energy, compressed fluid, phase-change heat or chemical energy. Each mechanism has a different energy density, response time, efficiency, site requirement and durability. Pumped hydro returns water downhill after using electricity to pump it upward, with a round-trip loss. Flywheel energy grows with the square of angular speed, but mechanical stress and containment impose limits. Sensible thermal storage uses heat capacity; phase-change storage adds latent heat at appropriate temperatures. Compressed-air storage interacts with thermodynamics of compression and expansion, so a pressure-only calculation is inadequate. Selecting a technology requires a service definition: seconds of fast response, days of shifting, industrial process heat or seasonal energy supply.

## Fundamental relationship, symbols and SI dimensions

`E_gravity=mgh; E_flywheel=½Iω²; E_sensible≈mcΔT; round-trip η=E_delivered/E_supplied under matched interfaces.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Each expression follows from a work integral under a specified physical model: gravitational work over height, rotational kinetic energy from torque and angular acceleration, and heat capacity from enthalpy change. A real storage system includes friction, converter losses, heat leaks and hardware limits. Stored energy is not automatically recoverable as electricity at a given rated power.

## Reconstruct the example without external AI

For a mass of 1000 kg raised 10 m, compute gravitational storage as 98.1 kJ. Compare with 1 kWh and state why a practical pumped-storage facility requires substantial water flow, head and turbine/generator systems.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Never interpret mechanical storage formulas as instructions to construct high-speed rotors or pressurized vessels. Safe containment, fatigue and fault analysis are specialized fields.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [DOE How Hydropower Works](https://www.energy.gov/cmei/water/how-hydropower-works) — inspected: Flow and head determine hydraulic resource and conversion stages

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
