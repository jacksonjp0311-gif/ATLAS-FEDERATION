# 47. Off-policy evaluation: learning from a log that did not try every action

A logged agent policy may choose actions differently from a proposed new policy. Comparing observed rewards on the subset of records where they agree can be biased, because those records are not necessarily representative of the target policy's choices. Off-policy evaluation asks what the target policy would achieve using logs produced by a behavior policy. The question requires logged action probabilities, comparable task contexts, a well-defined reward and support for the target actions. It does **not** turn arbitrary self-reported outcomes into verified agent success.

## Basic inverse propensity scoring

For a deterministic target policy π and logged action `a_i` with behavior probability `b(a_i|x_i)`, define weight `w_i = 1(a_i=π(x_i))/b(a_i|x_i)`. Given bounded reward `r_i`, the simple IPS estimate is `(1/n)Σ_i w_i r_i`. A self-normalized ratio uses `Σ w_i r_i / Σ w_i`. These are different estimators: one targets a direct weighted average under supplied propensities, the other introduces ratio normalization which can reduce certain variance issues but is biased in finite samples. The effective sample size statistic `(Σw)^2/Σw²` can warn how few effective samples drive the result. It is not an assurance of identification.

If the target always selects an action the behavior policy never tried in a relevant context, no direct logged outcome exists. **Positivity/support is missing**. Guessing an outcome or silently clipping extreme weights invents evidence. The pure-Python `offline_importance_value` refuses zero propensities, missing action IDs and weights beyond the declared cap. It uses binary-bounded reward input only as a numerical illustration; no real logging policy, reward oracle or environmental confounders are verified.

## Worked calculation

For four constructed interactions, target action A appears on two rows with behavior probability .5 and rewards 1 and 0; the other two rows selected B. The nonzero weights are 2 and 2, yielding IPS mean .5, self-normalized mean .5, and effective sample size 2. The fact that there were four rows does not mean four informative target-action outcomes. If A had logging propensity .001, a realized weight of 1000 would dominate a tiny sample and exceed a declared cap of 100; the program refuses the estimate instead of silently announcing policy superiority.

## Identification and safety limits

Logged reward data may suffer confounding, delayed effects, censoring, selective reporting, hidden action versions and nonstationary tools. The behavior-policy propensity must actually be known or correctly estimated. Even a valid IPS calculation may evaluate a reward proxy rather than the user's real objective. Deep agent changes can alter state distribution, tool authorization and available actions, violating a simplistic stationary contextual model. More advanced doubly robust, model-based and sequential estimators have additional assumptions and are **not** implemented here.

A fair future test of memory-based or Bitwork-based routing should compare equal-budget, held-out outcomes under a genuine verified reward and a defensible logging or randomized design. Until then, IPS arithmetic belongs to the scientific reference, not the system's achievement claims.

**References:** Sutton and Barto, *Reinforcement Learning: An Introduction* (2018), publisher scope; prior Agent Atlas paired evaluation and causal-source records; original derivation of the simple IPS estimators. A complete review of counterfactual evaluation literature is deferred.
