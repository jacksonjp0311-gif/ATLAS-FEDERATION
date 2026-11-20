# 45. Multi-agent coordination: parallelism is not verified progress

A swarm is useful when independent subtasks can run concurrently and their outputs can be reconciled into one authorized result. More workers can also multiply overhead, inconsistent assumptions and failed handoffs. The number of agent spawns is not a measure of useful intelligence. The parent must own the goal revision and the evidence for admission and completion; specialists can research or propose artifacts, but cannot silently upgrade their own outputs to operator-approved truth.

## Work graph and lineage

Represent subtasks as a DAG. A node records stable task ID, parent goal revision, dependency IDs, owner, permitted operations, budget and deadline. A dependency is complete only when the required artifact or outcome was independently admitted. A worker report may be complete text but an incomplete task. A parent should distinguish `scheduled`, `running`, `report_received`, `evidence_verified`, `failed`, `cancelled` and `unknown_external_effect` rather than using one terminal flag.

Every message needs a unique envelope that binds sender, receiver, task, goal revision and receipt type. The receiver must ensure the message belongs to the currently authorized mission. This prevents an apparently successful child from a prior run from accidentally satisfying a new objective. Durable systems should preserve event ordering using a host-owned log. A model-generated transcript is valuable for human understanding but is not sufficient to authenticate that the tool or operator actually performed an action.

## Costs and partial outputs

For two workers that start simultaneously, their elapsed *wall time* should not simply be added as if serialized. Resource costs such as CPU/GPU time and paid API requests may add; elapsed time under concurrency follows the critical path and scheduling overhead. A claim that a swarm is faster must preserve both measurements. Parallel branches can also have a convergence cost: checking whether outputs conflict, merging changes, executing tests and obtaining an independent final assessment.

The MAST research, *Why Do Multi-Agent LLM Systems Fail?* (NeurIPS 2025), classifies failure modes including coordination and verification. Published annotations help organize what to inspect but are not unbiased estimates of physical or production failure frequencies. Several available trace labels are model-judge-produced, so annotation reliability remains an explicit evidence property. No real MAST record or physical multi-agent execution is imported by this v1 content edition.

## Failure demonstration

An upstream worker returns `complete`, but its parent dispatch ID belongs to another run. The coordinator should refuse admission even if the artifact hash matches a stated digest, because identity, authority and task lineage remain unverified. If an operation is marked submitted with unknown effects, another worker should not immediately repeat it. If the operator cancels, the parent must distinguish cleanup obligations from permission to continue external work.

## What would prove benefit

A fair experiment would pair the same tasks, tools and model with single-agent and swarm controllers, include trials with forced worker failure, estimate verified completion and repeated-trial reliability, and report communication overhead. It would check whether any increase in success survives held-out tasks and equal cost budgets. No such live benchmark is claimed here.

**Sources:** MAST, NeurIPS 2025, https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html ; public OpenTelemetry agent spans; original Agent Atlas task-graph and dispatch-reference models.
