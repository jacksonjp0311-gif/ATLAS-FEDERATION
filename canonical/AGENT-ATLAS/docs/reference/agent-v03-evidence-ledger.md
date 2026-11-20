# Every numerical result must carry assumptions and unverified questions

A re-usable context packet preserves original record/source revisions, evidence origin, labels/missingness, evaluation split, tool effect and host-verification scope alongside the reported result.

**Record:** `agent-atlas:agent-v03-evidence-ledger`  
**Revision:** `bbf9522107ddd4d2821c5a8ebc9887728eb4438103b7cf9a752d86686635cdeb`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation
- [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — Public discussion of uncertain outcomes, caller-provided idempotency key, late arrivals, atomic application/provider contracts
- [MAST-Data public annotated multi-agent trace collection](https://huggingface.co/datasets/mcemri/MAST-Data/blob/main/README.md) — Dataset card states 1,642 traces, seven MAS frameworks, 14 failure codes, labels LLM-judge rather than human; CC BY 4.0 card; no raw dataset bytes acquired

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
