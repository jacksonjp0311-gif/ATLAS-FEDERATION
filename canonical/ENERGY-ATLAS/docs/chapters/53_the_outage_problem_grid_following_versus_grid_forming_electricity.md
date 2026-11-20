# 53. The outage problem: grid-following versus grid-forming electricity

**Domain:** Resilient grids. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Many grid-connected solar inverters are designed to cease energizing an electrical grid during utility outages. This anti-islanding response is a safety feature, not a contradiction of the photovoltaic effect. A standalone microgrid needs appropriate islanding, grid-forming capability, storage, compatible load protection and safe reconnection, with dynamically stable voltage and frequency. Solar panels alone do not guarantee backup power. This chapter preserves this fundamental distinction because a post-disaster reader could otherwise infer a dangerous ability to energize wiring simply from a PV nameplate.

## Formula, units and preconditions

`At a stipulated instant, real-power supply balance satisfies P_generation + P_storage_discharge + P_grid_import = P_load + P_storage_charge + P_losses + P_curtailment. Dynamic feasibility requires additional equations and controls.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The balance is a necessary condition on accounting boundaries; it is not a sufficient condition for system stability. A static equality can hold while frequency, voltage, fault current, equipment ratings or synchronization are unacceptable. Grid-forming control requires a validated dynamical model and interconnection protections. The published DOE resilience overview distinguishes ordinary grid-tied PV shutdown from properly configured solar-plus-storage with islanding operation. Sandia's microgrid design toolkit provides decision-support concepts but does not independently verify any particular home-built installation.

## Reconstruct by hand and compare against code

Take a hypothetical 3 kW critical load and a 2 kW solar output at noon. The remaining 1 kW must come from storage, compatible backup or grid imports. If the utility is down and islanding hardware is absent, the 2 kW is not automatically usable. An energy ledger can quantify the shortage but cannot infer authorization to operate the equipment.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Voltage support, black start, inverter capabilities, grounding, interconnection requirements and safe isolation are outside this calculation. An equal power total can coexist with an unstable or unsafe island.

## Life-safety and professional boundary

Do not attempt ad-hoc grid backfeeding, modification of anti-islanding protection, or live electrical reconnection. This is an educational overview, not an installation procedure.

## Source provenance (links only)

- **U.S. DOE, Solar and Resilience Basics** — https://www.energy.gov/cmei/systems/solar-and-resilience-basics; inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **Sandia National Laboratories, Microgrid Design Toolkit** — https://energy.sandia.gov/programs/electric-grid/advanced-microgrids/microgrid-design-toolkit/; inspected portion: Official description of early-stage multiobjective microgrid design, cost-performance-reliability tradeoffs
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics** — https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics; inspected portion: Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
