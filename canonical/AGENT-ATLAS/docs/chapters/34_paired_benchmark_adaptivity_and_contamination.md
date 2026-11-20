# 34. Paired evaluation, adaptive leakage, and why a p-value is insufficient

An agent that “learns” should improve on genuinely unseen tasks, not simply better remember a benchmark. Paired evaluation compares a baseline and candidate on the **same task** with a consistent outcome definition and evaluator version. Task-level pairing controls some between-task difficulty, but it does not automatically control prompt leakage, reused seeds, stochastic environment changes, or self-selection of favorable tasks.

## Data contract

The v0.4 `paired_learning_audit` requires an experiment ID, frozen baseline and candidate revision hashes, evaluator revision hash, a candidate precommitment flag, a set of task IDs exposed during training, and paired rows with task version, evaluation/development split, evaluator version and two outcome states. Each outcome is `true`, `false`, or `null`; **null is missing, not failure**. The tool rejects mixed evaluator revisions or duplicate task IDs and identifies evaluation tasks also listed in training. If any development task is mixed into a proposed held-out panel, if the candidate was not precommitted, or if an outcome is unscored, the metadata cannot support a clean design label.

## Discordant pairs

Let B be the number of paired tasks that only the **baseline** passed, and C the number that only the **candidate** passed. There are `n=B+C` discordant pairs. Under a conditional null that improvement direction is symmetric among *independent discordant tasks*, C is Binomial(n,0.5), giving one-sided exact tail `P(X≥C | n, 0.5)`. This is a **statistical calculation** on reported labels. If n=0, the p-value is undefined in this reference rather than a manufactured success. If tasks are correlated by repository or benchmark family, a naive binomial significance test can be misleading.

The constructed six-task example has C=3, B=1, n=4, yielding one-sided p=5/16=0.3125. It is not evidence of improved agent behavior. More importantly, even a much smaller p-value would not authenticate the task labels, prove the candidate was frozen before evaluation, demonstrate deployment performance, or rule out benchmark contamination. In November 2026, public methodology discussions explicitly warn that familiar software coding benchmarks can be contaminated by training exposure.

## Adaptivity is a separate threat

Repeatedly tuning a candidate against the same withheld tasks converts the set into development data. “Reusable holdout” research addresses this statistically, but our method **does not implement** privacy-preserving reusable-holdout algorithms or multiple-testing correction. A long-running program should record candidate selection history, training exposure, task generation rules, time of evaluator freeze, sample sizes, failure semantics, costs, and reasons for exclusion. Ribeiro et al.'s CheckList offers a complementary pattern for probing specific behavioral capabilities beyond aggregate accuracy, but no live evaluation was performed in this package.

## Evidence required for a real conclusion

Obtain genuine task instances, signed or independently auditable expected outcomes, an unobserved test set or defensible fresh-task sampling, frozen prompts/models, a prespecified analysis and multiple repeats. Preserve task-level side effects, not just final prose or a model judge's label. Report a result as measured improvement only when the evaluator's semantic correctness and experimental design have been reviewed separately.
