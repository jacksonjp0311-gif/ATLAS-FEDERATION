# 16. Photovoltaic effects and semiconductor conversion

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Photovoltaic cells absorb photons in semiconductor junctions, producing charge carriers that a circuit can collect. Only photons within suitable spectral bands and subject to device losses contribute usefully. A module's rated DC output is measured under standard test conditions, not a guarantee of site power. Array output depends on incident plane-of-array irradiance, cell temperature, spectrum, orientation, shading, soiling, wiring and inverter limits. A useful introductory model scales rated power linearly with irradiance and applies a temperature coefficient around a reference 25°C; it deliberately omits low-light nonlinearities and more detailed diode behavior. Real energy forecasting requires weather series and module characterization.

## Fundamental relationship, symbols and SI dimensions

`P_DC≈P_rated(G/1000)(1+γ(T_cell−25°C)) for a specified module, irradiance G in W/m² and gamma in 1/°C.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Electrical output has dimensions voltage times current. Conversion efficiency is electrical output divided by incident optical power under controlled conditions. The linear model is a first-order expansion of rated module performance around calibration conditions, not a fundamental semiconductor theorem. When a temperature correction becomes negative, the approximation is outside its domain; the reference rejects rather than returning negative generated energy.

## Reconstruct the example without external AI

A rated 1000 W DC array at 1000 W/m² and 45°C with coefficient −0.004/°C produces 920 W under the linear model. Compare the result with measured inverter output and list the components omitted.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

No perpetual power exists at zero irradiance. A module rating is not a facility capacity factor, and a published record cell efficiency must not be substituted for a installed-array annual yield.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Solar Photovoltaic Technology Basics](https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics) — inspected: Solar cell, module, arrays, and DC/AC system concept
- [DOE Solar PV Performance and Efficiency Basics](https://www.energy.gov/cmei/systems/solar-photovoltaic-performance-and-efficiency-basics) — inspected: Conversion efficiency, IV curves, temperature and spectral effects
- [Sandia PV Performance Modeling Collaborative: PVWatts](https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/point-value-models/pvwatts/) — inspected: PVWatts basic power/irradiance/temperature point model; versions and low-light rules differ

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
