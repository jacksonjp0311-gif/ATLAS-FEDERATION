# 39. Storage reserve and multi-day autonomy

**Area:** Storage · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Battery capacity is an energy quantity; battery charge and discharge ratings are power quantities. The reserve margin is the stored energy intentionally left unused under a declared policy. A simple autonomy estimate divides usable deliverable stored energy by average daily demand, but realistic batteries have discharge-rate-dependent performance, temperature effects, aging, lower and upper voltage limits, parasitic loads, and protection logic. A stored energy estimate cannot guarantee uninterrupted output because a battery may trip or an inverter may be unavailable. Renewable replenishment and future weather must be represented as a sequence of intervals rather than one average value. Distinguish the lowest state of charge reached during the profile from its ending value.

## Equation, symbols and dimensional units

`E_usable = E_rated*(SOC_initial - SOC_floor)*eta_discharge; days_illustrative=E_usable / E_daily, for E_daily>0.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

Under the idealized definition, extractable useful energy is the decline in modeled stored-energy state multiplied by the discharge path efficiency. This gives an upper bound within the chosen model, not an engineered safe capacity. Charging roundtrip losses must be included separately; the charge path and discharge path efficiencies are not the same input. The model should refuse an initial state of charge below its declared reserve floor and reject efficiencies outside (0,1]. Physical BMS cutoff, state estimation and thermal constraints are deliberately omitted.

## Hand reconstruction and independent calculation

Take a stipulated 10 kWh battery at 75% modeled SOC, a 25% reserve floor and 90% discharge efficiency. The model gives 4.5 kWh deliverable above reserve. If the invented daily load is 2 kWh, the arithmetic produces 2.25 illustrative days with zero generation. Then add a 1 kW inverter ceiling and ask whether a single 2 kW pump is even a feasible load; the original energy-only estimate cannot answer yes.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Nameplate capacity is not necessarily available capacity, and voltage/temperature protection can interrupt service. A battery pack with enough kWh can be unsafe, incompatible or incapable of meeting peak power. No statistical guarantee follows from fixed-weather assumptions.

## Life safety and operational boundary

Battery systems require certified equipment, siting, electrical/fire protections and manufacturer instructions; avoid hazardous improvisation with damaged cells.

## Source navigation and preservation debt

- **DOE Energy Storage Strategy and Roadmap:** https://www.energy.gov/oe/energy-storage-strategy-and-roadmap — Energy storage technology and deployment; cross-technology requirements
- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. EPA, Battery Energy Storage Systems Safety and Incident Response:** https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe — Battery fire response, community planning, relevant standards; no site engineering standard reproduced

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
