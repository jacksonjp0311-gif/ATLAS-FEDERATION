# 08 — Single-decree Paxos and inherited accepted values

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Acceptor promises reject older ballots, and a proposer with quorum promises adopts the value of the highest-numbered already-accepted proposal observed.

## System model, assumptions and derivation

Phase 1 prepare(n): acceptor promises n only if n exceeds prior promise and returns its accepted ballot/value. Phase 2 accept(n,v) allowed iff n >= promised. The proposer must select prior accepted value with maximal ballot from its promise quorum, otherwise propose its own. Intersecting quorums then help preserve agreement for one decree under stable acceptor state.

**Formal invariant / expression:** `proposer_value = argmax_{accepted prior in quorum} accepted_ballot.value, else client_value.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

In a three-node run, ballot 1 for X is accepted by A and B. Ballot 2 sees B and C; because B reports X, ballot 2 must propose X even when client asks for Y. A deliberately incorrect proposer that discards B’s accepted value can choose Y and violate agreement.

## Repeatable numerical or code method

Execute sequential proposer reference, test stale ballots, missing majority, adopted value and the explicit unsafe control. Persist acceptor promised/accepted state before sending acknowledgements in any real protocol.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A Python acceptor object without storage durability, concurrency model or duplicate-message handling is an educational finite trace, not a production Paxos system.

**Evidence boundary:** Multi-Paxos leadership, flexible quorums, active byzantine agents and real-time scheduling unverified. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `PAXOS1998` — The Part-Time Parliament — Leslie Lamport (1998); https://www.microsoft.com/en-us/research/publication/part-time-parliament/. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.
