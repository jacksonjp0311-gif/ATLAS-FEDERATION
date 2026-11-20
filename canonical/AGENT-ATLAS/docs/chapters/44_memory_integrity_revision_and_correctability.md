# 44. Memory as a scientific claim, not a self-affirming text cache

An agent's long-term memory can preserve useful information, but it can also preserve errors, hidden assumptions, outdated procedures and apparently successful repairs that never worked. A memory item needs an object and an evidentiary status. Plain text is not enough: store a stable record ID and revision, what was observed, the task and environment, source IDs, applicable conditions, test or measurement that supported it, time/expiration, contradictory evidence and what would trigger re-evaluation.

## Separate three memory layers

**Episodic memory** records what happened in a run: tasks, context, observations, tool calls and receipts. **Semantic memory** stores generalized claims drawn from episodes or other knowledge sources; these need derivation and evaluation before promotion. **Procedural memory** stores reusable action templates, tool preconditions and constraints. A single successful episode does not establish that a procedural change is helpful across different tasks. A reflection such as “retry more aggressively” can cause harm when applied to idempotency-unsafe tools.

Reflexion (Shinn et al., NeurIPS 2023) demonstrates using linguistic feedback from previous trials to influence a future agent without updating model weights. That is an example of an agent design, not an assurance that every reflection is grounded. Store the **feedback origin**—external evaluator, human review, a tool’s measurable effect, self-critique or a simulation—and do not equate them. Memory should distinguish a candidate lesson from a verified generalization and permit rollback to an earlier revision when results disagree.

## Contradiction is valuable information

Two sources may contradict each other because of different conditions rather than error. A worker may claim a code patch is fixed while an independent test still fails. Keep both observations. Preserve original bytes and identifiers, add a typed contradiction or supersession edge, and record which test distinguishes them. Deleting the older result makes it harder to diagnose regressions. Using a language model to merge conflicts into a confident summary risks losing scientifically important ambiguity.

## Time and environment scope

A successful repair of a particular Windows file-lock error cannot automatically be transferred to Linux, a network timeout, a stale cache or a new provider API. Store OS/runtime, provider, model, resource, task revision, and failure mechanism. Expiration is not only clock time: source revisions, contract changes, missing prerequisites and a contradictory observation can all invalidate an action rule. “Persistent memory” without an invalidation plan is a liability.

## Evaluation gate

To claim memory helped, compare a memory-augmented agent against a memory-disabled baseline on independently authored, held-out tasks with the same model, tools, wall-time and budget. Precommit metrics and count negative outcomes. An agent reporting a learning insight is **not** itself evidence of higher task success. Better-looking answers can be caused by test leakage, easier tasks, changes in provider model or selective reporting.

**Sources:** Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*, NeurIPS 2023 (published abstract and paper scope); OpenTelemetry semantic conventions for memory/tool spans, published public evolving drafts. The memory governance contract is original project guidance and has not been validated on a deployed agent.
