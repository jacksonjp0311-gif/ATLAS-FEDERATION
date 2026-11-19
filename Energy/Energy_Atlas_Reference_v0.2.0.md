# Energy Atlas — Complete Scientific and Survival-Energy Reference v0.2.0

James Paul Jackson research program · 14 November 2026 · ATLAS FORGE Common Contract 1.0

**Content status:** active v0.2 research. No physical installation, plant authorization, original full-source archive or independent scientific review.

This manual preserves original derivations and methods in durable UTF-8 text. Its safety caveats are part of the science, not optional metadata.



## Complete chapter index

- 01_energy_work_power_and_si_dimensions.md

- 02_conservation_boundaries_and_energy_accounting.md

- 03_thermodynamic_state_and_the_first_law.md

- 04_entropy_irreversibility_and_the_second_law.md

- 05_carnot_bounds_and_the_meaning_of_heat_pump_cop.md

- 06_heat_capacity_calorimetry_and_phase_change.md

- 07_fourier_heat_conduction_and_thermal_resistance.md

- 08_convection_and_convective_boundary_conditions.md

- 09_thermal_radiation_and_the_fourth_power_law.md

- 10_thermal_transients_and_characteristic_time_scales.md

- 11_electrostatic_potential_current_and_dc_circuits.md

- 12_capacitors_inductors_and_transient_storage.md

- 13_ac_rms_power_factor_and_phasor_limits.md

- 14_balanced_three_phase_electricity_and_transformers.md

- 15_electric_power_grids_losses_and_system_boundaries.md

- 16_photovoltaic_effects_and_semiconductor_conversion.md

- 17_wind_turbines_aerodynamic_power_and_betz_s_ideal_limit.md

- 18_hydropower_head_and_water_resources.md

- 19_geothermal_heat_and_direct_thermal_services.md

- 20_heat_engines_rankine_cycles_and_combined_heat_and_power.md

- 21_nuclear_binding_energy_and_controlled_fission_electricity.md

- 22_fusion_physics_and_unverified_commercial_performance.md

- 23_electrochemical_batteries_and_capacity_versus_power.md

- 24_battery_charging_round_trip_losses_and_state_of_charge.md

- 25_hydrogen_and_electrochemical_conversion_pathways.md

- 26_thermal_gravitational_mechanical_and_pumped_storage.md

- 27_power_rating_energy_capacity_and_capacity_factor.md

- 28_distributed_generation_storage_dispatch_and_unmet_load.md

- 29_renewable_variability_curtailment_and_temporal_matching.md

- 30_energy_economics_discounted_cost_and_lcoe.md

- 31_energy_in_computation_and_physical_information_processing.md

- 32_energy_measurements_uncertainty_and_calibration.md

- 33_efficiency_versus_exergy_versus_capacity_factor.md

- 34_lifecycle_impacts_carbon_accounting_and_resource_constraints.md

- 35_resilient_power_microgrids_islanding_and_critical_loads.md

- 36_reconstruction_of_energy_systems_after_infrastructure_loss.md

- 37_from_energy_science_to_survival_services.md

- 38_multi_interval_microgrid_energy_accounting.md

- 39_storage_reserve_and_multi_day_autonomy.md

- 40_storage_fire_safety_and_thermochemical_limits.md

- 41_renewable_variability_seasonality_and_adverse_scenarios.md

- 42_critical_loads_priorities_and_partial_power_failure.md

- 43_water_pumping_energy_dynamic_head_and_delivered_service.md

- 44_water_heating_thermal_energy_and_disinfection_boundaries.md

- 45_thermal_shelter_insulation_and_degree_hours.md

- 46_heat_pumps_electric_resistance_and_second_law_interpretation.md

- 47_fuel_backed_generation_conservation_carbon_monoxide_and_backfeed.md

- 48_reliability_indicators_unmet_energy_is_not_outage_probability.md

- 49_metrology_and_source_recovery_under_infrastructure_failure.md

- 50_reconstructing_community_scale_energy_knowledge_from_first_principles.md


---


# 1. Energy, work, power, and SI dimensions

**Area:** Foundations. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Energy is a conserved physical quantity that can change form; power is its rate of transfer. Distinguishing these concepts is essential for preserving correct engineering knowledge. A 1 kW device operating for one hour transfers 1 kWh, or exactly 3.6 MJ, but it is not producing 1 kWh at every instant. Work from a force requires displacement in the force direction. A joule is a newton metre, a watt is a joule per second, and electric quantities introduce volts, amperes and ohms. A useful report states the measurement boundary, sign convention, interval, uncertainties and whether values are rated, sampled, inferred or calibrated. Primary units must not be silently mixed with engineering units. Energy per unit mass, area, cycle and delivered service are distinct performance measures.

## Fundamental relationship, symbols and SI dimensions

`P=dE/dt; E=∫P dt; 1 Wh=3600 J; 1 kWh=3.6×10^6 J; 1 W=1 kg·m²/s³.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Dimensional analysis checks equations before computation: power times time has dimensions energy, whereas power divided by time does not. For a time-varying load, multiply average power by the interval only when the average is explicitly measured or defined. Integrating sample values needs an interpolation assumption, not just endpoints. The SI brochure gives the authoritative unit definitions, while sampled energy remains subject to instrument accuracy. A source record can preserve exact unit definitions even when no original laboratory measurements are available.

## Reconstruct the example without external AI

A 600 W heater runs continuously for 30 minutes. Compute 300 Wh = 0.3 kWh = 1.08 MJ by hand and with unit_convert. Repeat for a 600 W peak device whose output varies; explain why its true energy can be lower than the rated calculation.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Watts and watt-hours are not interchangeable. Demand charges, power capacity and stored energy answer different questions. An energy value without units and a reference interval is not a physically usable measurement.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 2. Conservation boundaries and energy accounting

**Area:** Foundations. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

The first law of thermodynamics is an accounting principle: energy entering, leaving and accumulating inside a chosen system must balance. The boundary can enclose a battery, building, motor, power plant or entire grid. Changes in the boundary move terms between internal transfers and external flows without changing conservation. Real measurements rarely close exactly because sensors have uncertainty, flow channels may be omitted, and stored energy may be difficult to estimate. A nonzero residual identifies an accounting discrepancy; it does not by itself reveal which physical component is faulty. Conservation should be tested against measured input and output with separate uncertainty estimates, not enforced by silently assigning all differences to an arbitrary loss bucket.

## Fundamental relationship, symbols and SI dimensions

`ΔE_stored = E_in − E_out, and residual r = E_in − E_out − ΔE_stored.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The expression comes from integrating conservation over the time interval and classifying each transfer once. Work, heat, chemical fuel, electromagnetic energy and mass-borne enthalpy are different channels but contribute consistently under an explicit system definition. Subtracting inferred storage change from net flow leaves a measurable residual. If a test reports negative residual, possible explanations include unmetered input, inconsistent sign conventions, clock mismatch or drift. Distinguishing those mechanisms requires further observations, not a model’s self-report.

## Reconstruct the example without external AI

A test battery receives 1000 J, delivers 700 J and increases stored energy by 200 J. Its residual is 100 J. Write at least three alternative explanations for the 100 J, identify which additional measurements discriminate between them, and record all quantities as a constructed example.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

No claim of over-unity may follow from a single nonzero residual. Hidden energy inflow, measurement bias and definition mismatch must be excluded before considering unconventional mechanisms.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 3. Thermodynamic state and the first law

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Internal energy is a state function: its change depends on initial and final thermodynamic states, not the specific path. Heat and work are process-dependent transfers, not substances stored inside matter. A closed system excludes mass crossing its boundary; open systems require mass-flow enthalpy and kinetic and potential energy terms. The choice of sign convention must be explicit. We use heat into the system as positive and work done by the system as positive. Real engines often cycle through phases where pressure, temperature and composition vary; an ideal gas approximation applies only under conditions for which its constitutive law is adequate. State changes can be represented mathematically but actual thermodynamic properties require reliable material data.

## Fundamental relationship, symbols and SI dimensions

`ΔU = Q − W (closed system); W_reversible = ∫P dV; ideal gas PV=nRT.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The first law integrates energy conservation and assigns heat and work signs. For a reversible isothermal ideal gas, U depends only on T; therefore ΔU=0, so heat received equals the work delivered. Integrating P=nRT/V between V1 and V2 gives W=nRT ln(V2/V1). This result cannot be transferred to irreversible gas expansion against a finite external pressure without modeling the actual process path.

## Reconstruct the example without external AI

Expand one mole of ideal gas reversibly from 0.01 m³ to 0.02 m³ at 300 K. Calculate work by hand using nRT ln 2, then compare with the reversible_ideal_gas_work reference. List how the calculation changes when gas deviates from ideal behavior.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A temperature reading does not determine the internal energy of arbitrary material without heat-capacity, phase and composition information. Reversible work is an upper-limit idealization for a given process, not a promise about real devices.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 4. Entropy, irreversibility, and the second law

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

The second law constrains the direction and quality of energy transformations. Energy conservation alone permits many mathematically balanced processes that never occur spontaneously. Entropy quantifies aspects of dispersal and available microscopic arrangements, with reversible heat transfer defining dS=δQ_rev/T. For an isolated system, total entropy cannot decrease. Real engines and electrical conversions create entropy through friction, finite-temperature heat transfer, electrical resistance, mixing and chemical reactions. A useful energy library must distinguish energy from exergy: the latter is the potential to do useful work relative to a reference environment. Two energy quantities of equal joules can have very different capacities for mechanical work.

## Fundamental relationship, symbols and SI dimensions

`ΔS_isolated ≥ 0; dS=δQ_rev/T; exergy destroyed = T0 S_generated for a specified reference environment.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

A heat engine that moves heat from a hot source to a cold sink while delivering work can be evaluated by both first- and second-law balances. The inequality arises from the Clausius statement and reversible comparison cycles. Entropy generation identifies quality degradation, even though total joules are conserved. A reversible process maximizes efficiency under the idealized endpoint temperatures, but real material transport imposes finite rates and dissipation.

## Reconstruct the example without external AI

Explain why 1 kWh of electricity and 1 kWh of low-temperature waste heat have equal energy but unequal potential for useful work. Name the ambient reference temperature and which measurements would be needed to quantify exergy.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Entropy is not a casual synonym for disorder or the amount of useful knowledge. It does not prove that a computing system cannot improve its performance without external work; accounting must include its environment.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 5. Carnot bounds and the meaning of heat-pump COP

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A reversible heat engine operating between two fixed thermal reservoirs has a maximum possible thermal efficiency determined only by their absolute temperatures. The corresponding reversed ideal refrigerator and heat pump can move more thermal energy than the mechanical or electrical work they consume, because they transfer ambient heat as well as supply work. Their coefficient of performance can exceed one without violating conservation. This must not be confused with a heat engine that produces more work than heat input. Actual device performance is lower than reversible ideals due to temperature differences needed for finite heat transfer, compressors, throttling, electrical losses and defrost demands.

## Fundamental relationship, symbols and SI dimensions

