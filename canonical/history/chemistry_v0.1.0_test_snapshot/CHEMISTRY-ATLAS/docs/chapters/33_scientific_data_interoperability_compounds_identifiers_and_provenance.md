# Chapter 33 — Scientific data interoperability: compounds, identifiers, and provenance

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Public chemistry resources may expose names, molecular formulas, canonical structures, spectra and experimental properties through APIs. Machine-readable access is valuable, but an API response is not necessarily a primary published measurement. Compounds can have stereoisomers, isotopologues, tautomers, protonation states and salts; simplistic name-to-formula lookup can conflate important identities. A research vault must define a stable representation, dataset version, provenance of each property, uncertainty, assay context and licensing. The same principle applies to agent retrieval tools: sources must remain evidence, never executable instructions.

## Mathematical or physical principle

`Data identity ≠ chemical reality: a structured record requires compound ID + structure conventions + property conditions + origin + revision + rights.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

For a compound property table, prefer structured fields over free-text summaries, retain nulls, and distinguish measured versus predicted properties. PubChem PUG REST documents molecular formula, molecular weights and stereochemical SMILES fields; they are useful navigation capabilities, not an automatic license or proof of original experimental data for each row. A complete offline original-source archive needs an authorized snapshot and exact transport bytes, not a promise that the web service will remain reachable.

## Reconstruct an illustrative result offline

Take a toy record with molecular formula C2H6O and explain why it cannot, by itself, distinguish ethanol from dimethyl ether. Add structure representation, analytical evidence and source conditions before treating it as a unique compound.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No PubChem dataset was downloaded or experimentally checked here. Source rights, version history and compound-level evidence status remain separate obligations.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) — inspected: Molecular formula, weight, structure representations, and caller-visible property provenance limits
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
