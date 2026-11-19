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
