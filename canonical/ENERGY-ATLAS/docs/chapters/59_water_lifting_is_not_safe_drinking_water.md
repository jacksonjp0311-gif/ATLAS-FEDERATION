# 59. Water lifting is not safe drinking water

**Domain:** Water-energy coupling. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Electricity may operate a well pump, water-treatment equipment or pressure system, but delivered water volume does not establish potable quality. Hydraulic energy requires moving mass through a total dynamic head; electrical input adds pump and motor losses. Drinking-water safety requires independent knowledge of biological, chemical, radiological and physical contamination. Heating or disinfection can address some microbial hazards, but CDC and EPA guidance warns that fuel, toxic chemical or radioactive contamination is not removed by ordinary boiling. A power shortage can also impair pumps and treatment even when energy remains in storage.

## Formula, units and preconditions

`Hydraulic lifting: E_hydraulic=ρ g V H. Electrical input E_in=E_hydraulic/η_p. Sensible heating: Q=m c_p (T_final−T_initial).`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The first expression is gravitational work for a volume V lifted through head H, using a declared fluid density; dynamic head and losses depend on actual pipes, flow and equipment. The second follows from the definition of heat capacity, assuming no phase change and constant material properties over the interval. Neither equation treats water. A mathematically positive heating energy does not certify achieving a mandated disinfection temperature, duration, chemical removal, or safe storage.

## Reconstruct by hand and compare against code

Take 10 L of water at 20°C, model an increase to 70°C with c_p=4184 J/(kg·K), density 1 kg/L and an assumed useful energy fraction of 0.8. Compute 2,092,000 J useful thermal energy and 2,615,000 J input. That result says nothing about whether the water is safe to drink or how it should be treated.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

The example omits vessel heating, evaporation, changing heat capacity, local boiling point, biological validation and chemical contamination. The hydraulic expression does not design a pump, protect a well or guarantee availability.

## Life-safety and professional boundary

Follow official water advisories: suspected chemical contamination cannot be made safe simply by heating. Well electrical repairs require qualified checks, especially after flooding. This is not a purification procedure.

## Source provenance (links only)

- **U.S. CDC, How to Make Water Safe in an Emergency** — https://www.cdc.gov/water-emergency/about/index.html; inspected portion: Emergency potable-water advisories; treatment and health depend on hazard category
- **U.S. EPA, Emergency Disinfection of Drinking Water** — https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water; inspected portion: Public-health distinction between microbial disinfection and chemical contamination; this Atlas does not implement treatment procedures
- **CDC, How to Disinfect Wells After an Emergency** — https://www.cdc.gov/water-emergency/about/how-to-disinfect-wells-after-an-emergency.html; inspected portion: Safety page warning against electrical well repairs without qualification and against chemical contaminated water

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
