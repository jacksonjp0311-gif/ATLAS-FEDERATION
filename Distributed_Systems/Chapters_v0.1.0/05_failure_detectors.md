# 05 — Timeouts, suspicion and partial synchrony

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A local timeout is evidence of non-response, not proof of remote crash.

## System model, assumptions and derivation

Pure asynchrony supplies no known upper bound on message delay or processor scheduling. Partial synchrony permits eventual timing bounds after an unknown stabilization point, enabling liveness claims with timeouts while preserving separate safety reasoning.

**Formal invariant / expression:** `timeout_expired := observed_delay > local_threshold; timeout_expired does not imply crashed.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

With threshold 500 ms, an otherwise healthy node delayed 650 ms is falsely suspected. Repeating timeouts may improve responsiveness but does not make the failure detector omniscient.

## Repeatable numerical or code method

Construct delayed and permanently lost message traces; require safety properties under either trace and qualify progress by eventual delivery assumptions.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Aggressive retries can amplify load, causing more timeouts and a self-sustaining overload spiral.

**Evidence boundary:** No real WAN latency profile, calibrated clock or measured operational failure-detector completeness. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `DLS1988` — Consensus in the Presence of Partial Synchrony — Cynthia Dwork; Nancy Lynch; Larry Stockmeyer (1988); https://research.ibm.com/publications/consensus-in-the-presence-of-partial-synchrony. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
