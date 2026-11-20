# An operator stop outranks agent attempts to recover

An offline recovery decision model first honors host Stop, then uncertain submitted effects, missing dispatch lineage, blocked dependencies, unverified worker results and attempt budgets.

**Record:** `agent-atlas:operator-stop-priority`  
**Revision:** `de31bc38c9edeb39bbeb6e76e8bded96070034d606af0e060b6380a6f3a34906`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — Public discussion of uncertain outcomes, caller-provided idempotency key, late arrivals, atomic application/provider contracts
- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
