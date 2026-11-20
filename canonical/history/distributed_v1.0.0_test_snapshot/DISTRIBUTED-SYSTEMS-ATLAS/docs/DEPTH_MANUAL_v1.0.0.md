# ATLAS FORGE — Distributed Systems Atlas #12 · v0.1.0

**Original scientific federation. Single canonical collection.**

This is a new domain node added to the exact 17-node Software Design Patterns v0.1.0 predecessor. It is not a separate Atlas, a routing implementation or a claimed production consensus service.

There are 16 original technical chapters and 12 bibliographic source cards. All chapter records carry exact revision digests, source-record exact revisions and qualified dependency edges, and cross-domain links explicitly target four previous unmodified source record revisions.

The models are executable with Python 3 standard library. Their finite tests and independent enumerators establish only the checked mathematical properties within the stated model. A true network, crash-recovery, power-loss, enterprise transport security, Byzantine attacks, real-time guarantees, publisher byte authentication and independent scientific peer review remain HOLD.



---

# 01 — System boundaries and failure semantics

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A distributed system consists of independent state machines that exchange messages; their visible behavior depends on fault and timing assumptions.

## System model, assumptions and derivation

Safety means bad output never occurs; liveness means desirable progress eventually occurs under a stated schedule. Model crash-stop, crash-recovery, network loss, duplication, reordering, delay, partitions, Byzantine deviation and disk corruption as distinct failure families.

**Formal invariant / expression:** `Safety = forall admitted traces t: not Bad(t). Liveness = forall fair traces t: eventually Good(t).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For a three-node archive index, let A and B keep responding while C is disconnected. Quorum read/update can proceed on A,B only if their persisted state and protocol match. A simple local retry cannot establish whether C crashed or messages are delayed.

## Repeatable numerical or code method

Enumerate allowed fault events separately. Mark network delay unbounded unless timing is assumed, enforce one transition at a time for the finite model, record violated invariants and rejected counterexamples.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A paused but healthy node may be falsely suspected; a power-loss disk that acknowledges data before persistence is not a crash-stop process.

**Evidence boundary:** No real scheduling fairness or end-to-end delivery guarantee is established by a finite simulator. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `FLP1985` — Impossibility of Distributed Consensus with One Faulty Process — Michael J. Fischer; Nancy A. Lynch; Michael S. Paterson (1985); https://doi.org/10.1145/3149.214121. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

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


---

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


---

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


---

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


---

# 06 — Consistency, availability and network partitions

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

During a partition, an implementation that provides every reachable client a response may have to relax single-copy consistency; one must state exact definitions.

## System model, assumptions and derivation

Linearizability requires operations to appear atomic while respecting nonoverlapping real-time precedence. Partition tolerance means the system continues to obey its specification despite arbitrary message loss between components. The familiar CAP impossibility is about these formal definitions under partitions.

**Formal invariant / expression:** `P and A (every request eventually responds) and strict linearizable C cannot all be guaranteed in the asynchronous partition model.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

With a disconnected two-replica store, side A writes x=1 and returns success; side B, unable to talk to A, must choose to block, return stale data, or violate linearizable reads if it answers x=0.

## Repeatable numerical or code method

State the consistency model and availability liveness predicate; simulate a partition and assert the precise expected failure or abstention, not a slogan about arbitrary tradeoffs.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Classifying a system as CP or AP for all conditions obscures its normal-operation consistency, latency and stale-read behaviors.

**Evidence boundary:** Model assumes the paper’s formal availability definition, not a user satisfaction or SLA measurement. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `CAP2002` — Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services — Seth Gilbert; Nancy Lynch (2002); https://doi.org/10.1145/564585.564601. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

# 07 — Crash-fault quorums, overlap and availability

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Quorum intersection is a combinatorial prerequisite for transferring knowledge between rounds, but not a complete consensus protocol.

## System model, assumptions and derivation

Two sets of sizes q1 and q2 drawn from n nodes have intersection at least max(0,q1+q2-n). Hence every pair intersects iff q1+q2>n. Strict majority q=floor(n/2)+1 satisfies self-intersection.

