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
