# 17. Memory integrity is a provenance and conflict problem

A self-improving agent can become *less* reliable when it accumulates incorrect, stale, contradictory or out-of-context memories. Retrieving a stored claim by relevance is not the same as admitting that claim as true. Memory must include a subject, relation, context, value, source identity, source revision, qualification, and retention/expiry state. A text-only summary that discards these fields can turn an explicitly uncertain observation into a fabricated verified fact.

## Separate identity, context, and value

`compare_memory_claims` groups active records by exact `(subject, predicate, context)` strings. If two active records in the same group have distinct canonical JSON values, it emits an unresolved conflict including **both** claim IDs, source IDs, revisions, qualifiers and value digests. It deliberately does not choose the newest, longest, or highest-scored statement as the truth. Records with different contexts are not automatically conflicts. That is a narrow deterministic model, not sophisticated natural-language contradiction detection. Two equivalent paraphrases can be reported as different because the values are not semantically normalized. Likewise, two values with different time or process conditions should not have been grouped in the first place.

Expiry is explicit: the caller supplies `now_epoch`; expired claims are reported separately and do not contribute to current conflict groups. They are **not deleted**, because deleting protected evidence can obscure corrections and audits. Persistent memory retention, user deletion requests, privacy and access controls require a production storage and consent system beyond this model.

## Why reflection is not a learned fact

A reflective message such as “The previous repair failed because the model ignored the compiler error” can be a useful hypothesis, but the observation may support several explanations: truncated tool output, stale working tree, timed-out worker, or corrupted assignment. Store the causal interpretation as an inference, with alternatives and evidence. A later reproducible test may confirm one explanation, at which point the memory can be revised and superseded; do not silently rewrite the prior historical record.

A memory selection score, confidence language or frequency of retrieval is not a calibrated probability of truth. An agent's successful answer on a previous task does not make every reusable claim reliable on a future task. Source revision and relevant applicability matter more than the apparent authority of a compacted summary.

**Source boundary:** [LangGraph persistence guide](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx) distinguishes checkpoint state from cross-thread stores; [Reflexion paper abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) explains verbal reflection memory. The conflict-resolution algorithm here is an original deterministic research method; no semantic retrieval benchmark, forgetting implementation or live model has been tested.
