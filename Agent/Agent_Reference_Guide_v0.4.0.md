# Agent Atlas v0.4.0 — source-linked reference directory

**Goal → Observation → Authorized Action → Trace → Receipt → Independent Evaluation → Qualified Memory.**
This is a bounded research reference: passing method tests are not improved live-agent performance. All old source records remain immutable.

## Scientific chapters
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
- [15. Agent execution traces: lineage, overlap, missing evidence](chapters/15_agent_trace_structure_and_overlapping_time.md)
- [16. Recovering uncertain tool calls without duplicate side effects](chapters/16_unknown_side_effects_outbox_and_operator_stop.md)
- [17. Memory integrity is a provenance and conflict problem](chapters/17_memory_conflicts_revisions_and_retention.md)
- [18. Evaluating an agent upgrade on matched tasks](chapters/18_paired_agent_evaluation_and_discordant_tasks.md)
- [19. Multi-agent failure taxonomies, labels and denominators](chapters/19_MAST_taxonomy_labels_and_missingness.md)
- [20. Failure diagnosis when the same trace admits different explanations](chapters/20_failure_diagnosis_under_partial_observation.md)
- [21. Importing agent traces without executing their contents](chapters/21_dataset_governance_and_prompt_injection_in_traces.md)
- [22. Agent Atlas 0.2: what is learned and what is not](chapters/22_agent_v02_acceptance_map.md)
- [23. OpenTelemetry agent and tool spans: what the instrumented caller knows](chapters/23_otel_traces_and_lineage.md)
- [24. Recovery is a decision under unknown external state](chapters/24_external_effects_and_recovery_precedence.md)
- [25. MAST taxonomy: a coded failure label is not task ground truth](chapters/25_mast_groups_missingness_and_judge_reliability.md)
- [26. Agent reliability requires task-level repetitions and clean comparisons](chapters/26_repeatability_and_evaluation_design.md)
- [27. Orphan worker, stale receipt, and the parent-handoff boundary](chapters/27_orphan_workers_and_evidence_admission.md)
- [28. Agent-trace research must not execute its evidence](chapters/28_trace_privacy_security_and_untrusted_content.md)
- [29. Source closure, evidence maturity and reproducible failure hypotheses](chapters/29_agent_evidence_maturity_and_conditional_recommendations.md)
- [30. Agent Atlas v0.3 release scope and path toward authentic evaluation](chapters/30_agent_v03_release_and_original_trace_protocol.md)
- [31. Proof-carrying learning: what may an agent retain?](chapters/31_proof_carrying_agent_learning.md)
- [32. Parent dispatch and artifact evidence: a claimed finish is not a verified goal](chapters/32_parent_dispatch_and_artifact_evidence.md)
- [33. Uncertain external effects: recovery is an observation problem](chapters/33_partial_commit_retry_and_external_effects.md)
- [34. Paired evaluation, adaptive leakage, and why a p-value is insufficient](chapters/34_paired_benchmark_adaptivity_and_contamination.md)
- [35. Memory survives when qualifiers survive](chapters/35_agent_memory_conflicts_and_freshness.md)
- [36. Comparing failure labels without confusing agreement with truth](chapters/36_mast_label_agreement_not_ground_truth.md)
- [37. A failure taxonomy is a diagnostic hypothesis, not a score](chapters/37_model_selection_and_failure_taxonomy.md)
- [38. Agent Atlas v0.4: scientific status and build order](chapters/38_agent_v04_release_and_final_routing_sequence.md)

## Worked investigations
- [Investigation 01 — Worker result survives but the parent does not](investigations/01_failed_parent_worker_result.md)
- [Investigation 02 — An error is not a stop, and a stop is not an error](investigations/02_stop_vs_tool_error.md)
- [Investigation 03 — A swarm must not exceed the evidence or budget it has](investigations/03_budgeted_swarm_goals.md)
- [Investigation 04 — Retrieved content must not grant tool permissions](investigations/04_host_tool_authority_injection.md)
- [Investigation 05 — “Passed once” and “passed every time” are different results](investigations/05_reliability_metric_mismatch.md)
- [Investigation 06 — A memory without its qualifier becomes a false credential](investigations/06_compaction_removes_qualifications.md)
- [Investigation 07 — Two parallel workers, one missing verification](investigations/07_parallel_trace_lies_about_completion.md)
- [Investigation 08 — The tool times out after an external action](investigations/08_duplicate_side_effect_after_timeout.md)
- [Investigation 09 — Two sources disagree; the agent must not pick a winner](investigations/09_memory_contradiction_without_silent_override.md)
- [Investigation 10 — A paired benchmark can still mislead](investigations/10_paired_results_not_a_causal_upgrade.md)
- [Investigation 11 — A dataset annotation marked null is not evidence of absence](investigations/11_MAST_missing_annotations_not_negative.md)
- [Investigation 12 — Handoff for a future authentic agent trace](investigations/12_agent_trace_evidence_handoff_protocol.md)
- [Investigation 13 — A worker timeline double-counts simultaneous operations](investigations/13_otel_parallel_spans_are_not_wall_time.md)
- [Investigation 14 — An external API times out after possible mutation](investigations/14_uncertain_tool_submission_and_operator_stop.md)
- [Investigation 15 — A missing MAST annotation must not become “no failure”](investigations/15_model_judge_missing_labels_and_framework_groups.md)
- [Investigation 16 — One “improved” constructed trial is not evidence of better agents](investigations/16_repeated_task_outcomes_and_false_benchmark_success.md)
- [Investigation 17 — A completed worker result without its parent dispatch](investigations/17_orphan_receipt_requires_parent_dispatch.md)
- [Investigation 18 — Untrusted trace content masquerades as an instruction](investigations/18_redacted_trace_cannot_grant_permissions.md)
- [Investigation 19 — A matching hash does not authenticate a worker result](investigations/19_matching_hash_is_not_a_signed_host_receipt.md)
- [Investigation 20 — The timeout after a remote mutation](investigations/20_provider_timeout_vs_duplicate_external_effect.md)
- [Investigation 21 — A candidate improves on tasks it already saw](investigations/21_benchmark_leakage_and_false_learning_claim.md)
- [Investigation 22 — MAST failure annotations with missing labels](investigations/22_missing_mast_labels_and_annotator_agreement.md)
- [Investigation 23 — A learning record with contrary observations](investigations/23_memory_admission_keeps_contradictory_evidence.md)
- [Investigation 24 — Research protocol for an authentic agent-learning claim](investigations/24_research_handoff_for_genuine_agent_outcomes.md)

## Executable reference methods

```sh
python -m agent_atlas casebook
python -m agent_atlas advanced-casebook
python -m agent_atlas v03-casebook
python -m agent_atlas v04-casebook
python -m unittest discover -s tests -q
python tools/numerical_oracle_v04.py  # optional SciPy/NumPy
```

[Source register](SOURCE_REGISTER.md) · [Coverage limitations](COVERAGE_MATRIX.md) · [Casebook](CASEBOOK.md) · [Research templates](TEMPLATES.md) · [Release validation](VALIDATION_v0.4.0.md)

All 30 Atlas content domains before Bitwork routing, then integrated evaluation and desktop transfer. Agent v0.4 is not a final scoped v1.0.
