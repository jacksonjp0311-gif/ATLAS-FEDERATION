# Host verified is still a caller-reported state in an offline research fixture

A record labeled host_verified must retain the verification artifact, authority, context and state snapshot. Offline labels cannot authenticate those facts and cannot promote a worker message alone.

**Record:** `agent-atlas:host-verified-scope`  
**Revision:** `56d285948f170cf1cbb546aa325c2de78329dedc31330f8d081f7ef3b4da10b5`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
