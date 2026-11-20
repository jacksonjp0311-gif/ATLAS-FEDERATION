# 44. Water heating, thermal energy and disinfection boundaries

**Area:** Water · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Heating a known mass of water from one temperature to another can be estimated from sensible heat capacity, but thermal energy alone cannot establish potability. Actual water may contain pathogens, salts, heavy metals, pesticides or other chemicals. EPA emergency guidance explains that boiling and disinfection may reduce disease-causing microorganisms but generally do not remove many chemical contaminants. A model of water temperature is thus a separate engineering component from a verified microbiological/chemical treatment process. The energy ledger also omits the vessel's heat capacity, evaporative loss, elevation-dependent boiling conditions and power time constraints. Do not infer sterilization from reaching a modeled target temperature.

## Equation, symbols and dimensional units

`Q_sensible=m*c_p*(T_final-T_initial); Q_input=Q_sensible/eta_useful. Joules are converted to kWh by dividing by 3.6×10^6.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

The definition of specific heat capacity relates incremental heat to incremental temperature under stated conditions. For constant cp, integration from initial to final temperature yields m cp ΔT. This formula excludes latent heat for vaporization. An assumed overall efficiency can represent heat lost to surroundings in a coarse model, but cannot establish microbial lethality or safe storage of water. The water-energy calculator deliberately reports `water_potability_verified=False`. Detailed water treatment belongs with verified public health guidance and independent testing, not the energy model.

## Hand reconstruction and independent calculation

For an invented 2 kg water sample with cp=4,184 J/kg K, heated from 15 to 60°C, compute 376,560 J useful sensible heat. At 80% delivered heat, input is 470,700 J ≈ 0.131 kWh. Explain that this number cannot answer whether the water should be consumed or whether chemical contamination is present.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Temperature, power input, thermal treatment effectiveness and human health safety are different claims. Unknown source water cannot be declared safe from energy calculation or a model's selected temperature alone.

## Life safety and operational boundary

EPA/CDC emergency water advice supersedes this educational math; use verified treatment guidance and never assume boiling removes dissolved contaminants.

## Source navigation and preservation debt

- **U.S. EPA, Emergency Disinfection of Drinking Water:** https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water — Public-health distinction between microbial disinfection and chemical contamination; this Atlas does not implement treatment procedures
- **U.S. CDC, How to Make Water Safe in an Emergency:** https://www.cdc.gov/water-emergency/about/index.html — Emergency potable-water advisories; treatment and health depend on hazard category
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
