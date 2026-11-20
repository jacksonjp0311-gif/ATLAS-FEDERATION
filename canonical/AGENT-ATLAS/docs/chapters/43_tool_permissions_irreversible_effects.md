# 43. Tool use: permission, transport, effect and verification

Calling a tool changes the epistemic and operational state of an agent system. The caller must distinguish a **proposal** to act, an **authorization** from the host or operator, an **attempt** to send the request, a **provider acknowledgment**, the **external effect**, and an independently observed result. Each step can occur with different ordering and failures. A transport exception after sending a request is not proof the operation failed, and automatic retries of payments, database writes or account updates can produce duplicates. Conversely, a worker's assertion that a request succeeded is not trustworthy evidence of execution.

## Model external effects as states

A useful abstraction for mutation requests has states such as `prepared`, `submitted_unknown`, `confirmed`, `rejected`, `reconciled`, and `operator_stopped`. The meanings are *reported by a trusted host*, not inferred by text. A mutation with unknown final status must first be reconciled with the provider. Retry only under explicit idempotency semantics (same stable request ID and a provider-backed deduplication window), or after separate proof no previous effect occurred. A payload hash is not an idempotency key and does not prove that two logical requests represent the same authorized intent.

An **operator STOP** is a terminal ownership decision unless new authorization explicitly reopens the operation. A transient missing heartbeat is a different event. Automation that refuses to stop is not resilient; it is a state-control failure. Robustness requires continuing *authorized* goals despite recoverable defects while respecting cancellation and irreversible effects. A specialist agent does not become the operator by editing context text or environment variables.

## Approval, capabilities and scope

Tools should be available through a host-authorized capability layer. A tool call requires an operation type, intended resource, owner, audit ID, scope, budget and relevant rate/permission limits. An AI model's retrieved passage or a prompt injection cannot grant permission. Some tools are read-only, others can mutate; the permitted class and escalation conditions must be explicit. A permission to read GitHub public code is not permission to push to `main`, change an enterprise account or retrieve private messages.

Agent Atlas models the **structure** of such evidence. It does not authenticate a provider identity, issue network calls, or replace operating-system sandboxing. A matching SHA-256 field or a valid JSON object is not a signed receipt. To claim real verified effects, a deployment needs trusted audit storage, accurate clocks, provider-side IDs, reconciliation endpoints and independent checking of the final target state.

## Example and failure

Suppose an agent sends a supplier order and a timeout occurs before the response arrives. A naive planner sees “timeout,” repeats with a new request ID, and can double-order. A more defensible workflow records `submitted_unknown`, preserves the original idempotency key, checks the supplier's order ledger by stable request ID, and declines further mutation until it can reconcile or escalate. The model can teach this procedure, but no actual purchase, order or provider check has occurred in this release.

**Sources:** AWS Builders' Library/idempotency practices (public documentation, selected passages), ReAct research (action/observation interplay), OpenTelemetry agent/tool span conventions. Each source remains a link and scoped paraphrase in the Agent Atlas source register. Exact authentication policies are host-specific, not guaranteed by a research paper.