`η_Carnot=1−Tc/Th; COP_heating,max=Th/(Th−Tc); COP_cooling,max=Tc/(Th−Tc), with 0<Tc<Th in kelvin.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

A reversible engine has Qc/Qh=Tc/Th, and useful work Qh−Qc; substituting yields the efficiency. Reversing work and heat flows yields COP expressions. These follow from a reversible-cycle entropy balance, not a particular refrigerant or commercial appliance. Real COP depends on temperatures at the actual heat exchangers, flow rate and part-load operation, not merely outdoor air temperature.

## Reconstruct the example without external AI

For 500 K and 300 K reservoirs, compute theoretical engine efficiency 40%. For 400 K and 300 K, compute maximum heating COP 4. Contrast this with a device claiming 120% electrical conversion efficiency; explain why the latter is a different claim.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Temperatures in Celsius cannot be inserted directly into Carnot ratios. Equal reservoir temperatures create singular ideal COP formulas and no finite-temperature-difference heat engine work.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [ENERGY STAR Geothermal Heat Pumps Efficiency Criteria](https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria) — inspected: Definition and rating framework for coefficient of performance; product-specific ratings vary

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 6. Heat capacity, calorimetry, and phase change

**Area:** Thermodynamics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Heating a body requires knowing what its material is, which phase it occupies, and how heat capacity varies with temperature. The approximation Q=mcΔT is useful only where specific heat c is approximately constant and no phase transition occurs. During melting or boiling, latent heat can absorb energy with little temperature change at specified pressure, so a thermometer alone does not measure heat input. Thermochemical databases preserve standard enthalpy, entropy, heat capacities and phase-transition data, but those values depend on pressure, purity and measurement methods. A reconstruction-ready atlas must record source, reference state and uncertainty for every numeric property before using it in an engineering prediction.

## Fundamental relationship, symbols and SI dimensions

`Q≈mc_pΔT at constant pressure when c_p is constant; Q_phase=mL; generally Δh=∫c_p(T)dT + phase terms.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Integrating temperature-dependent heat capacity gives the correct enthalpy change for a single phase under suitable conditions. A simple constant-c calculation is a local approximation to that integral. For a heating curve across a phase boundary, divide the path into sensible-heat and latent-heat intervals. The first law ensures total energy accounting, but the material model determines how input energy changes temperature and phase.

## Reconstruct the example without external AI

Take 1 kg of a hypothetical solid with c=500 J/kg/K, heated by 10 K; compute 5 kJ. Now introduce a phase change with latent heat 50 kJ/kg and explain why adding 50 kJ may not increase temperature.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A material property quoted without source, composition, temperature and pressure is not universally valid. Do not extrapolate a heat-capacity table into chemically reactive or high-pressure regimes without evidence.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 7. Fourier heat conduction and thermal resistance

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Conduction moves heat in response to temperature gradients through a material. Fourier's law links heat flux to thermal conductivity and gradient, with a minus sign indicating flux down temperature. For a one-dimensional uniform slab under steady conditions, the heat rate is kA(Th−Tc)/L. The geometric approximation assumes no internal heat generation, constant conductivity, and negligible multidimensional paths. Thermal resistances in series can be added under the same one-dimensional steady assumption. In real buildings, motor windings and battery packs, contact resistance, radiation, convection and temperature-dependent conductivity matter. A useful calculation must not infer k from a single heat-rate observation without controlling area, thickness and other parallel pathways.

## Fundamental relationship, symbols and SI dimensions

`q'' = −k dT/dx; Qdot=kA(Th−Tc)/L; R_thermal=L/(kA).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Integrate Fourier's law across a slab with constant k and steady uniform flux, giving a linear temperature profile. Resistance form follows by rearrangement. For multiple layers with equal cross-sectional area and series flow, total temperature drop is QdotΣR_i, provided each layer reaches the same steady heat rate. This is a mathematical boundary-value result, not a measurement of a real composite wall.

## Reconstruct the example without external AI

A 0.1 m thick slab has k=1 W/m/K, area 2 m², and 10 K temperature difference. Derive 200 W, then double thickness and compare. Describe how thermal bridging creates departures from 1D predictions.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Conductivity units W/(m K) are not the same as heat transfer coefficient W/(m² K). A contact temperature sensor can alter the measured profile and does not certify the model.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [DOE Energy Efficiency Versus Energy Intensity](https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity) — inspected: Efficiency differs from sector intensity and structural changes

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 8. Convection and convective boundary conditions

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Convection combines bulk fluid motion and diffusion near a surface. Newton's cooling relation defines a heat-transfer coefficient h for a chosen geometry and state of fluid motion. This coefficient is not a fundamental constant: it depends on Reynolds number, Prandtl number, orientation, flow regime, fluid properties and characteristic length. Natural and forced convection can differ dramatically. A lumped surface model uses hA(Tsurface−Tfluid), but actual boundary-layer physics may require spatially varying coefficients or computational fluid dynamics. The reference calculation is a bookkeeping tool for a declared h, not an empirical prediction of h from equipment shape.

## Fundamental relationship, symbols and SI dimensions

`Qdot_conv=hA(T_surface−T_fluid). Nusselt number Nu=hL/k_fluid, conditional on geometry and flow.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The heat-transfer coefficient definition rearranges measured heat flux and temperature difference, and empirical correlations may estimate it under limited nondimensional ranges. Choosing an h outside the validity of a correlation can create large error while keeping the equation dimensionally correct. Energy that leaves the surface enters the fluid and must appear in a larger control-volume balance.

## Reconstruct the example without external AI

For h=2 W/m²/K, area=3 m² and a surface 10 K colder than the fluid, the signed convection rate is −60 W using outward-positive convention. Explain the sign and write what an air-speed measurement would need to support an estimated h.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A large positive fitted h does not prove high thermal efficiency, and one lab measurement should not be extrapolated to a different Reynolds number or shape.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Efficiency Versus Energy Intensity](https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity) — inspected: Efficiency differs from sector intensity and structural changes
- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 9. Thermal radiation and the fourth-power law

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

All bodies above absolute zero exchange electromagnetic radiation. A blackbody has an ideal radiative exitance proportional to the fourth power of absolute temperature. Real surfaces have emissivity and wavelength-dependent behavior; geometry introduces view factors, multiple reflections and participating media. A simple net exchange between a gray surface and a large isothermal surrounding environment is epsilon sigma A(T_surface⁴−T_surroundings⁴). That expression is a controlled approximation, not a universal radiative transfer solution. At high temperatures radiation can dominate thermal losses, which makes a linear-temperature approximation unreliable over large differences.

## Fundamental relationship, symbols and SI dimensions

`Qdot_rad≈εσA(T_s⁴−T_env⁴), 0≤ε≤1; σ≈5.670374419×10^-8 W·m^-2·K^-4.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Stefan–Boltzmann integration of ideal blackbody radiation gives total emitted flux σT⁴. Subtracting an idealized surrounding incident flux gives a net rate. The factor ε is a gray-body approximation; a real spectral emissivity could require integration over wavelength and angles. SI defining constants make the exact derived value of sigma calculable, though the decimal representation is rounded in this code.

## Reconstruct the example without external AI

Calculate the ideal net rate from 400 K to 300 K over one square metre with emissivity one. Reverse temperatures and verify the sign changes but magnitude stays equal. Then explain why changing view factor or emissivity affects a real enclosure.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Use kelvin, not degrees Celsius, under a fourth power. A net flux estimate does not prove safe material temperatures or fire resistance.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 10. Thermal transients and characteristic time scales

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Many real systems do not reach steady state before a measurement or demand change. A lumped thermal model treats a body as spatially isothermal, with thermal capacitance mc and a surface heat transfer hA. Its temperature difference from ambient decays exponentially when no internal heat is generated. The characteristic time is tau=mc/(hA). This model is appropriate only when internal thermal resistance is small relative to boundary heat transfer, commonly assessed with a small Biot number. Battery packs, computing modules, furnace walls and buildings often need spatial models because internal gradients cannot be ignored.

## Fundamental relationship, symbols and SI dimensions

`m c dT/dt = −hA(T−T_env); T(t)=T_env+(T0−T_env)e^(−t/τ); τ=mc/(hA).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Separate variables in the linear first-order differential equation, integrate d(T−Tenv)/(T−Tenv)=−dt/τ, and apply the initial condition. The exponential solution cannot predict sensor response or material changes unless those are modeled. At one time constant the temperature difference is 1/e of its starting value; after several time constants the system approaches ambient asymptotically.

## Reconstruct the example without external AI

For 10 kg, c=500 J/(kg K), h=20 W/(m² K), area=2 m², compute tau=125 s. Compare model temperatures after 125 and 250 s. State what a Biot-number calculation would need before using this on a real motor.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A negative or zero time constant is unphysical under this passive model. Uniform temperature and constant h are approximations, not universal physical truths.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Efficiency Versus Energy Intensity](https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity) — inspected: Efficiency differs from sector intensity and structural changes
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 11. Electrostatic potential, current, and DC circuits

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Electrical work is transferred when charge moves through a potential difference. Current is the rate of charge flow, voltage is energy per unit charge, and resistance models a relationship between current and voltage under specified material conditions. Ohm's law describes ohmic conduction; semiconductor devices, batteries and arcs may be strongly nonlinear. The passive sign convention makes absorbed power p=vi positive when current enters the positive-voltage reference terminal. Sources can deliver electrical power, indicated by negative absorbed power under that convention. Circuit equations enforce charge conservation at nodes and energy balance around loops, but measurement points and grounds must be defined explicitly.

## Fundamental relationship, symbols and SI dimensions

`I=dq/dt; V=dW/dq; V=IR for an ohmic element; P=VI; resistive dissipation P=I²R.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Kirchhoff's current law arises from charge conservation when node charge accumulation is negligible in the chosen circuit representation. Kirchhoff's voltage law relates potential differences around a loop under lumped/quasistatic assumptions. Dividing V by R determines current in a passive linear resistor. Thermal changes can shift R and invalidate a single fixed-resistance prediction.

## Reconstruct the example without external AI

For a 12 V source driving a 6 Ω resistor in an ideal circuit, compute 2 A and 24 W. Integrate over 10 seconds to get 240 J. Explain where the energy goes physically and why a non-ohmic LED should not be treated as a bare resistor.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Electricity is dangerous: textbook equations do not specify safe wiring, protection, voltage isolation, fault clearing or operator qualifications. These models must not be used to energize real high-voltage circuits.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 12. Capacitors, inductors, and transient storage

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Capacitors store energy in electric fields; inductors store energy in magnetic fields. Their constitutive laws connect voltage/current to changes over time. In a simple resistor-capacitor discharge, the voltage falls exponentially with time constant RC. In an inductor, an abrupt current change requires a large induced voltage according to the lumped ideal model, which can cause dangerous switching transients in real equipment. Stored field energy is not the same as delivered energy after conversion losses. Ideal linear component equations neglect parasitic resistance, dielectric absorption, leakage, saturation and breakdown. An engineering energy library must preserve the limitations of a lumped approximation.

## Fundamental relationship, symbols and SI dimensions

`E_C=½CV²; E_L=½LI²; i_C=C dv/dt; v_L=L di/dt; V_RC(t)=V0 e^(−t/RC).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For RC discharge, charge balance gives C dV/dt=−V/R. Separating variables yields exponential voltage and quadratic decay of stored energy. A real capacitor may lose usable energy through series resistance or internal leakage; applying the ideal formula beyond rated voltage can cause component failure. Energy can be conserved while being transformed into resistor heat.