**Formal invariant / expression:** `min_overlap=max(0,q1+q2-n); majority=floor(n/2)+1.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For n=5, q=3; any two quorums overlap at >=1 node. Failure of 2 replicas leaves 3 responsive and permits quorum; failure of 3 leaves at most 2 and forces abstention. For n=6, q=3 can select disjoint sets: overlap is not guaranteed.

## Repeatable numerical or code method

Enumerate combinations for n<=8 and compare against the independent arithmetic prediction. Track unavailable nodes and the logical availability predicate.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Intersecting quorums do not guarantee safety when nodes forget accepted ballots after restart, or proposers ignore prior accepted values.

**Evidence boundary:** A quorum is not evidence that an acknowledged write was physically flushed or that Byzantine faults were handled. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `PAXOS1998` — The Part-Time Parliament — Leslie Lamport (1998); https://www.microsoft.com/en-us/research/publication/part-time-parliament/. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

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


---

# 09 — Replicated logs and leader-election invariants

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A replicated state machine needs an agreed ordered command history, not just agreement on isolated values.

## System model, assumptions and derivation

Raft separates leader election, log replication and safety. Terms and per-index log metadata guard against inconsistent leaders, while the committed prefix cannot be overwritten by future elected leaders if election and commit rules are respected.

**Formal invariant / expression:** `For committed prefix length c: apply_i(log[1:c]) must be deterministic and equal across correct replicas of same membership/epoch.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

If a follower has entries (1:A,2:B), a new leader may reconcile an uncommitted suffix but may not erase a committed entry 1:A. The reference compares this narrative with single-decree Paxos; it does not claim to implement Raft.

## Repeatable numerical or code method

Write adversarial histories: stale leader, conflicting log suffix, crash after append before commit, and restart with persisted term. Require an explicit invariant checker and model checker before claiming agreement.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Electing a leader by largest wall-clock timestamp instead of log term and committed-entry rules risks electing stale replicas.

**Evidence boundary:** No multi-decree Raft service, election scheduler, snapshot installation or membership reconfiguration implementation in this edition. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `RAFT2014` — In Search of an Understandable Consensus Algorithm — Diego Ongaro; John Ousterhout (2014); https://web.stanford.edu/~ouster/cgi-bin/papers/raft-atc14.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

# 10 — Semilattice CRDT merge and eventual convergence

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A state-based CRDT converges when updates inflate replica state in a join-semilattice and repeated deliveries merge by the associative, commutative and idempotent join.

## System model, assumptions and derivation

A grow-only counter stores a nonnegative per-node integer map and merges pointwise maximum; readout sums components. An observed-remove set stores unique add dots and a tombstone set; a removal only removes dots observed at that replica, allowing concurrent add wins.

**Formal invariant / expression:** `join(a,b)=join(b,a); join(join(a,b),c)=join(a,join(b,c)); join(a,a)=a.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Replica A counts {A:2}, B counts {B:3}; merge yields total 5 regardless of message order. For OR-Set, A removes dot A:1 while B concurrently adds B:1; after merge the item remains present due to B:1.

## Repeatable numerical or code method

Run GCounter/ORSet with repeated and reordered merges; compare with independent maxima over finite vectors, test dot uniqueness and removal semantics.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Unique event dots and stable replica identifiers are prerequisites. Tombstone cleanup without a causal stability protocol can resurrect removed values.

**Evidence boundary:** CRDT convergence does not imply serializable transactions or general conflict-free business semantics. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `CRDT2011` — A Comprehensive Study of Convergent and Commutative Replicated Data Types — Marc Shapiro; Nuno Preguiça; Carlos Baquero; Marek Zawirski (2011); https://asc.di.fct.unl.pt/~nmp/pubs/tr-inria-2011.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

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


---

# 12 — Idempotent command journals and scope of exactly-once

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A unique transaction key with an atomic state update can prevent duplicate local database mutations, but cannot guarantee exactly-once remote or physical effects.

## System model, assumptions and derivation

Within a single SQLite transaction, insert a unique key and change local materialized state. On retry, first query the key; equal payload returns prior effect without reapplying. A conflicting payload with the same key must be rejected. Commit configuration, file system and backup policy matter.

**Formal invariant / expression:** `apply_once(key,delta) = prior_state if key already in journal and delta equal; otherwise prior_state+delta on first insert.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Submit k=repair-7, delta=+3 twice; tally rises by 3 once. Submit the same k with delta=+4; reject. After process restart, a fresh connection reports committed local tally.

