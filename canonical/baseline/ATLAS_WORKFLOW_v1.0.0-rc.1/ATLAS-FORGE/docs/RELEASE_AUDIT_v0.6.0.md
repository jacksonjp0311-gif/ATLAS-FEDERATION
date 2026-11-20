# Atlas Forge release audit 0.6.0

12 November 2026. Content-first engineering checkpoint; navigation work deferred.

The common store now contains 467 records: Signal 232, Cymatics 132 and Measurement 103. The 370 legacy records and their original evidence labels are retained. Measurement adds 12 scoped records and nine source pages in this increment. Contradictory publisher values are linked and travel together in context without changing the retrieval engine.

## Executed checks

| Check | Result |
| --- | --- |
| Forge unittest suite | 176 passed, 0 skipped |
| Measurement unittest suite | 110 passed, 0 skipped |
| Full workflow runner | Passed all 11 stages and expected next-domain refusal |
| JSON-schema conformance | 467 common records; 4 schemas checked |
| Primary-source record structure | Passed; not independent scientific verification |
| Synthetic casebooks | 17 retained cases passed |
| Published-data reproduction | All 11 checked NIST StRD targets within published last-digit tolerance |
| Handbook comparison | Six discrepancies retained, not silently passed or retuned |
| Separate NumPy least-squares check | Linear and quadratic scaled coefficients and residual standard deviations agree |
| Seeded covariance comparison | 600 positive-definite cases passed; 5 invalid covariance cases rejected |
| Isolated local-wheel installation | Both packages 0.6.0 installed; 467 records, conflict preservation and source case verified |
| Navigation preservation | Eight runtime modules match v0.4 baseline pins and prior workspace bytes |
| Existing nodes and artwork | Signal, Cymatics and approved Forge image bytes unchanged |
| Domain order | 30 proposed/active domains; Measurement is the only active one |

Executed on Python 3.13.5 / Linux. Results are authored software regressions and numerical comparisons, not an independent blinded scientific or model-quality study. Both project test suites are run using their actual source paths through `PYTHONPATH`; this avoids the missing-package invocation problem visible in the previous conversation. The earlier baseline was independently rerun: 170 Forge and 75 Measurement tests passed with no skips.

## Reproduction

From the full workspace:

```sh
python3 ATLAS-FORGE/tools/run_workflow.py --measurement MEASUREMENT-ATLAS --out ATLAS-FORGE/output/check-v06-local
python3 tools/validate_domain_queue.py
python3 MEASUREMENT-ATLAS/tools/published_case_oracle.py
python3 MEASUREMENT-ATLAS/tools/numerical_oracle.py
python3 tools/check_release.py verify .
```

Choose a fresh output directory each run. NumPy is an optional developer dependency for the last two numerical comparisons; it is not needed for the runtime or the source-case CLI. The published-data calculator requires an explicit separate invocation; search never executes node code.

## What has not been done

No local physical calibration experiment, independent human review, calibration certification, complete traceability record, raw original transport-byte capture, published inverse-interval reproduction, Windows execution, new browser test, live Bitwork run or downstream AI answer evaluation is claimed. The 40 observations are a checked decimal transcription of published NIST data. The file hash authenticates only this local representation; the original-file byte hash remains null. Model assumptions, unspecified source units and collection-order confounding remain visible.

No gate was waived. The v1 criteria remain candidate/unfrozen; scientific scope and review, real Bitwork-to-AI execution, held-out comparisons and supported-platform verification are still open. Measurement remains active. Nothing was pushed to GitHub or installed on the user's desktop.

## Receipts

Actual logs and output are in `docs/receipts/v0.6.0/`. G4/G5 software-only decisions refer to release-input hashes; they are not scientific validation. Distribution hashes and post-extraction test results are reported in the companion `ATLAS_RELEASE_CHECKS_v0.6.0.json`.
