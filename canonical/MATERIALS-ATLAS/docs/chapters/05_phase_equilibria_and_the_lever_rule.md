# Chapter 05. Phase equilibria and the lever rule

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A phase diagram represents equilibrium constraints under specified pressure, temperature and composition. Solvus, liquidus and solidus boundaries are not interchangeable. An equilibrium phase diagram does not guarantee a rapidly cooled or diffusion-limited sample has reached the predicted state. Metastability, nucleation barriers, microsegregation and finite rate introduce kinetics that this first edition does not solve.

Within a binary two-phase tie line with compositions `C_alpha` and `C_beta`, an overall composition `C0` has `f_beta=(C0-C_alpha)/(C_beta-C_alpha)` and `f_alpha=1-f_beta`. Every composition must use the *same mass- or mole-fraction basis* and tie line at the same temperature and pressure. This arithmetic is a conservation statement conditional on only the two specified phases. A third phase or incompatible bases invalidates it.

NIST’s solidification lever-rule material explicitly assumes complete diffusion in the equilibrium stepping model. It is therefore not an automatic prediction of as-cast microstructure. If measured phase fractions disagree, first inspect thermal history and tie-line source before claiming that conservation failed.

**Counterexample:** the overall composition lies outside the chosen tie endpoints, making one computed fraction negative. The calculator rejects this rather than hiding the extrapolation. Near-identical endpoints imply an unstable denominator and large sensitivity to composition uncertainty; do not rely on the fractions alone for acceptance.

## Reference capsules for this chapter

- **Equilibrium diagrams do not ensure equilibrium specimens** (concept): A phase diagram requires specified conditions and equilibrium assumptions. Thermal history and kinetics can keep actual phases away from equilibrium predictions.
- **Binary two-phase lever rule** (equation): Given two endpoints on one tie line and a composition between them, the beta fraction is (C0-Ca)/(Cb-Ca). Compositional bases must match.
- **Out-of-range tie lines must be rejected** (method): Negative phase fractions indicate incompatible inputs or extrapolation, not a physical negative amount of material. Missing phases and nonequilibrium render the model inapplicable.

## Publisher portions used

[NIST-LEVER](https://www.ctcms.nist.gov/~kattner/solidifc/lever.html) · [MP-PD](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
