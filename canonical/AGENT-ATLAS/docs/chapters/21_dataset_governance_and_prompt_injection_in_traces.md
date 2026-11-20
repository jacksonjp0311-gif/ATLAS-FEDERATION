# 21. Importing agent traces without executing their contents

Agent traces often contain untrusted data: user prompts, scraped pages, repository files, tool output, support tickets, and natural-language plans. These fields can include credentials, private details, copyrighted content or instructions attempting to impersonate a privileged host. Reading a trace for research must not turn those strings into commands. The intended architecture is a **data-only parser** that validates the schema and produces bounded evidence records, with separate trusted execution mechanisms never implicitly invoked by the trace reader.

## Bounded minimum schema

The `analyze_trace` function deliberately accepts only span metadata, not raw prompts or tool arguments. A future importer may accept OpenTelemetry-style nested spans or MAST's framework-specific traces, but needs source-version pinning, timestamp unit conversion, safe content limits, trace provenance and privacy filtering. Untrusted strings can be retained as inert quoted text or digests where licensed, never executed, and must not expand permission scopes. A source link does not grant an agent API access. The tool authorization catalog remains owned by the host, not by provider text.

The MAST summary accepts 14 explicit annotation codes; this prevents unknown future taxonomy codes from being mistaken for a valid present label. A future schema migration must preserve versioned labels and avoid pooling incompatible human-annotation rounds. A dataset license such as CC BY 4.0 for a card does not authorize ingestion of confidential source prompts that happen to appear in a trace. Real data needs appropriate rights, privacy review, retention controls, and a configurable deletion/revocation process.

## Study quality versus benchmark quality

A descriptive analysis of available traces can reveal recurring failure patterns; it cannot establish universal agent reliability unless source selection, task distribution, model versions, missingness and label processes are understood. Repeating a deterministic harness test thousands of times can increase confidence in its software implementation under the sampled fixtures but is not equivalent to a realistic language-agent trial. A cached dataset may reduce collection cost but can become stale; corrections must be versioned and compared with untouched older evidence.

## A reusable ingestion packet

Record source URL, dataset revision/commit, original bytes hash if acquired, local normalized hash, license/consent boundaries, field mapping, filtered or redacted columns, row count, missingness, original annotations, taxonomy version, model and framework metadata, time-zone/clock assumptions, and independent evaluation receipts. If an external source cannot be fetched, record `not_acquired` rather than inventing a successful import. When trace content is sensitive, the public Atlas should store only high-level schema and derived non-identifying statistics.

**Sources:** [OpenAI trace export/OTLP docs](https://developers.openai.com/api/docs/guides/agents-api/tracing); [MAST-Data dataset card](https://huggingface.co/datasets/mcemri/MAST-Data/blob/main/README.md); [OWASP LLM application risks](https://owasp.org/projects/top-10-for-large-language-model-applications). The current implementations are offline metadata calculations only.
