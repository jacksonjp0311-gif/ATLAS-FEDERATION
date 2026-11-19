# 14 — Deterministic fault schedules and oracle separation

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A reproducible finite trace is evidence only for those states and schedule bounds, not an argument for the infinite space of asynchronous executions.

## System model, assumptions and derivation

Represent a message scheduler by a finite sequence of delivery, delay, drop, duplication, crash and restart events. Keep protocol state separate from expected oracle state. Enumerate all small trace classes where possible, log random seeds for any randomized campaign.

**Formal invariant / expression:** `coverage = verified_checked_traces / explicitly_enumerated_trace_set; not P(real_world_success).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For n=5 nodes, independently enumerate every pair of size-three quorums and compute minimum overlap. Compare this to the analytic bound; negative control n=6, q=3 yields a disjoint pair.

## Repeatable numerical or code method

The independent oracle enumerates combinatorial sets and separate scalar component ordering. Negative test intentionally runs a proposer that violates inherited-value rule.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Ten thousand good finite traces are not a quantified probability of avoiding a real outage; hidden correlated faults remain unmodeled.

**Evidence boundary:** No formal model checking over unbounded delays or adversarial byzantine faults. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `PAXOS2015` — Paxos Made Moderately Complex — Robbert van Renesse; Deniz Altinbuken (2015); https://doi.org/10.1145/2673577. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
