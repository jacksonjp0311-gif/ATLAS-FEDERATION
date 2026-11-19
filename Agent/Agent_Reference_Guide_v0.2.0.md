# Agent Atlas v0.2 — Scientific reference guide

Agent quality is a property of a real deployed system and evaluation environment, not this reference node. All new traces and test outcomes are constructed.

## Chapters
1. [01. Agent, workflow, model and environment are different objects](chapters/01_agent_workflow_boundary.md)
2. [02. Tool use separates intention, invocation and observed effect](chapters/02_tool_observation_action_feedback.md)
3. [03. An agent observes through channels, not direct access to truth](chapters/03_partial_observation_and_belief.md)
4. [04. Goals are dependency graphs with evidence predicates, not fixed agent slots](chapters/04_goal_graph_dependencies_and_dispatch.md)
5. [05. Memory is a retrieval problem and an evidence-admission problem](chapters/05_memory_reflection_and_provenance.md)
6. [06. Multiple agents introduce coordination, conflicting evidence and hidden cost](chapters/06_multiagent_coordination_and_conflict.md)
7. [07. Durable execution separates recovery from unauthorized continuation](chapters/07_durable_execution_retries_and_stops.md)
8. [08. Evaluate state success and repeated-trial reliability, not only the final prose](chapters/08_reliability_pass_all_and_evaluation.md)
9. [09. Tool exposure, prompt injection and excessive agency are architecture risks](chapters/09_security_and_host_authority.md)
10. [10. Agent traces need provenance, time, cost and actionable receipts](chapters/10_traceability_telemetry_and_sources.md)
11. [11. Improving agent behavior requires counterfactual evidence, not a scoreboard](chapters/11_optimization_budget_and_self_improvement.md)
12. [12. Failure mode analysis is necessary for productive agent repair](chapters/12_failure_taxonomy_and_diagnosis.md)
13. [13. Benchmark design, distribution shift and leakage](chapters/13_benchmark_design_and_leakage.md)
14. [14. Agent Atlas release contract and the last-stage routing rule](chapters/14_release_contract_and_cross_domain_links.md)
15. [15. Agent execution traces: lineage, overlap, missing evidence](chapters/15_agent_trace_structure_and_overlapping_time.md)
16. [16. Recovering uncertain tool calls without duplicate side effects](chapters/16_unknown_side_effects_outbox_and_operator_stop.md)
17. [17. Memory integrity is a provenance and conflict problem](chapters/17_memory_conflicts_revisions_and_retention.md)
18. [18. Evaluating an agent upgrade on matched tasks](chapters/18_paired_agent_evaluation_and_discordant_tasks.md)
19. [19. Multi-agent failure taxonomies, labels and denominators](chapters/19_MAST_taxonomy_labels_and_missingness.md)
20. [20. Failure diagnosis when the same trace admits different explanations](chapters/20_failure_diagnosis_under_partial_observation.md)
21. [21. Importing agent traces without executing their contents](chapters/21_dataset_governance_and_prompt_injection_in_traces.md)
22. [22. Agent Atlas 0.2: what is learned and what is not](chapters/22_agent_v02_acceptance_map.md)

## Investigations
1. [Investigation 01 — Worker result survives but the parent does not](investigations/01_failed_parent_worker_result.md)
2. [Investigation 02 — An error is not a stop, and a stop is not an error](investigations/02_stop_vs_tool_error.md)
3. [Investigation 03 — A swarm must not exceed the evidence or budget it has](investigations/03_budgeted_swarm_goals.md)
4. [Investigation 04 — Retrieved content must not grant tool permissions](investigations/04_host_tool_authority_injection.md)
5. [Investigation 05 — “Passed once” and “passed every time” are different results](investigations/05_reliability_metric_mismatch.md)
6. [Investigation 06 — A memory without its qualifier becomes a false credential](investigations/06_compaction_removes_qualifications.md)
7. [Investigation 07 — Two parallel workers, one missing verification](investigations/07_parallel_trace_lies_about_completion.md)
8. [Investigation 08 — The tool times out after an external action](investigations/08_duplicate_side_effect_after_timeout.md)
9. [Investigation 09 — Two sources disagree; the agent must not pick a winner](investigations/09_memory_contradiction_without_silent_override.md)
10. [Investigation 10 — A paired benchmark can still mislead](investigations/10_paired_results_not_a_causal_upgrade.md)
11. [Investigation 11 — A dataset annotation marked null is not evidence of absence](investigations/11_MAST_missing_annotations_not_negative.md)
12. [Investigation 12 — Handoff for a future authentic agent trace](investigations/12_agent_trace_evidence_handoff_protocol.md)

## Source, capability and release limits

[Source register](SOURCE_REGISTER.md) · [Coverage and gaps](COVERAGE_MATRIX.md) · [Casebook](CASEBOOK.md) · [Research protocols](TEMPLATES.md) · [Validation](VALIDATION_v0.2.0.md).
All thirty reference domains are to be built before any Bitwork routing work, then integrated testing and desktop transfer.
