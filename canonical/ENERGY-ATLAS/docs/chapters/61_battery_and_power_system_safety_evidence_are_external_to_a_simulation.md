# 61. Battery and power-system safety evidence are external to a simulation

**Domain:** Safety systems. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Stationary energy-storage systems can fail through thermal, electrical or mechanical mechanisms, including fire and thermal runaway. Even correct arithmetic over a prescribed state of charge does not guarantee cell or pack safety. Engineering judgments require equipment-specific ratings, tested protection coordination, proper installation, fire-response planning and the applicable edition of standards. The 2026 edition of NFPA 855 describes requirements for stationary energy storage; this Atlas retains a short bibliographic pointer rather than reproducing a restricted standards document.

## Formula, units and preconditions

`Necessary numerical constraints: 0≤E≤E_max, 0≤P_charge≤P_c,max, 0≤P_discharge≤P_d,max. Neither inequality is sufficient for operational safety.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The constraints limit a scalar energy and power budget. A real battery pack has cell-voltage variation, allowable temperature and current, contactor status, potential arc or internal fault, and control communications. None is entailed by knowing a single E_t variable. The failure of a BMS signal may produce a physically unsafe state even if the energy ledger remains perfectly balanced. This is a broader lesson in modeling: mathematical invariants require a faithful mapping to physical sensors and actuators before their satisfaction can be claimed.

## Reconstruct by hand and compare against code

Consider two abstract packs with the same nominal capacity, efficiency and initial stored energy. Give one an unavailable temperature sensor and the other a validated sensor. The energy-ledger trajectories can match exactly, yet the real safety assessment must differ. Record the missing measurement as unknown and refuse to label the first pack safe.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

No electrochemical reaction rates, fire spread, suppression or code-compliance testing are implemented. Missing fault-current and protection information invalidates any construction claim.

## Life-safety and professional boundary

Never bypass battery protections or modify energized storage equipment based on this reference. Licensed and qualified personnel, current standards and official emergency services are required.

## Source provenance (links only)

- **NFPA 855, Stationary Energy Storage Installation Standard, 2026 edition** — https://www.nfpa.org/product/nfpa-855-standard/p0855code?l=134; inspected portion: Product description and 2026 edition overview only; standard is copyrighted and full clauses were not acquired
- **U.S. EPA, Battery Energy Storage Systems Safety and Incident Response** — https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe; inspected portion: Battery fire response, community planning, relevant standards; no site engineering standard reproduced

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
