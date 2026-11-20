# 41. Bellman planning: optimality belongs to the chosen objective and model

An agent policy can be optimal *relative to its assumed objective and transition dynamics* while still failing a human goal. A Markov decision process (MDP) assumes the state presented to the policy contains enough information to predict the next-state distribution and reward conditional on the action. An LLM may not have such a state. A tool response or a summary of conversation can omit relevant variables. The Markov assumption must be treated as a model constraint, not an automatically true property of agent traces.

## Finite-horizon recursion

For a finite state set `S`, action set `A`, transition probabilities `T(s'|s,a)` and reward `R(s,a,s')`, define terminal value `V_0(s)` explicitly. For `k≥1` actions remaining,

`Q_k(s,a) = Σ_(s') T(s'|s,a) [R(s,a,s') + γ V_(k-1)(s')]`,

`V_k(s) = max_(a) Q_k(s,a)` and `π_k(s) = argmax_(a) Q_k(s,a)`.

`γ` is the declared discount (here 0≤γ≤1). An optimizer needs all competing actions and a valid transition probability for each. If an action was never observed, inventing its transition outcomes does not turn an estimate into a model. The `finite_horizon_mdp` teaching utility validates dimensions and probability normalization, then solves backwards for a small supplied model. It reports the action choice at each horizon and does not call a model, sample a world, or claim measured success.

## Worked calculation

For a single state with one action, reward 1 every time, no terminal value and `γ=1`, `V_k=k`. With `γ=.5`, two actions remaining gives `V_2=1+0.5=1.5` if the reward is 1 each step; with zero reward and terminal value 10 at two steps remaining, the value is `10×0.5²=2.5`. These examples are fully specified arithmetic. They show that different terminal assumptions and discount factors lead to different numbers for the same state. A different reward function could lead to a different policy even with identical transitions.

## Reward hacking and verification

A reward is not automatically the user's objective. If a worker receives credit for returning a formatted report, it may optimize report completion without actually fixing a file. If success is defined by a reviewer text string, a model may produce that string while missing the task. For scientific reliability, define an independently inspectable task outcome and preserve the distinction between a score, a proxy and a verifiable external state. Cost penalties should record unit basis: CPU seconds, API tokens, dollars, operator actions and elapsed wall time are not interchangeable without explicit weights. Higher reward on a synthetic task is not proof of better real-life performance.

## When the Bellman equation is insufficient

Open-ended natural language tasks often lack a known finite state space, stable reward definition or measured transition matrix. Partial observability requires belief-state planning; multiple agents can create nonstationary or strategic dynamics; external tool calls can be irreversible; delayed feedback can make apparent immediate reward misleading. Such cases need different methods and stronger evidence. Agent Atlas v1 does **not** claim to solve arbitrary POMDPs or learn policy parameters; the small finite model is an educational reference.

**References:** Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press 2018 (publisher overview and chapter scope, not full-book audit), https://mitpress.mit.edu/9780262039246/reinforcement-learning/ ; Kaelbling et al. (1998), DOI 10.1016/S0004-3702(98)00023-X. Source rights remain external.
