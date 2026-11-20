# Measurement Atlas checkpoint 0.7.0 release audit

12 November 2026. Measurement coverage and conditional inverse intervals; navigation unchanged.

## Implemented scope

Measurement has 76 bounded reference records, 41 source cards and five retained starter records (122 total). The common three-node view has 486 records. Fourteen new bounded records, five source pages, a methods supplement, ten authored review questions and five synthetic coverage examples were added. Existing 24 review questions, eight published-case questions, eight chapters and all older numerical examples remain preserved.

New tools require explicit statistical assumptions: bounded Student t factors, independent-component effective degrees of freedom, conditional expansion, fitted-mean and future-response intervals, and monotonic-band inverse-calibration intervals. Default inversion rejects out-of-range endpoints. Optional clipping is explicitly labeled. Finite numerical scope and the sufficient derivative condition are documented.

## Actual checks

- Baseline independently rerun locally: 176 Forge + 110 Measurement tests, no skips.
- Updated suites: 182 Forge + 154 Measurement tests, no skips.
- Thirteen workflow stages pass; next-domain action is correctly refused.
- Four common schemas validate 486 records.
- 110 Student t factors compare to installed SciPy within the predeclared 2e-9 scaled absolute tolerance; maximum observed difference about 2.49e-11.
- NumPy fit/covariance plus SciPy Brent inversion agrees with both endpoints within 4.66e-10 source unit; declared tolerance 1e-5.
- The 20,000-trial, fixed-seed synthetic coverage study records rates and Monte Carlo uncertainty. It is not physical validation or an independently held-out experiment.
- Retained 600 covariance cases and five rejection cases, 17 old synthetic examples, eleven certified regression targets and six prior display discrepancies remain unchanged.
- Eight navigation modules, both other node snapshots, approved hero artwork, prior Pontius capture bytes and v1 criteria match baseline hashes.

Initial tests exposed four stale inventory-count assertions after corpus expansion. Only inventory expectations were updated (467→486 total, 103→122 Measurement, 62→76 bounded additions); no scientific target or tolerance was relaxed. Those initial failure logs remain under build_history.

## Evidence limits

The new inverse interval matches two of three publisher display targets; the upper endpoint differs by about 0.7636 source unit against a fixed 0.5-unit tolerance. The computation is cross-checked, not falsely labeled as complete publisher agreement. Cause is unresolved. Original publisher-file bytes could not be obtained; data remain the prior checked transcription. No new physical measurements or inferred units/certificates were added.

No independent human review, supported Windows run, browser rerun, live Bitwork, actual AI consumption or independent held-out comparison is claimed. G4/G5 have current local engineering receipts. Other gates remain partial, blocked or not run, and v1 criteria are not owner-frozen. Neither scientific v1 nor another domain is authorized.

## Reproduce

```sh
python ATLAS-FORGE/tools/run_workflow.py --measurement MEASUREMENT-ATLAS --out ATLAS-FORGE/output/check-new
python MEASUREMENT-ATLAS/tools/coverage_oracle.py
python MEASUREMENT-ATLAS/tools/coverage_simulation.py
python tools/check_release.py verify .
```

Use a fresh receipt directory. NumPy/SciPy are optional developer-only dependencies. The separate ATLAS_RELEASE_CHECKS_v0.7.0.json records clean-wheel and extracted-archive outcomes after packaging. No GitHub or desktop mutation is performed by this release.
