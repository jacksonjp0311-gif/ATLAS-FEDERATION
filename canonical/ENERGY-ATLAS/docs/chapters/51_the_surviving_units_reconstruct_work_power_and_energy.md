# 51. The surviving units: reconstruct work, power, and energy

**Domain:** Foundational metrology. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

A survivor with no digital calculator should first distinguish power (the rate of transferring energy) from energy (the integrated transfer over time). Watts, joules, watt-hours and kilowatt-hours are related by definitions; changing the symbol without converting units produces a different physical quantity. The SI provides a coherent method to derive a unit rather than relying on a proprietary instrument display. A power meter reading at one moment cannot establish daily energy, just as a battery energy rating does not establish the peak current or inverter output it can supply. In any future reconstruction, preserve the instrument measurement, calibration status, interval length, sign convention and the system boundary.

## Formula, units and preconditions

`1 W = 1 J/s; E[J] = ∫ P[W] dt[s]; 1 kWh = 3,600,000 J. For piecewise constant intervals E_kWh = Σ_i P_kW,i × Δt_h,i.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

The integral sums infinitesimal transfers of energy, and the discretized model approximates or exactly represents stipulated constant-power intervals. A reversible conversion factor does not validate the measurement that entered the formula. A watt is defined from the joule and second, whereas a joule can be reduced to kg m² s⁻². When using three-phase AC equipment, real power and apparent power differ, so multiplying arbitrary voltage and current magnitudes alone is not always a delivered-energy calculation. Keep the acquisition conditions with each equation.

## Reconstruct by hand and compare against code

An illustrative two-interval load uses 1.5 kW for two hours and 0.5 kW for four hours. Compute 5 kWh = 18 MJ. Compare a falsely reported 5 kW power rating to the true energy. Derive units by replacing kW with 1000 J/s and hours with 3600 s. A reader needs no specialized model to repeat this calculation.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Missing timestamps, rounded meters, unobserved standby loads, inverse sign conventions, and overloaded wiring can invalidate an equipment conclusion while preserving the unit arithmetic. No uncertainty estimate is justified by an exact conversion alone.

## Life-safety and professional boundary

Do not use this mathematics to approve a physical electrical installation. Measurement and protection require properly rated instruments and qualified assessment. The source record includes the SI version and its bibliographic provenance, not a fabricated calibration certificate.

## Source provenance (links only)

- **BIPM The International System of Units (SI) Brochure, ninth edition** — https://www.bipm.org/en/publications/si-brochure; inspected portion: Energy, power, voltage and electrical units, formal SI definitions
- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
