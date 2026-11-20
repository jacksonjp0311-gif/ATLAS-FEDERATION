# 11 — Two-phase commit, atomic outcome and blocking

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Two-phase commit coordinates participant votes but can block after participants persist prepared state and the coordinator is unavailable.

## System model, assumptions and derivation

Phase 1: coordinator asks each participant to prepare and durably log YES/NO. Phase 2: it records and broadcasts COMMIT if all vote YES, otherwise ABORT. A YES participant may remain PREPARED without a decision; unilateral abort after YES can conflict with later COMMIT.

**Formal invariant / expression:** `decision = COMMIT if forall participant votes YES, else ABORT; after PREPARE and lost coordinator: outcome = UNRESOLVED.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Two participants vote YES; coordinator fails before durable decision. Both remain prepared, unable to safely infer commit or abort from silence. This is atomicity versus progress, not a consensus solution.

## Repeatable numerical or code method

Test transitions from INIT -> PREPARED/ABORTED -> COMMITTED and reject forbidden commit after abort. Inject coordinator unavailability immediately after prepare.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Treating “no reply” as a NO vote after the YES was durably recorded can violate atomic decision assumptions.

**Evidence boundary:** No distributed transaction manager, durable participant logs or real crash recovery implemented. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `GRAY1978` — Notes on Database Operating Systems — Jim Gray (1978); https://doi.org/10.1007/3-540-08755-9_9. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
