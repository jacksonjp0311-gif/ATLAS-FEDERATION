# Investigation 07. A treatment changes the next treatment decision

**Question:** What would happen to the outcome if every unit followed two particular treatment decisions, when the first decision changes a covariate that affects the second?

Imagine an equipment maintenance program measured at the start of each interval. At baseline a unit has L0. The team makes an initial choice A0. Later, a new diagnostic L1 is measured. A1 is then chosen based partly on L1. The outcome Y is the probability of a specified defect during follow-up. This example is a synthetic process model; it contains no machine observations.

A naive model that adjusts for the post-A0 diagnostic as though it were an ordinary baseline covariate can remove pathways through which A0 influences Y, or change the population being compared. A longitudinal g-formula instead constructs risks for *intervention regimes* through the intermediate-state transition and the final outcome model. This is not a claim that a real study satisfies exchangeability.

**Run:** `python -m causal_atlas longitudinal examples/longitudinal.json`.

The model specifies baseline mass 1, P(L1=1|A0=0)=1/5, P(L1=1|A0=1)=3/5, and risks `1/10 + A0/10 + A1/5 + L1/10`. It computes a 17/50 risk contrast between the static strategies (1,1) and (0,0). The four output risks and the provenance `stipulated_binary_transition_and_outcome_probabilities` allow independent arithmetic inspection. The result is not an observational estimator.

A real investigation needs documented treatment decisions, past outcomes, intermediate covariate histories, censoring, the strategy a unit could have followed, and support for those histories. It must justify the temporal ordering and conditional exchangeability at *each* decision. If an intermediate state is almost never observed under one treatment history, estimates may rely on unstable extrapolation. Preserve these limitations in the context package with the numerical contrast.

**Reference:** [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook), Part III on time-varying treatment and treatment-confounder feedback; [chapter 14](../chapters/14_longitudinal_gmethods.md).


## Investigative follow-up

A practical data request would ask for an event log showing when each decision occurred, what diagnostic history was visible at that moment, what intervention was feasible, and what outcomes were recorded or censored. It should also request the data schema, treatment-rule revisions and evidence about changing process conditions. A sensitivity check can ask how the risk contrast changes when the intermediate transition probabilities are changed over a stated range. This is evidence acquisition, not a substitute for collecting observations under the proposed treatment strategies.
