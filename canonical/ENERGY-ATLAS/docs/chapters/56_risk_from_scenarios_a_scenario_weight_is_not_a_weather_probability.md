# 56. Risk from scenarios: a scenario weight is not a weather probability

**Domain:** Uncertainty and resilience. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Energy systems face interacting uncertainties: renewable supply, equipment failures, fuel logistics, demand, weather, storage degradation and human operations. A common error is to present an average across a few scenarios as a reliability forecast. A weighted mean is mathematically defined whenever the weights sum to one, but its interpretation as an expected physical outcome requires a representative sampling scheme and defensible probabilities. A list of hand-selected adverse cases can serve stress testing and reveal a failing service, without assigning the probability that such conditions will occur.

## Formula, units and preconditions

`Given cases s with stated weights w_s, ∑w_s=1: scenario-weighted unserved energy E*=Σ_s w_s U_s. Weighted fraction of cases with shortage q*=Σ_{s:U_s>0}w_s.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The formula is linear arithmetic, not a weather distribution estimator. Correlations matter: a long cloudy period can coincide with high heating demand and unavailable fuel delivery, so treating the events as independent understates joint stress. At least one severe-but-plausible combined case should be analyzed. The reference rejects weights that do not sum to one rather than rescaling silently and hiding a data-entry error. A maximum among supplied cases is only the worst of those cases, not an upper bound across every physically possible future.

## Reconstruct by hand and compare against code

Two hypothetical scenarios have shortages 0 kWh and 10 kWh with selected weights 0.8 and 0.2. The weighted shortfall equals 2 kWh. That number is not a 20% physical outage probability unless the 0.2 weight came from a justified probability model. Alter the selection to 0.5/0.5 and demonstrate the changing average without changing the plant itself.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Missing scenarios, nonstationary climate, poor equipment maintenance and dependent failures can invalidate a probabilistic claim. Tiny synthetic samples do not calibrate tail risks.

## Life-safety and professional boundary

This reference only informs scenario comparison and documentation; it must not be represented as a community emergency-management risk assessment without local validated inputs.

## Source provenance (links only)

- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context
- **Sandia National Laboratories, Microgrid Design Toolkit** — https://energy.sandia.gov/programs/electric-grid/advanced-microgrids/microgrid-design-toolkit/; inspected portion: Official description of early-stage multiobjective microgrid design, cost-performance-reliability tradeoffs

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
