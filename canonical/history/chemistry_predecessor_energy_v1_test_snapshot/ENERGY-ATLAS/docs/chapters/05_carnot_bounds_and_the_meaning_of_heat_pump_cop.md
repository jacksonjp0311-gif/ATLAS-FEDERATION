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
