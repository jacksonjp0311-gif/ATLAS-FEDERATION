# Atlas Forge 0.4.0 release audit

Date: November 12, 2026. This is an engineering checkpoint, not Measurement v1 acceptance.

## Actual local checks

| Check | Outcome | Scope |
| --- | --- | --- |
| Forge unit/regression suite | 165 passed | Includes all 75 baseline tests, new common/runtime/HTTP/guard/scaffold/adversarial fixtures |
| Measurement suite with Forge available | 55 passed | Includes all 31 baseline tests, numerical edge cases and shared reference tests |
| Common conformance | 399 records, 3 nodes, 8 typed relations | Hash/format/exact-link structure, not scientific truth |
| JSON Schemas | 4 checked; all records and sample contexts accepted | Optional developer jsonschema check |
| Source-intake structure | 20 bounded records, 9 source cards | Metadata/link/qualifier checks, not an independent source review |
| Agent skill headers | 5 passed | Project-local instruction files; not global installation |
| NumPy numerical comparison | 600 valid cases agree; 5 invalid cases rejected | Seed 86422; relative error at most 2.318e-15; synthetic numerical cross-check |
| Synthetic worked casebook | 5 examples passed | Explicit assumptions and units; no laboratory data |
| Clean wheel installation | Passed with no runtime dependencies beyond the two local wheels | Isolated Linux Python 3.13.5, no source-checkout import |
| UI rendering/event handlers | Desktop 1440x1000 and mobile 390x844 passed offline | Shipped JS with captured real local HTTP responses; image, contexts, budgets, no-match and JSON download |
| Direct browser navigation | Environment blocked loopback navigation | ERR_BLOCKED_BY_ADMINISTRATOR; not reported as end-to-end browser success |
| Windows run | Not run here | CI matrix retained, not yet executed remotely for this checkpoint |

Local HTTP endpoint and boundary tests ran against the actual server. Offline browser checks are distinct from those HTTP tests. Test logs, exact commands, installation logs and browser receipts are in `receipts/current/`.

## Authored retrieval diagnostic

The 25-question authored, previously seen set contains 20 target-record questions and five lexical no-match probes. BM25 returned a target at rank 1 for all 20. The simple lexical-overlap baseline hit the top five for all 20, with MRR5 0.925. Both returned no match for the five deliberately out-of-vocabulary probes. All 25 assembled contexts passed replay validation and byte budgets.

These exact-title-heavy fixtures are useful regressions, not an independent evaluation of semantic retrieval, out-of-domain understanding, real Bitwork or AI answer quality. No speed, energy or quality superiority claim follows from them.

## Gate decisions

G4 generic software conformance and G5 context-integrity software checks have local regression evidence. G1 scope and G2 scientific coverage remain partial. G3 still needs the full declared unit-aware domain case scope despite the passing numerical checks. G6 real Bitwork-to-Atlas-to-AI is blocked, G7 independent held-out comparison is not run, and G8 is partial pending supported-platform and direct browser verification. Criteria are proposed, not yet owner-approved/frozen. `v1_ready` and `next_domain_allowed` remain false.

The gate checker binds any claimed pass to actual-execution receipts, current release inputs and current criteria. This is an auditable local workflow guard, not authentication of a reviewer or a security barrier against a user editing the repository.

## Preservation and limitations

The 370 prior reference records are retained without promoted evidence labels. There are 20 new bounded Measurement records and nine new source-page cards. Legacy exports/HTTP remain frozen. The approved Forge artwork is byte-identical to v0.3. Existing Signal, Cymatics and Perci repositories have not been changed. No package was published or installed on the user's desktop by this work.

The actual Perci interface was inspected at commit 0811f45a5c7322f77a17c75856eabc9a7a620870; no Atlas-specific prototype map or live call is claimed. Source-portion checks are assistant checks, not peer review. Exact hashes validate identity, not scientific correctness. See BITWORK_BRIDGE.md and the companion Measurement source register.

Final source ZIP checks and extracted-archive test results are summarized in the delivery-level RELEASE_CHECKS.json, avoiding a checksum self-reference inside the archive.
