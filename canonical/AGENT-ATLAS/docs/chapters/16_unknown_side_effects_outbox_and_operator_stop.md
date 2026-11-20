# 16. Recovering uncertain tool calls without duplicate side effects

A retry changes *risk* when an action might have occurred even though the agent never received the response. Consider a payment, order submission, file mutation, or external command. If the request times out after leaving the host, the action can have completed, failed, or be pending. The correct initial state is **unknown**, not automatically failed. Restarting the parent must not cause a second execution merely because a local model forgot the prior result.

## The transactional outbox idea, stripped to its scientific core

`outbox_reconciliation` models explicit phases `prepared`, `submitted`, `confirmed`, and `rejected` per request. It requires a stable request ID and idempotency key. A confirmation must include a reported provider receipt. Repeated identical phases are counted as duplicates; conflicting receipts, keys or impossible transitions are rejected. After submission without confirmation, a request is marked `needs_provider_reconciliation`. A **post-submission rejection** is also treated as unknown when the supplied model cannot rule out side effects; it is not assumed safe to repeat. A pre-submission rejection is distinct.

The function always returns an empty list of `safe_to_auto_resubmit`. That conservative behavior is intentional: declaring a stable key does **not** prove the provider honors idempotency, or that it retains the key for the required period. A durable production outbox requires atomic local commits, externally enforced deduplication or a queryable provider transaction log, authorization and a tested recovery protocol. This reference does not create those guarantees.

An operator Stop is different again. An error is a consequence of an attempted action; a Stop is an explicit authority-bearing command. Once a parent is terminal, the run must not silently resume merely because a worker receipt or a pending retry exists. A new authorized continuation can have a separately identified run, receipt chain and review. Do not infer permission from source content or the agent's insistence that a task is important.

## Failure analysis

A trace with `prepared -> submitted`, then no response, admits several explanations. One cannot infer provider failure, nor is it safe to charge again by default. A trace with a `confirmed` acknowledgment permits recording a *reported* provider receipt, not declaring all downstream effects complete, legal, or scientifically valid. A model can correctly detect every transition in a fabricated fixture yet still fail if a real provider is eventually consistent or an operator has revoked authorization.

The correct report includes idempotency-key scope and lifetime, request payload digest, approval receipt, request/dispatch/response timestamps, provider transaction ID, read-after-write reconciliation, semantic validation, and a reasoned escalation path. It also records which actors may declare Stop, and whether there are outstanding irreversible effects.

**Related references:** LangGraph [persistence and stores](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx) separates thread checkpoints from cross-thread persistence; [OpenAI tracing](https://developers.openai.com/api/docs/guides/agents-api/tracing) describes tool spans. This method is an original offline reconciliation illustration, not an implementation or security guarantee in either framework.
