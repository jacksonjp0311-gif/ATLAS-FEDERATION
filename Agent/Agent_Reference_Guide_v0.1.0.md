# Agent Atlas v0.1.0 — scientific reading guide
**Agent capability is a property of a deployed system under a particular task/evaluation environment, not of this reference library.**
Research flow: Define goal → Specify permitted observations and tools → Plan dependencies → Act only after host admission → Verify receipts → Grade end state → Preserve failure evidence.

## Fourteen scientific chapters
- [01. Agent, workflow, model and environment are different objects](chapters/01_agent_workflow_boundary.md)
- [02. Tool use separates intention, invocation and observed effect](chapters/02_tool_observation_action_feedback.md)
- [03. An agent observes through channels, not direct access to truth](chapters/03_partial_observation_and_belief.md)
- [04. Goals are dependency graphs with evidence predicates, not fixed agent slots](chapters/04_goal_graph_dependencies_and_dispatch.md)
- [05. Memory is a retrieval problem and an evidence-admission problem](chapters/05_memory_reflection_and_provenance.md)
- [06. Multiple agents introduce coordination, conflicting evidence and hidden cost](chapters/06_multiagent_coordination_and_conflict.md)
- [07. Durable execution separates recovery from unauthorized continuation](chapters/07_durable_execution_retries_and_stops.md)
- [08. Evaluate state success and repeated-trial reliability, not only the final prose](chapters/08_reliability_pass_all_and_evaluation.md)
- [09. Tool exposure, prompt injection and excessive agency are architecture risks](chapters/09_security_and_host_authority.md)
- [10. Agent traces need provenance, time, cost and actionable receipts](chapters/10_traceability_telemetry_and_sources.md)
- [11. Improving agent behavior requires counterfactual evidence, not a scoreboard](chapters/11_optimization_budget_and_self_improvement.md)
- [12. Failure mode analysis is necessary for productive agent repair](chapters/12_failure_taxonomy_and_diagnosis.md)
- [13. Benchmark design, distribution shift and leakage](chapters/13_benchmark_design_and_leakage.md)
- [14. Agent Atlas release contract and the last-stage routing rule](chapters/14_release_contract_and_cross_domain_links.md)

## Six investigations
- [Investigation 01 — Worker result survives but the parent does not](investigations/01_failed_parent_worker_result.md)
- [Investigation 02 — An error is not a stop, and a stop is not an error](investigations/02_stop_vs_tool_error.md)
- [Investigation 03 — A swarm must not exceed the evidence or budget it has](investigations/03_budgeted_swarm_goals.md)
- [Investigation 04 — Retrieved content must not grant tool permissions](investigations/04_host_tool_authority_injection.md)
- [Investigation 05 — “Passed once” and “passed every time” are different results](investigations/05_reliability_metric_mismatch.md)
- [Investigation 06 — A memory without its qualifier becomes a false credential](investigations/06_compaction_removes_qualifications.md)

## Run offline demonstrations
```sh
python -m agent_atlas casebook
python -m agent_atlas describe
python tools/numerical_oracle.py # optional NumPy and NetworkX
```
The casebook is author-constructed; there are **no language model invocations, live tool calls, held-out benchmark results, or provider-side transactions**.

## Source and maturity navigation
[Coverage/missing evidence](COVERAGE_MATRIX.md) · [Sources](SOURCE_REGISTER.md) · [Casebook](CASEBOOK.md) · [Research protocols](TEMPLATES.md) · [Validation](VALIDATION.md).
This node is independent of the Bitwork and cross-domain routing work, explicitly deferred until all 30 domain reference nodes exist.
