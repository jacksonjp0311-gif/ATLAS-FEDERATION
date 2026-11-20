# 20. Failure diagnosis when the same trace admits different explanations

A parent agent can receive a worker completion message without the final artifact, or a tool timeout after a side effect, or a prompt that contains malicious instructions inside retrieved text. In each situation the trace supports some conclusions and leaves others unresolved. The correct investigative unit is a **set of hypotheses and discriminating evidence**, not a single assertion guessed from a language-model summary.

## Four classes of evidence

1. **State observations**: the actual tool/provider response, file hash, schema check, environment version, system measurement, and other externally grounded artifacts.
2. **Event integrity**: a sequence with explicit actors, run/task lineage, attempt identifiers, and a trustworthy storage/clock model. A local hash chain detects changes relative to its known head but is neither signer attestation nor durability.
3. **Model interpretation**: the agent's natural-language reason for a failure. Useful for triage but not evidence of the external state until tested.
4. **Independent verification**: an evaluator or experiment that can distinguish rival explanations, under a declared task rubric and source chain.

Consider a worker that times out after receiving an assigned task. Rival hypotheses include a provider call that is still running, a model answer lost in transit, a receipt write failure, a child run that completed but was not reconciled, and an actual failed solution. Repeatedly spawning new workers without distinguishing those states wastes computation and can double side effects. Parent supervision should first inspect its durable assignment, provider slot, attempt ID, checkpoint/receipt and permission to resume. A verified worker result may be reused; a worker's self-asserted result cannot be final committed without goal predicates.

## Counterexample structure

A tree with a successful root span, two successful tool spans and an incomplete final verification could be reported as completed by an agent UI. The trace analyzer returns `success_claim_without_verification_record`. It has not *proved* the task failed: the validator might simply have been omitted from instrumentation. The next action is to query the actual task-state evidence. A different trace with a clean verification span still may be wrong if the evaluator is faulty or the source was poisoned. These are **two distinct uncertainty cases** and require different follow-up tests.

Likewise, detecting two contradictory memories does not identify which is correct. Preserve both revisions, context and qualifiers; request current evidence. Apparent model consensus across multiple agents does not create independent corroboration if all copied the same source or generation error. A high-quality agent harness must represent unknown explicitly, because forced guesses compound errors downstream.

**Sources and scope:** [MAST paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html) on failure taxonomy; [OpenAI trace grading guide](https://developers.openai.com/api/docs/guides/trace-grading) on workflow-level diagnostics; [LangGraph persistence](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/persistence.mdx) on stored checkpoints. This Atlas does not connect to a real provider, retry an external tool, or adjudicate private system incidents.
