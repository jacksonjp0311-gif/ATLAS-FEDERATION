# 39. Cross-language comparison requires a sampling design

Language is universal to humans, but linguistic properties vary substantially across families, regions, histories, communities, modalities, and traditions of documentation. A claim about “most languages” needs an explicit sampling population and a consistent definition of the measured feature. Counting the number of entries returned by a database is insufficient. Some language families contain thousands of documented varieties, while others have a single listed language; their representation in a dataset reflects scholarly attention as well as genealogical realities.

## What is counted

Define a unit of analysis: a named language, a dialect, a speaker, a construction, a recorded utterance, or a language-family lineage. A word-order construction can depend on clause type and information structure; labeling one language simply SOV or SVO can hide internal variability. Language identifiers must be tied to a named classification release and a source; a label alone does not guarantee a consistent population over time.

WALS's introduction explains why maximizing genealogical and areal diversity is crucial and documents the composition and documentation gaps of its samples. The observed fraction of languages possessing feature F is `p_naive=(Σ_i 1[F_i])/(number of known F_i)`. A simple sensitivity statistic is `p_family=(1/K)Σ_f ((Σ_{i in f}1[F_i])/(number of known F_i in family f))`, where K is the number of families with at least one observed value. These quantities answer different descriptive questions. Equal family weighting does not remove areal diffusion, inconsistent family taxonomy, missingness, or nonrandom language selection.

## Demonstration and counterexample

Consider a toy sample: three languages in family A all show F, while one of two languages in family B lacks F and the other has an unknown value. The naive observed fraction is 3/4; equal family weighting produces (1+0)/2=1/2. Neither proportion estimates the worldwide frequency without a defensible sample and missingness model. A database's “unknown” must not automatically become a false feature observation.

`typology_by_family` computes both figures, records unknown values and source-supplied family assignments, and refuses duplicate language IDs. It does not authenticate those assignments. Genuine scientific work should stratify by genealogical and geographic factors, document feature criteria, examine family reclassifications and estimate uncertainty with clustering or appropriate models rather than treating all languages as independent random draws.

## What a future reader must preserve

Record survey design, language IDs, feature definitions, source passages and licensing, sampled communities, classification versions, exclusion criteria, unknown/mixed cases, and data transformed from raw observations. Preserve the raw feature judgments separately from aggregate statistics. A queryable database without these facts cannot support reproducible linguistic universals.

**Sources:** WALS introduction (Comrie, Dryer, Gil and Haspelmath, publisher page) and CLDF specification; these are selected documentation pages, not original sampled data acquired in this release.
