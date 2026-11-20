# 22. Missingness, measurement error and selection are part of the causal model

The variables in a dataset are recorded measurements, not direct access to underlying scientific states. Treating recorded exposure and outcome values as exact can create or reverse associations. Inclusion in the dataset itself may depend on treatment, outcome, survival, or unrecorded causes. An apparently clean regression can then estimate an association in a selected group unlike the original target population.

## Measurement error is structural

A pressure sensor can be biased by calibration drift, temperature, or software changes. An interview measure can be affected by recall and by outcome status. In both cases, measurement error is not necessarily independent or nondifferential. A classical error model that attenuates a linear slope does not apply to every exposure, outcome type, timing or missingness mechanism. Draw the measurement process explicitly alongside the substantive causal graph, with observed and latent nodes separated.

Record measurement units, sensor/instrument versions, calibration dates, blinding if relevant, resolution, missing flags, sampling protocols and changes across treatment groups. The Measurement Atlas should supply technical metrology concepts, but its uncertainty calculation cannot by itself repair unmeasured confounding. Shared identifiers and provenance let the nodes complement each other while keeping their evidence statuses separate.

## Missing outcomes are not zeros

The current `missing-bounds` tool offers sharp arithmetic bounds for completely counted binary arm populations when missing outcomes can be either 0 or 1. If n observations were expected and only o are observed, with s successes, the risk lies between s/n and (s+n−o)/n. The difference interval follows by subtracting the extreme arm risks. It is not a confidence interval and requires no imputation. Real studies often have additional assumptions, sampling uncertainty and dependence that these simple bounds do not represent.

Complete-case selection can bias comparisons if loss to follow-up depends on treatment or outcome. Assigning zero to a missing outcome is an explicit hypothetical rule, not a neutral default. Multiple imputation and inverse-probability-of-censoring weighting require their own data, models and assumptions; neither is implemented by the bound tool.

## Selection, survival and timestamps

Restricting to surviving workers, completed batches, treated survivors, or records with a post-treatment measurement can condition on consequences of the treatment and outcome. A collider can induce an association even when none exists marginally. Survivorship can change not only effect estimates but the estimand itself. A study should say whether it targets all eligible units, a principal stratum or a post-treatment selected subgroup; the latter often requires assumptions not observed in the records.

**References:** Hernán and Robins [*Causal Inference: What If*](https://miguelhernan.org/whatifbook) includes measurement bias and selection bias chapters; [Hernán and Robins target-trial protocol](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/) addresses selection and censoring. These pages support the topic scope, not an automatic assessment of any particular database.
