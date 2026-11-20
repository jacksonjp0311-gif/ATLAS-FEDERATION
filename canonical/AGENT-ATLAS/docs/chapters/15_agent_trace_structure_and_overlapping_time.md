# 15. Agent execution traces: lineage, overlap, missing evidence

An agent trace is not a conversation transcript with timestamps pasted beside messages. A scientifically useful trace needs explicit span identity and nesting, precise time definitions, actor and model versions, tool resources, observed outcomes, and evidence references. A root turn may contain concurrent subagents and repeated model/tool operations. Children can overlap. Their summed durations are **not** elapsed user-visible time, and token counters can include subagent usage inconsistently if counted at both parents and children.

## A bounded span model

`agent_atlas.trace_science.analyze_trace` accepts one tree with `id`, `parent_id`, `kind`, `start_ms`, `end_ms`, `status`, and `evidence_ref` for each span. Kinds are `agent`, `model`, `tool`, or `verification`. Statuses are `success`, `failed`, and `incomplete`. Every child must have one parent whose interval contains its own, with one root `agent` span, no cycles, duplicate IDs, or missing parents. The timestamps are declared in a **single monotonic millisecond clock** and are supplied as metadata; the function does not infer clock synchronization across machines. Cross-host timestamps require an independently calibrated clock transformation, not an arbitrary subtraction.

The root interval gives end-to-end elapsed time. For any parent, the union of its direct-child time intervals gives a covered time, preventing naive double counting when peers overlap. The implementation reports **sum of per-parent child union durations**, so the total still includes nested levels and must not be mistaken for global deduplicated wall time. It is a hierarchy diagnostic rather than a time invoice. It separately counts successful tool spans with explicit evidence pointers, reported successful verification spans, and failure/incomplete statuses.

## A report is not evidence

Even a `verification` span with `status='success'` and an `evidence_ref` is a **reported** verification, not independent proof. The model has not authenticated the evaluator, checked the referenced artifact against the requested goal, or established that the environment's state changed. An agent run claiming final success without any such span earns the diagnostic `success_claim_without_verification_record`, not an automatic failure label or invented validator outcome. A tool success without an evidence pointer is likewise flagged.

Telemetry can omit uninstrumented side effects and can misreport outcomes; a well-formed tree is insufficient to verify action truth. Tools may overlap or be retried; the tool name alone does not prove host permission. A human or machine evaluator must interpret task-specific evidence. Source excerpts and web pages are untrusted trace inputs, not commands to a host.

**Research sources:** [OpenAI Agents API tracing documentation](https://developers.openai.com/api/docs/guides/agents-api/tracing) describes session/turn/span relationships, overlap and missing token counts; [Agents SDK tracing](https://openai.github.io/openai-agents-js/guides/tracing/) describes tool calls, handoffs, guardrails and custom spans. These are documentation snapshots checked in 2026, not inspected private agent traces or a claim that every deployment records all actions.
