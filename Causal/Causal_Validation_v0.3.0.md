# Causal Atlas validation 0.3.0

Checked 12 November 2026 on Python 3.13.5, Linux. These are local engineering checks and authored numerical comparisons, not independent human review, a held-out AI benchmark or empirical causal validation.

## Executed checks

| Check | Outcome |
|---|---|
| Causal test suite | 193 passed, zero skipped |
| Preserved Forge suite | 188 passed, zero skipped |
| Preserved Measurement suite | 218 passed, zero skipped |
| Complete source workflow | 599 tests pass; four nodes, 610 records, schema and exact source closure pass |
| Synthetic calculations | Five original cases, twelve earlier investigations and twelve new IV/RD checks pass |
| New separate IV/RD calculation | NumPy SVD line fitting and explicit population enumeration: 3,758 scalar comparisons over 240 line datasets, 200 type populations and one fuzzy case; all within 1e-10 scaled absolute tolerance |
| Earlier estimation comparison | 1,700 scalar comparisons and 196 exhaustive small missing-outcome bounds pass |
| Graph comparison | 2,536 d-separation comparisons agree with NetworkX |
| Isolated installation | Current Causal 0.3.0 wheel plus unchanged baseline Forge/Measurement wheels installed and used outside the source tree |
| Preservation | All 771 baseline files; other three common nodes; approved artwork; build policy; all 73 preceding Causal record revisions unchanged |

The new numerical comparison's largest scaled error was 2.3658663744245647e-14. Its seed and 1e-10 comparison threshold were declared before its execution. It is developer-created evidence, not a prospectively blinded or externally authored study. The inherited HTTP aborted-client tests can log BrokenPipeError while passing; no navigation/server fix is claimed.

## Reproduction

From the collection root, run `python tools/check_collection.py --out output/check-local` using a fresh directory. It supplies all shared source paths. Optional checks: `python CAUSAL-ATLAS/tools/quasi_oracle.py`, `python CAUSAL-ATLAS/tools/estimation_oracle.py`, and `python CAUSAL-ATLAS/tools/graph_oracle.py`. NumPy/NetworkX are optional developer dependencies, not new runtime dependencies. Missing optional tools report not_run rather than a pass.

The local RD calculator fits point estimates only. No robust intervals, data-driven bandwidth choice, density test, weak-IV confidence set or design authentication is implemented. All new numerical examples are synthetic; no authentic study dataset was acquired. Three new source cards have indexed-abstract-only scope, not complete-paper review. One PDF's visual screenshot access failed and is disclosed. Source-locator presence alone does not pass scientific review.

## Release checks

File inventories and ZIP integrity are checked after final content is packaged. The external `ATLAS_COLLECTION_RELEASE_v0.3.0.json` binds the completed archive and records extracted-archive reruns without a self-referential hash. These checks establish byte consistency, not authorship or scientific truth.

## Remaining work

Causal content readiness and final collection acceptance remain false. Authentic study reproduction, defensible statistical inference, longitudinal treatment/confounding, mediation/interference/transportability, independent scientific review and deferred host/model evaluation are still open. Materials remains queued. No remote publication, desktop installation, sharing change or account-Memory edit occurred.
