# A narrow OTel span adapter must reject content-bearing fields

Mapping supported agent, model and tool spans from caller-provided metadata requires a consistent trace ID, exact lineage, timestamps and explicit tool name. Unrecognized payload fields are refused rather than ingested.

**Record:** `agent-atlas:otel-metadata-strict`  
**Revision:** `d983c70223c92ecc5cf65f33567a2e090cc20daabacf9d94743f17eb86506cc7`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation
- [OpenTelemetry GenAI execute-tool span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) — Development-status public execute_tool span section; tool call ID when available, error.type, sensitive content warnings
- [OpenTelemetry GenAI span content and privacy boundaries](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) — Public guidance distinguishes metadata from opt-in input/output and tool content fields, which can be sensitive

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
