# Atlas Forge content checkpoint 0.5.0 release audit

**12 November 2026 · Local Linux/Python 3.13.5 execution · James Paul Jackson project**

## Scope and deliberate non-work

Measurement remains the active domain. The owner requested scientific reference depth now and navigation later. Eight navigation/runtime modules are byte-identical to 0.4.0; the Signal and Cymatics common-node files and approved artwork remain preserved. No next domain was built. No GitHub repository or desktop installation was modified.

## Content inventory

The common view holds **446 records**: Signal 232, Cymatics 132, Measurement 82. Measurement consists of 50 bounded reference records, 27 source cards and five preserved unreviewed starter records. The 47-record increment is 30 bounded records plus 17 source pages. These numbers count reference objects, not independent scientific validations.

The companion Measurement repository now supplies eight chapters, 50 individual record pages, four blank review templates, 12 additional synthetic calculations, and 24 authored review questions. The earlier five synthetic cases remain. The review questions have not been used in a consuming-model evaluation.

## Executed checks

- Forge: **170 tests passed**. Measurement: **75 tests passed**. Total: **245**.
- Common conformance and JSON Schema checks passed for 446 records across three enabled nodes.
- Source-intake structure, local current-content links, evidence locators, content assumptions and limitations, project-local skills, and the unchanged-runtime checks passed.
- Twelve new and five retained synthetic casebook calculations passed. They are invented inputs, not instrument readings or calibration certificates.
- The seeded NumPy cross-check passed 600 positive-definite covariance cases and rejected five invalid cases. Maximum relative error: 2.3171296437844394e-15. It is an additional computational oracle, not independent human or laboratory review.
- Both version 0.5.0 wheels built and installed with no network dependencies in a fresh environment. The installed packages expose 446/82 records, assemble and validate context, and pass numerical smoke checks outside the source tree.
- The workflow runner completed all stages and confirmed that advancing to Causal Atlas is blocked.

Actual logs and receipts: [current receipts](receipts/current/). The older receipts are separately preserved under `receipts/v0.4.0/`. Artifact hashes attest byte consistency, not scientific truth or reviewer identity. The final delivery ZIP and extraction verification are recorded in the companion `ATLAS_RELEASE_CHECKS_v0.5.0.json` delivered alongside the archive.

## Gate status

G4 common software conformance and G5 context software integrity have refreshed actual local receipts for this release's input hash. G1, G2, G3 and G8 remain partial; G6 is blocked and deferred, G7 is not run. Candidate acceptance criteria have not been frozen/owner-approved for a final independent study. **scientific_v1_accepted=false; next_domain_allowed=false**. Deferring navigation does not waive those gates.

## Limits

Public source portions were inspected by the assistant and paraphrased into bounded original records; no independent scientific review or reproduction was added. Source locators and caveats are in the Measurement source register. A historical NIST TN 1297 reporting page carries an out-of-date/update-status notice, preserved as a limitation rather than silently treated as current certification guidance.

No new physical data, authentic calibration certificates, live Bitwork run, actual AI consumption, independent held-out evaluation, Windows run, browser run, remote service or account-Memory installation is claimed. Existing HTTP regression tests ran; occasional BrokenPipe logging from clients that intentionally disconnect does not represent a failed test. Existing UI/routing features were not developed in this content phase.

## Reproduce

Run the workspace `RUN_CHECKS.cmd` (Windows execution not verified here) or `python3 ATLAS-FORGE/tools/run_workflow.py --measurement MEASUREMENT-ATLAS --out ATLAS-FORGE/output/new-check`. Optional full schema checks need jsonschema; the numerical oracle needs NumPy. Core library and calculations have no third-party runtime dependencies. Keep the current scope/evidence work on Measurement, then return to navigation and final acceptance before Causal.
