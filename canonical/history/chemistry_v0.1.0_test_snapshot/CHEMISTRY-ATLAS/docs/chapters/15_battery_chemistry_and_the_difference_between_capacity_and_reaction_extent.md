# Chapter 15 — Battery chemistry and the difference between capacity and reaction extent

**Domain:** Electrochemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Battery performance connects active material composition, reversible electron transfer, ionic transport, electrodes, electrolyte stability and thermal behavior. Stoichiometry can bound theoretical charge, but practical capacity is lower and depends on use, rate, aging and degradation. Electrochemical free energy relates to reversible cell voltage only under appropriate phase and activity conventions. Batteries must therefore be modeled across chemical, electrical and thermal domains, with protection and hazard controls separate from the theoretical energy stored in reactants. This connection is central to future computing infrastructure because power availability and battery safety affect processors, storage and communication devices.

## Mathematical or physical principle

`Q_theoretical=n_e F; E_reversible=−Δ_rG/(nF), with charge Q in C and reaction Gibbs energy Δ_rG in J per mol reaction extent.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Multiplying reaction extent by electron stoichiometry gives moles of transferred electrons, hence coulombs. Dividing the thermodynamic free energy per reaction mole by charge per reaction mole yields voltage for an ideal reversible transformation. This is not a real constant terminal voltage; concentration, activity, polarization and transport change the observed voltage as state evolves. Thermal runaway and short-circuit hazards are not deducible from this reversible model.

## Reconstruct an illustrative result offline

For a hypothetical reaction carrying 2 mol electrons per mol extent, compute 2F coulombs. If the reversible energy per extent were a stated value, calculate E and explain why measured terminal voltage and capacity could differ.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No electrolyte formulation, abusive testing, improvised battery construction or protection bypass is provided. These topics require certified engineering and standards separate from theory.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
