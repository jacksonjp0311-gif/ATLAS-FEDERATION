# 58. Fuel-backed power: chemistry, exhaust and uncertainty

**Domain:** Energy conversion and public health. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Combustion fuels carry chemical energy. A generator converts some of that input into electrical energy and rejects the rest as heat, acoustic energy and other losses. The conversion factor depends on load, fuel composition, temperature, maintenance and the actual engine. A fuel volume is not a delivered-electricity measurement. Fuel-backed generation also introduces potentially fatal carbon monoxide exposure. Scientific preservation must retain this safety fact alongside energy conversion equations, because a survivor can otherwise follow correct arithmetic into a lethal application.

## Formula, units and preconditions

`E_electric = η_e E_chemical. Chemical-fuel budget after an interval: E_fuel,next=E_fuel,current−E_electric/η_e. Example chemical input 10 kWh × 0.3 = 3 kWh electric.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

For an energy-only ledger, electrical output cannot exceed stipulated rated output, chemical fuel energy multiplied by conversion efficiency, or the deficit being addressed. Conservation then includes both useful electrical output and conversion losses. This does not prove an engine can start, deliver rated power under stress, maintain exhaust control or meet emissions rules. Where a fuel source has unknown composition, its lower heating value must be recorded as an uncertain input, not silently replaced with a universal constant.

## Reconstruct by hand and compare against code

Assume 10 kWh of chemical fuel input and a 30% electrical conversion fraction: at most 3 kWh becomes electricity under the stated model, while 7 kWh is rejected as heat and other losses. If the requested backup output is 4 kWh, record 1 kWh unmet even if the source can run continuously. Do not turn this arithmetic into an operating procedure.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

CO accumulation depends on ventilation, wind, leaks and building pathways; this chapter does not simulate gas dispersion. Grid backfeed, fuel ignition, exhaust and engine controls are external physical safety questions.

## Life-safety and professional boundary

CDC guidance warns that portable generators and combustion equipment must never be used inside or near a home. This library provides no instructions for unsafe exhaust routing, backfeeding or engine modifications. Official emergency and qualified electrical instructions prevail.

## Source provenance (links only)

- **U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages** — https://www.cdc.gov/carbon-monoxide/about/index.html; inspected portion: Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design
- **U.S. DOE, Solar and Resilience Basics** — https://www.energy.gov/cmei/systems/solar-and-resilience-basics; inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