## Repeatable numerical or code method

Use the sqlite3 standard library, WAL and synchronous FULL as a software setting; independently reopen DB and validate state. Never call external actuator within the same transaction and infer exactly-once.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** If a remote printer starts a motor after a successful RPC but before acknowledgment, retrying may start it twice, regardless of the SQLite key.

**Evidence boundary:** No measured disk cache honesty, power-cut tests, external delivery reconciliation or production concurrency races. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LINEAR1990` — Linearizability: A Correctness Condition for Concurrent Objects — Maurice Herlihy; Jeannette Wing (1990); https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

# 13 — Content-addressed integrity and restart reconstruction

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

A SHA-256 hash chain detects many accidental or unsophisticated modifications under an intact, trusted head; it does not authenticate data against an attacker who can rewrite the whole chain.

## System model, assumptions and derivation

Canonicalize each event into UTF-8 sorted-key JSON. Let H_0 be fixed genesis, H_{i+1}=SHA256(bytes(H_i)||canonical(event_i)). Recompute after restart and reject any mismatch before rebuilding projections.

**Formal invariant / expression:** `H_(i+1) = SHA256(H_i || encode_canonical(event_i)).`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

For events {a:1},{b:2}, compute two heads. Change the first event to {a:2} without changing the published head and the chain verification fails. But attacker can recompute both if no trusted anchor is externalized.

## Repeatable numerical or code method

Use journal.extend_chain/verify_chain; require event schema validation, canonical encoding, checksum and independent head copy for long-term archival.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** Bit rot, truncation and malicious re-signing require different mitigations. A trusted external anchor and immutable backups are not implemented.

**Evidence boundary:** Cryptographic integrity is not physical storage reliability, authenticity without protected key or scientific source verification. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `LINEAR1990` — Linearizability: A Correctness Condition for Concurrent Objects — Maurice Herlihy; Jeannette Wing (1990); https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

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


---

# 15 — Transport, partitions and replica reconciliation

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

Transport reliability and logical replication correctness are separate problems: TCP does not automatically imply transactional exactly-once processing at the application layer.

## System model, assumptions and derivation

Messages need stable IDs, schema versions, bounded sizes, sequence or causal metadata and explicit retry policy. During partition, local state may diverge within the specified consistency model. Reconciliation must guard against replay, loss, duplicate delivery, and stale membership.

**Formal invariant / expression:** `Safety envelope = validated_identity + accepted_schema + bounded_payload + durable_commit_rule + replay_policy.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

Disconnect B, queue updates on A, reconnect and deliver the same update twice; a GCounter merge is idempotent but a naive integer increment is not. Distinguish eventual convergence from ordered log agreement.

## Repeatable numerical or code method

Simulate duplicates and reorder; verify a CRDT merge and compare to strict state-machine command replay. Add CRC/hash only for corruption detection, not identity trust.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A stale node with a reused replica ID can violate unique-dot assumptions and a client can read stale data after partition heal while background anti-entropy is incomplete.

**Evidence boundary:** No actual network stack or authenticated wire protocol implemented; operational performance unknown. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `BAYOU1995` — Managing Update Conflicts in Bayou, a Weakly Connected Replicated Storage System — Douglas B. Terry and colleagues (1995); https://doi.org/10.1145/224056.224070. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

# 16 — Offline distributed-system reconstruction and acceptance ladder

**ATLAS FORGE / original federation / Distributed Systems v0.1.0**

## Reconstructible scientific question

ATLAS FORGE should let a future operator rebuild communication and distributed storage from validated primitives, but must separate the educational algorithm from a service ready to preserve life-critical data.

## System model, assumptions and derivation

The technical dependency ladder runs: reliable single-node arithmetic and storage -> message framing and schema -> causal event logs -> independent replica snapshot -> failure model -> quorum/consensus test implementation -> durable replica log -> fault-injected recovery -> real-host network and power-loss evidence. Every promotion needs its own receipt.

