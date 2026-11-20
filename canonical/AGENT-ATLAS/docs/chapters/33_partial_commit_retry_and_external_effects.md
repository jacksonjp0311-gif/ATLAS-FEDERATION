# 33. Uncertain external effects: recovery is an observation problem

An agent invokes an external service to send a message, create a purchase, change permissions, or write to a remote database. The client times out. Three physical possibilities remain: the request never arrived, the service committed it but the response was lost, or the effect remains pending. None can be concluded from the client timeout alone. Retrying blindly can create a duplicate side effect. Refusing to retry forever can also block legitimate progress. The correct next action depends on the service's idempotency semantics and the evidence available.

The old outbox/recovery methods in Agent Atlas already distinguish prepared, submitted, unknown and confirmed states. The v0.4 artifact gate adds a second constraint: a valid parent–goal–artifact chain does not eliminate an outstanding ambiguous provider effect. The `submitted_unknown` state takes precedence over apparent success. This produces the decision `reconcile_external_effect_first`; it is not a command that executes reconciliation. Neither the model nor an agent is authorized to call tools through the reference code.

## Plan versus execution

A useful lifecycle has a *prepared* intent, host permission, stable request ID, idempotency key if the provider supports one, submission time, provider receipt or explicit uncertainty, reconciliation request, and host-verified outcome. A repeated client operation can be idempotent only if the provider implements appropriate deduplication and maintains the mapping for the relevant retention period. A locally reused string is not by itself a guarantee of exactly-once execution.

An operator's Stop must retain meaning. A worker reporting progress after Stop should be archived for diagnostics, but the host must not silently resume it, reissue an externally mutating tool, or promote its result. A planned retry is a *consideration* under policy, not proof that the previous request failed. Fallback to another model is appropriate only when it does not duplicate a previously committed effect and remains authorized by the host.

## Failure experiments

In a constructed packet, parent dispatch matches, artifact hashes match, worker reports completion, and the evaluator reports pass. Add `submitted_unknown`: the gate refuses result admission and calls for provider reconciliation. Add Stop as well: Stop prevails. Change the parent dispatch: the result becomes a foreign worker receipt. Keep other fields identical and change the observed goal revision: it is stale. These independent negative controls prevent one positive signal from masking important conflicting signals.

## Evidence and scope

The AWS Builders' Library idempotency pattern and the OpenTelemetry GenAI tool-span conventions provide the relevant public background. This edition contains no durable outbox, provider connection, external resource mutation, or production authority management. It tests state transitions on authored fixtures. A real future study should deliberately inject lost responses, delayed provider receipts and multiple service replicas into a controlled, authorized test environment and measure true duplicated effects and recovery latency.
