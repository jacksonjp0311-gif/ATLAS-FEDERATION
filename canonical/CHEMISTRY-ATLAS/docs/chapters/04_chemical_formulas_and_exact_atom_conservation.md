# Chapter 04 — Chemical formulas and exact atom conservation

**Domain:** Stoichiometry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A chemical equation describes chosen reactant and product species with coefficients; balancing its elemental counts is a necessary mathematical condition for a valid chemical transformation. It is not evidence that the reaction proceeds spontaneously, quickly, safely or with specified selectivity. Formulas can contain nested groups and integer multiplicities, but charged species, isotopic labels and coordination compounds may require richer notations. An archive should preserve the original representation and show exactly what a parser accepts. For simple neutral species, a vector of counts per element provides a sparse conservation matrix; its nullspace contains formally balanced coefficient assignments.

## Mathematical or physical principle

`For matrix A of product-negative/reactant-positive atom counts, Aν=0, ν_i>0. Primitive integer ν obtained from rational nullspace when unique.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Each row corresponds to an element; conservation requires that total atoms on each side agree for that element. Rational Gaussian elimination gives exact candidate coefficients without floating-point rounding. When the nullspace has more than one independent dimension, arbitrary choices are possible and the algorithm should refuse to guess. The first edition intentionally rejects unsupported charge notation: a neutral atom balance alone cannot handle ionic redox charge conservation.

## Reconstruct an illustrative result offline

For 2 H2 + O2 → 2 H2O, write hydrogen and oxygen row balances and show both residuals equal zero. Repeat with incorrect coefficients 1,1,1 to exhibit nonzero residuals. The provided exact-Fraction code reconstructs primitive coefficients.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Balanced equations do not prove that chemicals are accessible, reactions occur under ambient conditions, or that mixing would be safe. Some syntactically balanced proposals are experimentally unrealizable.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms
- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
