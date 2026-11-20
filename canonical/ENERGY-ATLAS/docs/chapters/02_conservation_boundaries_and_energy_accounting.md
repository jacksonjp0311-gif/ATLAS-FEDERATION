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
