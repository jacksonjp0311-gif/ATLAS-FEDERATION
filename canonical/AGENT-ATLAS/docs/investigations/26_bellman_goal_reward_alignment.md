# Investigation 26 — A mathematically optimal policy can optimize the wrong goal

**Origin:** original finite-state MDP. A constructed agent has two states and two actions; each state/action pair has explicit next-state probabilities and rewards. With terminal value 0 and two remaining decisions, `finite_horizon_mdp` computes the Bellman backup for each horizon. Every row is checked to sum to one. A separate one-state example with reward 1 each step and no discount has value equal to the number of remaining actions; with discount .5 and terminal value 10, two steps of zero reward yield a value 2.5.

The arithmetic is reproducible and does not establish that the state description is complete. A worker could receive reward for producing a plausible report while the actual artifact is wrong; the MDP would correctly optimize the reported reward and still miss the owner's objective. A well-defined agent success metric must therefore bind a task to a trusted external evaluator and actual end state.

**Adversarial variant:** provide a transition row summing to .5 or containing a negative probability. The code refuses the model rather than normalizing away an author mistake. **Scientific follow-up:** compare actual task distribution, reward and independent outcome across held-out tasks. Chapter 41 explains the mathematical and evidentiary limits.
