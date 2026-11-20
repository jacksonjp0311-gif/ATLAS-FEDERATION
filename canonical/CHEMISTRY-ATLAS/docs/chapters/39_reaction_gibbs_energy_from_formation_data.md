# 39. Reaction Gibbs energy from formation data

**Field:** Thermochemistry · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Thermochemical tables can preserve a powerful form of knowledge: standard formation Gibbs energies and enthalpies at specified states, temperature and phase. A reaction's standard change is a stoichiometric sum of product values minus reactant values, but only if the source data use compatible conventions and independent measurement/uncertainty histories. Copying a number from a website without the phase, standard pressure, source revision or reference temperature is not enough to reconstruct the prediction. The NIST Chemistry WebBook supports diverse thermochemical datasets; this initial Atlas does not contain its complete original data. We therefore use invented values to test arithmetic while explicitly separating software correctness from genuine thermodynamic evidence.

## Equation and definitions

`Δ_r G°(T) = Σ_products ν_j Δ_fG°_j(T) − Σ_reactants ν_i Δ_fG°_i(T); likewise Δ_rH°=ΣνΔ_fH°, and ln K=−Δ_rG°/(RT).`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

The relation follows from the definition of a reaction extent ξ and the derivative of mixture Gibbs energy with respect to ξ at constant T,p. Each product contributes a positive stoichiometric coefficient and each reactant a negative one. Standard-state formation energies for species at the same T and compatible phase/reference conditions combine to give the standard reaction change. Inferring kinetic reaction rates or actual conversion from Δ_rG° alone is invalid: the system might be kinetically blocked or involve competing pathways.

## Reconstruct without external AI

Invent A with Δ_fG°=−1 kJ/mol and B with Δ_fG°=−3 kJ/mol at 300 K, with A→B at unit coefficients. Calculate Δ_rG°=−2 kJ/mol and ln K=2000/(R×300). Independently verify the sign and dimensional consistency. Mark the data invented and identify the phase fields a real source would require.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

Do not interpolate/extrapolate standard formation energies to a different temperature without heat-capacity, entropy and phase-change data. A large computed K does not guarantee reaction completion or laboratory safety; original values require authenticated sources.

## Source provenance and rights

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — Equilibrium, chemical potential and Gibbs relationship, 2025 online edition

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
