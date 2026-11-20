# 47. Fuel-backed generation: conservation, carbon monoxide and backfeed

**Area:** Thermal Resilience · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Fuel-powered generation can provide energy during renewable shortages, but it introduces combustion gases, fire, noise, fuel quality, maintenance and electrical backfeed hazards. The first calculation relates fuel volume to chemical energy and assumed electrical conversion efficiency. That arithmetic cannot tell whether a generator is safely installed, properly isolated from the utility, ventilated, maintained or able to provide stable AC power under real load. CDC guidance warns that carbon monoxide from portable generators can cause fatal poisoning in enclosed or nearby spaces. A research reference should preserve these safety boundaries as part of the physics, not present an incomplete fuel-to-kWh calculation as a practical operating procedure.

## Equation, symbols and dimensional units

`E_chemical[kWh]=fuel_volume[L]*heating_value[MJ/L]/3.6; E_electric=E_chemical*eta_electric.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

Heating value describes the chemical energy under a stated lower/upper heating value convention, not a measured device output. The electrical efficiency depends on operating point, equipment and environment. The difference between input and output includes multiple heat, friction, exhaust and auxiliary losses, and cannot be assigned to a single mechanism without additional measurements. Dividing by 3.6 converts MJ to kWh. The model requires caller-supplied values so it does not fabricate a current fuel specification or generator efficiency.

## Hand reconstruction and independent calculation

Invent fuel volume 5 L, heating value 35 MJ/L, and electrical efficiency 25%. Compute 48.61 kWh chemical input and 12.15 kWh hypothetical electricity. Explain why this does not authorize connecting the generator to a building or assess carbon monoxide risk; actual fuel grade, rated capacity, safe placement and transfer equipment remain unverified.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Never infer a safe operating duration from fuel volume alone; startup, transient loading, engine condition and hazardous emissions are missing. Improper utility backfeeding can injure others even when local voltage appears acceptable.

## Life safety and operational boundary

Never use generators or fuel burners indoors or near openings; CDC guidance describes required outdoor separation and CO alarms. Electrical interconnection requires approved transfer equipment and qualified installation.

## Source navigation and preservation debt

- **U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages:** https://www.cdc.gov/carbon-monoxide/about/index.html — Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design
- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