**Formal invariant / expression:** `Release acceptance = source integrity AND exact-version graph AND finite tests AND reconstructed archive; physical acceptance requires external measured experiments.`

The variable meanings and scope follow from this model. Node counts are dimensionless; logical time is expressed as discrete ticks and is not physical seconds unless a clock model states a measured mapping. When a set is involved, cardinalities count distinct node identities, not messages. These definitions must be preserved by a future implementation before interpreting its outputs.

## Worked constructed investigation

A local laptop with two VM replicas can simulate three endpoints but shares one power source, storage controller and failure domain; it cannot establish independent fault tolerance. Use multiple isolated hosts and forced power-cut tests only after correct safe bench preparation.

## Repeatable numerical or code method

Restore Atlas using exact predecessor and incremental patch; run the full federation suite, then independently verify replicated snapshot reproducibility. Record observed hashes and external source gaps.

**Practical reconstruction criterion:** Save the input state, declared scheduling model, exact software version, expected independent relation, observed output and any invariant violation. Re-run in a clean Python environment without external network dependencies. Preserve the failed traces as first-class knowledge; do not quietly remove a failing case when fixing code.

## Negative case and uncertainty

**Failure case:** A USB backup whose copy succeeds is not validated until a fresh machine restores it and checks source-file hashes. A laptop-only simulation is not multi-host disaster qualification.

**Evidence boundary:** Operational acceptance remains on HOLD: publisher bytes, independent expert review, real power-loss, network certification, cryptographic trust and field reproducibility. This chapter is original educational explanation, not physical experimental verification, independent peer review, source-original authentication, a certified safety interlock or a complete implementable distributed service.

## Primary background locator and provenance

Bibliographic key: `DLS1988` — Consensus in the Presence of Partial Synchrony — Cynthia Dwork; Nancy Lynch; Larry Stockmeyer (1988); https://research.ibm.com/publications/consensus-in-the-presence-of-partial-synchrony. This is a source pointer; original publisher bytes and page-specific claim mapping remain unverified.

## Cross-domain applications

Software Design Patterns supplies state-machine and durable-journal programming vocabulary; Computer Architecture supplies memory/storage assumptions; Computation supplies deterministic algorithmic semantics; Measurement supplies evidence and uncertainty handling. External hardware-level claims remain separate HOLDs.


---

# Substantive scoped v1.0.0 evolution: formal safety, recovery, and negative cases

# 17 — Crash-recovery acceptor: persistence before response

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 17**

## Scientific question

What must survive restart if an acceptor promises ballot n and reports an accepted value?

## Mathematical and engineering foundation

An acceptor stores the largest promised ballot p and the highest accepted pair (a,v) in nonvolatile state. The command PREPARE(n) must not acknowledge a new promise until p>=n has been durably recorded. ACCEPT(n,v) must not report accepted until the accepted tuple and promise have crossed the same durability boundary. If a restarted acceptor forgets a promise, it may accept an older ballot after a new proposer relied on the promise. If it forgets an accepted pair, a new proposer might choose a different value even though a majority previously accepted one. The latter defeats the core highest-prior-accepted-value argument. In Paxos, ballot uniqueness belongs to proposers and must be globally enforced; an acceptor cannot safely accept different values for the same ballot.

## Derivation and formal invariant

Let durable state D=(p,a,v). PREPARE(n) with n>p produces D'=(n,a,v) and returns (a,v). ACCEPT(n,w) with n>=p produces D'=(n,n,w) and returns success, except conflicting reuse of accepted ballot n is rejected. The write-ahead transaction is a logical atomic transition, not a claim that every physical controller flushes honestly. A non-volatile test must record storage model, acknowledgement semantics, OS, filesystem, drive firmware, cache settings, and emergency power schedule.

## Worked constructed investigation

On a fresh SQLite file: PREPARE(5) returns (-1,None). Recreate the Python process and PREPARE(4) returns no promise. ACCEPT(5,"A") persists (5,5,"A"). Reopen and PREPARE(6) returns (5,"A"). The next proposer inherits A, not its own suggested B. The two transaction boundaries can be reproduced offline with `durable_acceptor.py`.

## Reproduction procedure and negative control

