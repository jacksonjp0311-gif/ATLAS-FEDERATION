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
