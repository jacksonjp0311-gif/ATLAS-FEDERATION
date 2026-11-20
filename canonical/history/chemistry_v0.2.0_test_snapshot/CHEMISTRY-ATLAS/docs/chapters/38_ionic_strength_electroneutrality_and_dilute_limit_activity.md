# 38. Ionic strength, electroneutrality and dilute-limit activity

**Field:** Solutions · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Ionic strength quantifies a concentration-weighted effect of dissolved ionic charges on electrostatic screening. Multivalent ions contribute proportional to the square of charge number, so a small amount of highly charged species can matter more than an equal concentration of monovalent ions. The concentration-based definition is a simple weighted sum; it is not proof that a solution is electrically neutral, a particular phase is stable, or a metal is safe to dissolve. A model must report net charge imbalance separately, since a list of measured ions may be incomplete. The Debye–Hückel limiting law predicts an idealized leading behavior of logarithmic activity coefficients only at sufficiently low ionic strength and under a specified solvent and temperature. It must not be extrapolated into concentrated industrial electrolytes or process baths as though universally accurate.

## Equation and definitions

`I_c = 1/2 Σ_i c_i z_i². For the limiting-law illustration log10 γ_i ≈ −A z_i²√I, where A is a solvent- and temperature-specific supplied parameter.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

The square-charge weighting follows from the ionic screening model and charge symmetry in the linearized dilute electrostatic approximation. The model sums caller-provided molarity and formal charge numbers and separately computes Σ c_i z_i. A small nonzero imbalance may reflect unmeasured counterions or analytical uncertainty; large imbalance cannot be resolved by assuming missing ions have negative concentration. The limiting-law coefficient A varies with solvent dielectric and temperature; the reference deliberately requires it as an input and refuses concentrations above a declared illustrative dilute cap.

## Reconstruct without external AI

Construct a hypothetical 0.01 mol/L cation with z=+1 and 0.01 mol/L anion with z=−1. Then I=0.01 mol/L and the net charge is zero. Replace the cation with z=+2 while leaving the rest unchanged and show both increased ionic strength and nonzero apparent charge imbalance. The calculation must flag the missing electroneutrality evidence.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

The presence of a positive and negative ion is not sufficient evidence of solution speciation; hidden complexes, ion pairing and solvent reactions may matter. An IUPAC definition and a low-concentration mathematical law cannot guarantee a real industrial electrolyte's conductivity or safety.

## Source provenance and rights

- [IUPAC Gold Book 5.0 — ionic strength](https://goldbook.iupac.org/terms/view/I03180) — IUPAC concentration/molality ionic strength 1/2 Σ c z²; 2025 online term edition
- [IUPAC Gold Book 5.0 — activity](https://goldbook.iupac.org/terms/view/A00115) — IUPAC term definition a=exp((μ−μ°)/RT), 2025 online Gold Book v5; individual term CC BY-SA 4.0 license

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
