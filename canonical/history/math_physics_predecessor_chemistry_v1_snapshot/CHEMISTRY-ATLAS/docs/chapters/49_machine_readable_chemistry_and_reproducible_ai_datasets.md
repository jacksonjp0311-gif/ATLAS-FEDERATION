# 49. Machine-readable chemistry and reproducible AI datasets

**Field:** AI and knowledge systems · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Advanced AI models for chemistry require structured data, not just natural-language passages. Each record should distinguish molecular identity, empirical chemical structure, calculated property, measurement method, uncertainty, phase, source, version, rights and train/evaluation exposure. PubChem offers programmatic compound, substance, and assay retrieval, while Materials Project provides computational materials data; they have different provenance and distinct data-model assumptions. A model that learns from one dataset cannot automatically claim held-out performance when the same source record appears under another identifier. Raw original files and transformations must be archived separately. A chemistry model should return missing data as unknown and maintain contradictory measurements when source contexts differ.

## Equation and definitions

`A source-aware datum can be represented as (source_id, edition, artifact_hash, chemical_id, phase, property, unit, conditions, method, uncertainty, rights, transformation_hash). This tuple is metadata structure, not a scientific equation.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

A reproducible training/evaluation dataset begins with versioned source acquisition and unique document identifiers. Split by molecular scaffold, material family or publication group when testing genuine generalization, and check exact and near-duplicate overlap across identifiers. Preserve original molecule representations and atom/bond/charge semantics; plain chemical formulae cannot distinguish structural isomers. Keep computed values (e.g., density functional theory) separate from experimental measurements, and never allow model-generated predictions to masquerade as authenticated laboratory data.

## Reconstruct without external AI

Invent a compound record with a PubChem CID, two source IDs, temperature, unit, and value. Give it a separate derived computation with a new source ID. Show how a dataset lacking a transformation record could accidentally treat both as independent observations. Record an uncertainty field as null rather than inventing a precise confidence interval.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

A perfect retrospective model score may result from memorization, leakage or mislabeled data. This Atlas does not download actual PubChem/Materials Project data, train a model, or measure emergent chemical generalization.

## Source provenance and rights

- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) — Molecular formula, weight, structure representations, and caller-visible property provenance limits
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api) — Materials Project data API, computational vs observed provenance, dataset and code version distinctions

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
