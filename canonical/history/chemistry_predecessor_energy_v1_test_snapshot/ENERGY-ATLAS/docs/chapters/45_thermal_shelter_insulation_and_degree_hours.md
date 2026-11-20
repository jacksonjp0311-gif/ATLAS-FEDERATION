# 45. Thermal shelter, insulation and degree-hours

**Area:** Thermal Resilience · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

In prolonged power outages, reducing thermal losses can improve survivability without adding generation. A simple quasi-steady building model uses aggregate heat-loss coefficient UA, in watts per kelvin, and sums positive indoor–outdoor temperature degree-hours. It gives an approximate thermal-energy requirement but not a prescription for heating equipment. Infiltration, wind, solar gains, internal moisture, occupancy, thermal mass, ventilation and freeze risks can dominate real performance. A building may become unsafe before a calculated energy budget is exhausted. The model must clearly separate desired indoor temperatures, expected weather and heating system conversion efficiency, all of which require evidence and qualified assessment.

## Equation, symbols and dimensional units

`Q_loss (kWh)=UA (W/K) * sum[(T_inside - T_outside)_+ * duration_h] / 1000.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

Heat transfer through an idealized envelope is proportional to temperature difference when UA is treated as constant. Integrating the heat-loss rate yields the degree-hour formula. A lower UA represents stronger thermal resistance under the stated mechanism, but cannot be assumed to preserve safe ventilation. The model excludes latent loads, moisture movement, thermal storage and wind-driven infiltration unless an independently measured UA already includes them. Energy demand estimates need both input temperature profiles and calibrated building characteristics.

## Hand reconstruction and independent calculation

Set UA=150 W/K and an invented 120 K·h total positive degree-hours. Compute 18 kWh of modeled heat loss. Repeat with UA=75 W/K and obtain 9 kWh. Explain the conditional result: this does not prove that a particular retrofit halves total household energy or remains safe for indoor air quality.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Any claim of real shelter adequacy requires safe indoor temperature and ventilation assessment, not just energy balance. A structure can have low modeled heat loss but dangerous combustion or CO hazards.

## Life safety and operational boundary

Combustion heating, venting and indoor air quality need properly installed equipment and official carbon monoxide precautions; do not improvise indoor fuel use.

## Source navigation and preservation debt

- **ENERGY STAR Geothermal Heat Pumps Efficiency Criteria:** https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria — Definition and rating framework for coefficient of performance; product-specific ratings vary
- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
