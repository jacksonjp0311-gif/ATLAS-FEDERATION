# Investigation 25 — A diagnostic reading updates belief but does not prove a cause

**Origin:** original constructed POMDP example. **External measurements:** none. A system has two possible states, normal and degraded, with prior probabilities 0.6 and 0.4. The action-conditioned transition law is `[[0.9,0.1],[0.3,0.7]]`, producing prediction `[0.66,0.34]`. A new reading has likelihood 0.8 if the state is normal and 0.1 if degraded. Multiplying and normalizing gives posterior `[0.528/0.562,0.034/0.562] ≈ [0.9395,0.0605]`.

This is not an actual reading from a robot or motor; it demonstrates Bayesian conditioning under **supplied transition and observation laws**. The posterior is only as credible as the model. If the sensor calibration, initial probabilities or true state set are wrong, the computation can be exact but the conclusion false.

**Adversarial variant:** supply an observation with zero probability in every modeled state. The correct response is `observation probability zero; posterior not identified`, not assigning the most convenient state. The refusal does not diagnose whether the sensor was attacked, the operator erred, or the physical model omitted a state.

**Reproduce:** `python -m agent_atlas v1-casebook`, then inspect `belief-update-observation` and `impossible-observation-refusal`. Chapter 40 contains derivation and source scope. **Research follow-up:** obtain an independently measured sensor likelihood model and a source trace; perform model-checking under unseen operating conditions.
