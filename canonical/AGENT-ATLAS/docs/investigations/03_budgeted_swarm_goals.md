# Investigation 03 — A swarm must not exceed the evidence or budget it has

**Origin:** original synthetic four-task DAG. A mission has `collect` (cost 2), `analyze` (cost 4), `audit` (cost 3) and `publish` (cost 1). Both analyze and audit depend on collect, while publish depends on both. The calculated critical path cost is 7 in an arbitrary cost unit; this is neither elapsed wall time nor a live token count.

If collect is complete and the current worker budget is 4, both analysis and audit are *logically ready*, but only one fits the submitted budget. With higher capacity and budget, they can both be admitted. If collect fails, their descendants remain blocked until an authorized recovery resolves that dependency. The example supports a principle, not an optimal scheduling claim.

This model has no fixed four-agent limit and supports up to 256 declared tasks, but that does not mean the actual runner has been modified. A live swarm would additionally need resource ownership, expected-value routing, provider concurrency limits, provenance of each result, deadlines, worker lifecycles, cancellation semantics and actual dynamic admission. That engineering belongs to a later integration project.

**Counterfactual challenge:** compare the same work done by one worker sequentially, two workers in parallel and many workers with coordination overhead. Measuring only raw parallelism hides added model/tool cost. A correct experiment controls for task complexity, model version and evidence quality, then records total time, successful final states and failures.

**Sources:** Anthropic agent architecture patterns; MAST multi-agent failure mechanisms.
