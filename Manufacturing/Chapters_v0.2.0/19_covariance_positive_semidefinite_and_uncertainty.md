# Chapter 19: Why covariance must be positive semidefinite

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`u_y² = aᵀ Σ a, and Σ must be symmetric PSD`

## Scientific derivation and engineering reasoning

An uncertainty budget is not just a set of individual standard deviations and pairwise correlations. Every physically possible covariance matrix must be symmetric positive semidefinite (PSD): for every real vector a, aᵀΣa≥0. If this condition fails, the matrix assigns a negative variance to some linear combination of measurands and cannot represent a valid multivariate uncertainty model. Checking each |Cov(i,j)|≤σiσj is necessary but not sufficient for three or more correlated quantities.

A bounded symmetric Jacobi eigenvalue method can evaluate the small matrices encountered in educational tolerance stackups. Validate finite entries, symmetry and a scale-aware nonnegative eigenvalue condition; then propagate uncertainty with the quadratic form. Because real metrology can be extremely ill-conditioned, distinguish solver tolerance from physical measurement uncertainty. A numerical eigenvalue tolerance must not be misrepresented as proof that the source covariance estimates were calibrated.

Constructed counterexample: Σ=[[1,.9,.9],[.9,1,−.9],[.9,−.9,1]] has admissible pairwise magnitudes yet a negative eigenvalue and must be rejected. Valid test: two standard deviations 3 and 4 with zero covariance give u=5. With covariance +0.5 between two unit-standard-deviation contributors, the uncertainty of their sum is √3. Correlations should be inferred from appropriate paired observations, not chosen to make a tolerance stackup pass.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.covariance_budget_psd`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Measurement covariance must be estimated from real calibration/control data, currently absent.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
