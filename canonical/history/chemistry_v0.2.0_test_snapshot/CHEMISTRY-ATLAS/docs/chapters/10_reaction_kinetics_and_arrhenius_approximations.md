# Chapter 10 — Reaction kinetics and Arrhenius approximations

**Domain:** Chemical kinetics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Reaction rates describe how species amounts or concentrations change over time. A thermodynamic driving force and a rate law answer different questions: a stable equilibrium may require geological time if the kinetic barriers are large. The Arrhenius relationship models the temperature dependence of certain rate constants over a limited range; its apparent activation energy can change with mechanism. A first-order exponential decay is one possible kinetic model, not a universal description of chemical aging, degradation or polymerization. The parameter and conditions must be preserved alongside a measured dataset, and fits require independent validation.

## Mathematical or physical principle

`k(T)=A exp(−E_a/RT); ln(k2/k1)=−(E_a/R)(1/T2−1/T1); C(t)=C0 exp(−kt) for first order.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Taking logarithms of the Arrhenius form eliminates the preexponential factor and permits a ratio of rates at two absolute temperatures. Separating dC/dt=−kC gives the exponential first-order solution. Both derivations assume temperature and mechanism conditions that may not hold in an industrial process. A rate inferred from only two points can reflect transport effects or multiple pathways instead of a single activation barrier.

## Reconstruct an illustrative result offline

Take invented Ea=20 kJ/mol and compare a model rate constant at 300 K and 330 K. Confirm the rate increases under this positive-Ea assumption. Separately use a first-order k=0.1/s to compute concentration after 10 seconds.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Never use this teaching rate law to set hazardous reactor residence times, unstable chemical storage, or an accelerated-aging safety claim without independent material/kinetic testing.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
