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
