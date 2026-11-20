# An untrusted trace must not become instructions or permissions

The metadata adapter accepts only a named allowlist; untrusted trajectory text, prompt instructions, provider tokens, and tool arguments must not authorize action or be echoed by default.

**Record:** `agent-atlas:trace-privacy-boundary`  
**Revision:** `6b8f4a10e1deea11ec49a0ce2e3830748ce3cbf66aa6bdb25c649f0e413a635f`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI span content and privacy boundaries](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md) — Public guidance distinguishes metadata from opt-in input/output and tool content fields, which can be sensitive

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
