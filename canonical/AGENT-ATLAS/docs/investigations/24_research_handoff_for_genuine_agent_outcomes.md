# Investigation 24 — Research protocol for an authentic agent-learning claim

This handoff defines what an independent experiment must collect before Agent Atlas can claim that evidence-preserving memory or recovery makes a model better. It is not an instruction to run an unattended agent or modify a user's accounts.

**Task frame:** choose a task population not already used to tune the agent. Record source instance identifiers, difficulty strata, model/prompt and tool-release revisions, cost budgets, evaluator ownership, and what counts as a completed external effect. Preserve a time-stamped immutable receipt for every goal dispatch, tool attempt, provider reconciliation and final artifact, along with task-specific outcome checks from a separate verifier.

**Design:** assign matched tasks to baseline and candidate, prespecify a primary outcome, limit adaptive tuning against the evaluation split, repeat with multiple seeds, and track both successes and uncertainty. Avoid pooling development examples or missing results into the evaluation denominator. Measure not only task correctness but unsupported tool attempts, duplicate side effects, recovery latency and correct abstentions. Preserve failure reports as evidence, not as claims of performance improvements.

**Security/privacy:** do not expose prompts, secrets or raw tool arguments in public telemetry. Import metadata-only traces by default. Label LLM-judge and human annotations separately, and protect raw source evidence according to rights/privacy review. Retain exact source version and file hash when authenticated. A hash of a locally transcribed dataset does not prove original source bytes.

**Stopping criteria:** no host-authoritative dispatch; unverified external tool effect; missing evaluator version; training/evaluation leakage; inconsistent task or result provenance; significant unresolved label bias; unknown data rights; lack of independent review. These gaps should cause explicit abstention or a request for proper evidence. The research outcome can be “not identifiable from current traces.”
