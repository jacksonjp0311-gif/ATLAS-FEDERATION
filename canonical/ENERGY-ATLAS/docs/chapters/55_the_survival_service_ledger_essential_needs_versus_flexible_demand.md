# 55. The survival-service ledger: essential needs versus flexible demand

**Domain:** Survival service systems. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

A grid failure may leave more demand than available energy. The first question then becomes: which defined services can be sustained with measurable evidence? This research reference separates *stipulated* critical and discretionary energy demand, renewable generation, storage reserves and fuel-backed generation, then reports unserved portions explicitly. The critical/flexible labels are mathematical inputs chosen by an external planner; the algorithm does not decide ethical or medical priorities. Even a service marked “served” in the energy ledger may fail from incompatible power quality, fuel hazards, missing equipment or a dangerous installation.

## Formula, units and preconditions

`For each interval: E_demand=E_critical+E_flexible; E_in=E_renewable+E_fuel_chemical−ΔE_stored; E_out=E_served+E_curtailment+E_conversion_loss; E_in−E_out=0 within numeric tolerance.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The model assigns usable renewable energy first, then energy above the battery reserve subject to charge/discharge limits, then a limited backup fuel budget. It prioritizes critical demand in reporting delivery, and counts unmet energy instead of clipping the entire request to the available supply. The chemical input to the backup is converted using a stipulated electrical efficiency, never silently treated as electric kilowatt-hours. Chronological storage state links all intervals, preventing the same stored joule from being spent twice. An independent oracle should implement the recurrence separately and check conservation.

## Reconstruct by hand and compare against code

A constructed 2-hour interval has a 1 kW critical load and 2 kW flexible load, with no solar input and only a 1 kW discharge limit. The ledger can deliver at most 2 kWh from that discharge path over the interval, potentially leaving part of the flexible demand unserved. Repeat with finite fuel and a later surplus-renewable interval to observe reserve recovery and conversion losses.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

This is not dynamic electrical dispatch. It omits AC voltage and frequency, inverter efficiency variation, surge current, startup sequencing, critical minimum duty cycle and hard service dependencies. It does not estimate real-world outage probability.

## Life-safety and professional boundary

Do not use calculated priority allocations to certify medical support, public utility resilience or safe electrical installation. Qualified operators and independent measurements are required for critical services.

## Source provenance (links only)

- **Sandia National Laboratories, Microgrid Design Toolkit** — https://energy.sandia.gov/programs/electric-grid/advanced-microgrids/microgrid-design-toolkit/; inspected portion: Official description of early-stage multiobjective microgrid design, cost-performance-reliability tradeoffs
- **U.S. DOE, Solar and Resilience Basics** — https://www.energy.gov/cmei/systems/solar-and-resilience-basics; inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **DOE Energy Storage Strategy and Roadmap** — https://www.energy.gov/oe/energy-storage-strategy-and-roadmap; inspected portion: Energy storage technology and deployment; cross-technology requirements

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
