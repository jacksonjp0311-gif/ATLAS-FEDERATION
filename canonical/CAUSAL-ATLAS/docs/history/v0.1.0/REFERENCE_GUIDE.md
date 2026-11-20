# Causal reference guide

All referenced IDs are prefixed `causal-atlas:` and resolve through the common node manifest. Read the complete record, including its qualifiers, rather than its title alone. The source register supplies the inspected portions.

## 1 Define the question

Start with `estimand`, `average-effect`, `trial-protocol`, `time-zero` and `adherence`. Fill in the study-plan template before selecting a numerical tool. Distinguish a question about the job stream as it was observed from a question about a chosen target job mix.

## 2 State the assumed structure

Use `dag-assumptions`, `identification` and `do-versus-see`. Provide the graph as explicit edges. The package does not turn an undocumented graph into a verified account of the world.

## 3 Examine adjustment and selection

Consult `backdoor`, `dseparation`, `collider`, `collider-descendant`, `mediator`, `pretreatment` and `no-set`. Run graphical checks only after deciding what each node and arrow means. Record unobserved nodes explicitly and exclude them from the list of available adjustment variables.

## 4 Calculate under declared support

Use `standardization`, `exchangeability`, `positivity`, `empty-strata` and `target-change`. The code accepts explicit target weights and refuses missing support in positive-weight strata. It does not silently fill missing groups from a regression or pool them away.

## 5 Test a fully specified mechanism

Use `factorization` and `model-limits`, then inspect the synthetic process case. Every probability in that mechanism is part of the example's input. They are not estimates learned by the tool. The graph and finite probabilities define the conditional result.

## 6 Audit the evidence

Use `data-validation`, the source register and the review rubric. Record what was observed, what was assumed, what was merely computed, and what competing explanation remains possible. Keep source review separate from a test that two algorithms return the same value.
