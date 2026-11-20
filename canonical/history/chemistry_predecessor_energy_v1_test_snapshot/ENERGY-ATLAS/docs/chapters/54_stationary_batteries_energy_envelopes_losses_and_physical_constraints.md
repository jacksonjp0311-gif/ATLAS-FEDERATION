# 54. Stationary batteries: energy envelopes, losses and physical constraints

**Domain:** Energy storage. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

A battery has an energy capacity, power limit, permitted state-of-charge range, efficiency, temperature range and degradation behavior. The usable energy may be materially below the nameplate capacity. Charging and discharging introduce losses and can trigger protection constraints. A mathematical controller that only tracks stored kilowatt-hours cannot certify charge acceptance, fault response or safe operation. In disaster applications, realistic reserve policy must be specified before dispatch, and exact energy balance must distinguish energy withdrawn from the battery from energy delivered to a load.

## Formula, units and preconditions

`E_(t+1)=E_t+η_c P_charge Δt−P_discharge Δt/η_d, bounded by E_min≤E_t≤E_max and power limits.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The recurrence arises from conservation with two conversion fractions. If 1 kWh enters at η_c=0.9, only 0.9 kWh is added. Delivering 0.9 kWh at η_d=0.9 removes 1 kWh, so the two-way fraction is 0.81. Power and energy are independent constraints: a large capacity does not guarantee sufficient instantaneous output. The model should refuse energy states below a predeclared reserve, instead of quietly borrowing energy that the battery cannot deliver.

## Reconstruct by hand and compare against code

A stipulated 10 kWh capacity starts at 7 kWh and has a reserve floor at 2 kWh. With η_d=0.9, its maximum useful delivered energy is 4.5 kWh before the floor, ignoring power restrictions. Reconstruct this figure from E_available=(7−2)×0.9. Then compare two identical energy demands over different durations; a rate limit may make one impossible.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

The example does not model temperature-dependent chemistry, thermal runaway, cell balancing, manufacturer discharge limits, aging, inverter conversion losses or detailed cell state estimation. A numerical state update is not a battery management system.

## Life-safety and professional boundary

NFPA 855's 2026 edition addresses stationary energy-storage installation hazards. The full standard is not archived or reproduced here. Actual battery systems require equipment approvals and applicable local safety processes; never bypass built-in protection.

## Source provenance (links only)

- **DOE Energy Storage Strategy and Roadmap** — https://www.energy.gov/oe/energy-storage-strategy-and-roadmap; inspected portion: Energy storage technology and deployment; cross-technology requirements
- **NFPA 855, Stationary Energy Storage Installation Standard, 2026 edition** — https://www.nfpa.org/product/nfpa-855-standard/p0855code?l=134; inspected portion: Product description and 2026 edition overview only; standard is copyrighted and full clauses were not acquired
- **U.S. EPA, Battery Energy Storage Systems Safety and Incident Response** — https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe; inspected portion: Battery fire response, community planning, relevant standards; no site engineering standard reproduced

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
