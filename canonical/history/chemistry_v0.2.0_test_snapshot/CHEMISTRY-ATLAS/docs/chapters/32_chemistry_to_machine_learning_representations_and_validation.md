# Chapter 32 — Chemistry to machine learning: representations and validation

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical machine learning transforms molecules, materials, graphs, sequences or spectra into numerical representations. The representation determines what information a model can learn and which distinctions it loses. A chemical formula cannot distinguish structural isomers; a SMILES string may encode structure but requires stereochemical and tautomer conventions. Dataset leakage can arise from duplicated compounds, near-duplicate scaffolds, shared measurement sources and repeated spectra. A model that predicts a chemical property on familiar variants may fail for new materials, solvents or measurement regimes. Machine-readable chemistry requires provenance and evaluation design, not merely a high benchmark score.

## Mathematical or physical principle

`Predictive error E=(1/N)Σ_i L(f(x_i),y_i), valid for a declared held-out sampling and target; not causal discovery by itself.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A prediction is evaluated against a reference measured property under defined conditions, with training exposure and split identities documented. A split by random rows can leak the same compound or scaffold through multiple records; more stringent splits may test generalization. Missing labels and censored detection-limit measurements require explicit treatment. External model embeddings do not certify molecular identity or lawful access to source data. The underlying chemical physics remains useful even when a trained model is unavailable.

## Reconstruct an illustrative result offline

Build a fictional dataset with one chemical formula repeated in training and evaluation under different sample IDs. Explain why a random row split can exaggerate predictive performance. Propose separate compound identity, source document and scaffold checks before claiming genuine unseen-material prediction.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This release has no trained chemical model or independently validated discovery system. The chapter gives evaluation principles; chemical safety and experimental verification remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) — inspected: Molecular formula, weight, structure representations, and caller-visible property provenance limits
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
