# Materials Atlas teaching casebook · 0.1.0

**The 11 cases are entirely original constructed examples**, not published experimental measurements or newly performed material calculations. Their purpose is to teach conditional formulas and explicit refusal behavior. Run `python -m materials_atlas casebook` for numeric values, assumptions and assertions.

1. **Unit-cell density:** Calculate ideal cubic-cell density from invented lattice and site inputs; warn that physical porosity invalidates direct bulk interpretation.
2. **Indexed diffraction:** Convert an illustrative full `2θ` value to `d`; refuse to identify phases from one peak.
3. **Two-phase tie line:** Apply the lever rule for ordered compositions on one declared equilibrium tie line.
4. **Free thermal expansion mismatch:** Produce microstrain, not fabricated interface stress.
5. **Engineering tensile point:** Calculate one stress and strain pair; do not claim yield or modulus.
6. **Two-phase scalar mixture:** Compare iso-strain and iso-stress moduli, not validated composite properties.
7. **Formula energy:** Subtract declared same-scale elemental references and normalize per atom.
8. **Synthetic convex hull:** Compute energy above a supplied binary phase set, not synthesis viability.
9. **Missing competing phase:** Detect a candidate lying below the prior supplied-phase hull; signal incomplete reference set.
10. **Method/origin refusal:** Reject property arithmetic between measured and computed entries even when units match.
11. **Outside two-phase region:** Reject a tie-line composition that would yield a negative phase fraction.

Every case returns `origin=synthetic_authored_teaching` and `not_real_material_validation=true`. No external DFT job or laboratory work has been performed.

## Worked investigations

- [Diffraction And Identity](investigations/01_diffraction_and_identity.md)
- [Phase Equilibrium And Hull](investigations/02_phase_equilibrium_and_hull.md)
- [Tensile Property Context](investigations/03_tensile_property_context.md)
- [Thermal Interface And Selection](investigations/04_thermal_interface_and_selection.md)


## v0.2.0 additional worked tests

`python -m materials_atlas advanced-cases` executes nine cases: one numerical replay of NIST's published Hahn1 observations plus eight author-constructed examples or explicit refusals. This command does not fit the Hahn1 model, perform real material tests or approve a design. `python -m materials_atlas published-hahn1` provides the complete scientific qualifiers and certified comparisons. For optional two-algorithm numerical refitting run `python tools/hahn1_oracle.py` with NumPy and SciPy.


## v1.0.0 — publisher numerical checks and bounded original models

Eight cases are available through `python -m materials_atlas v1-cases`. Case 1 uses six selected two-decimal NIST copper thermochemistry publisher rows, comparing three quantities per row; the seven other cases are original analytical or synthetic model checks. No new laboratory observations. Full narrative and refusals: investigations 12–19.

| Case | Reproduced or bounded result | Inference forbidden |
|---|---|---|
| NIST copper Shomate | [Public derivative: source-dependent numerical comparison withheld pending SRD69 clearance] | Published solid-phase fit only; no alloy equivalence |
| Enthalpy fit | ΔH(400→900 K) ≈ 13.3665 kJ/mol | Latent heat or phase crossing |
| Coupon corrosion | 0.0467949 mm/y equivalent mean for hypothetical sample | Pit maximum or life |
| Layer conduction | R≈0.35005 K/W, Q≈142.8367 W in a hypothetical stack | Actual equipment surface temperature |
| Isothermal JMAK | Synthetic half-fraction at ≈832.55 s | Nonisothermal furnace recipe |
| Norton creep | Doubling stress gives 8× calculated steady rate when n=3 | Rupture-time prediction |
| Conditional Weibull | Assumed volume doubling gives S², only after explicit physical hypothesis | Empirical fitted Weibull size scaling |
| Input refusal | Invalid physical units/ranges produce errors | Interpreting rejected inputs as measurements |
