# 04 — Vector clocks, concurrency and membership

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Vector clocks can distinguish causal order from concurrency when all participants share a fixed coordinate map and messages carry complete vectors.

## System model, assumptions and derivation

Componentwise relation V < W iff all components of V are <= corresponding components of W and at least one is strictly less. Event increments its local coordinate; receive takes componentwise max then increments its own coordinate.

**Formal invariant / expression:** `V < W iff (forall k V[k]<=W[k]) and (exists k V[k]<W[k]).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For two nodes, V_A=(1,0) and V_B=(0,1) are incomparable. After B receives A’s stamp, V_B=(1,1); A’s event is now causally prior to B’s receipt.

## Repeatable numerical or code method

Replay the fixed-membership clock model. Inject incomplete vector, stale merge, concurrent updates; compare to an independent componentwise enumerator.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Dynamic membership changes coordinate identity and compression assumptions; treating absent components as zero without a protocol can invent causality.

**Evidence boundary:** Operational membership transitions, clock garbage collection and byzantine stamps are outside v0.1. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LAMPORT1978` — Time, Clocks, and the Ordering of Events in a Distributed System — Leslie Lamport (1978); https://doi.org/10.1145/359545.359563. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
