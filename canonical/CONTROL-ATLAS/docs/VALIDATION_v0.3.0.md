# Control Atlas v0.3.0 validation and scientific boundaries

**Release classification:** substantial research-content increment, NOT a Control scientific/content v1.0 release, hardware-safety proof or independent engineering peer review.

## Executed evidence

- Full six-node checks: **884 automated tests passed, zero skips** (Forge 188, Measurement 218, Causal 233, Materials 122, Control 123). Shared contract/schema, source closure and bounded context checks passed.
- Added independent numerical library comparison: **1,700 author-generated cases** cross-checked using NumPy/SciPy; maximum relative scaled difference approximately 4.98e−16. This verifies implementation arithmetic, not the physical truth of the models.
- Existing Control numerical tools reran successfully with their original caveats.
- Fresh isolated Python environment installed Forge, Measurement, Causal, Materials and Control wheels. The Control wheel exposed **145 exact-version records**, validated bundled context and ran both old and new casebooks without source-tree imports.
- **All 117 old Control record revisions and 64 old Control relationships retained unchanged**, along with five other domain snapshots and the historical baseline. The original v0.2 archived software is preserved separately.
- A failure of the P=I Lyapunov candidate was explicitly tested for a stable nonnormal matrix; the output correctly means `candidate_not_certified`, not `plant_unstable`.
- An exact one-sample-delay model shows a counterexample where a stable nominal scalar pole becomes unstable. This is an original model exercise and not evidence a machine failed.
- The watchdog demonstration refused stale/invalid/large-innovation samples; the fallback command is NOT physically safety-rated and no device was operated.

## Scientific work not done

No independently acquired plant data, sensor calibration, industrial device control, qualified timing/actuator hazard study, formally verified stability proof, nonlinear uncertainty or general MIMO robust controller, domain-expert review, native Windows validation, live Bitwork pipeline or downstream held-out AI evaluation was performed. Source pages were inspected only within listed scopes, and no copyrighted full textbooks/papers are mirrored. Results are educational and research-oriented.

## Reproducibility

From the collection root: `python tools/check_collection.py --out output/new-unique-run`; from Control: `python -m control_atlas robust-casebook`; optional numerical comparisons `python tools/robust_numerical_oracle.py`. Use a fresh output folder. See `RELEASE_CHECKS_v0.3.0.json` for exact machine data.
