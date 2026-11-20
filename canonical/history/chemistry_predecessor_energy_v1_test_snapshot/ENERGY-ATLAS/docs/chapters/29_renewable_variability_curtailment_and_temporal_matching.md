# 29. Renewable variability, curtailment, and temporal matching

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Wind and solar output vary with weather, time and geographic conditions. An average capacity factor cannot reveal whether generation meets load at the right hours. Time correlation between supply and demand, storage duration, interconnection limits and reserve requirements determine reliability. Curtailment means available renewable output is not used because of grid constraints, market signals or equipment conditions; it is not evidence the sunlight or wind contained no energy. A strong analytical library preserves time-series provenance, sampling rate, missing intervals, calendar/time zones, asset rating and measurement uncertainty. Aggregating all hours into one annual energy total can conceal damaging outages.

## Fundamental relationship, symbols and SI dimensions

`Net load(t)=Load(t)−VariableGeneration(t); E_deficit=∫max(0,NetLoad(t))dt under a declared time series and no storage.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The max operator separates deficit periods from surplus. Integrating the signed net load can cancel surpluses and deficits that occur at different times, implying false instantaneous feasibility. Storage can shift some energy but incurs losses, finite duration and finite power. Different weather years can lead to different adequacy outcomes even if annual mean production is similar.

## Reconstruct the example without external AI

Compare two synthetic hours: renewable output 4 kW then 0, load 2 kW each hour. Total generation equals total demand, but without storage the second hour has 2 kWh unmet. Explain the role of a battery and why a 2 kWh nameplate may not suffice with efficiency losses.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not equate annual net-zero energy with continuous reliability or zero environmental impact. The problem is temporal and spatial matching.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
