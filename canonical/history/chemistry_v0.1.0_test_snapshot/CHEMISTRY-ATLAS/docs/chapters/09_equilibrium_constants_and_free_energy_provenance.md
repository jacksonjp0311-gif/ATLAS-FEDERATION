# Chapter 09 — Equilibrium constants and free-energy provenance

**Domain:** Thermodynamics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Equilibrium constants are thermodynamic descriptors tied to specified species, activities, phases and temperature. They cannot be copied between different reaction representations without checking stoichiometry and standard states. For strongly favorable reactions, K may be too large for a common binary floating-point number; log K remains useful and avoids overflow. A scientific reference should preserve logarithmic values and their source uncertainties. The existence of one equilibrium constant never describes how quickly equilibrium is approached, whether products precipitate, or whether a material degrades under operation.

## Mathematical or physical principle

`K=exp(−Δ_rG°/RT); ln K=−Δ_rG°/(RT).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

At fixed T, the reversible equilibrium condition is zero Gibbs change, so setting Δ_rG°+RT lnK=0 yields log K directly. Multiplying all reaction coefficients by a factor changes the conventional equilibrium constant accordingly: the same physical equilibrium can have a different numeric K under a redefined equation. For this reason an archive must couple values to exact reaction stoichiometry and standard states.

## Reconstruct an illustrative result offline

Given Δ_rG°=−RT at any positive T, demonstrate lnK=1 and K=e. Multiply the formal reaction by 2 and observe that Δ_rG° doubles, so K becomes e² under the new representation.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

An equilibrium constant in concentration units is generally not a thermodynamic standard-state constant; the log requires dimensionless activities. Extremely high K does not prove perfect conversion or absence of competing chemistry.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
