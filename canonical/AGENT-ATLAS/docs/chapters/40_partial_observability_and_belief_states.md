# 40. Partially observable agents: inference is conditional on the world model

An agent cannot always see the true task state. The state may be the real location of an object, whether a transaction committed, whether an API worker is still running, or whether a manufacturing measurement is biased. A **partially observable Markov decision process (POMDP)** represents this by a state-transition law, an observation channel, and a *belief state*: a probability distribution over possible states conditional on available observations and the assumed model. Kaelbling, Littman and Cassandra (1998) show how belief states connect planning with partial observability. Their formalism is not an assurance that any AI-written world model is calibrated.

## One-step Bayesian filter

Let `b_t(s)` be the current belief before action `a`. The predicted belief is

`b^-_(t+1)(s') = Σ_s T(s'|s,a) b_t(s)`.

After observing `o`, multiply by its likelihood and normalize:

`b_(t+1)(s') = Z(o|s',a) b^-_(t+1)(s') / Σ_j Z(o|j,a)b^-_(t+1)(j)`.

The denominator is the model probability of the observed evidence. If it is zero, the observation is **impossible under the model**. Dividing by zero, forcing an arbitrary state, or treating the observation as an automatic proof of sensor corruption would be wrong. Record the inconsistency and inspect the transition, sensor and environmental assumptions. If transition probabilities do not sum to one or an observation likelihood is outside [0,1], the model is ill formed and cannot support inference.

## Worked example

Use two hypothetical states, normal and degraded. The prior belief is `b=[0.6,0.4]`; transitions are `[[0.9,0.1],[0.3,0.7]]`. The prediction is `[0.66,0.34]`. An observation channel assigns likelihood 0.8 under normal and 0.1 under degraded for a particular reading. After that reading, the unnormalized weights are `[0.528,0.034]`, evidence probability `0.562`, and posterior `[0.93950...,0.06050...]`. Those numbers are a *calculation under declared probabilities*, not a diagnosis of real equipment. Another plausible transition matrix or sensor calibration could produce a different posterior for the same observed reading.

The offline `belief_update` function requires explicit state and observation probabilities and refuses an observation with zero evidence. It neither estimates likelihoods nor infers whether a real worker has stopped. For a real system, the evidence packet must include the sensor/probe method, calibration or measurement provenance, time stamps, missingness and changing equipment conditions, as well as alternative models.

## Limits of a belief distribution

A precise posterior does not mean the world is precisely known. Unmodeled states, adversarial observations, drift, correlated errors and missed instrument data can make it wrong. A belief state should not be reported without the likelihood model, prior origin, action and sampling assumptions. Treat missing probabilities as **unknown**, not zero. Inference from a trace can require a richer causal model of what produced the observation, especially if an agent selectively collects evidence while pursuing its objective.

The future Bitwork router may retrieve source information supporting the state and observation models, but it must not fabricate the models themselves. The order remains content first, routing last. **This edition implements the mathematics only, not a live POMDP controller.**

**Primary source:** Kaelbling, Littman and Cassandra, *Planning and acting in partially observable stochastic domains*, *Artificial Intelligence* 101 (1998), 99–134, DOI 10.1016/S0004-3702(98)00023-X (publisher abstract inspected): https://www.sciencedirect.com/science/article/pii/S000437029800023X . Additional formulas are standard conditional probability derivations.
