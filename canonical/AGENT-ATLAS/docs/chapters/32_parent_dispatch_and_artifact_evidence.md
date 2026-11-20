# 32. Parent dispatch and artifact evidence: a claimed finish is not a verified goal

A distributed agent environment can produce a worker result after the parent has stopped, restarted, or changed its goal. It can also produce a plausible artifact hash with no durable evidence that the artifact exists or corresponds to the requested goal. Receipt **lineage** is therefore a necessary condition for evaluating work: task ID, goal revision, parent dispatch ID, worker receipt ID, artifact identity, evaluator revision, and source of observation must be connected.

## Conditional evidence contract

The v0.4 `audit_artifact_proof` input is a narrow, exact-field structured packet. It compares the expected SHA-256 field with a caller-supplied observed hash, requires the worker receipt dispatch to match the parent dispatch, binds the goal to a specific revision, distinguishes worker completion from reported evaluator result, and makes operator Stop take priority. It also places any externally submitted but uncertain effect into `reconcile_external_effect_first`, regardless of a plausible final artifact.

This is deliberately **not** signature verification. A malicious or erroneous caller could set both hash fields to the same false value, falsely claim a host observed the artifact, and supply an evaluator revision. The function has not read the original artifact bytes, verified a trusted public key, or looked up a provider-side transaction. Accordingly, even a structurally complete packet returns `structurally_eligible_given_trusted_host_facts`, **never** `verified_success`. A trusted host, independent outcome evaluator and task-specific semantic tests would have to supply additional validation outside this reference package.

## Priority matters

A fixed decision order avoids dangerous shortcuts: Stop overrides all pending work; an uncertain external submission requires reconciliation; mismatched or missing parent dispatch blocks admission; foreign goal revisions and artifact hash mismatches block the result; reported worker completion and evaluator status remain separate. If the evaluator rejects the result, do not rename the failure a success because the worker was done. A reported successful tool call does not prove its side effect persisted; a successful local file write does not prove the project-level acceptance tests passed.

These cases are motivated by documented OpenTelemetry agent/tool tracing fields and AWS idempotency guidance, but the API semantics and durable host authority are not built here. Hashes express byte equality only if computed from actual trusted bytes. OpenTelemetry spans often record **observed caller activity**; missing or delayed spans and timing are not provider-side truth.

## Research follow-up

For a real system, collect host-generated immutable dispatch receipts, worker identity and attempt, the actual artifact bytes (or a host-computed hash with anchored storage), tool-side reconciliation, allowed task scope, evaluator release, preserved tests, and a trusted signature or equivalent authority chain. A host must validate these before re-admitting the worker's learning. Failure to obtain that evidence is an observable reason to stop or escalate, not a defect to hide with another retry.
