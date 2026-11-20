# Chapter 12. Decision ledger and cross-domain reuse

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A materials selection decision needs a target environment, design constraints, hazard context, availability, cost assumptions, validated property distribution and alternative candidates. A bounded Atlas reference can support this reasoning but cannot replace qualification testing. Define a decision before retrieving attractive data: What failure mode matters? Which property controls it? Which state and test are representative? What would change the result?

Treat knowledge as a versioned network of *claims with support and limits*, not a flat database of numbers. Phase stability depends on reference energies and assumed conditions; diffraction spacing depends on wavelength and reflection indexing; tensile stress depends on specimen geometry. The context compiler must keep those dependencies intact and refuse unsupported answers when qualifiers are missing.

Our repeated workflow is **discover → inspect → represent → reproduce → compare → qualify → reuse → revise**. The first Materials release includes no independently obtained original laboratory data, no actual phase identification, and no new external simulation. Its casebook deliberately separates invented inputs from published principles; counts of records or passing tests are not completeness metrics.

**Future scope:** CALPHAD and finite-temperature phase-field kinetics; quantitative diffusion and transformation; EBSD/XRD refinement; tensor mechanics and fracture; corrosion tests; microstructural images with rights; real benchmark datasets and uncertainties. These remain explicitly open rather than silently implied by twelve chapter titles.

## Reference capsules for this chapter

- **Selection requires service constraints** (method): Define environment, loads, aging, safety class, test standards, failure modes, cost and target before using tabulated material values.
- **Measurement and causal interfaces remain distinct** (concept): Materials owns conditional physical claims, Measurement owns calibration and uncertainty, Causal owns intervention effects, Manufacturing will own equipment-specific diagnosis.
- **Unknowns should travel with material claims** (method): When processing history, test basis or physical conditions are missing, context consumers must preserve uncertainty and abstain from certification.

## Publisher portions used

[NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system) · [MP-GLOSSARY](https://github.com/materialsproject/public-docs/blob/main/glossary-of-terms.md)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
