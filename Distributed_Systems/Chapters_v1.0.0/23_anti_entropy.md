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
