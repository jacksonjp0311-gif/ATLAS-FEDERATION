# 18. Evaluating an agent upgrade on matched tasks

An apparently improved success rate can reflect a different task distribution, a more generous evaluator, changed test data, repeated retries, or leaked benchmark answers. A strong comparison uses the **same task instances**, pinned environment, fixed outcome rubric, recorded model/tool versions, cost units and seeds where appropriate. Matched tasks do not themselves prove random sampling or causal identification: task selection may be biased, environmental randomness may differ, or external models may have seen the evaluation data.

## Paired binary outcomes

For each task, record baseline success, candidate success and costs. Four pair types are possible: both pass, both fail, candidate-only pass, baseline-only pass. The observed success-rate difference is `(candidate-only - baseline-only)/n`. It is not `pass^k`, not an answer-quality judgment, and not a confidence interval. Retain the task IDs to prevent the same run from appearing twice. The `paired_eval` calculator separately counts discordance, success difference and mean candidate-minus-baseline cost.

Under a restrictive null where each **independent discordant task pair** is equally likely to favor either system, an exact two-sided sign/binomial test gives `min(1, 2 Pr[Binom(d,1/2) <= min(improved,regressed)])`. The calculator reports this p value as a descriptive inference tool. It does not establish that task pairs were independent or exchangeable, that the benchmark was hidden during tuning, or that an outcome evaluator was correct. Correlated tasks, shared solutions or multiple model versions break those assumptions. With zero discordance, the exact p value is 1; that is not proof of equivalence.

## Cost, latency and decision sufficiency

Cost needs its basis declared: API usage, tool calls, wall time, energy, human review and failed retries are not interchangeable. A system that saves tokens while producing more invalid artifacts may increase real operating cost. The paired code accepts caller-supplied nonnegative scalar costs on an assumed common basis; it does **not** infer dollars or GPU-hours. It reports both success and cost change because neither dominates without a declared decision objective.

Development and evaluation splits are retained explicitly. Combining them in one observed rate is useful for auditing a supplied dataset but must **not** be interpreted as a blinded held-out benchmark. A proper future Atlas evaluation must pin task/version IDs before tuning, keep an untouched evaluation split, report selection/exclusions, and compare against strong simple baselines such as direct tool use and a single-agent loop, not just another expensive swarm.

**Published context:** [OpenAI agent evals](https://developers.openai.com/api/docs/guides/agent-evals) recommends traces, graders, datasets and repeated runs; [SWE-bench benchmark contamination discussion](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) explains why training exposure can undermine leaderboard generalization; [τ-bench abstract](https://arxiv.org/abs/2406.12045) distinguishes repeatability measures. No current live benchmark runs are included here.
