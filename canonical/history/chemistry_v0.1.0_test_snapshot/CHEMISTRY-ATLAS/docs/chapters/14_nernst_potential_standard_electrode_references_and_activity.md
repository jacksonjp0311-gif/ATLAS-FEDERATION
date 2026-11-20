# Chapter 14 — Nernst potential, standard electrode references, and activity

**Domain:** Electrochemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Electrode potential is an intensive thermodynamic quantity under specified reference electrodes and electrochemical conditions. The Nernst equation relates equilibrium electrode potential to standard potential and a dimensionless reaction quotient built from species activities. Real electrodes may display overpotential, resistance, concentration gradients and other deviations under load. A standard potential without reference convention or phase and ionic-state information can be meaningless in comparative calculations. Battery nameplate voltage is not automatically a Nernst equilibrium prediction for every temperature and state of charge.

## Mathematical or physical principle

`E_eq=E°−(RT/nF)ln Q, with n positive integer electrons and Q an activity-based dimensionless quotient.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Starting from ΔG=−nFE for a reversible electrochemical reaction and ΔG=ΔG°+RT lnQ, substituting yields the potential correction. At Q=1 the correction is zero. Larger product activity relative to reactants changes the equilibrium potential in a direction set by the stipulated quotient. The derivation assumes equilibrium interfaces and an externally measured standard reference. Under operating current the electrode can depart from that equilibrium value.

## Reconstruct an illustrative result offline

Set E°=1 V, n=1, T=298.15 K, Q=1 and recover 1 V. Change Q to 10 and evaluate the potential correction; report that this is not a forecast of delivered battery power.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Without cell identity, phase, reference electrode, activities, kinetics and load, the number has no operational device validity. The code cannot charge batteries or control chemical processes.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
