# 20. Heat engines, Rankine cycles, and combined heat and power

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Thermal power plants convert some heat from combustion, fission, concentrated solar or geothermal processes into mechanical and then electrical work. Real cycles use pumps, turbines, heat exchangers and condensers. The Rankine cycle is a foundational steam-power model; Brayton cycles underpin gas turbines. Cogeneration or combined heat and power (CHP) captures thermal output for useful heating or industrial service, improving total useful-energy utilization without violating heat-engine efficiency limits. Plant efficiency depends on fuel higher or lower heating value, ambient conditions, equipment condition, load and heat-demand matching. Condenser rejection and cooling infrastructure are part of the energy balance.

## Fundamental relationship, symbols and SI dimensions

`η_electric = W_electric/Q_fuel; η_CHP_useful=(W_electric+Q_useful_heat)/Q_fuel; 0≤η≤1 within closed fuel-energy boundary.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For a heat engine, first-law balance partitions heat input into work and rejected heat over a complete cycle. CHP counts only heat that actually serves a validated demand; dumping unwanted low-grade heat does not increase useful efficiency. A plant reporting higher electrical efficiency may still have different fuel boundaries and lower heating value reference. Second-law analysis constrains feasible temperature-limited work extraction.

## Reconstruct the example without external AI

A plant consumes 100 units of fuel energy and produces 30 units electric work, 40 units useful heat, and 30 units other rejection. Calculate electrical efficiency 30% and combined useful efficiency 70%, then identify the necessary heat-customer operating schedule.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not add thermal energy at one temperature to electricity as if both had identical usefulness in exergy or economic value. A CHP figure cannot exceed the physically accounted fuel input without investigating omitted energy sources.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [ENERGY STAR Geothermal Heat Pumps Efficiency Criteria](https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria) — inspected: Definition and rating framework for coefficient of performance; product-specific ratings vary

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
