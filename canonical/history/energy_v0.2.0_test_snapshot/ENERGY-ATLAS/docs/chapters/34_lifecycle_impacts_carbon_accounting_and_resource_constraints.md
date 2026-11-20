# 34. Lifecycle impacts, carbon accounting, and resource constraints

**Area:** Metrology. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Energy technologies have impacts across materials extraction, fabrication, construction, operation, fuel supply, maintenance and end of life. Direct plant-stack emissions are not the same as lifecycle greenhouse-gas intensity. A battery or solar panel may have zero direct combustion emissions during operation but embodied manufacturing impacts, land/water demand and recycling constraints. Assessments must state functional unit such as grams CO2-equivalent per delivered kWh, system boundary, grid mix, recycling allocation and time horizon. Numeric environmental comparisons should come from harmonized datasets, not invented generic constants. Economic and climate objectives can conflict with local ecological or social constraints.

## Fundamental relationship, symbols and SI dimensions

`I_lifecycle=(Σ stage emissions_kgCO2e)/(Σ life delivered kWh), under documented boundary and attribution method.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The ratio is an inventory quotient, not a universal physical property of a technology. Its denominator can vary with device life, degradation, climate and curtailment; the numerator can vary with the electricity mix used in manufacture and accounting conventions. Independent lifecycle evidence requires audited upstream inputs and sensitivity analysis. An energy-only model cannot validate greenhouse-gas emissions or social effects.

## Reconstruct the example without external AI

Use a constructed device with 1000 kgCO2e embodied impact and 10000 kWh lifetime delivery, yielding 0.1 kgCO2e/kWh. Halve its lifetime production and demonstrate that intensity doubles. Explain why this example is not a measured technology result.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not assign a zero lifecycle impact to a zero-stack-emission resource, or confuse different CO2-equivalence time horizons and allocation rules.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
