# 17. Wind turbines, aerodynamic power, and Betz’s ideal limit

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

The kinetic energy flux through a rotor-swept area is proportional to density, area and the cube of wind speed. A turbine can extract only part of that flux; the ideal steady actuator-disk model gives the Betz maximum power coefficient 16/27. Real machines also obey cut-in, rated, cut-out and fatigue limits. Wind fields vary with height, terrain, atmospheric stability and turbulence. Power curves measured at standard conditions cannot simply be multiplied by a regional average wind speed; because power scales with the cube of speed before rating, the distribution matters. A full resource assessment needs hub-height wind time series, air density, array losses and electrical conversion data.

## Fundamental relationship, symbols and SI dimensions

`P_wind=½ρAv³; P_rotor=CpP_wind, 0≤Cp≤16/27 in the ideal actuator-disk model.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For a mass flow of air moving at velocity v, kinetic energy per mass is v²/2 and volume flow scales with Av, giving kinetic power ρAv³/2. Betz's result balances upstream and downstream momentum across a slowed ideal stream tube; extracting all energy would halt the flow and eliminate throughput. The upper bound does not apply to arbitrary non-actuator devices or justify real turbine efficiency measurements.

## Reconstruct the example without external AI

For air density 1.2 kg/m³, area 10 m², speed 10 m/s and Cp=0.4, compute 2400 W. Double wind speed and explain the eightfold ideal pre-rated power increase. Then explain why a real turbine would reach rated power and eventually shut down.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A power coefficient above 16/27 should trigger model review, not be reported as evidence of revolutionary wind physics. Real coefficients and measurement boundaries must be distinguished.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE How Do Wind Turbines Work?](https://www.energy.gov/cmei/systems/how-do-wind-turbines-work) — inspected: Wind turbines use aerodynamic lift/drag to rotate generators; resource and designs vary
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
