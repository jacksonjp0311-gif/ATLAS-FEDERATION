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
