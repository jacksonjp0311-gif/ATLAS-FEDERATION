# Atlas 1.0.0 release candidate 1 audit

**12 November 2026. Final v1 acceptance is not established.** This candidate completes a substantial practical Measurement reference increment while preserving all agreed acceptance gates. Measurement remains the only active new domain. The Python package version is `1.0.0rc1`; display/archive version is `1.0.0-rc.1`.

## Implemented and bounded

The Measurement node contains **141 records**: 92 bounded scientific/editorial records, 44 source cards and five preserved starter records. The shared Forge runtime reads **505 records** from Signal, Cymatics and Measurement. Sixteen bounded records and three source pages were added. Eight core chapters remain; focused supplements address units, certificate interpretation and decision rules. Thirty core authored questions plus retained separately named supplements are development material, not an independently authored held-out evaluation.

The new tools perform finite-catalog unit algebra with explicit quantity kind; affine temperature and uncertainty conversion; structured operator-transcribed certificate review; explicit expanded-to-standard uncertainty; additive specification models; conditional normal state-of-knowledge probabilities; and named guard-band decisions. They do not authenticate a certificate, establish traceability, certify conformity, determine global decision risks or infer an unstated coverage model. New publisher examples are numerical illustrations, not laboratory observations.

## Actual checks

| Check | Outcome on this Linux host |
| --- | --- |
| Forge complete source suite | 188 passed, zero skipped |
| Measurement complete source suite | 218 passed, zero skipped |
| Candidate workflow | All 14 stages passed; next-domain refusal worked |
| Common conformance and four schemas | 505 records, three nodes; valid |
| Primary-reference structure | 92 bounded records; 43 new-format primary pages; valid |
| New practical casebook | 8 passed, including 4 publisher illustrations and 4 synthetic workflow checks |
| Separate 60-digit probability algorithm | 334 cases passed; maximum absolute error 1.111e-16 |
| Retained covariance algorithm comparison | 600 positive-definite cases passed; 5 invalid cases rejected |
| Retained t-quantile comparison | 110 cases within declared tolerance |
| Retained Pontius comparison | Both model fits agree with NumPy; 11 certified targets retained; publisher disagreements preserved |
| Clean local-wheel install | Both packages loaded from isolated site-packages; 505 records and new commands exercised |
| Final-readiness preflight | Correctly returns exit 2; v1 and next-domain acceptance remain false |

Complete receipts and command logs are included in Forge `docs/receipts/current`. The prior release receipts are preserved under `docs/receipts/history/v0.7.0`. Final archive hashes and extracted-archive rerun results are in the separately delivered release-check JSON, avoiding a self-referential archive checksum.

G3 (declared-model engineering), G4 (common conformance) and G5 (context integrity) now have actual, input-bound local receipts. They are not independent scientific review. The release preflight also requires passed G3/G6/G7/G8 receipts to bind the Measurement source digest, so updating one project invalidates dependent approval rather than leaving a Forge-only green state.

## Preservation

Thirty-seven byte comparisons pass, including eight core navigation/runtime modules, both prior domain nodes, artwork, the acceptance criteria, domain queue, and original Pontius/interval resources. No navigation feature was added. Earlier numerical discrepancy targets were not loosened, erased or silently passed. Original upstream transport bytes remain unavailable after attempted acquisition; existing checked transcriptions retain that status.

## Outstanding before final 1.0

G1 scope and acceptance-plan approval/freeze; G2 complete release-critical source review and recorded independent-review status; G6 real pinned Bitwork-to-record-to-model execution; G7 independent held-out comparative evaluation; and G8 supported Windows execution and final release validation remain partial, blocked or not run. The criteria remain unfrozen. No gate was removed to obtain a version label. Other Atlas domains remain queued.

The retained local HTTP server writes a `BrokenPipeError` traceback when an intentionally aborted test client closes its connection. This is reproducible baseline logging, not a newly repaired behavior; the affected tests pass. It is disclosed rather than describing the run as free of logged exceptions. Initial new assertions and smoke-harness input shape mistakes were corrected to the existing documented contracts; numerical tolerances were not relaxed.

No independent human reviewer, actual calibration certificate, Windows host, live Bitwork runtime or consuming-model evaluation has been invented. No GitHub, desktop, sharing or account Memory changes were made by this build.

## Reproduce

From the complete workspace, run `python tools/run_candidate_checks.py`, then `python tools/v1_readiness.py --require-final`. The latter is expected to refuse final acceptance. Optional independent numerical implementations require NumPy, SciPy or mpmath as stated in their individual tool files; the scientific runtime has no third-party dependencies.

Use the native Windows launcher `RUN_V1_ACCEPTANCE.cmd` on the intended host to create an actual platform receipt. Configuration is not a platform pass. See Measurement `docs/V1_REVIEW_HANDOFF.md` for scientific review and later integration work.
