# Chapter 06. Thermodynamic models and phase stability

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A formation energy per atom subtracts compatible elemental reference energies from the total phase energy and divides by atom count. On a common energy scale, the lower convex envelope of candidate energies across composition yields a **relative 0 K stability ranking** for the *supplied competing phase set*. `E_above_hull` measures energy above that envelope. It does not determine kinetic accessibility, equilibrium at room temperature, chemical compatibility under humidity, or manufacturing cost.

The Materials Project’s formation-energy and hull documentation is explicit about zero-temperature electronic energies and about functional mixing. In particular, calculated entries from GGA, GGA+U and r2SCAN can require corrections before being placed in the same hull. The same composition’s computed energy can shift with model version, correction and database release. An uncorrected mixed-functional list is not a valid apples-to-apples competitor set.

**Toy hull:** if a binary end member has energy 0, a phase at x=0.5 has energy -0.40 eV/atom, and a candidate at x=0.3 is -0.18 eV/atom, the reference hull interpolation is -0.24; the candidate is 0.06 eV/atom above that *supplied* hull. A more favorable phase omitted from the database could lower the hull and change the result.

At finite temperature and pressure the relevant Gibbs free energy includes entropy and PV contributions. A zero-temperature electronic energy is not measured Gibbs free energy. Do not compare to a published calorimetric enthalpy without a thermodynamic conversion model, uncertainty and source harmonization. **The tool cannot claim synthesizeability.**

## Reference capsules for this chapter

- **Reference-consistent formation energy** (equation): E_f=(E_phase-sum(n_i*mu_i))/sum(n_i) in per-atom electronic-energy units, provided all references and corrections share a compatible basis.
- **Lower convex envelope of supplied phases** (method): A binary 0 K hull computes the lowest convex mixture of provided energies at composition x. Missing competing phases and corrected energy scales limit its use.
- **0 K DFT stability is not room-temperature Gibbs stability** (concept): Computed electronic energies usually omit temperature-dependent entropy and kinetic effects. Do not report 0 K energy-above-hull as a room-temperature measured equilibrium result.
- **Functional mixing requires correction consistency** (method): GGA, GGA+U and r2SCAN total energies cannot be blindly combined. The Materials Project documents compatibility and correction pipelines.
- **Database release can alter computed properties** (concept): Materials Project correction schemes and thermodynamic entries evolve. Preserve database version, calculation identifiers and correction model.

## Publisher portions used

[MP-PD](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds) · [MP-CALC](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details) · [MP-ENERGY](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability) · [MP-GLOSSARY](https://github.com/materialsproject/public-docs/blob/main/glossary-of-terms.md) · [MP-RELEASE](https://docs.materialsproject.org/changes/database-versions)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
