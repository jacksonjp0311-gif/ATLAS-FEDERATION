# 35. Resilient power: microgrids, islanding, and critical loads

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Power resilience means preserving essential services despite disruptions. A robust microgrid must identify critical loads, generator and storage operating constraints, fault detection, protection, grid-forming controls, communications, fuel supplies and trained operators. The sequence of safe islanding and reconnection is specific to equipment and utility interconnection rules. A simplified energy budget can estimate whether a hospital's nominal battery stores enough kWh, but cannot guarantee safe operation under high inrush currents, reactive loads, faults or equipment failure. Recovery priorities also depend on human needs, not just objective functions. A survival atlas should teach the distinction between energy planning and legally authorized electrical operations.

## Fundamental relationship, symbols and SI dimensions

`Critical-load energy minimum E_need≈∫P_critical(t)dt; storage usable delivery < nameplate capacity after SOC reserve and conversion losses.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The expression integrates demand, but a real plan must check peak kW, power quality, switching and fault capability. Resilience also requires scenario analysis: cloudy periods, fuel interruption, battery faults and communication loss can be correlated. A design that meets average load may still fail an emergency peak. Service restoration must be supervised by qualified professionals with tested emergency procedures.

## Reconstruct the example without external AI

Construct an emergency schedule with one 500 W critical load for 8 hours: 4 kWh before storage losses. Compare to a nominal 5 kWh battery at 80% usable depth of discharge and 90% discharge efficiency, giving only 3.6 kWh delivered; identify the deficit.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not energize emergency electrical equipment or attempt grid islanding from this manual. Protective coordination, certification and qualified engineering are essential.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
