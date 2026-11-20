# 57. Bounding uncertain supply and demand without invented precision

**Domain:** Interval mathematics. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

When no defensible probability distribution exists, interval bounds are sometimes more honest. Stipulate a minimum and maximum load and generation for one period. Because arithmetic is monotone in these terms, one can bound the energy deficit for every condition inside the stated rectangle. The method is conservative and may be loose: the maximum load and minimum generation might not occur simultaneously. That looseness is appropriate when correlations and timing are unknown. An interval represents an assumed hard range, not a confidence interval with a probability attached.

## Formula, units and preconditions

`D_max=max(0,(L_max−G_min)Δt); D_min=max(0,(L_min−G_max)Δt), where L and G are kW and Δt is hours.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The upper bound follows because the shortage function max(0,L−G) increases with L and decreases with G. Monotonicity means its maximum over the rectangular interval occurs at L_max and G_min; its minimum occurs at L_min and G_max. Subtracting a stipulated ideally usable reserve gives a numerical illustration but does not validate the reserve, power limit or loss model. A true time-varying bound should integrate across intervals, not multiply peak power by an arbitrary duration.

## Reconstruct by hand and compare against code

Suppose L∈[1,3] kW and G∈[0.2,2] kW for four hours. The required shortage ranges from 0 to 11.2 kWh before storage. An idealized 2 kWh reserve reduces the upper numerical deficit to 9.2 kWh. This is an enclosure under the selected ranges, not a site-specific energy forecast.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Assuming a reserve is 100% deliverable can understate real shortfall. The method does not model dynamic frequency, temperature derating, minimum startup power or correlated interval excursions.

## Life-safety and professional boundary

This numerical bound is a planning exercise only. It does not authorize equipment sizing or medical continuity claims; validate real demand and resource data first.

## Source provenance (links only)

- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context
- **U.S. DOE, Solar and Resilience Basics** — https://www.energy.gov/cmei/systems/solar-and-resilience-basics; inspected portion: Grid outages, islanding, inverter/storage requirements, resilience terminology; site-specific technical design not inspected

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
