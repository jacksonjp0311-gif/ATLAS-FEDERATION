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
