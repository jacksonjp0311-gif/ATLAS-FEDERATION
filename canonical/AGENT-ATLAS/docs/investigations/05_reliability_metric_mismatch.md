# Investigation 05 — “Passed once” and “passed every time” are different results

**Origin:** author-created Boolean outcomes for three tasks, each attempted three times: `[T,T,F]`, `[T,T,T]`, and `[F,T,F]`. All tasks succeed **at least once**, so observed pass-any-3 is `3/3 = 1`. Only one task succeeds in **all three** repeats, so observed pass-all-3 is `1/3`. A report saying “100% success” without identifying the metric is misleading for reliable operation.

The overall per-attempt fraction is `6/9=2/3`. A simple i.i.d. model would predict `(2/3)^3 ≈ 0.296` chance of all three successful attempts, but the observed fraction is 1/3. The discrepancy is not meaningful evidence against the model with such small data, and the independence assumption may fail if individual tasks differ in difficulty or repeats share context.

**Benchmark protocol:** present outcomes and all denominators; preserve task IDs, seeds, grading process, tool state, time budget, model version and user environment. Do not combine “some task solved once” and “consistent execution across repeated attempts.” A real agent benchmark must use a predeclared representative task distribution and independent outcome verification, not an assistant's self-reported success.

**Result:** exact calculation of two descriptive statistics. **Not shown:** any model improvement, external API action or true probability for a new task. The 30-domain integration benchmark comes only after all content libraries exist.

**Source:** τ-bench paper; AgentBench and SWE-bench for different targets.
