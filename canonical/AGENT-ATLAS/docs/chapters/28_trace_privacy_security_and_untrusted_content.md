# 28. Agent-trace research must not execute its evidence

Raw agent transcripts often contain user secrets, source code, URLs, credentials, retrieved web text, and tool-call arguments. They can also contain malicious-looking instructions that were supplied as lower-trust task content. An evidence-analysis library has no reason to treat those instructions as authority. The most reliable boundary is to keep the research input **structured metadata** and to refuse unknown content fields at ingestion.

The v0.3 OpenTelemetry adapter accepts a narrow allowlist: operation name, tool name, agent name, requested model and error type, each as bounded strings. It rejects `gen_ai.input.messages`, output messages, system instructions, tool-call arguments and any other key outside its static schema. The method does not retain those rejected payloads in an output summary. It does not attempt semantic content cleansing and is not a general privacy scrubber. If a separately privileged tool engine reads the same raw text and follows its instructions, this adapter cannot prevent that other engine from doing so.

## Retention is not free

Even nominal metadata can be personal or linkable: conversation identifiers, tool names, error strings, timing sequences and agent names may reveal workflows. A real data pipeline needs permission, minimization, retention policies, access controls, encryption as applicable, deletion, and explicit research consent/legal basis. A content hash helps detect changes to retained bytes only when the expected digest and source identity are trustworthy. It neither proves the original producer, reconstructs omitted spans nor validates a model's account of reality.

Do not mirror the full MAST trajectory corpus simply because a dataset card has a permissive label. Confirm exact dataset version and upstream rights, and take precautions against secrets and third-party content embedded in trace messages. An analysis of derived label counts might avoid most of this by loading only the dataset's schema and label metadata.

## Threat model

A malicious trace row may try to impersonate a system message, modify a code path, issue a tool call, or assert a positive evaluation. These are text or metadata assertions, not capabilities. The program contains no agent tool connectors. It validates exact fields and enumerated types; unknown fields produce errors rather than being reinterpreted as new instructions. This is an input-scoping guarantee for the local function, **not** a universal agent security guarantee.

**Sources:** OpenTelemetry GenAI tool and agent span documentation, especially optional content attributes and sensitive input warnings. No private trace was acquired, inspected or published in this release.
