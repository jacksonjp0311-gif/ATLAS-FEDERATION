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