Reject a fresh lower ballot after restart; reject a conflicting same-ballot value. Run a deliberately broken recovery that resets p to -1 and show stale ACCEPT becomes possible. Do not call a process restart a power-cut or a cross-host recovery test.

## Assumptions, evidence class and known failures

The reference uses SQLite WAL and synchronous FULL, but does not simulate torn sectors, write-cache lies, VFS error paths, NFS, replication, power loss, or malicious storage.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/durable_acceptor.py`. Bibliographic source card: `distributed-systems-atlas:source:PAXOS_SIMPLE2001` at exact revision `0b62f5c76aca4a167d492efbd69408c780de49d72f880ad401178c1dc711ae22`. Full source locator: https://www.microsoft.com/en-us/research/publication/paxos-made-simple/. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 18 — Bounded multi-proposer Paxos agreement and counterexamples

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 18**

## Scientific question

Can two competing ballots choose different values when quorums overlap and promises persist?

## Mathematical and engineering foundation

Agreement is a safety assertion: if value v is chosen at a ballot b, any later chosen value must also be v. Distinct ballots 1 and 2 may be proposed concurrently. Each proposer first gathers a majority of Phase-1 promises; it adopts the value of the highest accepted proposal among those responses, or its own candidate when none exists. Phase-2 acceptance is allowed only at acceptors not subsequently promised a higher ballot. Network loss can remove arbitrary replies; it cannot invent acceptance or erase a durable promise. Majority overlap guarantees that a later quorum touches a previous chosen quorum but adoption, not overlap alone, enforces value continuity.

## Derivation and formal invariant

For N=3, quorum size Q=floor(N/2)+1=2. Any two majorities intersect in at least 2Q-N=1 acceptor. The model enumerates nondeterministic Phase-1 responder subsets, Phase-2 delivered subsets, and either proposer ordering. The explorer stores normalized immutable acceptor states, phase counters and chosen values. It checks invariant |set(chosen)|<=1 at every state. It is a *macro-step* transition system: phases are atomic per chosen responder subset. It does not cover every byte-level delivery interleaving in a real network.

## Worked constructed investigation

Start three acceptors at (-1,-1,None). P1 prepares at A,B, then accepts A at A,B; A is chosen. P2 then prepares B,C, sees B's previously accepted (1,A), adopts A, and chooses A. With an intentionally incorrect proposer that ignores the prior accepted value, P2 can instead choose B, violating agreement. The counterexample has four phase actions and is retained as evidence, not discarded as an inconvenient test.

## Reproduction procedure and negative control

Breadth-first enumeration uses an explicit maximum-state limit. A truncated search returns UNKNOWN, never PASS. Save the discovered state count, bounds and negative mutation trace in the evidence receipt. Scope is three acceptors, two uniquely numbered single-decree proposers, one attempt each, with lost replies and phase interleavings.

## Assumptions, evidence class and known failures

A bounded state exploration cannot prove infinite-state Paxos, fair eventual progress, all transport message races, dynamic membership or Byzantine resistance.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/model_check.py`. Bibliographic source card: `distributed-systems-atlas:source:PAXOS_SIMPLE2001` at exact revision `0b62f5c76aca4a167d492efbd69408c780de49d72f880ad401178c1dc711ae22`. Full source locator: https://www.microsoft.com/en-us/research/publication/paxos-made-simple/. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 19 — Completed histories and the linearization witness

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 19**

## Scientific question

When does an observed register history admit a single atomic sequence consistent with wall-clock ordering?

## Mathematical and engineering foundation

A completed operation has an invocation time s and response time e, with s<e. If operation A completed before B began, then A must precede B in any valid linearization. Overlapping operations have no forced order from time alone. A legal sequential register starts with a known value r0; a successful write(v) replaces r, and read() returns the current r. The checker seeks any permutation of completed operations that respects non-overlap precedence and sequential register semantics. It must not label unknown or pending invocations as confirmed failures or successes.

## Derivation and formal invariant

Define a directed precedence edge A->B when end(A)<=start(B). A sequential witness is a topological ordering of this real-time partial order that satisfies read and write specification. A write of value '1' at [1,2] followed by a read at [3,4] returning '0' has no witness (assuming initial '0' and no intervening write). If write spans [1,5] and the read spans [2,3], a read of '0' can be linearized before that write; stale-looking response is not automatically a violation.

