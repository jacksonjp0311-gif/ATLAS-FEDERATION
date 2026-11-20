# Investigation 14 — An external API times out after possible mutation

**Origin:** a constructed distributed execution state. A task has a parent-dispatch record and one completed attempt. A side-effectful request was submitted, but no trusted response was observed. An agent that treats the timeout as a failure and immediately submits again risks duplicate effects.

The offline `recovery_decision` chooses `reconcile_provider_before_resubmit` while the submitted state remains unknown. If an operator Stop is recorded, Stop has higher priority than reconciliation or retry. A missing parent dispatch yields `require_parent_dispatch`; a worker success with no host verification yields `verify_worker_result` rather than final completion. A pending worker yields `observe_running_worker`, not a new attempt.

**Evidence still missing:** provider query by caller request ID, idempotency semantics, source and time window, exact authorization, and proof the operation's intended effect occurred. Even a reported provider acknowledgment is not a general independent task validator. The state machine does not execute any API call. AWS Builders Library discusses caller-supplied idempotency and unknown outcomes; this local scenario is original.
