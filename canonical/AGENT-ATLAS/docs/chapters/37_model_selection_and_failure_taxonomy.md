# 37. A failure taxonomy is a diagnostic hypothesis, not a score

A multi-agent system can fail because of planning errors, tool authorization, lost context, partial execution, input misunderstandings, inadequate verification, or stale environment state. Different failures may yield the same outward trace: an incomplete final answer could reflect premature stopping, hidden worker failure or a tool timeout after a successful side effect. A diagnostic taxonomy is useful because it specifies *which additional observations would distinguish explanations*, rather than merely blaming a model.

## Orthogonal axes

Track **failure location** (planner, worker, tool, host, evaluator), **evidence origin** (worker report, host observation, provider receipt, independent task adjudication), **time** (before external submission, after submission, after restart), and **effect reversibility**. A trace span that ended with success indicates an instrumented API returned, not that the goal was satisfied. A worker that failed after a provider commit cannot safely be retried as if the external action never occurred. A confident evaluator can still be wrong if it shares the worker's unverified assumptions.

## Design experiments that break ambiguity

The v0.4 casebook includes one packet that appears complete yet cannot authenticate its own host fields, a missing or foreign dispatch, a stop combined with uncertain submission, a supposedly held-out evaluation contaminated by training exposure, and a conflict-aware memory admission review. Each is a controlled failure-injection *model*, not a production incident. A real postmortem would compare event logs, external state, task semantics, costs and environment revisions under the same goal.

For behavioral evaluation, build a matrix of capabilities and perturbations rather than test only aggregate completion. The CheckList methodology provides one published precedent for systematic behavioral test design. Agent-specific examples might perturb tool latency, response ordering, corrupt evaluator labels, parent restart timing, stale task definitions or inconsistent system clocks. They require a safe offline or authorized test environment and should measure genuine task outcomes, not only whether a simulator returned its expected classification.

## Reliability as a bounded decision process

The correct result of a diagnosis may be *insufficient evidence*. If an external submission's state is unknown, reconcile. If an evaluator is stale, freeze or rerun the outcome check under the current version. If evidence conflicts, retain both claims until a discriminating test. If a worker is alive, observe rather than retry. If operator Stop is active, stop remains authoritative. These are research hypotheses for future host integration, not self-authorizing behavior by this reference package.

A stronger Agent Atlas v1 will eventually need authentic, rights-cleared agent traces, independently checked outcomes, repeated trials under controlled changes, and evidence of improved generalization. None is claimed by v0.4. Every software test in this release is distinct from that scientific acceptance gate.
