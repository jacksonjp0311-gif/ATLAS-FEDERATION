# 18. Hydropower, head, and water resources

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Water moving through a height difference can transfer gravitational potential energy to a turbine. Under a simple incompressible steady model, available power scales with density, gravitational acceleration, volumetric flow and head. Turbine-generator efficiency converts hydraulic head into electric output. Real systems have penstock friction, changing reservoir levels, cavitation risk, environmental flow constraints, sediment and regulatory requirements. Pumped storage uses electricity to move water uphill and later recover some energy; it is storage with losses, not a source that creates energy. River hydrology and site surveys matter more than assuming one permanent head and flow.

## Fundamental relationship, symbols and SI dimensions

`P_hydro=ρgQHη; hydraulic power P_available=ρgQH, 0≤η≤1.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Potential energy of mass m at elevation difference H is mgH; mass flow rate is ρQ, yielding power ρgQH. Efficiency accounts for mechanical and electrical conversion within a declared boundary. The formula does not provide environmental suitability or legal authority to alter waterways. Scaling flow in a hypothetical example is simple; predicting real available flow across seasons is not.

## Reconstruct the example without external AI

With water density 1000 kg/m³, flow 1 m³/s, net head 10 m and conversion efficiency 0.8, calculate approximately 78.5 kW. Halve flow and compare, while listing the flow and head surveys a real project would require.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Head and flow cannot be assumed constant from a single measurement. A physically feasible power calculation is not a permit, safety assessment or ecological-impact study.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE How Hydropower Works](https://www.energy.gov/cmei/water/how-hydropower-works) — inspected: Flow and head determine hydraulic resource and conversion stages
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
