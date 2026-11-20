# Investigation 28 — A better logged score is not proof the new memory helped

**Origin:** four original fake logged interactions. A proposed target policy always chooses action A. Two logging rows took A with propensity .5 and rewards 1 and 0; two rows took B. The IPS nonzero weights are 2 and 2, giving a simple mean .5, a self-normalized ratio .5 and an effective sample size of 2. This shows why four logged interactions do not necessarily give four informative observations for a target action.

**Failure:** if propensity for action A were .001, a realized importance weight of 1000 could dominate the estimate. The tool refuses weight above a declared bound rather than silently clipping or reporting a confident improvement. In real deployment the propensity may be unknown, model behavior may change with context, outcome labels may be self-reported, and selection may be confounded. Without a matched, independent outcome oracle, any causal claim that memory increased task success is unverified.

**Reproduce:** `python -m agent_atlas v1-casebook`; inspect `policy-evaluation-ips` and `low-propensity-refusal`. **Follow-up:** precommit a randomized or otherwise valid evaluation on unseen tasks, verify rewards and repeat trials at equal tool and cost budgets. Chapter 47 explains the assumptions and missing estimators.