## Worked constructed investigation

Run `history_witness([Op('w','write',1,2,value='1',result='ok'), Op('r','read',3,4,result='1')])`: witness ('w','r'). Change only the returned read value to '0': the witness becomes None. Overlap the two intervals and the same '0' read is consistent. Verify the implementation against a separate brute-force permutation oracle over 1,000 finite three-operation histories.

## Reproduction procedure and negative control

Cap the number of completed operations at nine to avoid pretending this exponential checker scales. Reject invalid time intervals, duplicate IDs, unsupported methods and unobserved return values. A real distributed-service history must include client-clock error estimates, process IDs, invocations, responses, and what happened to indeterminate operations after timeout.

## Assumptions, evidence class and known failures

This is a one-register educational checker. It is not Elle, Jepsen, multi-key serializability, a proof of real-time clock accuracy, or a general database consistency auditor.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/linearizability.py`. Bibliographic source card: `distributed-systems-atlas:source:LINEAR1990` at exact revision `cdceae6ef1d6c67c420c4e19a5b4d9f1606b61946140365a760b45f5bbfe413d`. Full source locator: https://www.cs.columbia.edu/~wing/publications/HerlihyWing90.pdf. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 20 — From safety invariants to conditional liveness

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 20**

## Scientific question

Why does finding no agreement violation fail to prove a distributed system will terminate?

## Mathematical and engineering foundation

A safety property has a finite counterexample: one unsafe transition suffices. Liveness quantifies over infinite executions and therefore needs scheduling or fairness assumptions. An asynchronous network can delay messages indefinitely without distinguishing the situation from a crashed process. In the model, losing every Phase-1 reply yields no decision but also no disagreement. A legal leader election under eventual synchrony may offer progress after stabilizing conditions; ordinary unreliable timeouts are only suspicions. Adding a finite timeout is not a substitute for a delivery assumption.

## Derivation and formal invariant

Use separate indicators: agreement_safe in {True, False, Unknown}; progress_observed in {True, False}; and progress_assumptions as an explicit predicate. Example assumption A: a majority of non-Byzantine acceptors remains reachable, messages between selected nodes are eventually delivered, and a unique proposer retains leadership long enough to complete two phases. Without A, a finite deadlocked prefix does not establish liveness failure; without stable storage, A does not rescue safety.

## Worked constructed investigation

Case 1: three nodes, B partitioned, A and C reachable; Q=2, a proposer can choose after promises and acceptances reach both. Case 2: only A reachable; no proposer reaches Q=2; agreement remains true yet progress stalls. Case 3: two proposers repeatedly preempt each other; a fairness or leader-stability mechanism becomes necessary for progress.

## Reproduction procedure and negative control

Record event schedules, fault injection seed, observed partition graph, log of accepted proposals, decision eligibility, and what is assumed to improve after network stabilization. Do not mistake a passing bounded model check for a liveness theorem.

## Assumptions, evidence class and known failures

The provided finite explorer intentionally makes no infinite-schedule fairness claim and tests no real network scheduler or failure detector.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/model_check.py`. Bibliographic source card: `distributed-systems-atlas:source:PAXOS_SIMPLE2001` at exact revision `0b62f5c76aca4a167d492efbd69408c780de49d72f880ad401178c1dc711ae22`. Full source locator: https://www.microsoft.com/en-us/research/publication/paxos-made-simple/. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 21 — Membership changes and cross-configuration quorum safety

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 21**

## Scientific question

What breaks if an archive cluster silently changes voter sets?

## Mathematical and engineering foundation

For a fixed voter configuration C, majority quorums overlap because their cardinalities exceed half of |C|. During a configuration change, a majority of C_old need not intersect a majority of C_new if voters are added or removed without a joint protocol. E.g. old={A,B,C}, new={D,E,F}; both have quorum size 2 but share no voter. A safe reconfiguration procedure must enforce overlap of committing quorums across the transition or use a proven joint-consensus/log-entry rule, with terms and activation order persisted.

## Derivation and formal invariant

