# 63. Repair the evidence before repairing the energy system

**Domain:** Maintenance and verification. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Survival-scale energy infrastructures need both repair knowledge and disciplined evidence. When power is lost, an engineer distinguishes the system state, measured symptoms, suspected mechanisms, and permitted actions. A missing solar output can reflect darkness, anti-islanding protection, converter faults or upstream electrical interruption. A battery can report state of charge yet be unable to deliver rated power. Blindly changing connections can create additional hazards. This chapter presents a research diagnostic sequence of observations and assumptions, not an operating procedure for energized equipment.

## Formula, units and preconditions

`Candidate cause H_i; observed evidence O; posterior P(H_i|O) ∝ P(O|H_i) P(H_i), conditional on a specified model and credible measurement channels.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

Each hypothesis should make a discriminating prediction. Without measured likelihoods and priors the equation is a framework, not a calibrated fault diagnosis. A safe investigation records time, source, measurement uncertainty, control state and independent observation, then compares results with expected boundaries. Any intervention should be reviewed for hazards and permissions. Retain failed hypotheses and contradictory evidence; erasing them loses the ability to understand recurrent failures.

## Reconstruct by hand and compare against code

Suppose a source shows zero delivered electrical power. List two competing explanations: source generation absent and inverter intentionally disconnected under utility outage. They predict different observations about daylight and grid state. Write a table of predicted signals, then mark as “unknown” any measurement that was not actually obtained. No live troubleshooting is performed.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Even well-matched symptoms do not identify a cause without adequate instrumentation, model validity and alternative explanations. Model confidence cannot substitute for grounding or protective inspection.

## Life-safety and professional boundary

The Atlas contains no live electrical repairs, override codes or hazardous fault-induction instructions. Real maintenance requires qualified personnel, manufacturer procedures and safe isolation.

## Source provenance (links only)

- **U.S. DOE, Solar and Resilience Basics** — https://www.energy.gov/cmei/systems/solar-and-resilience-basics; inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected
- **Sandia National Laboratories, Microgrid Design Toolkit** — https://energy.sandia.gov/programs/electric-grid/advanced-microgrids/microgrid-design-toolkit/; inspected portion: Official description of early-stage multiobjective microgrid design, cost-performance-reliability tradeoffs
- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
