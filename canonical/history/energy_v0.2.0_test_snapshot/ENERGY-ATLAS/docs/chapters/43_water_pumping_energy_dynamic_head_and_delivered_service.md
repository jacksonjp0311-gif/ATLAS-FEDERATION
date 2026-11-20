# 43. Water pumping: energy, dynamic head and delivered service

**Area:** Water · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A water service needs both a physical source of water and a means of moving it. The gravitational potential energy of raising a known volume through a height can be reconstructed from density, gravity and elevation change. A real pump's total dynamic head also includes friction and pressure requirements and changes with flow, pipe geometry and pump characteristics. Therefore the basic equation can estimate minimum hydraulic work under a stipulated head, but cannot select a pump or confirm actual flow. Electrical input requires an aggregate efficiency measured at the relevant operating point. Water service must be tracked separately from drinking-water safety: energy to lift or warm water says nothing about microbial or chemical contamination.

## Equation, symbols and dimensional units

`W_hydraulic = rho*g*V*H, joules; E_input=W_hydraulic/eta_pump, where rho is kg/m^3, V is m^3, H is m, g is m/s^2.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

Density times volume gives mass, gravitational acceleration times height gives energy per unit mass. Multiplying yields a joule-dimensional expression. If the required head doubles and all assumptions stay unchanged, ideal work doubles; if efficiency halves, electrical input doubles. But real efficiency may vary with flow and speed. A model declaring a constant efficiency outside its tested envelope may be physically inaccurate. A pump whose peak power exceeds the inverter rating can fail despite a small total Wh requirement.

## Hand reconstruction and independent calculation

Assume 1 m3 of water, 10 m total dynamic head, density 1000 kg/m3 and aggregate efficiency 50%. Compute ideal hydraulic work 98,066.5 J and electrical input 196,133 J = 54.48 Wh. Then explain what site-specific evidence is needed for actual head, pump curve, water source, start-up current and water safety.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

This is neither a pump installation specification nor a sanitation standard. Hydrostatic pressure, water hammer, pressure vessels, electrical isolation, well contamination and pump-motor startup are not resolved.

## Life safety and operational boundary

Do not treat a water-energy calculation as a potable-water certification. Follow local water-safety authorities for drinking water, especially when chemical contamination is possible.

## Source navigation and preservation debt

- **DOE How Hydropower Works:** https://www.energy.gov/cmei/water/how-hydropower-works — Flow and head determine hydraulic resource and conversion stages
- **U.S. EPA, Emergency Disinfection of Drinking Water:** https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water — Public-health distinction between microbial disinfection and chemical contamination; this Atlas does not implement treatment procedures
- **U.S. CDC, How to Make Water Safe in an Emergency:** https://www.cdc.gov/water-emergency/about/index.html — Emergency potable-water advisories; treatment and health depend on hazard category

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
