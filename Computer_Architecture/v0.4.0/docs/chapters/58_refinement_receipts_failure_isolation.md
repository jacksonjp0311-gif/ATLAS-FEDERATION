# Chapter 58 — Finite refinement receipts and fail-closed test batches

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Evidence proposition
Two implementations agreeing is useful but not sufficient to prove either correct. ATLAS FORGE's layered finite checks compare an independent structured-source evaluator, ISA reference, microcycle model and NAND arithmetic netlist. Disagreement is reported with explicit trace context. Successful finite cases are recorded as machine-readable claims with hashes and bounded input domains.

A batch runner should never report success for the entire collection simply because some programs finished. Each job receives a separate receipt indicating `passed` or `failed_closed`, and the batch status is the logical AND of these statuses. Unsupported instructions, exhausted input, program traps, nonterminating loops under the configured bound, and inconsistent outputs all become failures or HOLD—not omitted or substituted with invented traces.

## Worked challenge
Run a valid source-to-boot program, an invalid source program with an unrecognized operation, and a second valid program. The middle failure must be isolated and visible while the first and third receipts retain their own hashes. Re-run to compare canonical output. Then supply an intentionally infinite loop to the arithmetic refinement verifier and verify it returns HOLD rather than claiming all instructions were checked.

## Scientific caution
The independence here is algorithmic and finite; the same researchers wrote the test code, and a qualified external auditor has not signed it. Test fixtures cannot establish arbitrary program equivalence, computational complexity bounds, physical CPU behavior or secure execution. A published receipt's SHA-256 also does not establish author identity absent an authenticated trust anchor.

## Equation, implementation, and provenance

- **Key relation:** `expected_state = ISA(ROM,inputs) = microcycle(ROM,inputs) for retired steps`.
- **Reference algorithm:** `v04_bootstrap.verify_boot_batch; v02_trace.differential_retirement`.
- **Units:** instruction count, trace hashes and binary outputs.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