## Reconstruct the example without external AI

A 1 F capacitor at 10 V stores 50 J. Through a 1 Ω resistor, one time constant is 1 second, and the remaining voltage is 10/e V. Derive how much energy has dissipated by that time.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

An RC time constant is not a battery self-discharge law. Stored energy in a capacitor can be small despite high peak power delivery; never confuse power density and energy density.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 13. AC, RMS, power factor, and phasor limits

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Alternating current and voltage vary with time. Under sinusoidal steady-state conditions, RMS amplitudes relate to equivalent resistive heating, and phase difference determines real and reactive power. Apparent power is measured in volt-amperes, real power in watts, and reactive power in vars. A power factor of 0.8 means only part of apparent power contributes to average active transfer under the defined sinusoidal model; it does not automatically measure motor mechanical efficiency. Inductive and capacitive loads exchange field energy with the source. Nonsinusoidal waveforms contain harmonics, making simple single-angle formulas insufficient. The direction of reactive power and whether current leads or lags must be declared.

## Fundamental relationship, symbols and SI dimensions

`Single-phase sinusoidal: S=V_rms I_rms; P=S cosφ; Q=S sinφ; P²+Q²=S².`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The average of v(t)i(t) over one sinusoidal period gives Vrms Irms cosφ after product-to-sum identities remove a zero-mean double-frequency term. The quadrature component is convention-dependent, so a signed Q requires a stated reactive reference. Three-phase balanced systems sum the three phase powers and simplify to sqrt(3) Vline Iline pf; this fails for arbitrary unbalanced conditions.

## Reconstruct the example without external AI

A 230 V RMS circuit draws 10 A at power factor 0.8. Compute apparent power 2300 VA, real power 1840 W and |reactive| 1380 var. Describe what additional waveforms are needed for a distorted electronic load.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not use a phase-angle power factor formula to estimate harmonic-rich loads without additional analysis. A high pf is not equivalent to high energy efficiency or improved power-system reliability.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 14. Balanced three-phase electricity and transformers

**Area:** Electrical. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Most bulk electrical systems use three-phase alternating power. Under balanced sinusoidal operation, line voltage and current yield total real power sqrt(3) Vline Iline cosφ. Transformers change voltage and current levels using electromagnetic induction, ideally conserving apparent power while exchanging voltage ratio for current ratio. Real transformers have winding resistance, magnetic core losses, leakage flux, saturation and insulation constraints. Their connection configuration (delta or wye) determines line-to-phase relationships. Voltage step-up can reduce line current for a fixed power transfer and thereby reduce resistive losses, but actual electrical safety, transient stability and grid protection are much more complex than one ideal ratio.

## Fundamental relationship, symbols and SI dimensions

`P_3φ=√3 V_LL I_L pf, S_3φ=√3 V_LL I_L; V2/V1≈N2/N1, I1/I2≈N2/N1 (ideal).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For an ideal transformer, the induced voltage in each winding is proportional to the time derivative of common core flux times its turns; therefore the voltage ratio is the turn ratio. Conservation of instantaneous average power implies the inverse current ratio in magnitude. In a transmission path, I²R scales as current squared, motivating higher voltage for equal transfer. In actual AC networks, conductor resistance, reactive flow, corona effects and stability requirements must also be considered.

## Reconstruct the example without external AI

An ideal 100-turn primary connected to a 200-turn secondary doubles voltage. If the secondary supplies 3 A at 240 V, the primary ideally draws 6 A at 120 V. Recalculate I²R loss for a line with fixed resistance when current is halved.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A textbook ideal transformer is not a construction manual or high-voltage clearance procedure. Never energize a real network based on these calculations alone.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 15. Electric power grids, losses, and system boundaries

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A power grid connects generating resources to loads through transmission, distribution, power electronics, protection devices and control systems. Real grids must balance generation and consumption plus losses at every instant, but frequency and voltage are dynamical states rather than constants guaranteed by an energy sum. A static energy ledger can identify missing accounting but cannot certify angular stability, fault recovery, harmonic limits or protection coordination. High-voltage transmission reduces current for given power and can reduce resistive loss; reactive power and line impedance also matter. A microgrid can operate grid-connected or islanded only when its architecture supports suitable voltage/frequency formation and fault protection. Reliable infrastructure knowledge requires one-line diagrams, equipment nameplates, operating envelopes and tested protection settings, not merely formulas.

## Fundamental relationship, symbols and SI dimensions

`Static balance: P_generation + P_import = P_load + P_loss + P_charge + P_export (under defined signs). Line heating P_loss≈I_rms²R for each conductor.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Kirchhoff's laws enforce network constraints for a lumped electrical model. AC power flow has nonlinear voltage-angle relationships that are not solved by the static scalar balance. Variable renewable generation and storage require time resolution; energy conserved over one day does not guarantee sufficient power at the evening peak. The EIA grid description maps physical stages of generation, transmission and delivery but does not specify one universal real grid.

## Reconstruct the example without external AI

A feeder delivering 10 A through two conductors each of 0.2 Ω loses 40 W in the simple model. Compare with 5 A and hold line resistance constant. Identify which real cable and protection measurements would be necessary before installation.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A balanced daily kWh report does not prove every second of demand was met. A standalone grid operation plan needs real-time control and safety validation, outside this reference package.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 16. Photovoltaic effects and semiconductor conversion

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Photovoltaic cells absorb photons in semiconductor junctions, producing charge carriers that a circuit can collect. Only photons within suitable spectral bands and subject to device losses contribute usefully. A module's rated DC output is measured under standard test conditions, not a guarantee of site power. Array output depends on incident plane-of-array irradiance, cell temperature, spectrum, orientation, shading, soiling, wiring and inverter limits. A useful introductory model scales rated power linearly with irradiance and applies a temperature coefficient around a reference 25°C; it deliberately omits low-light nonlinearities and more detailed diode behavior. Real energy forecasting requires weather series and module characterization.

## Fundamental relationship, symbols and SI dimensions

`P_DC≈P_rated(G/1000)(1+γ(T_cell−25°C)) for a specified module, irradiance G in W/m² and gamma in 1/°C.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Electrical output has dimensions voltage times current. Conversion efficiency is electrical output divided by incident optical power under controlled conditions. The linear model is a first-order expansion of rated module performance around calibration conditions, not a fundamental semiconductor theorem. When a temperature correction becomes negative, the approximation is outside its domain; the reference rejects rather than returning negative generated energy.

## Reconstruct the example without external AI

A rated 1000 W DC array at 1000 W/m² and 45°C with coefficient −0.004/°C produces 920 W under the linear model. Compare the result with measured inverter output and list the components omitted.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

No perpetual power exists at zero irradiance. A module rating is not a facility capacity factor, and a published record cell efficiency must not be substituted for a installed-array annual yield.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Solar Photovoltaic Technology Basics](https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics) — inspected: Solar cell, module, arrays, and DC/AC system concept
- [DOE Solar PV Performance and Efficiency Basics](https://www.energy.gov/cmei/systems/solar-photovoltaic-performance-and-efficiency-basics) — inspected: Conversion efficiency, IV curves, temperature and spectral effects
- [Sandia PV Performance Modeling Collaborative: PVWatts](https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/point-value-models/pvwatts/) — inspected: PVWatts basic power/irradiance/temperature point model; versions and low-light rules differ

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 17. Wind turbines, aerodynamic power, and Betz’s ideal limit

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

The kinetic energy flux through a rotor-swept area is proportional to density, area and the cube of wind speed. A turbine can extract only part of that flux; the ideal steady actuator-disk model gives the Betz maximum power coefficient 16/27. Real machines also obey cut-in, rated, cut-out and fatigue limits. Wind fields vary with height, terrain, atmospheric stability and turbulence. Power curves measured at standard conditions cannot simply be multiplied by a regional average wind speed; because power scales with the cube of speed before rating, the distribution matters. A full resource assessment needs hub-height wind time series, air density, array losses and electrical conversion data.

## Fundamental relationship, symbols and SI dimensions

`P_wind=½ρAv³; P_rotor=CpP_wind, 0≤Cp≤16/27 in the ideal actuator-disk model.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For a mass flow of air moving at velocity v, kinetic energy per mass is v²/2 and volume flow scales with Av, giving kinetic power ρAv³/2. Betz's result balances upstream and downstream momentum across a slowed ideal stream tube; extracting all energy would halt the flow and eliminate throughput. The upper bound does not apply to arbitrary non-actuator devices or justify real turbine efficiency measurements.

## Reconstruct the example without external AI