For any two allowed decision quorums Q_old and Q_new, a necessary intersection constraint is Q_old ∩ Q_new != empty for conflicting values. A joint-config rule may require separate majorities from both old and new voter sets. However, this numerical condition alone does not prove reconfiguration correctness: leadership terms, log match, commit index and stale configuration fencing need independent proof.

## Worked constructed investigation

Worked example: old voters A,B,C and new C,D,E. Old majority A,B and new majority D,E are disjoint despite one common *member* C. Therefore mere overlapping membership does not imply all quorums intersect. A design that casually overwrites the voter list can split decisions. Preserve old configuration until an agreed transition entry is committed and recovered.

## Reproduction procedure and negative control

Reconstruction exercise: enumerate all old/new voter majority subsets, compute minimum intersection and report disjoint witnesses. Use a historical log with original voter-set revision and deployment epochs; treat all output as a necessary numerical precondition, not a deployed algorithm.

## Assumptions, evidence class and known failures

No executable dynamic-membership consensus or Raft joint-consensus implementation is provided; this chapter is a documented hazard and acceptance gap.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `docs/chapters/21_reconfiguration.md`. Bibliographic source card: `distributed-systems-atlas:source:RAFT_DISSERTATION2014` at exact revision `49ce4c200d48777a71b082959fe23660bea955f7fd613711bcf2f9bc2c04c888`. Full source locator: https://github.com/ongardie/dissertation. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 22 — State-machine replication snapshots and log prefixes

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 22**

## Scientific question

How can a recovering node trust a snapshot without confusing integrity with consensus?

## Mathematical and engineering foundation

A deterministic replicated state machine applies committed commands in the same total order to the same initial state; its state after prefix k is S_k = f^k(S0,c1..ck). A snapshot may record S_k, last included index k, term/epoch t, schema revision, command prefix hash H_k, and content digest. Before installing a snapshot the receiver must ensure it corresponds to a committed prefix recognized by the protocol, not merely a matching SHA-256. An attacker or broken leader can compute a valid hash over the wrong history.

## Derivation and formal invariant

Let H_0 be an agreed genesis digest and H_i=SHA256(H_{i-1} || canonical(command_i)). Equality H_k(source)=H_k(receiver) detects accidental corruption in transmitted bytes if the expected head is trusted, but does not certify consensus or source authenticity. After install, replay commands k+1..n with exactly-once *local application* guard; distinguish already applied from accepted but uncommitted records.

## Worked constructed investigation

Constructed case: a snapshot at index 10 contains state counter 37 and H_10. Recovery reads snapshot, validates its recorded digest, checks protocol committed index >=10 and trusted head H_10, then replays commands 11 and 12 only. A node that applies command 10 again produces an incorrect count despite each individual command being mathematically valid.

## Reproduction procedure and negative control

Maintain two ledgers: (1) protocol-proven commit state, (2) storage-level checksums and atomic rename receipts. Test corruption detection, missing prefix and conflicting head as negative controls. Archive the recovery inputs and expected state in the offline evidence bundle.

## Assumptions, evidence class and known failures

Snapshot checksums and deterministic replay do not prove trust anchors, peer authenticity, real replicated-log safety or storage persistence under power failure.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `docs/chapters/22_snapshots.md`. Bibliographic source card: `distributed-systems-atlas:source:RAFT_DISSERTATION2014` at exact revision `49ce4c200d48777a71b082959fe23660bea955f7fd613711bcf2f9bc2c04c888`. Full source locator: https://github.com/ongardie/dissertation. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 23 — Replica reconciliation, causal stability and tombstone deletion

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 23**

## Scientific question

When can a set replica forget deletion metadata without resurrecting old elements?

## Mathematical and engineering foundation

An observed-remove set remembers per-add unique dots and records tombstones for dots already observed and removed. Merge is set union over add facts and removed dots, producing an associative, commutative, idempotent join. Deleting tombstones merely because the local display no longer contains an element is unsafe: an offline peer can later re-send a pre-removal add dot, resurrecting it. Safe garbage collection requires knowledge that all relevant replicas have observed the removal, or an epoch/anti-entropy protocol that prevents obsolete peers from rejoining unqualified.

## Derivation and formal invariant

