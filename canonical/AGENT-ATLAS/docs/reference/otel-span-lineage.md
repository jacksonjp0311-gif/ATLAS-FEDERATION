# A reported trace is not a causal account of every event

Even a complete-looking nested OTel span tree can omit hidden work, provider effects, logs dropped by sampling, or parent operations. A tool span with success status is a recorded report, not outcome proof.

**Record:** `agent-atlas:otel-span-lineage`  
**Revision:** `8797d28bd7dd6ce98a35c6e9eb8f32fa3828c14ba5fcc77513edab41c99c714b`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation
- [OpenTelemetry GenAI execute-tool span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) — Development-status public execute_tool span section; tool call ID when available, error.type, sensitive content warnings

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
