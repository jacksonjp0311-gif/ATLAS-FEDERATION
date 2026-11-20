# Chapter 22: Finite-sample yield is not guaranteed reliability

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`p_hat=k/n; Wilson 95% lower bound < 1 even when k=n`

## Scientific derivation and engineering reasoning

A batch with all passing tested units is not proven to have 100% yield. For n independent Bernoulli trials with k observed passes, the score-based Wilson interval gives bounded confidence limits for the unknown pass fraction. It remains finite at k=0 and k=n, unlike naive p±z√(p(1−p)/n) which collapses to zero width at these extremes.

The interval assumes representative, independent, identically distributed trials and a specified pass/fail definition. It does not address convenience sampling, clustered wafer defects, shared systematic process errors, instrument false acceptance, untested field conditions, or burn-in lifetime. Sample correlation can cause the nominal interval to substantially understate uncertainty.

Constructed result: k=n=100 yields a point estimate of 1.0 but a Wilson 95% lower confidence limit around 0.963, not 1.0. With no tested samples, the calculation is undefined and must be refused rather than returning a comforting default.

When qualifying semiconductor or additive-manufactured components, report which population was sampled, what pass criteria were used and whether each unit's outcome was independently observable. Retain nonconforming parts, root-cause records and uncertainty intervals alongside successes.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.wilson_yield_interval`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Wilson confidence requires independent representative observations; no physical trial data are included.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
