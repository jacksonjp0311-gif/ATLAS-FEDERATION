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
