# Chapter 29 — Thermochemical datasets and machine-readable scientific memory

**Domain:** Metrology  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A durable chemistry archive requires versioned numeric property records with units, phases, standard states and citation lineage. Thermochemical databases aggregate contributions from experiments and evaluations; a number stripped of its original context may be wrong for a new phase or temperature. A good machine record separates an original observation, an evaluated recommended value, an extrapolated fit, and a hypothetical teaching input. Dataset references may be copyrighted or carry independent reuse restrictions. When original source bytes cannot be retained, that absence must remain explicit instead of being silently filled by generated data.

## Mathematical or physical principle

`Data record = (species identity, property, value, unit, T, p, phase, source revision, uncertainty, applicable range, rights).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A measurement is not made more accurate by storing more decimal places. Reproducing a Shomate or Arrhenius fit requires coefficients, parameter definitions and temperature range; using coefficients outside that range may generate plausible but scientifically invalid numbers. A hash identifies file bytes relative to a trusted digest; it does not establish authorship or license. In an offline rebuild, the next researcher should be able to audit each transformation from original measurement to a derived property.

## Reconstruct an illustrative result offline

Create a fictional record for a solid's heat capacity with value 500 J/(kg K) at a specified temperature, plus ±20 uncertainty and a documented source. Then show how removing the phase or temperature makes the record unsuitable for general use.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No full NIST WebBook entries, OpenStax chapters or restricted standards have been copied into this edition. Compiled source rights require separate verification for authentic archival acquisition.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
