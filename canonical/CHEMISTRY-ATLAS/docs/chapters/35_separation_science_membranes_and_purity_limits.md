# Chapter 35 — Separation science, membranes, and purity limits

**Domain:** Chemical engineering  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Separating mixtures into components can require phase changes, selective adsorption, chromatography, filtration or membranes. The selected method depends on chemical potential, molecular size, charge, volatility and interaction with the separation medium. Separation is not inherently complete: two compounds may have nearly indistinguishable properties, and concentrating a trace component can require substantial energy and time. Materials, battery and semiconductor industries depend on high purity, but a purity specification must identify relevant contaminants, analytical detection limits and process yield. Reproducible design uses declared feed and product compositions, not an unverified claim that a generic filter removes every impurity.

## Mathematical or physical principle

`For a nonreacting component i: n_i,feed = n_i,product + n_i,waste + Δn_i,inventory. Recovery fraction = n_i,product/n_i,feed if feed>0.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The component balance follows from conservation of atomic identity in a nonreactive separator. Each stream may carry multiple constituents and a process can preferentially enrich one component while discarding another. Overall total-mass conservation can pass even when the desired component's recovery is poor, so species-resolved measurements matter. A thermodynamic separation limit can constrain the minimum work, but real energy demand also depends on transport, irreversibilities and equipment details. No separation technology can be selected safely from a recovery percentage alone.

## Reconstruct an illustrative result offline

For a hypothetical separation, feed contains 10 mol of harmless component X. Product contains 8 mol X, waste 1 mol X and inventory grows by 1 mol X. Conservation closes and process recovery is 80%. Explain why this says nothing about chemical purity of the product if an unmeasured impurity Y accompanies it.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This is chemical accounting only, not a solvent, distillation, membrane, purification or hazardous extraction protocol. Real separation safety, effluent treatment, contamination limits and experimental validation remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
