# Metadata-only recording limits—but does not eliminate—trace leakage

GenAI span content fields, tool inputs, results, system instructions and user messages can carry secrets and untrusted instructions. The bounded adapter deliberately declines to store them.

**Record:** `agent-atlas:otel-sanitization`  
**Revision:** `ee9a1c59442c0191b3db3b5e51fb48bbb96a43cde81f38fda5eb238cdd040363`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI span content and privacy boundaries](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) — Public guidance distinguishes metadata from opt-in input/output and tool content fields, which can be sensitive

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
