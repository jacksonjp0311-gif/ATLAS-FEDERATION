# A completed worker receipt without parent dispatch is incomplete lineage

An asynchronous worker receipt can exist even if the parent no longer recognizes a dispatch. Without linked parent request, a final answer cannot be admitted as authenticated goal completion.

**Record:** `agent-atlas:orphan-receipt-denial`  
**Revision:** `749c6aa5274156fc3ac045ccc9dce0307cf79f8d8c737aa8e7687e4fa000bd6e`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
