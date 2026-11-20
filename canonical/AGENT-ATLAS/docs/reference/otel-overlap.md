# Nested span durations must not be summed as elapsed time

For parallel spans under one root, elapsed time is root end minus start, not the sum of child durations; report overlap-aware union coverage and avoid double counting.

**Record:** `agent-atlas:otel-overlap`  
**Revision:** `912efff685eed1248ca80693dcf9e94d6e1a10fc9927a61db38c0085d5346732`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
