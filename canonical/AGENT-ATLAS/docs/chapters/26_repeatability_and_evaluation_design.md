# 26. Agent reliability requires task-level repetitions and clean comparisons

A model can pass one trial but fail another under a different sampling seed, context length, order of tool observations or provider state. For each task i and arm a, let `Y_iaj` be the *reported* binary success of repetition j. Three operational summaries differ: (i) average single-trial success, (ii) pass-any over k repeats, and (iii) pass-all over k repeats. The latter is `I(all_j Y_iaj=1)` for each task and answers whether the configured system succeeded on every attempt in the specified experiment. It is **not** estimated by raising a measured single-run success proportion to k unless additional independence and stationarity assumptions are supported.

## Strict task panel

The `repeatability_panel` reference requires identical task IDs, versions, evaluator versions, split labels and **complete repetition indices** for baseline and candidate. It rejects missing, duplicate or mismatched trials; one failure cannot be filled with a conveniently assumed success. It reports all-pass and any-pass per task, and total cost on the caller's explicit common cost basis. The panel does not authenticate the evaluator, verify real task completion, identify sampling schemes or run an agent.

A constructed two-task example uses k=3 trials. In the baseline, one task succeeds in two of three attempts and the other fails all three; neither baseline task is pass-all. All six synthetic candidate attempts are set to success; the candidate's observed pass-all fraction is 1.0. This **does not** demonstrate an agent improvement, because the fixture author chose the outcomes. It demonstrates the exact arithmetic and makes complete repeated evidence mandatory.

## Statistical design and scientific limitations

A credible next benchmark needs independent task samples or an explicitly defined finite task population, predeclared evaluation outcomes and score rubric, controlled model and tool versions, preserved task/source hashes, randomized execution order, consistent resource budgets, failure capture and split leakage checks. A paired task study must preserve pairing. Multiple attempts on one task are *not* independent extra tasks. Confidence intervals should respect task-level clustering; checking many candidate versions on the evaluation set creates selection bias. An evaluator that judges its own generated text cannot provide independent task ground truth merely through a confidence score.

Costs and latency are multi-dimensional: billed tokens, tool requests, wall-clock delay and human interventions may matter differently. The declared `cost_units` in the local panel is not assumed to be tokens, dollars or GPU time. Future full-scale benchmarking should compare against an unchanged baseline on held-out tasks and report negative results, not just successes.

**Related sources:** [τ-bench study](https://arxiv.org/abs/2406.12045), [AgentBench](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html), and existing Agent Atlas paired-evaluation chapter. These sources motivate the design but are not benchmark runs in this package.
