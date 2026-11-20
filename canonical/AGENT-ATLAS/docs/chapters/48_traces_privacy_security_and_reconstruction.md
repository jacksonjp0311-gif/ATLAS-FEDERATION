# 48. Trace preservation must not become a new execution or privacy risk

An agent trace can contain data from external documents, tool responses, prompts, customer records and identifiers. A science-ready archive should preserve **structural evidence** while minimizing sensitive content. Spans describe logical agent, model and tool operations; the evolving OpenTelemetry GenAI conventions are helpful for naming and correlating those operations. They do not supply an independent correctness oracle, and the source itself warns about capturing full instruction, input and output content. Storing all traces indefinitely because storage is cheap can create an avoidable security and privacy problem.

## A minimal trace envelope

For each event preserve the run ID, task ID, parent ID, goal and environment revisions, actor role, operation category, start/end timestamps and clock basis, allowed tool class, effect state, outcome evidence level, artifact/receipt identity and redacted error classification. For tool calls, keep request IDs, provider response class and idempotency/reconciliation state. For evaluations, keep the rubric revision and whether it was independent. It must remain clear which facts were directly observed, which were model claims, and which are missing. A worker-submitted span is not proof of its own origin.

Do not store arbitrary retrieved prompts or tool outputs as executable policy. Prompt injection is untrusted task data; another document cannot grant permissions or rewrite the host's stop behavior. Public corpora and research examples can contain personal or licensed content. A release should preserve rights, access limitations and carefully scoped data transformations rather than mirroring external documents without consent. For publicly shareable research, redacted metadata can be more appropriate than verbatim conversation transcripts.

## Reconstructing failures

A useful trace lets an investigator distinguish at least five possibilities after a missing final result: the parent never dispatched; the child was dispatched but stopped; the child completed an artifact that was not admitted; a mutating call was submitted but its external effect is unknown; or an admitted artifact later failed an independent evaluator. Those paths demand different recovery policies. Treating all of them as an undifferentiated timeout creates unnecessary repeats and can corrupt external state.

A tamper-evident hash chain can detect changes *relative to a trusted retained root*, but if the attacker controls the whole chain and its claimed root, mathematical hashing alone does not authenticate an operator or provider. Digital signatures or independently witnessed receipts need real deployment trust anchors; they are not simulated by printing 64 hex characters.

## Reconstruction and longevity

Preserve a human-readable table or JSONL projection of every operationally important state transition. Include schema definitions and a read-only parser. A future researcher should be able to reconstruct a task history without access to the original proprietary vendor. If full source bytes cannot be retained, a bibliographic record plus an original paraphrase and an explicit “missing source” label is preferable to pretending the source has been archived. The survival audit validates fixity and references but not user identities or science.

**Sources:** OpenTelemetry GenAI agent and client span specifications (living public GitHub documentation), https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md ; Library of Congress Recommended Formats Statement 2025–2026, https://www.loc.gov/preservation/resources/rfs/data.html . This is original engineering governance, not production threat-model certification.
