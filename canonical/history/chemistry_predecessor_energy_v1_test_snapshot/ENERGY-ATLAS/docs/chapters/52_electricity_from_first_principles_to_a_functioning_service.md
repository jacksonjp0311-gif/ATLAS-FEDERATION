# 52. Electricity from first principles to a functioning service

**Domain:** Power systems. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

Electrical energy service requires a source, conversion equipment, conductors, loads, control and protective devices. This chain is more complex than the isolated identity P=VI. DC loads may draw pulsating current and AC loads may require inrush current or reactive power; a nominal energy budget is not an electrical safety design. Frequency and voltage regulation involve dynamic feedback. A nameplate specifies operation under stated conditions and can be derated by ambient temperature, altitude and duty cycle. This edition preserves the distinction between an abstract mathematical service and a tested appliance.

## Formula, units and preconditions

`For a steady DC resistive load: P=VI=I²R=V²/R. Energy over duration t: E=Pt. In ideal single-phase sinusoidal AC: P=V_rms I_rms cos φ.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

Ohm's law and Joule heating connect voltage, current and resistance under the stated linear resistive model. A conductor's dissipation depends on current squared, so a current error can produce a larger relative thermal-loss error. For AC, phase angle matters; a reactive load may draw current without receiving equivalent average real power. Actual waveforms may be nonlinear, with harmonics and transients that this scalar model omits. Conservation of energy remains mandatory, but it does not imply that all stored or generated energy is accessible on demand.

## Reconstruct by hand and compare against code

Using a hypothetical 24 V DC resistance of 12 Ω, calculate 2 A and 48 W. Over 3 hours the energy is 144 Wh. Derive I=V/R and show P=VI. Compare to an AC load with the same RMS voltage-current product but power factor 0.6: its mean real-power value differs.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

The DC example assumes a fixed resistor and steady voltage. It does not represent real medical equipment, motor starters, protection requirements, or a safe low-voltage installation. Power factor alone cannot describe distorted waveforms.

## Life-safety and professional boundary

No live-wiring or backfeed steps are provided. IEEE/NFPA rules, local codes, appropriate protective equipment and licensed electricians must govern real work. The Atlas does not substitute for certification or life-safety review.

## Source provenance (links only)

- **BIPM The International System of Units (SI) Brochure, ninth edition** — https://www.bipm.org/en/publications/si-brochure; inspected portion: Energy, power, voltage and electrical units, formal SI definitions
- **U.S. DOE, Distributed Energy Resources and Microgrids Basics** — https://www.energy.gov/cmei/systems/solar-integration-distributed-energy-resources-and-microgrids-basics; inspected portion: Distributed resources, boundaries, microgrid disconnect and island operation; no operational controller audited

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
