# 2 Identify an effect before estimating it

An estimator converts observed inputs into a number. Identification explains why a particular function of observed information would equal the desired causal quantity under stated assumptions. These jobs must stay separate. A highly accurate numerical routine can estimate an association that answers no causal question.

## A counterexample an AI must retain

The new exact example constructs two binary models with identical observations. In Model A, a fair hidden variable U sets both A and Y: `A=U` and `Y=U`. In Model B, A is fair and `Y=A`. Both produce half their observations at `(A=0,Y=0)` and half at `(A=1,Y=1)`. Thus the observed difference between treatment groups is one in both.

Under an intervention setting A, Model A leaves U and Y unchanged, giving causal effect zero. Model B changes Y, giving effect one. The code enumerates the joint distributions and interventions with the existing finite-model engine. It does not merely hard-code the two effects.

This is an original nonidentification demonstration for this observation set and these allowed models. It shows why a perfect observed predictor is insufficient by itself. It is not an impossibility claim about every additional experiment or source of information. Random assignment, substantive constraints, or other evidence could distinguish the models.

## What the current graph tools can do

A directed acyclic graph states assumed directional relationships and omissions. The local separation algorithm checks graphical paths. The sufficient back-door checker asks whether a supplied adjustment set contains prohibited treatment descendants and blocks back-door paths in the supplied graph. It does not learn the graph, prove that omitted causes do not exist, or implement every identification criterion. Formal definitions and algorithm anchors remain in the retained [Pearl 2010 source record](https://pmc.ncbi.nlm.nih.gov/articles/PMC2836213/) and DAGitty documentation.

Three small graphs are useful for reasoning:

* `L -> A`, `L -> Y`, `A -> Y`: L is a proposed common cause; suitable adjustment can remove that path under the graph and other identification assumptions.
* `A -> M -> Y`: M lies on the pathway. Blocking it does not generally preserve the total-effect question.
* `A -> C <- Y`: selecting or conditioning on C can open an association absent before selection.

Do not interpret the first pattern as an instruction to adjust for every available baseline variable. Timing is necessary context, not a sufficient selection rule. A pre-exposure variable can have a different graphical role. Write why it belongs in the adjustment set.

## Derive the standardized target

Let L denote a fully specified baseline stratum. Under consistency, conditional exchangeability of the relevant potential outcomes and treatment given L, and positive treatment support in all target-relevant strata,

`E_T[Y(a)] = sum_l E[Y | A=a,L=l] * P_T(L=l)`

when the conditional outcome responses are applicable to that target. To see the logic, average the potential outcome within each stratum, replace its conditional mean with the corresponding treatment-group mean using exchangeability and consistency, then average over the target weights. Moving to a different population requires an additional reason that those conditional responses carry over; target weights alone do not prove transportability.

The implementation accepts explicitly supplied stratum counts and target weights. An unsupported positive-weight stratum is not filled with a guessed rate. The source anchor for conditional randomization and standardization is [Hernán and Robins 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC2652882/). The displayed derivation is our own short explanation of the identification substitutions, not a reproduced publication passage.

## Model omissions belong in the result

A graph with `U -> A` and `U -> Y`, where U is unobserved, may have no observed set satisfying this package's sufficient back-door check. The output says exactly that. It must not say every causal question is impossible, nor that a sophisticated estimator automatically solves the hidden-variable problem.

Keep alternative plausible graphs when substantive evidence cannot decide among them. When a conclusion depends on removing an edge, record the evidence for that removal. A data-driven graph candidate is an assumption object to review, not a scientifically authenticated map of the system.

**Related records:** `identification`, `dag-assumptions`, `pretreatment`, `mediator`, `collider`, `no-set`, `observational-equivalence-example`.
