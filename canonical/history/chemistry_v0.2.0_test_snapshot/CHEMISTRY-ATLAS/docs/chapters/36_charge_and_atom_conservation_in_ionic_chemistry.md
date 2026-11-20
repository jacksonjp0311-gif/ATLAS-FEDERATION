# 36. Charge and atom conservation in ionic chemistry

**Field:** Stoichiometry · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

A chemical equation can conserve every element and still violate electrical charge conservation. That is why balancing neutral molecular formulae is not enough for electrochemistry or ionic solution analysis. The first step is to distinguish a substance's label from its explicitly modeled composition and formal charge. A token like Fe3+ is an interpretation, not proof of the oxidation state in an actual sample; chemical species can interact, complex, dissociate, or transform in solution. For a constructed finite reaction, put all reactant atoms and charge on one side and all product atoms and charge on the other. Linear algebra then finds candidate nonnegative stoichiometric coefficients. A unique one-dimensional rational nullspace gives an unambiguous primitive ratio relative to the supplied species; a larger nullspace must be refused as underdetermined rather than arbitrarily chosen. This protects a research archive from presenting a mathematically chosen solution as observed reaction feasibility.

## Equation and definitions

`For each element e, Σ_reactants ν_i a_(e,i) − Σ_products ν_j a_(e,j)=0; for charge, Σ_reactants ν_i z_i − Σ_products ν_j z_j=0. The coefficient nullspace is computed using exact rational arithmetic.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Treat the element and formal-charge counts as rows of an integer matrix, with positive columns for reactants and negative for products. Reduced row echelon form over rational numbers prevents floating rank errors. With one free coefficient, back-substitute, clear denominators and divide by the integer greatest common divisor. Verify every residual independently. A mathematical row for an electron contains no atoms and formal charge -1. The model does not solve electron energies, electronic spin, solution speciation, or product kinetics. In a real reaction, electron transfer and electroneutrality can involve counterions and phases not included in the simplified notation.

## Reconstruct without external AI

Supply one H+ species with H=1 and charge +1, one OH- species with H=1,O=1 and charge -1, and H2O with H=2,O=1, charge 0. The exact primitive coefficients are 1:1→1. Independently verify hydrogen, oxygen and charge totals. A second authored example Fe3+ + e− → Fe2+ balances formal charge; it is notation, not an electrochemical experiment.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

An equation can be balanced yet chemically impossible or violently hazardous. Formal charge and oxidation state are not identical concepts. Multiple independent reactions yield nonunique nullspaces; the model rejects those cases without pretending to select a physically favored pathway. No synthesis or handling procedures are inferred.

## Source provenance and rights

- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific
- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
