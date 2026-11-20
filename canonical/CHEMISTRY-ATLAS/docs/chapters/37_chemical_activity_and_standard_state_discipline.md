# 37. Chemical activity and standard-state discipline

**Field:** Thermodynamics · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Chemical potential connects concentration, pressure, composition, and a chosen reference state. For nonideal substances it is generally wrong to replace dimensionless activity by a numerical molarity everywhere. Chemical activities depend on phase, ionic interactions and standard-state definitions, and the same physical sample may yield different numerical activity coefficients under differing conventions. The IUPAC Gold Book defines activity from the difference between chemical potential and standard chemical potential at a given temperature. That definition is central to reconstructing equilibria from primary evidence. An Atlas should preserve whether a value is concentration, partial pressure, molality, fugacity or activity, alongside temperature, pressure, composition and provenance. If a chemical source provides only one numerical constant without its standard state, it is not enough to reproduce a rigorous thermodynamic prediction.

## Equation and definitions

`μ_i = μ_i° + RT ln(a_i), where a_i is dimensionless activity; Q = Π_i a_i^(ν_i) with products positive and reactants negative.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Chemical potential is defined as the partial derivative of Gibbs energy with respect to amount of species at fixed temperature, pressure and other amounts. Integrating the ideal mixture logarithmic term yields the activity relation; the activity coefficient expresses departure from ideal reference behavior under its declared convention. Stoichiometric summation gives Δ_r G=Δ_r G°+RT ln Q. At equilibrium for a reversible reaction the net reaction Gibbs driving force vanishes, so ln K = −Δ_r G°/(RT). In real electrolytes, activities cannot be inferred from arbitrary molarity values without a credible activity model.

## Reconstruct without external AI

Take an invented reaction whose activity quotient Q is 10 and Δ_r G°=−5000 J/mol at 298 K. Compute Δ_r G=−5000+RT ln(10) by hand. Compare the answer to treating raw concentration numbers as dimensionless without specifying a 1 mol/L reference; explain why the latter shortcut can break thermodynamic reproducibility.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

An activity coefficient is not a universal chemistry constant. Standard states differ between phases and conventions; ionic solutions can require electrochemical-potential treatment. A sign-correct calculation with unmeasured activities is not experimentally validated reaction direction or yield.

## Source provenance and rights

- [IUPAC Gold Book 5.0 — activity](https://goldbook.iupac.org/terms/view/A00115) — IUPAC term definition a=exp((μ−μ°)/RT), 2025 online Gold Book v5; individual term CC BY-SA 4.0 license
- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — Equilibrium, chemical potential and Gibbs relationship, 2025 online edition

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
