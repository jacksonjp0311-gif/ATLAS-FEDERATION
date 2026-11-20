# Investigation 16 — One “improved” constructed trial is not evidence of better agents

**Origin:** authored outcomes. Two task IDs are each run three times under baseline and candidate labels. The author sets all candidate successes to True and baseline outcomes to mixed/failed. The offline panel returns baseline pass-all=0 and candidate pass-all=1. The statistics are exactly calculated—but the data were invented, not measured. Concluding an AI improvement from the numerical difference would be false.

The tool enforces complete task-by-arm-by-trial keys and consistent evaluator/task version and split. Remove one attempt or change the evaluator version on one arm, and it refuses instead of normalizing away the mismatch. Pass-any and pass-all are distinct questions; task repetitions are not independent new tasks for sample-size purposes. No confidence interval or p-value from this toy exercise establishes a generalization result.

A credible comparison needs held-out tasks, independent outcome checks, budget and seeds, contamination detection, real model/tool versions, and a predeclared statistical analysis plan. A negative result would be as important as a positive result.
