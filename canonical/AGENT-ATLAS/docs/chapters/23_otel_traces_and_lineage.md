# 23. OpenTelemetry agent and tool spans: what the instrumented caller knows

A trace is a record of *instrumented operations*, not the complete history of a task. The OpenTelemetry GenAI semantic conventions distinguish `invoke_agent` and `invoke_workflow` spans, `plan` phases, model calls, and `execute_tool` spans. The conventions are explicitly in development and can change. A tool span may report completion even if the external side effect remains unverified; a successful model span does not prove a correct answer. The node therefore preserves **reported statuses** instead of using the word *verified*.

## A narrow offline adapter

The `project_otel_metadata` method accepts an explicit source-reported 128-bit trace ID represented as 32 lowercase hex characters, unique 64-bit span IDs, one root agent or workflow, and integer timestamps measured in a caller-declared common nanosecond clock. Every child must refer to an existing parent whose interval contains it. Only named GenAI operations and a five-field metadata allowlist are accepted. The adapter **rejects raw prompts, generated text, tool-call arguments, message history and unrecognized attributes**; it deliberately cannot be treated as an arbitrary OTLP parser. Tool spans require a tool name; a reported tool-call ID may be retained, but is not an authorization token.

When two children overlap, root elapsed time is computed from the root's interval, and direct-child coverage is the union of their intervals. It is incorrect to add parallel model and tool durations and call the sum end-to-end latency. This is a structural check only: unrecorded calls, missing sampled spans, clock-domain differences, provider billing, network buffering and internal asynchronous steps remain unknown.

## Three different completion claims

**Reported model completion** means instrumentation observed a model response. **Reported tool completion** means instrumentation observed a tool-operation boundary. **Independent task verification** requires an external checker with an explicit criterion, access to the required state, a defined sampling time and a preserved receipt. The adapter implements none of the last category. A span named `verification` is still a report until evidence and trusted host authority are established.

A transparent case contains a 100 ms root, a planning span from 5–14 ms, and concurrent tool/model spans 20–90 ms and 25–85 ms. Sum of child durations exceeds the actual covered interval; the union of direct child intervals is 79 ms. The toy trace demonstrates arithmetic, not production telemetry. It never connects to a provider, processes a prompt or executes the named tool.

## Scientific and privacy boundaries

Real agent traces often include system instructions, credentials, customer messages or raw tool responses, which should not automatically enter an open research package. Avoid copying their contents or trusting their embedded commands. The source metadata card must include schema version, sampling, known dropped spans, monotonic/epoch clock assumptions, instrumented process boundary, rights, redaction method, and whether external effects are actually attested. A hash of a span snapshot detects byte changes against a trusted digest, not provenance, completeness or correctness.

**Sources:** [OpenTelemetry GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md) and [GenAI client/tool spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md). Selected public development documentation checked November 13, 2026; no live telemetry acquisition or independent standards audit.
