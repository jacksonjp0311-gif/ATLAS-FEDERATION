# 02 — Events, causality, and partial orders

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Real-time order is different from the order of observable causal influence. Processes can observe independent events in different orders.

## System model, assumptions and derivation

Define a -> b if the same process executes a before b, or a is send and b its receipt, or there is a transitive chain. Neither a -> b nor b -> a makes events concurrent in the model. A total order can extend this partial order but will introduce arbitrary order between concurrent events.

**Formal invariant / expression:** `HB = transitive_closure(local_program_order union send_receive_edges).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Two isolated nodes A and B each issue an update. With no message passing, the updates are concurrent even if one machine clock happens to show an earlier timestamp.

## Repeatable numerical or code method

Write a finite event graph, explicitly add send/receive edges, compute transitive closure, and label concurrent pairs. Exclude physically observed time unless clock-error bounds are specified.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A Unix timestamp sorted log does not prove causality; NTP error, clock adjustments and partition delays can reverse timestamps.

**Evidence boundary:** Event graph measurements and trusted clock bounds must be separately collected. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LAMPORT1978` — Time, Clocks, and the Ordering of Events in a Distributed System — Leslie Lamport (1978); https://doi.org/10.1145/359545.359563. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