Let A be add-dot set and T the tombstone set; visible V={element e | exists dot d: (e,d)∈A and d∉T}. Merge (A,T) ⊔ (A',T') = (A∪A', T∪T'). This join proves convergence of the modeled sets without GC. A causal-stability lower bound for dot d requires every current member's observed frontier to cover d and safe management of membership churn. An acknowledgement from a single peer is insufficient.

## Worked constructed investigation

Replica A adds token x with dot A:1; B receives the add and removes x, producing T={A:1}. A is offline during removal. If B discards T then A later sends A:1 again, x reappears in B's visible set. Retaining T prevents resurrection. The event is a counterexample to unsound tombstone collection, not an implementation bug in the merge operator.

## Reproduction procedure and negative control

Rebuild and test with two isolated replicas, an add, an observed remove, a long partition, and a stale rejoin. Record dots, causal frontiers, membership revisions and how retired replicas are fenced.

## Assumptions, evidence class and known failures

General CRDT stability and garbage collection are not implemented; the v0.1 OR-Set intentionally retains tombstones indefinitely.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `distributed_atlas/crdts.py`. Bibliographic source card: `distributed-systems-atlas:source:ELLE_2020` at exact revision `2f7d2a82cbcc093fa16e9c83f269b93940c6b1e0e3f8e647aad2e0609386f7c9`. Full source locator: https://github.com/jepsen-io/elle. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.


---

# 24 — Offline protocol verification and reproducible scientific evidence

**ATLAS FORGE / Distributed Systems / original scoped content v1.0.0 / chapter 24**

## Scientific question

What is the smallest defensible evidence package for a future builder to distinguish a safe algorithm from a reassuring simulation?

## Mathematical and engineering foundation

A protocol claim must bind its model and observable predicates. Preserve an input manifest with exact program and corpus revisions, dependencies, checker bounds, CPU/runtime, random seeds, failure rules, observed counterexamples and a complete pass/fail receipt. Distinguish (a) an abstract mathematical property, (b) a checked finite executable model, (c) a fault-injected host-level implementation, (d) measured physical hardware durability, and (e) external qualified scientific review. Advancement through one layer does not silently promote another.

## Derivation and formal invariant

Construct a chain of independent evidence: logical oracle based on alternate formulation; negative mutation that is guaranteed to fail; full federation regression against exact unchanged predecessor; deterministic archive hash; isolated fresh restore; finally human or instrumented validation. Model checker PASS is bounded by the enumerated state count; if a cap is reached, the result is INCOMPLETE, not PASS. A SHA-256 manifest proves equality only to an authenticated expected digest; without trusted signing it can accompany a malicious rewrite.

## Worked constructed investigation

The scoped release exercise runs the three-acceptor model-checker, a 1000-history independent linearizability oracle, database process restart tests, full common-contract tests and archive reconstitution. Record mismatches rather than adjusting test expectations until they pass. Preserve a legacy 18-node fixture so all previous release-specific tests execute unchanged.

## Reproduction procedure and negative control

For an actual physical experiment, specify network fault injector settings, drive/OS and cache, power-cut triggering circuitry, ground truth observer, exact timing resolution, number of trials, original traces and reviewer signatures. None of these measurements is generated by this software-only increment.

## Assumptions, evidence class and known failures

This content establishes an independently reproducible offline software reference only; no production certification, publisher-original authentication or proof over unbounded networks follows.

The equations and protocols are educational reference models, not authenticated original publisher text. Integer ballot numbers and node counts are dimensionless. Logical event ticks are not calibrated seconds; measured physical time is required to make latency claims. All claims must retain source qualification, model bounds and unverified evidence status. A future system must not treat absence of counterexamples in this finite model as universal correctness.

## Software, reference, and future validation

Reference: `evidence/independent_oracle_v1.py`. Bibliographic source card: `distributed-systems-atlas:source:SQLITE_SYNCHRONOUS` at exact revision `68638793cfc152570a206410b31bbdd9ba752143f1a9c9535f39d30ba4d37000`. Full source locator: https://www.sqlite.org/pragma.html. No publisher original PDF is bundled; no rights to redistribute external paper content are asserted. Independent physical or qualified external review: **HOLD**.
