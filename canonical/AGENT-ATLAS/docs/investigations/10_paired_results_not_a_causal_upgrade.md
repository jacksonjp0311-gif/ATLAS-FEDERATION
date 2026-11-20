# Investigation 10 — A paired benchmark can still mislead

Eight invented evaluation task pairs produce: candidate-only success on three, baseline-only success on two, both success on two, and both failure on one. Baseline observed success is 4/8; candidate observed success is 5/8, so the observed difference is 12.5 percentage points. Those numbers are task-pair arithmetic, not an agent-ability gain or statistical proof of superiority.

An exact two-sided sign test conditions on five discordant independent pairs and gives a p value of **1** for a 3:2 split. The p value neither proves identical ability nor validates the outcome judge. If the task pairs are strongly correlated or selected after tuning, the sign test's assumptions do not hold. The model also reports mean candidate-minus-baseline cost separately; a success difference without resource constraints can be a poor decision metric.

A real evaluation should lock the task set, evaluator, source data version, model/tool permissions and baseline; predeclare outcomes and costs; log all task failures; compare matched input instances; and quarantine an untouched holdout from prompt and tool design. A benchmark known during training can overstate generalization. Repeatedly testing on the same questions while changing the system creates a development set, not a fresh evaluation.

**Sources:** OpenAI agent eval guidance and SWE-bench contamination discussion. This case uses wholly constructed Boolean task outcomes; no language model was run.
