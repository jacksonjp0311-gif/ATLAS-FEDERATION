# Investigation 08 — The tool times out after an external action

An authored outbox trace records `prepared` and `submitted` for request R1 with idempotency key K1, then stops. The external provider outcome is unknown. A new model state sees only a timeout and decides to retry immediately. That would be a classic duplicate-effect risk if the original action succeeded and the provider doesn't enforce the submitted idempotency key.

`outbox_reconciliation` returns R1 under `needs_provider_reconciliation`, with `safe_to_auto_resubmit=[]`. Replaying an identical `submitted` record counts a duplicate observation, not a new tool execution. A provider-reported confirmation after submission is recorded distinctly but is still not proof of a correct semantic final effect. An inconsistent changed confirmation or key is rejected.

The scientific ambiguity is **where the failure occurred**: before dispatch, after dispatch but before provider acknowledgment, after effect but before receipt persistence, or during reconciliation. Without an actual provider transaction lookup and signed/host-validated journal, these are alternative hypotheses, not a single known root cause. The offline code never contacts a provider and cannot produce exactly-once execution guarantees.

A useful live-system experiment must deliberately inject faults between prepare/submit/provider commit/receipt persistence, restart the process, reconcile transactions and count duplicate or missing side effects over repeated trials. Record host authorization and operator Stop separately. The important lesson is not “retry harder,” but “recover evidence before repeating possibly irreversible effects.”

**Sources:** LangGraph persistence semantics and OpenAI Agents trace descriptions. This is a constructed fixture.
