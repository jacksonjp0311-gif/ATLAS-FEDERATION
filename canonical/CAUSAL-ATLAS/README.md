![Atlas Forge approved hero graphic](assets/atlas_forge_knowledge_hub.png)

# CAUSAL ATLAS

**Version 1.0.0 — scoped scientific knowledge *content edition* · Atlas Common Contract 1.0**  
**James Paul Jackson Research Program · 12 November 2026**

An apparent improvement does not prove its cause. Causal Atlas preserves the concepts, estimands, identification assumptions, counterexamples, methodological references, and executable teaching calculations needed to ask *what changed because of an intervention* rather than merely *what changed afterward*.

**Release distinction:** v1.0 is a complete, tested software and reference edition for the **declared bounded scope below**, not a comprehensive encyclopedia of causal inference, not an independently reviewed scientific textbook, and not evidence that an arbitrary dataset identifies a causal effect. The scientific, live Bitwork/AI and Windows deployment acceptance remains incomplete. Causal Atlas stays separate from Forge's shared data-only retrieval runtime.

## Enter the knowledge library

| Destination | Use |
|---|---|
| [Reference guide](docs/REFERENCE_GUIDE.md) | 24 structured scientific chapters; start from a question, not an estimator |
| [All-in-one depth manual](docs/DEPTH_MANUAL_v1.0.0.md) | Chapters, investigations, forms and source appendix in a portable Markdown reference |
| [Thirteen investigations](docs/REFERENCE_GUIDE.md#investigations) | Synthetic model checks plus one authentic historical descriptive tabulation |
| [Source register](docs/SOURCE_REGISTER.md) | Authoritative origins, inspection boundaries, rights and provenance |
| [Individual records](docs/reference/) | Machine-exact record IDs, original derivations, equations, assumptions and limits |
| [Method-selection directory](docs/chapters/24_method_selection_directory.md) | Which design fits which question, and what must be measured first |
| [Coverage matrix](docs/COVERAGE_MATRIX.md) | What exists, what is only explained, and what remains unimplemented |
| [Casebook](docs/CASEBOOK.md) | Earlier bounded arithmetic examples and the new advanced calculations |
| [Historical reproduction](docs/REAL_DATA_REPRODUCTION.md) | 1973 Berkeley application counts: descriptive standardization without causal claims |
| [Tool and estimation contract](docs/ESTIMATOR_CONTRACT.md) | Exact inputs, returned statuses and inference exclusions |
| [Release verification](docs/VALIDATION.md) | Tests, source limits, reproducibility and deferred v1 acceptance |
| [Common node manifest](atlas_manifest.json) | Versioned machine-readable discovery and evidence maturity |

## What this edition actually covers

Core topics include well-defined treatments and target trials; potential outcomes, DAGs, identification, confounding, mediators and colliders; standardization, supplied propensity-weighted methods and bounded augmented estimation; missing-outcome bounds; IV and weak-instrument warnings; sharp/fuzzy RD point calculations; staggered-adoption DiD comparisons; finite two-decision g-formula; stochastic-mediator contrasts; two-unit interference; conditional effect transport; negative controls and sensitivity; measurement error; scientific uncertainty; source rights; and evidence-preserving context assembly.

The v1 boundary deliberately **excludes automatic causal discovery, fitted nuisance models, robust general sampling inference, a complete longitudinal/MSM implementation, full target-trial emulation, universal graph identification, arbitrary RD bandwidth inference, or certification of actual causal effects**. Established external software may implement parts of these methods, but that does not confer validity on an empirical design. Refer to [remaining gaps](docs/COVERAGE_MATRIX.md).

## Try the bounded methods (Python 3.10+)

From this source directory:

```powershell
py -3 -m causal_atlas --version
py -3 -m causal_atlas advanced-casebook
py -3 -m causal_atlas longitudinal examples/longitudinal.json
py -3 -m causal_atlas staggered-did examples/staggered_did.json
py -3 -m causal_atlas mediation examples/mediation.json
py -3 -m causal_atlas interference examples/interference.json
py -3 -m causal_atlas transport examples/transport.json
py -3 -m causal_atlas binomial-interval examples/binomial_interval.json
py -3 -m causal_atlas ucb-admissions examples/ucb_admissions.json
```

Earlier `estimate`, `population`, `missing-bounds`, `wald`, `iv-population`, `iv-sensitivity`, `rd`, `fuzzy-rd`, `rd-bandwidths`, `casebook`, `investigations`, `quasi-casebook`, `separation`, `adjustment`, `standardize`, and `reference` commands remain available. Mathematical operations require no third-party runtime dependencies. Optional numerical research oracles use NumPy/SciPy/NetworkX. Graphs and estimators do not authenticate any study design.

## Feed a compatible AI without losing the evidence

The Common Contract exposes `discover`, `search`, exact revision `fetch`, typed `neighbors`, budgeted `assemble_context`, `validate_context`, and `changes_since`. Every record includes provenance, source locators or gaps, assumptions, applicability, evidence status and limitations. The reference corpus and human-readable Markdown are both included, with prior revisions preserved and versioned.

Forge's search and context runtime is **shared and unchanged**. Current Bitwork routing is deferred; these publications do not claim a live integration, lower research cost, or better AI answers. Retrieved material is data, not instructions to execute. Results that cannot be supported should remain unresolved.

## Science and provenance boundaries

The Berkeley case reproduces public aggregate application counts and a descriptive Simpson reversal; it does **not** identify a causal effect of recorded sex or adjudicate discrimination. The 1973 table appears in the R base dataset documentation. Only an attributed, normalized numeric transcription is bundled because rights to the redistributed original data files were not confirmed. Synthetic cases are marked as such. Earlier Source v0.3 access limits remain preserved. This is evidence-preserving reference development, not peer review or scientific certification.

## Next acceptance work

Independent source and methodology review, fully reproducible rights-cleared causal study replications, study-valid sampling inference, live downstream Bitwork-to-AI evaluation, and native Windows checks are not completed. The collection remains local; it has **not** been pushed to GitHub or installed on the user's computer.

See [release readiness](docs/V1_READINESS.md) and [contributing guidelines](AGENTS.md). The 30-domain queue is owned by the separate Forge collection. **Materials Atlas remains next and unstarted.**
