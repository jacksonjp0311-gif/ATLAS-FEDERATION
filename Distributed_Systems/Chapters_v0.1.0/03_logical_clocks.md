# 03 — Lamport scalar clocks and message envelopes

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Scalar logical clocks preserve the implication causal precedence => increasing clock values, but cannot prove causal precedence from numeric ordering alone.

## System model, assumptions and derivation

For local/send event L_i := L_i+1. For receive of stamp s, L_i := max(L_i,s)+1. This ensures send timestamp is less than its receipt timestamp. Ties may be broken with a stable process ID for a deterministic total-order extension.

**Formal invariant / expression:** `L_i(receive(s)) = max(L_i_before,s)+1.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Node A starts at 0 and sends a message stamped 1. B already processed four local events, so B receives at logical 5. A later local timestamp 2 does not mean A observed B’s receive.

## Repeatable numerical or code method

Run clocks.py LamportClock and compare send/receive monotonicity with algebraic max. Include malformed timestamp and overflow policy in real implementation.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** If two unrelated events carry logical values 2 and 3, their numeric order alone cannot establish that one caused the other.

**Evidence boundary:** Python integer is arbitrary precision; real embedded counters require bounded rollover specification. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LAMPORT1978` — Time, Clocks, and the Ordering of Events in a Distributed System — Leslie Lamport (1978); https://doi.org/10.1145/359545.359563. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
