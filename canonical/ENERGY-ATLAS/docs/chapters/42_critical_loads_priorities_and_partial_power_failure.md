# 42. Critical loads, priorities, and partial-power failure

**Area:** Resilience · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

During disruptions, energy allocation becomes a governance problem as well as a mathematical one. Some devices can tolerate reduced power; others have minimum operation, start-up and uninterrupted continuity requirements that cannot be represented by simply serving half their requested kilowatts. An educational priority algorithm can demonstrate tradeoffs, but it cannot choose ethically correct allocations or certify life-sustaining equipment. The reference asks every service to declare a requested power, minimum acceptable power under a qualified contract, and a group priority; if a minimum is not met, the algorithm flags it. It does not assume that allocating 80% power provides 80% service. A critical service inventory must have accountable operators, replacement equipment and independent tests before use.

## Equation, symbols and dimensional units

`Per interval: 0<=P_served,j<=P_requested,j and sum_j P_served,j<=P_available. Minimum delivered power is a separate boolean constraint P_served,j >= P_min,j, not implied by energy balance.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

A mathematical scheduler can allocate by priority and scale within a tied group to satisfy a power cap. That policy ensures only an arithmetic total and deterministic order, not safety or fairness. If a water pump is rated for a fixed minimum voltage, scaling its kilowatts proportionally may not operate it; if medical equipment cannot tolerate interruption, a nonzero allocation may still be a failure. Avoid modeling a safety-critical device with a continuous fraction of utility unless independent behavior data support it.

## Hand reconstruction and independent calculation

Three invented services request water pumping 0.5 kW (priority 1), lighting 0.2 kW (priority 2) and thermal equipment 1.8 kW (priority 2). Only 1 kW is available. Compute the priority-first allocation, inspect the unmet energy and flags for the declared minimum service powers. Then rerun with 3 kW and compare; no answer should claim safe clinical or pump operation.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

A policy chosen by code is not human triage authorization. “Priority 1” is a user-assigned label, not a medical or moral rule. Startup currents, equipment protection and minimum continuous duty are not modeled.

## Life safety and operational boundary

Never rely on this fractional allocation for life-critical equipment; use professionally assessed backup and emergency procedures instead.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages:** https://www.cdc.gov/carbon-monoxide/about/index.html — Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
