# Chapter 17 — Reaction engineering, transport, and residence time

**Domain:** Chemical engineering  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A reactor converts material while moving heat and species. Scale changes make mixing, heat transfer and diffusion compete with intrinsic kinetics. A rate law measured in a small vessel may cease to describe production at large scale because concentration and temperature become spatially nonuniform. A residence-time distribution describes how long material spends inside a process rather than guaranteeing every fluid element reacts equally. Chemical engineering equations must retain phase, density and applicable fluid models. A useful atlas teaches nondimensional comparisons and the distinction between chemical and physical time scales, without asserting one process recipe works for every chemistry.

## Mathematical or physical principle

`τ_nominal=V/Q for a steady volume-flow approximation; conversion X=(F_A,in−F_A,out)/F_A,in for specified feed basis.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Dividing a vessel's effective liquid volume by volumetric flow gives a nominal residence scale under incompressible continuous flow. It is not the actual time distribution in a nonideal vessel. Conversions require measured molar flow and a chemical species, not merely mass totals. Reaction extent from the previous chapter provides theoretical stoichiometric bounds; real thermal transport and product formation rates determine whether those bounds can be approached. A process that conserves all atoms might still be unsafe or consume excessive energy.

## Reconstruct an illustrative result offline

Invent volume 2 m³ and flow 0.5 m³/h, obtaining nominal τ=4 hours. Explain why a bypass channel or nonuniform mixing would make some fluid parcels exit much sooner than four hours. Report the missing reactor mixing model rather than declaring complete conversion.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This chapter contains no actionable reactor startup, synthesis temperatures, hazardous catalysts or material recipes. Scale-up requires external safety, waste handling, and process-control evidence.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