For air density 1.2 kg/m³, area 10 m², speed 10 m/s and Cp=0.4, compute 2400 W. Double wind speed and explain the eightfold ideal pre-rated power increase. Then explain why a real turbine would reach rated power and eventually shut down.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A power coefficient above 16/27 should trigger model review, not be reported as evidence of revolutionary wind physics. Real coefficients and measurement boundaries must be distinguished.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE How Do Wind Turbines Work?](https://www.energy.gov/cmei/systems/how-do-wind-turbines-work) — inspected: Wind turbines use aerodynamic lift/drag to rotate generators; resource and designs vary
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 18. Hydropower, head, and water resources

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Water moving through a height difference can transfer gravitational potential energy to a turbine. Under a simple incompressible steady model, available power scales with density, gravitational acceleration, volumetric flow and head. Turbine-generator efficiency converts hydraulic head into electric output. Real systems have penstock friction, changing reservoir levels, cavitation risk, environmental flow constraints, sediment and regulatory requirements. Pumped storage uses electricity to move water uphill and later recover some energy; it is storage with losses, not a source that creates energy. River hydrology and site surveys matter more than assuming one permanent head and flow.

## Fundamental relationship, symbols and SI dimensions

`P_hydro=ρgQHη; hydraulic power P_available=ρgQH, 0≤η≤1.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Potential energy of mass m at elevation difference H is mgH; mass flow rate is ρQ, yielding power ρgQH. Efficiency accounts for mechanical and electrical conversion within a declared boundary. The formula does not provide environmental suitability or legal authority to alter waterways. Scaling flow in a hypothetical example is simple; predicting real available flow across seasons is not.

## Reconstruct the example without external AI

With water density 1000 kg/m³, flow 1 m³/s, net head 10 m and conversion efficiency 0.8, calculate approximately 78.5 kW. Halve flow and compare, while listing the flow and head surveys a real project would require.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Head and flow cannot be assumed constant from a single measurement. A physically feasible power calculation is not a permit, safety assessment or ecological-impact study.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE How Hydropower Works](https://www.energy.gov/cmei/water/how-hydropower-works) — inspected: Flow and head determine hydraulic resource and conversion stages
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 19. Geothermal heat and direct thermal services

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Geothermal resources exploit thermal energy in Earth's subsurface. Applications include direct heat, district heating, ground-source heat pumps and geothermal electricity where temperature and flow are sufficient. Ground-source heat pumps do not usually tap deep high-temperature geothermal reservoirs; they use the ground as a moderate-temperature exchange environment. Resource adequacy depends on permeability, temperature gradient, sustainable heat extraction, fluid chemistry and drilling conditions. A simplified thermal power estimate requires mass flow and enthalpy difference, not merely underground temperature. Resource classifications, induced seismicity and water chemistry are distinct from thermodynamic possibility.

## Fundamental relationship, symbols and SI dimensions

`P_thermal≈ṁ(h_in−h_out), with mass flow ṁ in kg/s and specific enthalpy h in J/kg.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The steady-flow first law accounts for enthalpy transported by the working fluid, plus pumps, heat exchange and mechanical work. For pure liquid under narrow temperature range h change may be approximated with c_pΔT. The approximation breaks down across phase changes and significant pressure effects. A real electricity cycle needs a heat sink and faces Carnot/exergy constraints.

## Reconstruct the example without external AI

Construct a stream of 1 kg/s cooling through 20 K with constant c_p=4200 J/kg/K, giving 84 kW of thermal transfer. Specify why this cannot be interpreted as 84 kW of electrical output without a thermodynamic cycle and temperature bounds.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Geothermal heat is not globally uniform or always indefinitely renewable at a particular extraction rate. Source temperature alone cannot establish project viability.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Geothermal Explained](https://www.eia.gov/energyexplained/geothermal/) — inspected: Geothermal heat and direct-use/electricity pathways
- [ENERGY STAR Geothermal Heat Pumps Efficiency Criteria](https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria) — inspected: Definition and rating framework for coefficient of performance; product-specific ratings vary

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 20. Heat engines, Rankine cycles, and combined heat and power

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Thermal power plants convert some heat from combustion, fission, concentrated solar or geothermal processes into mechanical and then electrical work. Real cycles use pumps, turbines, heat exchangers and condensers. The Rankine cycle is a foundational steam-power model; Brayton cycles underpin gas turbines. Cogeneration or combined heat and power (CHP) captures thermal output for useful heating or industrial service, improving total useful-energy utilization without violating heat-engine efficiency limits. Plant efficiency depends on fuel higher or lower heating value, ambient conditions, equipment condition, load and heat-demand matching. Condenser rejection and cooling infrastructure are part of the energy balance.

## Fundamental relationship, symbols and SI dimensions

`η_electric = W_electric/Q_fuel; η_CHP_useful=(W_electric+Q_useful_heat)/Q_fuel; 0≤η≤1 within closed fuel-energy boundary.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

For a heat engine, first-law balance partitions heat input into work and rejected heat over a complete cycle. CHP counts only heat that actually serves a validated demand; dumping unwanted low-grade heat does not increase useful efficiency. A plant reporting higher electrical efficiency may still have different fuel boundaries and lower heating value reference. Second-law analysis constrains feasible temperature-limited work extraction.

## Reconstruct the example without external AI

A plant consumes 100 units of fuel energy and produces 30 units electric work, 40 units useful heat, and 30 units other rejection. Calculate electrical efficiency 30% and combined useful efficiency 70%, then identify the necessary heat-customer operating schedule.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not add thermal energy at one temperature to electricity as if both had identical usefulness in exergy or economic value. A CHP figure cannot exceed the physically accounted fuel input without investigating omitted energy sources.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Chemistry WebBook SRD 69](https://webbook.nist.gov/chemistry/) — inspected: Thermodynamic data types and dependence on state, material, reference condition
- [ENERGY STAR Geothermal Heat Pumps Efficiency Criteria](https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria) — inspected: Definition and rating framework for coefficient of performance; product-specific ratings vary

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 21. Nuclear binding energy and controlled fission electricity

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Nuclear reactions convert differences in nuclear binding energy into kinetic energy and radiation, much of which becomes heat in reactor systems. The mass-energy relation E=Δmc² describes an ideal mass defect, not a complete prediction of a plant's electric output. Commercial fission plants use controlled chain reactions, heat removal, steam cycles, shielding and multiple safety systems. Distinguish the microscopic energy of fission events from reactor thermal power, turbine mechanical output, generator efficiency, operating capacity factor and waste-management requirements. The scientific reference can teach energy conservation and mass defect without offering design or operational instructions for radioactive materials or reactors.

## Fundamental relationship, symbols and SI dimensions

`E_released≈Δm c²; c=299792458 m/s (exact), with mass defect Δm in kg.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

A reaction's initial and final rest masses differ; conservation of mass-energy means released energy appears as motion, photons or other channels. Simply multiplying a bulk mass by c² is not a claim that all that matter can be converted in a practical reactor. Fuel composition, reaction pathways, thermal conversion efficiency, capacity limits and safety constraints make actual electricity generation far smaller than naïve all-mass conversion examples.

## Reconstruct the example without external AI

For a hypothetical mass difference of 10^-9 kg, compute approximately 8.99×10^7 J. Explicitly state that this is an algebraic conversion of a *specified* mass defect, not a fuel recipe, reactor yield or measurement.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not use this reference to assemble, operate or modify a nuclear system. The absence of operational instructions is intentional, and reactor safety requires qualified regulatory engineering.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Nuclear 101: How Does a Nuclear Reactor Work?](https://www.energy.gov/ne/articles/nuclear-101-how-does-nuclear-reactor-work) — inspected: Fission heat, cooling, steam turbines and electrical generation overview
- [NIST CODATA 2022 recommended fundamental physical constants](https://physics.nist.gov/cuu/Constants/) — inspected: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 22. Fusion physics and unverified commercial performance

**Area:** Generation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Fusion joins light nuclei into heavier products and can release binding energy under particular reaction conditions. Stars sustain fusion through extreme temperatures and gravitational confinement. Terrestrial research explores plasma confinement, turbulence, plasma-facing materials, sustained burning, tritium fuel cycles and engineering conversion of heat to electricity. A reported scientific fusion gain can use a narrow accounting boundary (for example energy delivered to a target versus fusion output), while a commercial plant must account for all facility energy input, heat conversion, recirculating power, reliability and maintenance. The distinction is essential for honest claims. The current scientific literature and DOE programs describe active progress but do not imply that every proposed architecture has demonstrated grid-scale economic electricity.

## Fundamental relationship, symbols and SI dimensions

`Q_plasma=E_fusion/E_auxiliary_heating under a declared plasma boundary; overall electric efficiency requires facility net electrical output/input accounting.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Reaction mass defects follow E=Δmc²; achieving a net facility gain depends on confinement, material integrity, fuel supply and conversion. One ratio cannot substitute for another when denominators differ. An energy balance across a larger boundary may reveal laser, cryogenic, magnet or support-power costs excluded from a small-boundary Q. This is not a critique of a specific experiment without its original measurements; it is a general accounting requirement.

## Reconstruct the example without external AI

Given a toy plasma experiment with 10 arbitrary units of fusion output and 5 units of plasma heating, report Q_plasma=2, then add 20 units of facility overhead and show why the facility has not demonstrated positive net electrical output in that toy scenario.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Never equate plasma gain, wall-plug gain and net delivered electricity. Fusion fuel cycles, materials and regulatory constraints remain experimental and engineering questions.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Fusion Energy Sciences](https://www.energy.gov/science/fes/fusion-energy-sciences) — inspected: Fusion physics and unresolved materials, fuel-cycle, plasma and commercial engineering gaps
- [DOE Nuclear 101: How Does a Nuclear Reactor Work?](https://www.energy.gov/ne/articles/nuclear-101-how-does-nuclear-reactor-work) — inspected: Fission heat, cooling, steam turbines and electrical generation overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 23. Electrochemical batteries and capacity versus power

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Rechargeable batteries store energy through chemical potentials and convert between electrical and chemical energy through electrochemical reactions. Their nominal capacity is often quoted in ampere-hours or watt-hours, but usable capacity depends on voltage, temperature, discharge rate, age, cell balance and allowed state-of-charge limits. Power capability depends on internal resistance, electrode kinetics, thermal management and protection electronics. A battery with high energy capacity need not provide high short-duration power, and a high-power cell need not provide large total energy. Battery management systems protect cells against overcharge, deep discharge, overcurrent and thermal events; a formula for state of charge is not a substitute for such protection.

## Fundamental relationship, symbols and SI dimensions

`E_stored≈∫V_terminal I dt within stated sign convention; nominal energy ≈ V_nominal×Ah, not exact if voltage varies.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Chemical free-energy differences drive an open-circuit cell potential, while terminal voltage differs under load because of internal losses and polarization. Coulomb counting integrates current but accumulates measurement bias and must be corrected by calibration or independent state estimates. A pack has cell-level safety limits that can bind before the nominal overall energy is exhausted.

## Reconstruct the example without external AI

A nominal 10 V, 100 Ah storage unit is often labeled 1 kWh. Explain why measuring terminal voltage under a varying load is necessary for a better energy estimate, and why 1 kWh capacity does not guarantee that a 2 kW load can be supplied for 30 minutes safely.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not use a simple energy-balance model as battery charging firmware or a safety controller. Chemistry-dependent thermal runaway risks, degradation and BMS limits require separate validated engineering.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 24. Battery charging, round-trip losses, and state of charge

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A useful elementary battery model tracks stored energy in kWh, charge input and delivered discharge power. With fixed one-way efficiencies, stored energy increases by η_charge P_charge Δt and decreases by P_discharge Δt/η_discharge. The difference appears as loss and heat under a chosen accounting boundary. A round trip through the battery returns less electrical energy than supplied unless idealized efficiencies equal one. This says nothing about Coulombic efficiency, calendar aging, nonlinear voltage, cell mismatch or safe charge acceptance. A physically accountable model rejects a step that exceeds capacity rather than silently clipping storage and hiding the excess energy.

## Fundamental relationship, symbols and SI dimensions

`E_next=E_current+η_ch P_ch Δt−P_dis Δt/η_dis; η_roundtrip≈η_chη_dis (matched boundaries).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The relation follows from ordinary energy accounting: input electrical energy times charge efficiency becomes stored chemical energy, while delivered electrical energy requires a larger internal energy decrease. Defining the reference endpoints matters: including inverter and transformer losses changes efficiency. In a multi-hour dispatch the battery's power rating, state-dependent performance and reserve constraints must be modeled in addition to energy capacity.

## Reconstruct the example without external AI

Start with 5 kWh in a 10 kWh idealized battery. Charge at 2 kW for one hour with η_ch=.9, obtaining 6.8 kWh. Then discharge a specified amount and compute how much internally stored energy must be consumed at η_dis=.8.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A step that requests more than available energy is invalid. Automatically changing output without explicitly recording curtailed discharge invents a delivered service that was never supplied.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [DOE Energy Storage Grand Challenge Roadmap](https://www.energy.gov/energy-storage-grand-challenge/articles/energy-storage-grand-challenge-roadmap) — inspected: Energy storage use cases and technology constraints

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 25. Hydrogen and electrochemical conversion pathways

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Hydrogen is an energy carrier produced from other primary energy sources. Electrolysis uses electrical work to split water, while fuel cells can convert chemical reaction free energy into electrical work. Hydrogen production efficiency must specify lower or higher heating value, water conditions and whether heat inputs are included. Storage and transport require compression, liquefaction or other engineering approaches that consume energy and introduce losses. A hydrogen production pathway can be useful for specific industrial feedstocks or storage use cases, but hydrogen conversion is not a net energy source: the energy delivered from a complete production-storage-conversion chain cannot exceed all energy entering its boundary.

## Fundamental relationship, symbols and SI dimensions

`E_electrical_in=E_chemical_H2/η_electrolysis under one declared heating-value convention; E_electric_out≈η_fuelcell E_chemical_H2.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The complete system efficiency is the product of sequential efficiencies under consistent accounting conventions. Changing from LHV to HHV shifts numeric reported percentages without altering physical energy, so reference basis must be stated. Faraday's law connects charge passed to a theoretical amount of electrochemical product, but actual Faradaic efficiency and gas purity require measurements. Real safety includes flammable gas handling, pressure vessels and leak detection.

## Reconstruct the example without external AI

Assume synthetic stage efficiencies .7 for electrolyzer, .9 for storage/transport and .5 for fuel cell. Multiply to get .315 overall energy efficiency, then explain why the result is not a forecast of any specific technology's economics.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not infer water splitting is over-unity because a fuel cell later returns electricity. Hydrogen storage and gas-handling design require accredited safety practice, absent here.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Hydrogen Fuel Basics](https://www.energy.gov/cmei/fuels/hydrogen-fuel-basics) — inspected: Hydrogen carrier, production methods, fuel cells and electrolysis
- [DOE Hydrogen Production: Electrolysis](https://www.energy.gov/cmei/fuels/hydrogen-production-electrolysis) — inspected: Electrolyzer fundamentals and technology types

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 26. Thermal, gravitational, mechanical, and pumped storage

**Area:** Storage. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Electricity can be stored indirectly as gravitational potential, kinetic energy, compressed fluid, phase-change heat or chemical energy. Each mechanism has a different energy density, response time, efficiency, site requirement and durability. Pumped hydro returns water downhill after using electricity to pump it upward, with a round-trip loss. Flywheel energy grows with the square of angular speed, but mechanical stress and containment impose limits. Sensible thermal storage uses heat capacity; phase-change storage adds latent heat at appropriate temperatures. Compressed-air storage interacts with thermodynamics of compression and expansion, so a pressure-only calculation is inadequate. Selecting a technology requires a service definition: seconds of fast response, days of shifting, industrial process heat or seasonal energy supply.

## Fundamental relationship, symbols and SI dimensions

`E_gravity=mgh; E_flywheel=½Iω²; E_sensible≈mcΔT; round-trip η=E_delivered/E_supplied under matched interfaces.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Each expression follows from a work integral under a specified physical model: gravitational work over height, rotational kinetic energy from torque and angular acceleration, and heat capacity from enthalpy change. A real storage system includes friction, converter losses, heat leaks and hardware limits. Stored energy is not automatically recoverable as electricity at a given rated power.

## Reconstruct the example without external AI

For a mass of 1000 kg raised 10 m, compute gravitational storage as 98.1 kJ. Compare with 1 kWh and state why a practical pumped-storage facility requires substantial water flow, head and turbine/generator systems.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Never interpret mechanical storage formulas as instructions to construct high-speed rotors or pressurized vessels. Safe containment, fatigue and fault analysis are specialized fields.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [DOE How Hydropower Works](https://www.energy.gov/cmei/water/how-hydropower-works) — inspected: Flow and head determine hydraulic resource and conversion stages

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 27. Power rating, energy capacity, and capacity factor

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Power capacity states an instantaneous or sustained rate, while energy capacity states how much service can be delivered over time. A 100 kW generator at 50% capacity factor produces half the energy it would produce at continuous full rating over the defined interval, but capacity factor does not equal thermodynamic efficiency. A battery rated at 100 kW and 100 kWh has a nominal one-hour duration at rated power under ideal conversion, yet usable duration depends on efficiency, allowable discharge and temperature. Capacity factors for intermittent sources must be computed over actual hourly generation, not from one favorable period. Outages, dispatch restrictions and curtailment are distinct contributors to lower output.

## Fundamental relationship, symbols and SI dimensions

`Capacity factor CF=E_generated/(P_rated×Δt), 0≤CF≤1 for physical output under the same rating and interval.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The denominator is the hypothetical upper-bound energy if the plant produced nameplate power throughout the period. Actual output integrates instantaneous power. CF is a utilization measure; it does not describe fuel conversion efficiency or operating margins. Comparing technologies requires equivalent measured boundaries and service value, not merely ranking CF.

## Reconstruct the example without external AI

A 100 kW resource delivers 500 kWh during a ten-hour period, so CF=.5. Calculate the same resource's CF if output was curtailed by 100 kWh, and identify whether physical resource, demand or reliability explains the change.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A reported CF above one signals inconsistent rated capacity, measurement scope, time interval or data, rather than a breakthrough in energy conversion.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [EIA Levelized Cost of Electricity Glossary](https://www.eia.gov/tools/glossary/index.php?id=levelized_cost) — inspected: Definition of real levelized cost; project-specific assumptions needed

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 28. Distributed generation, storage dispatch, and unmet load

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A small isolated electrical system must provide sufficient instantaneous power while respecting storage power and energy constraints. A dispatch model consumes timeseries of renewable generation and load, routes surplus into charging where available, and records curtailed generation or imported energy separately. During deficits it discharges storage within limits, then records unmet demand or required grid imports. A daily kWh balance alone cannot guarantee power adequacy at a specific time. Storage dispatch may require forecast uncertainty, reserve policies and reactive power support that a scalar energy model does not provide. A valid ledger must distinguish load actually served from demand requested and must not silently create energy by clipping battery state.

## Fundamental relationship, symbols and SI dimensions

`For each interval: generation + discharge + import = served_load + charge + export + curtailment + losses, with all terms sign-consistent.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The interval balance follows from conservation. A battery step adds state continuity between intervals. If maximum charge and discharge powers are not imposed, a model can make impossible spikes even with adequate total kWh. If reserve and grid-forming requirements are omitted, the result is only an idealized energy feasibility exercise. Matching all energy flows is necessary but insufficient for voltage and frequency stability.

## Reconstruct the example without external AI

Construct a two-hour toy load series 1 kW then 3 kW, with solar 3 kW then 0 and a 2 kWh battery. Allocate surplus and deficit, record charge/discharge losses, and identify any unmet load with no grid connection. Use separate source and storage states.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not claim a functioning or safe microgrid from an energy-only simulation. A grid needs protection, frequency regulation, grounding and synchronized power-electronic controls.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements
- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 29. Renewable variability, curtailment, and temporal matching

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Wind and solar output vary with weather, time and geographic conditions. An average capacity factor cannot reveal whether generation meets load at the right hours. Time correlation between supply and demand, storage duration, interconnection limits and reserve requirements determine reliability. Curtailment means available renewable output is not used because of grid constraints, market signals or equipment conditions; it is not evidence the sunlight or wind contained no energy. A strong analytical library preserves time-series provenance, sampling rate, missing intervals, calendar/time zones, asset rating and measurement uncertainty. Aggregating all hours into one annual energy total can conceal damaging outages.

## Fundamental relationship, symbols and SI dimensions

`Net load(t)=Load(t)−VariableGeneration(t); E_deficit=∫max(0,NetLoad(t))dt under a declared time series and no storage.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The max operator separates deficit periods from surplus. Integrating the signed net load can cancel surpluses and deficits that occur at different times, implying false instantaneous feasibility. Storage can shift some energy but incurs losses, finite duration and finite power. Different weather years can lead to different adequacy outcomes even if annual mean production is similar.

## Reconstruct the example without external AI

Compare two synthetic hours: renewable output 4 kW then 0, load 2 kW each hour. Total generation equals total demand, but without storage the second hour has 2 kWh unmet. Explain the role of a battery and why a 2 kWh nameplate may not suffice with efficiency losses.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not equate annual net-zero energy with continuous reliability or zero environmental impact. The problem is temporal and spatial matching.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 30. Energy economics, discounted cost, and LCOE

**Area:** Economics. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Levelized cost of energy compares discounted lifecycle cost to discounted energy output under a specified project model. It can be useful for alternatives but does not by itself value when electricity is available, how reliably it meets peak demand, local grid constraints or the external impacts of a project. Capital cost, financing, capacity factor, fuel, maintenance, decommissioning, salvage and policy can change results. Real and nominal discount rates must not be mixed with inflation assumptions. A single cost figure cannot represent affordability for every community or determine technology desirability without service and risk analysis.

## Fundamental relationship, symbols and SI dimensions

`LCOE=(C0+Σ_t C_t/(1+r)^t)/(Σ_t E_t/(1+r)^t), in currency/kWh if E in kWh and currency units consistent.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Discounting expresses time preference and financing assumptions by placing future costs and output on a common present-value basis. The formula is an accounting ratio, not a physical law. If production is zero the denominator vanishes, making a numeric cost per kWh undefined. A model that reports LCOE without the generation series, assumptions and full time horizon is not reconstructible.

## Reconstruct the example without external AI

Choose illustrative capital cost 1000 units and ten years of 100 units annual cost and 1000 kWh output, with discount .05. Recompute using the reference code and then reduce generation 30% to see the increase. Do not present synthetic currency units as market prices.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A lower LCOE does not automatically mean lower total system cost. Firm capacity, grid reinforcement, reliability and external impacts are outside this simple formula.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Levelized Cost of Electricity Glossary](https://www.eia.gov/tools/glossary/index.php?id=levelized_cost) — inspected: Definition of real levelized cost; project-specific assumptions needed
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 31. Energy in computation and physical information processing

**Area:** Computing. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Computers consume electricity and dissipate heat while performing information processing. The energy used per operation depends on architecture, memory access, switching activity, voltage, clock rate, data movement, cooling and utilization. A count of model tokens, bit operations or agent steps is not by itself joules consumed. Dynamic CMOS power is approximately proportional to switching capacitance, voltage squared and frequency, subject to technology and workload. Memory bandwidth and cooling can dominate arithmetic energy. Energy efficiency comparisons require equal quality targets, measured power over a full interval and consideration of idle baseline. A routing system that reduces apparent model calls may still increase total energy by performing more memory retrieval or verification.

## Fundamental relationship, symbols and SI dimensions

`P_dynamic≈αCV²f; E_compute=∫P_wall(t)dt; energy per successful task = E_total/N_verified_successes.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Charging/discharging capacitive nodes gives the voltage-squared dynamic-power dependence, with activity factor absorbing average switching. This is a schematic physical model, not a calibrated description of a modern CPU or GPU. To evaluate an AI system, measure wall power and task outcome under identical conditions, including CPU/GPU, network and storage contributions. A reduction in latency is not necessarily energy reduction if active power rises.

## Reconstruct the example without external AI

Measure or hypothesize a 100 W computing system running for 30 seconds: 3000 J. If 10 tasks ran but only 5 were independently verified successful, energy per successful task is 600 J under the measured boundary. Explain how idle power changes that comparison.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

No Bitwork energy-saving advantage can be established from a frequency-only synthetic benchmark or from token counts without actual hardware measurements at controlled task quality.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 32. Energy measurements, uncertainty, and calibration

**Area:** Metrology. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

A scientific energy measurement begins by defining the measurand: electrical energy delivered to a load, chemical energy content of fuel, net heat transfer, or whole-facility electricity. Instruments have calibration uncertainty, resolution, drift, bandwidth, phase error and sampling limits. Measuring voltage and current separately does not always recover instantaneous real power, particularly with phase shift or distorted waveforms; a proper power analyzer integrates their product with synchronized sampling. Measurement uncertainties can be correlated, making simple independent-root-sum-of-squares formulas inadequate. A reconstructible result preserves device, calibration record, measurement interval, reference conditions and uncertainty propagation.

## Fundamental relationship, symbols and SI dimensions

`E≈Σ_i (P_i+P_(i+1))/2 × Δt_i for trapezoidal interpolation; u_y²≈Σ_i(∂f/∂x_i)²u_i² plus covariance terms.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Trapezoidal integration is exact for linear power variation between samples, but real transients between measurement points can be missed. Error propagation follows first-order linearization of the measurement model around estimates; it is not automatically valid for large nonlinear or non-Gaussian uncertainty. A robust study includes a second measurement method or known calibration source where possible.

## Reconstruct the example without external AI

Integrate three synthetic samples (t=0,10,20 s; P=10,10,20 W), giving 250 J by trapezoidal rule. Describe a pulse between samples that this calculation would completely miss. State an appropriate sampling or anti-aliasing plan.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A numerical result with many decimal places does not prove high physical accuracy. Calibration and timing traceability determine the defensible significant figures.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context
- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 33. Efficiency versus exergy versus capacity factor

**Area:** Metrology. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Energy conversion efficiency, thermodynamic exergetic efficiency, round-trip storage efficiency and generator capacity factor answer different questions. An electric motor can have high conversion efficiency while running only a few hours; its capacity utilization is then low. A heat pump can have COP greater than one while obeying the first and second laws. A thermal engine is bounded by the temperature of its heat source and sink. A perfect first-law balance can still have enormous exergy destruction through mixing or friction. A robust comparison must preserve each metric's numerator, denominator, source boundary, time interval and quality of output.

## Fundamental relationship, symbols and SI dimensions

`η_converter=E_useful/E_in≤1 under ordinary conversion; COP_heating=Q_delivered/W_input; CF=E_generated/(P_rated Δt).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The distinctions arise from different accounting denominators. A heat pump counts thermal energy moved from the environment as useful delivery, unlike a passive conversion ratio. A capacity factor compares delivered energy against rated full-power potential over time. An exergetic metric estimates useful work potential relative to environment. Conflating the metrics creates false over-unity headlines or misleading technology rankings.

## Reconstruct the example without external AI

Compare a 70%-efficient conversion device, a heat pump with COP 3, and a generator with CF .3. Describe what the number means in each case and why there is no simple universal ordering of energy performance.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A device efficiency greater than 100% is suspicious only after its precise definition is identified. Claims of net energy creation remain inconsistent with conservation unless unreported inputs or boundaries resolve the discrepancy.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context
- [ENERGY STAR Geothermal Heat Pumps Efficiency Criteria](https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria) — inspected: Definition and rating framework for coefficient of performance; product-specific ratings vary

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 34. Lifecycle impacts, carbon accounting, and resource constraints

**Area:** Metrology. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Energy technologies have impacts across materials extraction, fabrication, construction, operation, fuel supply, maintenance and end of life. Direct plant-stack emissions are not the same as lifecycle greenhouse-gas intensity. A battery or solar panel may have zero direct combustion emissions during operation but embodied manufacturing impacts, land/water demand and recycling constraints. Assessments must state functional unit such as grams CO2-equivalent per delivered kWh, system boundary, grid mix, recycling allocation and time horizon. Numeric environmental comparisons should come from harmonized datasets, not invented generic constants. Economic and climate objectives can conflict with local ecological or social constraints.

## Fundamental relationship, symbols and SI dimensions

`I_lifecycle=(Σ stage emissions_kgCO2e)/(Σ life delivered kWh), under documented boundary and attribution method.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The ratio is an inventory quotient, not a universal physical property of a technology. Its denominator can vary with device life, degradation, climate and curtailment; the numerator can vary with the electricity mix used in manufacture and accounting conventions. Independent lifecycle evidence requires audited upstream inputs and sensitivity analysis. An energy-only model cannot validate greenhouse-gas emissions or social effects.

## Reconstruct the example without external AI

Use a constructed device with 1000 kgCO2e embodied impact and 10000 kWh lifetime delivery, yielding 0.1 kgCO2e/kWh. Halve its lifetime production and demonstrate that intensity doubles. Explain why this example is not a measured technology result.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not assign a zero lifecycle impact to a zero-stack-emission resource, or confuse different CO2-equivalence time horizons and allocation rules.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 35. Resilient power: microgrids, islanding, and critical loads

**Area:** Infrastructure. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Power resilience means preserving essential services despite disruptions. A robust microgrid must identify critical loads, generator and storage operating constraints, fault detection, protection, grid-forming controls, communications, fuel supplies and trained operators. The sequence of safe islanding and reconnection is specific to equipment and utility interconnection rules. A simplified energy budget can estimate whether a hospital's nominal battery stores enough kWh, but cannot guarantee safe operation under high inrush currents, reactive loads, faults or equipment failure. Recovery priorities also depend on human needs, not just objective functions. A survival atlas should teach the distinction between energy planning and legally authorized electrical operations.

## Fundamental relationship, symbols and SI dimensions

`Critical-load energy minimum E_need≈∫P_critical(t)dt; storage usable delivery < nameplate capacity after SOC reserve and conversion losses.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

The expression integrates demand, but a real plan must check peak kW, power quality, switching and fault capability. Resilience also requires scenario analysis: cloudy periods, fuel interruption, battery faults and communication loss can be correlated. A design that meets average load may still fail an emergency peak. Service restoration must be supervised by qualified professionals with tested emergency procedures.

## Reconstruct the example without external AI

Construct an emergency schedule with one 500 W critical load for 8 hours: 4 kWh before storage losses. Compare to a nominal 5 kWh battery at 80% usable depth of discharge and 90% discharge efficiency, giving only 3.6 kWh delivered; identify the deficit.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

Do not energize emergency electrical equipment or attempt grid islanding from this manual. Protective coordination, certification and qualified engineering are essential.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [EIA Electricity Explained: Delivery to Consumers](https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php) — inspected: Generation, transformers, transmission and distribution, grid delivery overview
- [DOE Energy Storage Strategy and Roadmap](https://www.energy.gov/oe/energy-storage-strategy-and-roadmap) — inspected: Energy storage technology and deployment; cross-technology requirements

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 36. Reconstruction of energy systems after infrastructure loss

**Area:** Preservation. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Preserving energy knowledge for future generations requires more than an encyclopedia of device names. The library should make it possible to trace a physical service—light, heating, refrigeration, pumping or communications—from energy resource to useful demand through conversion and control. A future reader needs original principles, material properties with source and temperature, calibrated measurement practices, construction standards and safety limitations. It is important to preserve what is not included: this research version cannot safely instruct a nonexpert to build a high-voltage substation, pressure plant or nuclear reactor. Rebuilding technical civilization demands trained people, supply chains and verified standards as well as equations.

## Fundamental relationship, symbols and SI dimensions

`Reconstruction chain: resource → conversion → transmission/storage → controlled load → independently measured service, with signed energy ledger at each stage.`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

A system-of-systems argument requires every interface to preserve units, time basis and conservation. The receiving system's efficiency and operating envelope depend on upstream outputs and downstream loads. For example, a solar array, inverter and battery may each have a valid small-model equation, but combining them safely requires live protection and power-control specifications not represented in this corpus. Complete method reconstruction includes installation constraints, maintenance, calibration and failure diagnosis, and each missing piece should be named.

## Reconstruct the example without external AI

Start with the goal of powering a 10 W communications radio for 24 hours. Compute 240 Wh ideal load, then add a declared converter loss and storage reserve. Explain why the energy estimate does not certify antenna operation, battery safety, or power quality.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

The term “humanity's last knowledge” is an acceptance aspiration. Energy Atlas v0.1 is not a complete primary-source archive, qualified engineering specification or substitute for safety expertise.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [BIPM The International System of Units (SI) Brochure, ninth edition](https://www.bipm.org/en/publications/si-brochure) — inspected: Energy, power, voltage and electrical units, formal SI definitions
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.



---


# 37. From energy science to survival services

**Area:** Survival Systems · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Energy security is not identical to having energy in storage. A person needs services such as potable water, sanitation, thermal shelter, lighting, refrigeration, communications and safe transport. Each service has a demand profile, tolerances, start-up requirements, duration, and an acceptable interruption policy. An ideal 10 kWh energy budget does not establish that a motor can be started, a medical device remains continuously powered, or a community can operate a pump safely. Begin with a service inventory that distinguishes what must run continuously, what can be scheduled, and what cannot accept fractional power. Identify who is authorized to decide priorities, how actual requirements were obtained, and what evidence would show that a service was truly delivered. A source text containing a favorable model score is not confirmation of life-safety continuity.

## Equation, symbols and dimensional units

`For service j: E_j=integral P_j(t)dt, with P in kW and t in h yielding kWh. Served fraction E_served,j/E_requested,j is a descriptive energy metric, not a clinical or safe-operation reliability guarantee.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

For piecewise constant time blocks, multiply demand power by each interval duration and add. A service that needs continuous minimum input introduces constraints that pure summation omits: a device might consume 1 kWh in one hour but fail if its power is interrupted for five minutes. Peak demanded power, inrush, frequency, voltage, acceptable downtime and energy requirements must be carried separately. “Priority” is a declared human governance rule, not a formula that proves one service should be favored. The energy service inventory becomes an input to mathematical studies, not an autonomous controller.

## Hand reconstruction and independent calculation

Construct an invented shelter profile: lighting 0.15 kW for four hours, pump 0.6 kW for one hour, refrigeration 0.08 kW average for 24 hours, and communications 0.025 kW for 24 hours. Compute 0.6+0.6+1.92+0.6 = 3.72 kWh/day, then explain why the instantaneous power ceiling and equipment start-up still need separate assessment. Use the energy service card to document uncertainty in those invented average values.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

The sum is not a complete building energy model. Refrigeration demand depends on ambient temperature and duty cycle; critical medical care must not be planned from this generic arithmetic. A model with enough daily kWh can still fail because it lacks appropriate instantaneous power, protection, cooling, controls or qualified maintenance.

## Life safety and operational boundary

This text is a scientific reference, not a construction approval. A qualified professional must review real electrical hazards and life-critical service requirements before field implementation.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


# 38. Multi-interval microgrid energy accounting

**Area:** Survival Systems · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A microgrid is a bounded set of loads and resources that may operate connected to a larger electrical network or islanded under properly designed controls and protection. In a survival context the first numerical study is a time-resolved energy ledger: generation, load, stored energy, conversion losses, curtailment, imports and unserved demand. That accounting reveals when an assumed resource portfolio is insufficient. It does not model AC voltage, grid-forming controls, transfer-switch correctness, frequency regulation, neutral/ground bonding, relay coordination, or inverter fault behavior. The DOE resilience reference explicitly distinguishes ordinary grid-dependent solar from a properly configured independent solar-plus-storage system. Passing an energy ledger cannot override that requirement.

## Equation, symbols and dimensional units

`For interval i: (generation_i + imports_i - served_i - curtailed_i)*Delta t_i = Delta storage_i + conversion_loss_i, with power in kW and time in hours.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

This is conservation of energy across the declared modeled boundary. Renewable power first serves a stipulated load, then can charge a storage abstraction within its charge-power and energy bounds. A deficit can discharge storage subject to a discharge-power ceiling and efficiency, otherwise it is recorded as unmet load or a hypothetical grid import. Summing interval residuals tests internal bookkeeping. It does not establish that grid-connected power is available unless the scenario explicitly says so, or that the storage hardware can perform the requested duty. To call a field installation resilient would require data on faults, islanding transition, protection, startup, equipment ratings and controls.

## Hand reconstruction and independent calculation

Run a three-hour constructed scenario: solar 4 kW/0/0, load 2/3/3 kW, initial battery 1 kWh, capacity 4 kWh, charging/discharging maxima 2 kW with efficiencies 0.9. Calculate charge, curtailment, discharge, remaining load and conversion losses for each hour. Verify the total ledger residual is near zero, and inspect the nonzero unmet demand rather than renaming it a successful supply.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

The model is energy-only. It assumes an ideal available grid whenever flagged and no dangerous wiring procedure. A single weather trace is not a statistical resilience guarantee, nor is a battery represented by a single exact state of charge physically complete.

## Life safety and operational boundary

Never energize or island a real electrical installation from the model output. Grid interconnection, transfer switching and protections require qualified engineering and applicable codes.

## Source navigation and preservation debt

- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **DOE Energy Storage Strategy and Roadmap:** https://www.energy.gov/oe/energy-storage-strategy-and-roadmap — Energy storage technology and deployment; cross-technology requirements

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


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



---


# 40. Storage fire safety and thermochemical limits

**Area:** Storage · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Electrochemical storage contains energy in materials that may react during failure. Thermal runaway, venting, flammable gases, propagation between cells and inadequate fault isolation are separate hazard pathways. Safe system design requires independent evidence for cell chemistry, pack architecture, state of charge, thermal environment, ventilation, fire detection, spacing, response plans, and local regulation. Calculated voltage, capacity or round-trip efficiency does not verify any of these. The 2026 NFPA 855 standard contains installation and emergency-response requirements; its content remains copyrighted and was not copied into this library. EPA public guidance describes battery incidents and safety standards, but neither document constitutes certification of an unspecified design.

## Equation, symbols and dimensional units

`Energy available for release is not a fire-risk probability. E_chemical ≈ V_nominal*Ah (Wh) under a crude electrical nameplate model, not a heat-release-rate or explosion calculation.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

An electrical energy label reports nominal electrical work under an operating convention. During abuse or failure, heat can also arise from exothermic chemical pathways, so equating electrical nameplate energy to maximum fire heat release is unjustified. Accurate hazard assessment requires measured calorimetry, gas composition, cell and pack standards, and independent validation. A simplified charge/discharge model must never infer thermal-runaway thresholds or fire-suppression actions.

## Hand reconstruction and independent calculation

Read a hypothetical pack label of 48 V and 100 Ah and compute 4.8 kWh nominal electrical capacity. Record that the calculation does not say the pack is safe, whether it has protection, how it would behave under a short circuit, or its energy under failure. Build a source card listing manufacturer documents and applicable qualified tests needed before any physical evaluation.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Lithium battery faults can escalate rapidly. The package contains no DIY battery-building, short-circuit, cell venting or suppression instructions. Energy accounting does not establish electrical or fire safety.

## Life safety and operational boundary

Real battery installation and emergency response require current codes, certified hardware and local competent authorities; no remote model supplies permission or safety certification.

## Source navigation and preservation debt

- **U.S. EPA, Battery Energy Storage Systems Safety and Incident Response:** https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe — Battery fire response, community planning, relevant standards; no site engineering standard reproduced
- **NFPA 855, Stationary Energy Storage Installation Standard, 2026 edition:** https://www.nfpa.org/product/nfpa-855-standard/p0855code?l=134 — Product description and 2026 edition overview only; standard is copyrighted and full clauses were not acquired
- **DOE Energy Storage Strategy and Roadmap:** https://www.energy.gov/oe/energy-storage-strategy-and-roadmap — Energy storage technology and deployment; cross-technology requirements

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


# 41. Renewable variability, seasonality and adverse scenarios

**Area:** Survival Systems · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A single annual solar-energy average cannot establish that a system survives an extended winter storm or a series of cloudy days. Weather, resource availability and demand are temporally correlated; a high mean generation figure may hide a prolonged zero-output period. A robust first step is to preserve ordered time series of resource and demand under named scenarios, compute shortages and reserve depletion, then ask what range of unobserved conditions remains. The worst outcome among a small set of user-authored scenarios is not a statistical worst case for the local climate. Actual resilience engineering needs representative long-term measured data, correlation, uncertainty, equipment failures and plans for replenishment. The source data should include timestamp, measurement units, location/conditions, original bytes, sensor and version rather than only smooth charts.

## Equation, symbols and dimensional units

`For each scenario s: U_s = sum_i unmet_load_(s,i)*Delta t_i; U_worst_supplied=max_{s in S} U_s. This is a deterministic scenario statistic, not an expected shortage or a bound over every possible scenario.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

The max operation compares only the scenarios actually provided. Probability of failure requires a defensible sampling distribution over events, not a collection of plausible anecdotes. A chronological battery model must respect earlier charging and depletion; reordering the same daily totals can change unserved energy. A simulation that reports 0 unmet energy but lacks an islanding inverter, protection or a valid start condition cannot establish real uptime.

## Hand reconstruction and independent calculation

Compare two invented two-hour cases with 2 kWh initial capacity, a 1 kW discharge cap, and 0.9 efficiency: (A) load 1 kW, generation 2 kW; (B) load 3 kW, generation 0. Run both and identify the case with greater unserved energy. Add a third case with a two-day sequence to show why the order of wind/solar supply matters.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

“Worst of our tests” is not “worst imaginable weather.” Without actual resource measurement and equipment state, the profile cannot determine the safety of a site. Do not extrapolate from 2–3 illustrative intervals to multi-season survival.

## Life safety and operational boundary

This is scenario arithmetic only; emergency preparedness decisions require site data, qualified design and alternate safe evacuation/assistance plans.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **DOE Solar Photovoltaic Technology Basics:** https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics — Solar cell, module, arrays, and DC/AC system concept

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


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



---


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



---


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



---


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



---


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



---


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



---


# 48. Reliability indicators: unmet energy is not outage probability

**Area:** Resilience · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A survival power service is judged by the services it reliably provides. In an offline energy ledger, unserved energy is the positive sum of demanded electrical energy not supplied during the given intervals; the proportion unserved is that amount divided by requested energy. Counting the number of intervals with a shortage is another descriptive statistic. In probabilistic reliability analysis, expected energy not served (EENS) requires a probability measure over system states, weather, outages and failures; loss-of-load expectation and probability similarly depend on an event model. A fixed synthetic scenario does not establish an expectation. Explicitly naming denominators and observed or stipulated inputs prevents inflated claims of system endurance.

## Equation, symbols and dimensional units

`U(profile)=sum_i P_unserved,i*Δt_i. Unserved_share=U/sum_i P_load,i*Δt_i when demand>0. EENS=E_ω[U(ω)] requires a validated scenario distribution.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

A deterministic energy ledger integrates unserved power. It can be internally valid for one sequence even if its assumptions about generator availability are unrealistic. To calculate expectation, scenarios must have normalized probabilities with a defensible basis, or a statistically supported stochastic process. Samples are not independent simply because they contain different random seeds: correlated weather and equipment conditions can dominate failures. Service interruption count is not automatically equivalent to the number of people harmed or a medically unacceptable outage.

## Hand reconstruction and independent calculation

For an invented two-hour outage, load 3 kW each hour, supply 1 kW in the first hour and 0 kW in the second. Unserved energy is (2+3)*1=5 kWh of 6 kWh demanded, an 83.3% share. This is not an 83.3% probability of system failure; without event probabilities there is no expected metric.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Do not label maximum unserved energy among a few cases as a universal worst case. Real protection, failure modes, load volatility and supply variance are absent from energy-only models.

## Life safety and operational boundary

Critical system continuity must be independently qualified; no reliability label in this archive authorizes an actual electrical installation.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **NIST Measurement Uncertainty Guidance:** https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty — Measurement uncertainty, measurand, instrument and calibration context

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


# 49. Metrology and source recovery under infrastructure failure

**Area:** Preservation · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

If energy science must survive the loss of internet access and specialized vendors, numerical results need more than a copied constant. Each measurable quantity requires a definition, unit, reference state, measuring instrument, calibration method, uncertainties, and original evidence where permitted. The NIST 2022 CODATA adjustment supplies recommended values as of its declared scientific edition; exact SI defining constants must be distinguished from experimentally adjusted constants with standard uncertainties. The current Atlas contains derived constants in its own JSON but does not retain the original NIST publication bytes. This remains a documented preservation deficit, not a reason to invent a primary-source file or label a table authenticated from memory.

## Equation, symbols and dimensional units

`A measured quantity is reported as x ± u with unit and coverage convention. Dimensionless residual of balance r=(Ein−Eout−ΔEstored)/scale is an internal closure check, not experimental validation.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

To reconstruct a claim, record the traceable source URL/DOI/edition, publisher attribution, explicit value, uncertainty and covariance where applicable, and measurement conditions. For a derived result, state how uncertainty propagates and whether inputs are correlated. A near-zero energy-balance residual on invented numbers shows only that the arithmetic conserves its own bookkeeping. An engineer should also investigate unmodeled energy paths, sensor bias, sampling rates, rounding and operating regimes. Software tests provide regression evidence but cannot certify a real sensor or generator.

## Hand reconstruction and independent calculation

Compare exact c = 299,792,458 m/s (defined SI) with a non-exact measurement such as Newtonian gravitational constant G, whose CODATA recommendation carries uncertainty. Create a record distinguishing exact definition from measured adjusted value; then locate the original source document or explicitly mark it unavailable. Do not invent the uncertainty value when the source is inaccessible.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

A DOI is a locator, not an archived original. Publisher PDFs and normative standards may have copyright/rights restrictions. A copied checksum without original authenticated bytes is not a fixity proof of those bytes.

## Life safety and operational boundary

Only rights-cleared original materials with verifiable source hashes can move into a higher evidence level; otherwise preserve original explanation and the missing-source gap.

## Source navigation and preservation debt

- **NIST CODATA Recommended Fundamental Physical Constants, 2022 adjustment, 2025 publication:** https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022 — Publication metadata for 2022 adjustment, distinction between exact SI constants and adjusted measured values; full PDF not downloaded
- **NIST Measurement Uncertainty Guidance:** https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty — Measurement uncertainty, measurand, instrument and calibration context
- **BIPM The International System of Units (SI) Brochure, ninth edition:** https://www.bipm.org/en/publications/si-brochure — Energy, power, voltage and electrical units, formal SI definitions

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


# 50. Reconstructing community-scale energy knowledge from first principles

**Area:** Preservation · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

A future reader with only text and a calculator should be able to reconstruct a minimal energy budget: identify services, measure or reasonably estimate demand, convert all quantities to SI units, document sources and assumptions, calculate resource output and conversion limits, track storage and losses, and compare scenario shortfalls. The reader must also understand where a model stops: independently safe wiring, generator placement, battery fire protection, potable water treatment, fuel logistics and utility interconnection require contemporary local expertise and tested equipment. The Atlas should preserve those boundaries, not hand-wave them away with a high test count. Its most important survival property is to retain methods for discovering what is unknown and rebuilding evidence when equipment or primary publications are missing.

## Equation, symbols and dimensional units

`E_balance = Σ generated + imported − served − curtailed − Δstored − conversion_losses ≈ 0 for a modeled boundary. Safety_verified and reliability_verified remain separate variables without a value inferred from zero residual.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

Conservation provides an essential consistency condition: if inputs exceed modeled outputs and storage changes, either losses, boundary definitions, sensors or arithmetic are incomplete. A positive residual is a lead for investigation, not proof of a new energy source. An equal zero residual can occur by construction even when every input is fabricated. Survival engineering needs field-calibrated measurement and trustworthy institutions along with derivations and mathematics. Knowledge preservation means retaining the causes and counterexamples, not a simplified checklist of attractive answers.

## Hand reconstruction and independent calculation

Take one hypothetical day with 5 kWh solar input, 3 kWh of served electricity, 1 kWh of curtailed generation, and 0.5 kWh increase of storage. The remaining 0.5 kWh must be accounted for as modeled conversion losses or an unresolved residual. Recalculate with one factor intentionally omitted and record the discrepancy. Then list the missing physical safety and supply-chain evidence rather than declaring a working microgrid.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

This chapter is an offline educational reconstruction, not a construction guide for high-voltage wiring, improvised fuel, unsafe heating or potentially contaminated water. The full body of human energy science extends far beyond 50 chapters.

## Life safety and operational boundary

Always keep emergency safety and public-health knowledge alongside physical equations. At a real installation, follow qualified local codes, standards and service authorities.

## Source navigation and preservation debt

- **U.S. DOE, Solar and Resilience Basics:** https://www.energy.gov/cmei/systems/solar-and-resilience-basics — Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics:** https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics — Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- **U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages:** https://www.cdc.gov/carbon-monoxide/about/index.html — Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.



---


# Scientific source register

# Energy Atlas scientific source register v0.1.0

**All 20 source cards are link/selected-page references only**. Primary original transport bytes were not acquired. Licensed primary-copy acquisition and expert review remain open.

## BIPM-SI — BIPM The International System of Units (SI) Brochure, ninth edition

- URL: https://www.bipm.org/en/publications/si-brochure
- Inspected extent: Energy, power, voltage and electrical units, formal SI definitions
- State: selected_official_publisher_page
- Rights: BIPM reproduction conditions apply; no PDF transport bytes archived
- Original publisher bytes present: **no**. Expert human validation: **no**.

## NIST-CODATA — NIST CODATA 2022 recommended fundamental physical constants

- URL: https://physics.nist.gov/cuu/Constants/
- Inspected extent: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants
- State: selected_official_publisher_page
- Rights: NIST database may include non-U.S. Government authorship; specific reuse status requires review
- Original publisher bytes present: **no**. Expert human validation: **no**.

## NIST-WEBBOOK — NIST Chemistry WebBook SRD 69

- URL: https://webbook.nist.gov/chemistry/
- Inspected extent: Thermodynamic data types and dependence on state, material, reference condition
- State: selected_official_publisher_page
- Rights: Database may contain compiled non-government contributions; no values mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## NIST-UNCERTAINTY — NIST Measurement Uncertainty Guidance

- URL: https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty
- Inspected extent: Measurement uncertainty, measurand, instrument and calibration context
- State: selected_official_publisher_page
- Rights: Publisher rights vary, no original bytes archived
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-HEATPUMP — ENERGY STAR Geothermal Heat Pumps Efficiency Criteria

- URL: https://www.energystar.gov/products/geothermal_heat_pumps/key_product_criteria
- Inspected extent: Definition and rating framework for coefficient of performance; product-specific ratings vary
- State: selected_publisher_page
- Rights: Program specification may change; not a guarantee of real unit performance
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-EFFICIENCY — DOE Energy Efficiency Versus Energy Intensity

- URL: https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity
- Inspected extent: Efficiency differs from sector intensity and structural changes
- State: selected_official_page
- Rights: Original text not mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## EIA-GRID — EIA Electricity Explained: Delivery to Consumers

- URL: https://www.eia.gov/energyexplained/electricity/delivery-to-consumers.php
- Inspected extent: Generation, transformers, transmission and distribution, grid delivery overview
- State: selected_official_page
- Rights: EIA text and diagrams not mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-PV — DOE Solar Photovoltaic Technology Basics

- URL: https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics
- Inspected extent: Solar cell, module, arrays, and DC/AC system concept
- State: selected_official_page
- Rights: No third-party images or technology specifications mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-PV-EFF — DOE Solar PV Performance and Efficiency Basics

- URL: https://www.energy.gov/cmei/systems/solar-photovoltaic-performance-and-efficiency-basics
- Inspected extent: Conversion efficiency, IV curves, temperature and spectral effects
- State: selected_official_page
- Rights: Not a complete device database or site-specific resource study
- Original publisher bytes present: **no**. Expert human validation: **no**.

## SANDIA-PVWATTS — Sandia PV Performance Modeling Collaborative: PVWatts

- URL: https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/point-value-models/pvwatts/
- Inspected extent: PVWatts basic power/irradiance/temperature point model; versions and low-light rules differ
- State: selected_official_page
- Rights: The offline implementation is original simplification, not identical to an audited full PVWatts release
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-WIND — DOE How Do Wind Turbines Work?

- URL: https://www.energy.gov/cmei/systems/how-do-wind-turbines-work
- Inspected extent: Wind turbines use aerodynamic lift/drag to rotate generators; resource and designs vary
- State: selected_official_page
- Rights: Text/illustration not mirrored; Betz bound is standard ideal actuator-disk result, not independently rederived by DOE page
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-HYDRO — DOE How Hydropower Works

- URL: https://www.energy.gov/cmei/water/how-hydropower-works
- Inspected extent: Flow and head determine hydraulic resource and conversion stages
- State: selected_official_page
- Rights: Not water resource or ecological assessment
- Original publisher bytes present: **no**. Expert human validation: **no**.

## EIA-GEOTHERMAL — EIA Geothermal Explained

- URL: https://www.eia.gov/energyexplained/geothermal/
- Inspected extent: Geothermal heat and direct-use/electricity pathways
- State: selected_official_page
- Rights: No reservoir data or site-specific feasibility archived
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-NUCLEAR — DOE Nuclear 101: How Does a Nuclear Reactor Work?

- URL: https://www.energy.gov/ne/articles/nuclear-101-how-does-nuclear-reactor-work
- Inspected extent: Fission heat, cooling, steam turbines and electrical generation overview
- State: selected_official_page
- Rights: No reactor operation, materials or safety manual mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-FUSION — DOE Fusion Energy Sciences

- URL: https://www.energy.gov/science/fes/fusion-energy-sciences
- Inspected extent: Fusion physics and unresolved materials, fuel-cycle, plasma and commercial engineering gaps
- State: selected_official_page
- Rights: Program descriptions do not prove net commercial electric generation
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-STORAGE — DOE Energy Storage Strategy and Roadmap

- URL: https://www.energy.gov/oe/energy-storage-strategy-and-roadmap
- Inspected extent: Energy storage technology and deployment; cross-technology requirements
- State: selected_official_page
- Rights: Not a battery performance dataset or safety certification
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-ESGC — DOE Energy Storage Grand Challenge Roadmap

- URL: https://www.energy.gov/energy-storage-grand-challenge/articles/energy-storage-grand-challenge-roadmap
- Inspected extent: Energy storage use cases and technology constraints
- State: selected_official_page
- Rights: 2020 roadmap targets not reported as achieved in 2026
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-HYDROGEN — DOE Hydrogen Fuel Basics

- URL: https://www.energy.gov/cmei/fuels/hydrogen-fuel-basics
- Inspected extent: Hydrogen carrier, production methods, fuel cells and electrolysis
- State: selected_official_page
- Rights: Operational procedures, emissions data and original values not mirrored
- Original publisher bytes present: **no**. Expert human validation: **no**.

## DOE-ELECTROLYSIS — DOE Hydrogen Production: Electrolysis

- URL: https://www.energy.gov/cmei/fuels/hydrogen-production-electrolysis
- Inspected extent: Electrolyzer fundamentals and technology types
- State: selected_official_page
- Rights: No instructions for untrained gas production, high-pressure equipment or plant design
- Original publisher bytes present: **no**. Expert human validation: **no**.

## EIA-LCOE — EIA Levelized Cost of Electricity Glossary

- URL: https://www.eia.gov/tools/glossary/index.php?id=levelized_cost
- Inspected extent: Definition of real levelized cost; project-specific assumptions needed
- State: selected_official_page
- Rights: No current market prices or validated local project costs archived
- Original publisher bytes present: **no**. Expert human validation: **no**.


## New v0.2.0 public source-scoped references (8; not archived originals)

### DOE-RESILIENCE: U.S. DOE, Solar and Resilience Basics

- Official link: https://www.energy.gov/cmei/systems/solar-and-resilience-basics
- Inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- Rights: official DOE public HTML, selected scope only
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### DOE-MICROGRID: U.S. DOE, Distributed Energy Resources and Microgrids Basics

- Official link: https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics
- Inspected portion: Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited
- Rights: official DOE public HTML, selected scope only
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### EPA-BESS-SAFETY: U.S. EPA, Battery Energy Storage Systems Safety and Incident Response

- Official link: https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe
- Inspected portion: Battery fire response, community planning, relevant standards; no site engineering standard reproduced
- Rights: official EPA public HTML, selected scope only
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### NFPA-ESS-2026: NFPA 855, Stationary Energy Storage Installation Standard, 2026 edition

- Official link: https://www.nfpa.org/product/nfpa-855-standard/p0855code?l=134
- Inspected portion: Product description and 2026 edition overview only; standard is copyrighted and full clauses were not acquired
- Rights: rights-restricted publisher overview, no full technical standards text
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### CDC-CO-2026: U.S. CDC, Avoiding Carbon Monoxide Poisoning During Power Outages

- Official link: https://www.cdc.gov/carbon-monoxide/about/index.html
- Inspected portion: Portable-generator carbon monoxide risks and outdoor operating safety; not generator integration design
- Rights: official CDC public HTML; selected public-health recommendations
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### EPA-EMERGENCY-WATER: U.S. EPA, Emergency Disinfection of Drinking Water

- Official link: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water
- Inspected portion: Public-health distinction between microbial disinfection and chemical contamination; this Atlas does not implement treatment procedures
- Rights: official EPA public HTML; sanitation data cannot be inferred from thermal energy
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### CDC-WATER-2024: U.S. CDC, How to Make Water Safe in an Emergency

- Official link: https://www.cdc.gov/water-emergency/about/index.html
- Inspected portion: Emergency potable-water advisories; treatment and health depend on hazard category
- Rights: official CDC public HTML, selected public-health scope only
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.

### NIST-CODATA-2022-PUB: NIST CODATA Recommended Fundamental Physical Constants, 2022 adjustment, 2025 publication

- Official link: https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022
- Inspected portion: Publication metadata for 2022 adjustment, distinction between exact SI constants and adjusted measured values; full PDF not downloaded
- Rights: official NIST bibliographic record, not original paper bytes
- Original publisher bytes locally retained: **no**. Independent reviewer: **no**.


