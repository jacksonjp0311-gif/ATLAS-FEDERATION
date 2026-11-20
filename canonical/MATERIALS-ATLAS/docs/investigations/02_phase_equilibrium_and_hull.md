# Investigation 02 — Two different concepts of “stable”

**Evidence type:** Original fictitious binary-system model. External references: [NIST lever-rule assumptions](https://www.ctcms.nist.gov/~kattner/solidifc/lever.html) and [Materials Project phase diagram method](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds).

## Part A: an equilibrium tie line
Suppose, at a specified but otherwise fictional equilibrium temperature and pressure, an alloy has `C0=0.40` fraction of component B, and two coexisting phases are `C_alpha=0.20` and `C_beta=0.70` on the same mass-fraction basis. Conservation gives `f_beta=(0.40-0.20)/(0.70-0.20)=0.40` and `f_alpha=0.60`. These fractions are conditional on the existence of this *two-phase equilibrium state*. The result is not a cooling curve or an experimentally measured micrograph.

If a second source provides mole fractions instead of mass fractions, the calculator is not authorized to combine them directly. If a third phase is present or rapid cooling prevents complete diffusion, the lever rule does not predict the actual as-manufactured phases.

## Part B: a computational reference hull
A separate artificial model defines electronic energies for A at xB=0 as `0 eV/atom`, AB at xB=0.5 as `−0.40 eV/atom`, and B at xB=1 as `0 eV/atom`. A hypothetical candidate at xB=0.3 is `−0.18 eV/atom`. The binary lower hull at that composition is `−0.24 eV/atom`, making its distance above the supplied hull `+0.06 eV/atom`.

This is **not** the same calculation as the finite-temperature lever rule: the hull is a relative ranking on the specified 0 K electronic-energy scale among supplied candidates. It does not tell us a furnace's equilibrium phase fraction, a material's actual Gibbs free energy at service temperature, or a sample's cooling kinetics.

## Structural counterexample
If an omitted new phase at the same composition is found with electronic energy `−0.30 eV/atom`, the previous hull is incomplete and the relative stability calculation must be recomputed. The old `+0.06` result was correct for its *input set* but not necessarily for the completed system. A candidate below a supplied hull is flagged as evidence the reference list needs expansion; it is not an impossible negative physical energy.

## Evidence and decision
A valid computational phase claim must declare model/functional, corrections and database version, structure IDs, competing-phase coverage, energy normalization and temperature. Materials Project documents corrections for mixed exchange-correlation schemes; the initial numbers in this investigation are fabricated and not its database entries. The method must not be used to certify synthesis feasibility or real equilibrium without more evidence.
