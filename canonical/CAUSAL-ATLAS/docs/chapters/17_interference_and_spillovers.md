# 17. Interference and spillovers: another unit's treatment can matter

The familiar potential-outcome notation Y_i(a_i) assumes one unit's outcome does not depend on everyone else's treatment assignment. This no-interference simplification is implausible for contagious disease, social networks, learning effects, machine lines sharing a resource, or teams whose members coordinate. Under interference, one must define exposure at the relevant group or network level and decide which treatments are inside the causal unit.

## Explicit two-person cluster model

A small cluster with two units has four joint assignments: 00, 01, 10 and 11. Let Y0(a0,a1) be the first unit's outcome under both assignments. A **direct effect at neighbor status 0** is Y0(1,0)−Y0(0,0). At neighbor status 1 it is Y0(1,1)−Y0(0,1). A **spillover while own status is 0** is Y0(0,1)−Y0(0,0). These can differ. Compressing all four into one treatment effect can destroy information about the policy being evaluated.

The `interference` command accepts the complete table of two outcomes under all four assignments, checks bounded outcomes and reports these contrasts. In the synthetic example, the first unit's own-treatment effect with neighbor untreated is 3/10 and spillover on the first unit with own treatment off is 1/5. Because the table is stipulated, no estimation or randomization occurred. The tool's role is to teach how an estimand changes under spillovers.

## Partial interference and policy design

A common practical simplification is partial interference: effects may propagate inside a declared cluster, but not between clusters. A two-stage randomized design can randomize cluster exposure policies and within-cluster assignments; appropriate designs can identify direct and indirect effects under their assignment conditions. If units move between clusters or share a supply chain, partial interference may fail. Network exposure mappings may help define effects of neighbors or coverage proportions, but the mapping itself is a scientific assumption.

For a manufacturing network, a process change in one machine might divert maintenance staff, alter material queues or shift temperatures in shared equipment. A control machine may therefore cease to be truly untreated. The evidence plan should retain machine dependency maps, resource-sharing logs, timing, measured spillovers and candidate mechanisms. This is a hypothetical scenario; no actual factory observations are bundled.

## Reporting contract

Specify unit of assignment, unit of outcome, interference boundary, exposure mapping, causal target, assignment probabilities, cluster count, sampling units and dependence-aware uncertainty. If a study uses individual standard errors under shared clusters, mark a model limitation. A null direct effect does not imply no spillover effect. A network result cannot be transported to a different graph without further assumptions.

**Source:** Hudgens and Halloran (2008), [*Toward Causal Inference With Interference*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/), abstract and full article overview. This Atlas implements only a complete, stipulated two-unit potential-outcome table, not interference estimation from observed network data.
