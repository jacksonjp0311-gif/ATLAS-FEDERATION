# 62. Reconstructing truth: metrology, provenance and reproducibility

**Domain:** Scientific measurement. **Release:** Energy Atlas 1.0.0 scoped content.
**Evidence:** Original author-assisted synthesis with selected official publisher webpage citations. No physical system, original research data, or site measurement verified.

## Definition, goal and physical boundary

A calculation becomes scientific evidence only when its inputs have a traceable origin, uncertainty and applicable conditions. Energy measurement can require voltage/current sampling, instrument bandwidth, timing accuracy, meter calibration, load profile and a clear accounting boundary. A human-readable formula remains important when proprietary vendor data and cloud endpoints disappear, but the formula alone cannot reconstruct a measurement that was never retained. The survival library must keep original acquisition files where rights allow, exact immutable source versions, transformations, independent reference tests, and explicit gaps when any step is absent.

## Formula, units and preconditions

`Measured E = ∫ measured P dt; residual r=Σ E_in−Σ E_out−ΔE_stored. Significant r may represent measurement error, missing flows or an invalid boundary.`

Power (W or kW) and energy (J or kWh) must never be interchanged without time integration and unit conversion. Every equation is conditional on the specified physical or mathematical model; exact arithmetic does not verify observed inputs.

## Derivation and reasoning

A zero residual on synthetic inputs can be guaranteed by how the simulator was constructed; that is a numerical consistency check, not experimental conservation verification. Real mismatches need an uncertainty budget including calibration, sampling aliasing and storage-state estimation. Correlated errors cannot necessarily be combined as independent random terms. Publisher references such as NIST's CODATA constants describe selected measured or defined constants but do not supply the original local site's meter records. This content edition distinguishes bibliographic locator from original source byte archive.

## Reconstruct by hand and compare against code

A hypothetical meter reports 1.0 kWh generation, 0.8 kWh delivered and 0.2 kWh loss. Its residual is zero by arithmetic. Change an input reading to 0.9 kWh and calculate a 0.1 kWh discrepancy; list plausible missing terms rather than blaming the meter automatically. Record unit, instrument ID, calibration, timestamp and source-file hash for any real repeat.

Every numerical quantity in this exercise is an authored, deliberately stipulated example—not an observation of real devices. The offline `energy_atlas.survival_v1` module implements the relevant bounded models, and tests cover refusals as well as positive cases.

## Failure modes, alternative hypotheses and missing evidence

Unknown calibration, omitted standby consumption, clipping, weather time alignment, or altered source data can turn a plausible calculation into a false inference. Synthetic precision does not imply measurement accuracy.

## Life-safety and professional boundary

No field measurements, equipment calibration or scientific peer-review were carried out for these v1 examples. The stated residual is not a compliance or safety certificate.

## Source provenance (links only)

- **NIST Measurement Uncertainty Guidance** — https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty; inspected portion: Measurement uncertainty, measurand, instrument and calibration context
- **NIST CODATA 2022 recommended fundamental physical constants** — https://physics.nist.gov/cuu/Constants/; inspected portion: 2022 recommendation, speed of light, elementary charge, Boltzmann and Stefan-Boltzmann constants
- **NIST, Version History of the Fundamental Constants Database** — https://physics.nist.gov/cuu/Reference/versioncon.shtml; inspected portion: 2022 CODATA adjustment version 9.0; NIST recommended values and historical data versions

Original publication files were not downloaded or reproduced. Source-page citation is not the same as independent scientific review, valid equipment certification, or a verified local archive of the publisher's full material.
