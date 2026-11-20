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
