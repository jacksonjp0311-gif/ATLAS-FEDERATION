# Missing spans, missing labels and no observed actions are different

Sampling, dropped instrumentation or privacy redaction can hide spans; null MAST codes are missing labels; absence of a tool span does not prove no external side effect occurred.

**Record:** `agent-atlas:trace-missingness-taxonomy`  
**Revision:** `99a05f693b8d8fcab22e0ba812b933c9b7a11a9db3feaf2da3d9d2cf8648268c`  
**Status:** assistant-curated publisher scope; no independent review.

## Source links and inspected scope

- [OpenTelemetry GenAI agent and framework span conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) — Development-status public documentation: invoke_agent, invoke_workflow, plan and tool spans; no full instrumentation evaluation
- [MAST-Data public annotated multi-agent trace collection](https://huggingface.co/datasets/mcemri/MAST-Data/blob/main/README.md) — Dataset card states 1,642 traces, seven MAS frameworks, 14 failure codes, labels LLM-judge rather than human; CC BY 4.0 card; no raw dataset bytes acquired

**Limit:** offline research only; no live model, tool provider, causal benchmark or signed evidence.
