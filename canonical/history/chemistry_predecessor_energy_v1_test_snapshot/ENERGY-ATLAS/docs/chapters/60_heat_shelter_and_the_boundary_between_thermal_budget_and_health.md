# 60. Heat, shelter and the boundary between thermal budget and health

**Domain:** Thermal systems. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Heating demand depends on the thermal envelope and ambient conditions. A common approximation lumps heat losses into an aggregate UA term in watts per kelvin, which can be integrated across indoor-outdoor temperature differences. Internal gains can reduce the calculated heating requirement. Real shelters also exchange air and moisture, store heat in furnishings, receive sunshine, and need adequate fresh air. A numerical heat-loss budget is not a safe furnace, heater or ventilation design, especially during an infrastructure failure when improvised combustion can create CO exposure.

## Formula, units and preconditions

`Q_loss ≈ ∫ UA × max(0,T_inside−T_outside) dt; model input thermal energy = max(0,Q_loss−Q_internal_gains)/η_transfer.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The UA approximation follows from linearized steady thermal conductance: watts of heat transfer per unit temperature difference. Time-integration yields joules or watt-hours. A model with internal gains uses net loads, and a thermal conversion fraction represents how much energy input reaches the intended enclosure. A heat pump can have delivered thermal COP above one while still obeying the second law because it moves environmental heat. The effective COP depends on source temperature and operating conditions. These relationships are conditional, not an estimate of safe minimum shelter temperature.

## Reconstruct by hand and compare against code

With UA=200 W/K, 20°C inside and 0°C outside, ten hours of idealized loss is 40 kWh of heat. If useful delivery fraction is 0.8, the arithmetic input thermal energy is 50 kWh. Show why the result changes if the outside temperature varies hourly or if measured internal heat gains are included.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Temperature differences in °C equal differences in K, but absolute temperatures in Carnot relations must use kelvins. Infiltration, solar gains and moisture are not resolved. The model cannot establish safe indoor air quality or human health outcomes.

## Life-safety and professional boundary

Never replace ventilation or CO protection with a calculated energy budget. Consult qualified heating and public-health guidance for real buildings and equipment.

## Source provenance (links only)

- **ENERGY STAR Geothermal Heat Pumps Efficiency Criteria** — https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria; inspected portion: Definition and rating framework for coefficient of performance; product-specific ratings vary
- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context
- **U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages** — https://www.cdc.gov/carbon-monoxide/about/index.html; inspected portion: Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
