# 27. Power rating, energy capacity, and capacity factor

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Power capacity states an instantaneous or sustained rate, while energy capacity states how much service can be delivered over time. A 100 kW generator at 50% capacity factor produces half the energy it would produce at continuous full rating over the defined interval, but capacity factor does not equal thermodynamic efficiency. A battery rated at 100 kW and 100 kWh has a nominal one-hour duration at rated power under ideal conversion, yet usable duration depends on efficiency, allowable discharge and temperature. Capacity factors for intermittent sources must be computed over actual hourly generation, not from one favorable period. Outages, dispatch restrictions and curtailment are distinct contributors to lower output.

## Fundamental relationship, symbols and SI dimensions

`Capacity factor CF=E_generated/(P_rated×Δt), 0≤CF≤1 for physical output under the same rating and interval.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The denominator is the hypothetical upper-bound energy if the plant produced nameplate power throughout the period. Actual output integrates instantaneous power. CF is a utilization measure; it does not describe fuel conversion efficiency or operating margins. Comparing technologies requires equivalent measured boundaries and service value, not merely ranking CF.

## Reconstruct the example without external AI

A 100 kW resource delivers 500 kWh during a ten-hour period, so CF=.5. Calculate the same resource's CF if output was curtailed by 100 kWh, and identify whether physical resource, demand or reliability explains the change.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A reported CF above one signals inconsistent rated capacity, measurement scope, time interval or data, rather than a breakthrough in energy conversion.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [EIA Levelized Cost of Electricity Glossary](https://www.eia.gov/tools/glossary/index.php?id=levelized_cost) — inspected: Definition of real levelized cost; project-specific assumptions needed

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
