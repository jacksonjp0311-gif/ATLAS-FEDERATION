# Chapter 21: Process stability is a prerequisite to capability

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`Cp=(USL−LSL)/(6s), Cpk=min(USL−μ,μ−LSL)/(3s)`

## Scientific derivation and engineering reasoning

Capability indices compare tolerance width and observed variation. The indices Cp and Cpk are meaningful for a stable, adequately characterized process distribution, not automatically for arbitrary data. Cpk incorporates offset of the process mean from tolerance center. NIST explicitly separates process stability assessment from capability; a trend, tool drift, subgroup mixing or autocorrelation can invalidate ordinary summary assumptions.

The reference function therefore requires declarations of both stability and distribution evidence. If either is absent, it refuses to produce Cp/Cpk. Even when both declarations are present, it labels the result conditional and not independently authenticated: self-asserted flags are not calibrated instruments or reviewed stability plots.

A reproducible capability investigation needs sample order and subgroup rationale, sample size, controlled conditions, measurement-system repeatability, autocorrelation and a process-change log. Use a sample standard deviation with n−1 denominator, record mean and holdouts, and do not infer a six-sigma guarantee from a small convenience sample.

Constructed case: 20 values near 10 within limits [9,11] produce numerical Cp/Cpk under declared evidence, while the same data without stability evidence return HOLD. An identical repeated value has zero sample variance, which is not evidence of perfect manufacturing: the function explicitly refuses that inference.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.stable_process_capability`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Actual stability and distribution are not proved by boolean declarations; outside review remains required.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
