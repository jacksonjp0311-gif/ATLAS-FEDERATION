# 38. Multi-interval microgrid energy accounting

**Area:** Survival Systems · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A microgrid is a bounded set of loads and resources that may operate connected to a larger electrical network or islanded under properly designed controls and protection. In a survival context the first numerical study is a time-resolved energy ledger: generation, load, stored energy, conversion losses, curtailment, imports and unserved demand. That accounting reveals when an assumed resource portfolio is insufficient. It does not model AC voltage, grid-forming controls, transfer-switch correctness, frequency regulation, neutral/ground bonding, relay coordination, or inverter fault behavior. The DOE resilience reference explicitly distinguishes ordinary grid-dependent solar from a properly configured independent solar-plus-storage system. Passing an energy ledger cannot override that requirement.

## Equation, symbols and dimensional units

`For interval i: (generation_i + imports_i - served_i - curtailed_i)*Delta t_i = Delta storage_i + conversion_loss_i, with power in kW and time in hours.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

This is conservation of energy across the declared modeled boundary. Renewable power first serves a stipulated load, then can charge a storage abstraction within its charge-power and energy bounds. A deficit can discharge storage subject to a discharge-power ceiling and efficiency, otherwise it is recorded as unmet load or a hypothetical grid import. Summing interval residuals tests internal bookkeeping. It does not establish that grid-connected power is available unless the scenario explicitly says so, or that the storage hardware can perform the requested duty. To call a field installation resilient would require data on faults, islanding transition, protection, startup, equipment ratings and controls.

## Hand reconstruction and independent calculation

Run a three-hour constructed scenario: solar 4 kW/0/0, load 2/3/3 kW, initial battery 1 kWh, capacity 4 kWh, charging/discharging maxima 2 kW with efficiencies 0.9. Calculate charge, curtailment, discharge, remaining load and conversion losses for each hour. Verify the total ledger residual is near zero, and inspect the nonzero unmet demand rather than renaming it a successful supply.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

The model is energy-only. It assumes an ideal available grid whenever flagged and no dangerous wiring procedure. A single weather trace is not a statistical resilience guarantee, nor is a battery represented by a single exact state of charge physically complete.

## Life safety and operational boundary

Never energize or island a real electrical installation from the model output. Grid interconnection, transfer switching and protections require qualified engineering and applicable codes.

## Source navigation and preservation debt

- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **DOE Energy Storage Strategy and Roadmap:** https://www.energy.gov/oe/energy-storage-strategy-and-roadmap — Energy storage technology and deployment; cross-technology requirements

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
