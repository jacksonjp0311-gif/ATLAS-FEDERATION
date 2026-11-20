# 46. Heat pumps, electric resistance and second-law interpretation

**Area:** Thermal Resilience · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Electric resistance heaters convert electrical work into local heat approximately at a one-for-one energy ratio at the point of use. Heat pumps use external work to move heat from a colder source to a warmer sink, so the delivered thermal energy can exceed the input electrical energy. The coefficient of performance (COP) is therefore not a conventional power-conversion efficiency and may exceed one without violating energy conservation. Ideal reversible COP depends on absolute temperature difference, while actual performance depends on design, source conditions, defrost cycles, load, humidity, refrigerant and auxiliary heat. A nominal COP label at one rating condition is not a verified cold-weather field value.

## Equation, symbols and dimensional units

`COP_heating=Q_hot/W_input. For reversible operation COP_Carnot,heating=T_hot/(T_hot−T_cold) using absolute Kelvin; actual COP is lower under finite irreversibilities.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

The first law requires Q_hot=Q_cold+W_input. If the device transfers additional source heat, Q_hot/W_input can exceed one. The second law limits achievable COP by temperature reservoirs, and as their temperature gap widens the reversible bound decreases. Heat-pump electrical demand under a hypothetical constant COP is Q_required/COP, but real COP varies over time. The model should preserve both its idealized bound and the observed/reported test condition.

## Hand reconstruction and independent calculation

Suppose a shelter needs 10 kWh thermal under an authored load model. Electric resistance input is approximately 10 kWh at point-of-use unity conversion. If a hypothetical heat pump delivers average COP=2.5, input is 4 kWh. Explain how auxiliary resistance, defrost or colder source temperature could invalidate that assumption; no installed unit was tested.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Heat pumps are not perpetual motion machines, and high COP is not necessarily high energy availability during an outage. The source heat reservoir, inverter peak power and controls must be present.

## Life safety and operational boundary

This is not refrigerant-handling or heat-pump installation guidance; professional equipment ratings and ventilation requirements remain separate.

## Source navigation and preservation debt

- **ENERGY STAR Geothermal Heat Pumps Efficiency Criteria:** https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria — Definition and rating framework for coefficient of performance; product-specific ratings vary
- **NIST CODATA 2022 recommended fundamental physical constants:** https://physics.nist.gov/cuu/Constants/ — 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
