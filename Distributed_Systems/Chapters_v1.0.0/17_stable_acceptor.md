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
