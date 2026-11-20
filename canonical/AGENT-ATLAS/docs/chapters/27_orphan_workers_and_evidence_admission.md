# 27. Orphan worker, stale receipt, and the parent-handoff boundary

Asynchronous orchestration creates a state space wider than “worker finished” or “worker failed.” A worker may complete after a parent has timed out, returned a partial answer or been cancelled. A delayed receipt may correspond to an earlier attempt, and a new parent may have a similar task description. Without a run/task/attempt-bound dispatch record, it is not safe to admit the result as verified completion of the current goal. This is a causal provenance and distributed execution problem, not evidence of agent reluctance or missing willpower.

## Admission should be evidence-based

A valid workflow separates an authorized parent dispatch, worker execution and artifact, tool submission/acknowledgment, independent verification, and parent admission decision. Each stage should carry immutable IDs and revisions. A system can log successful worker completion but still lack a valid final receipt. An absent parent dispatch must trigger **require_parent_dispatch**, not a success. A reported success that lacks trusted verification becomes **verify_worker_result**. A worker still running remains **observe_running_worker** rather than being automatically duplicated.

The v0.3 reference provides an offline state table that enforces these ordering rules. It does not open sockets, schedule real workers, write durable persistence, issue approvals or perform tool calls. In a real host, the recovery worker must be able to query authoritative run state and provider reconciliation; stale and contradictory receipts need quarantine and eventual human review. An operator Stop is terminal to action dispatch even if a specialist would prefer to continue.

## Failure injection and metrics

Test each state: missing dispatch; duplicate late receipt; running worker; failed worker after a known non-side-effecting operation; side-effectful submission with unknown status; exhausted attempt budget; task verified by host; and explicit operator Stop. Do not simply count how often a simulation reaches a “success” node. Track exactly-once external effects under provider contract, false admission rate, stuck-task detection, redundant work, lost evidence, and time to verified completion. These need real host traces before publication as empirical agent reliability metrics.

**Reference:** OpenTelemetry agent span lineage and AWS idempotency semantics. This architecture can inform a later PEGASUS harness experiment, but **Agent Atlas itself does not modify PEGASUS** or claim to have learned from its live traces.
