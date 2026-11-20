# Chapter 08. Thermal expansion and transport

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Thermal expansion is directional for many crystals and composites. A scalar approximation `delta_L/L = alpha delta_T` requires a defined interval and, for larger ranges, a justified temperature dependence. Two freely expanding materials with coefficients alpha_a and alpha_b differ in free thermal strain by `(alpha_a-alpha_b)delta_T`. That mismatch is not itself an interface stress: constraint, modulus, geometry and bonding determine stress.

Thermal conductivity, thermal diffusivity and heat capacity are distinct quantities. A tabulated conductivity cannot be converted to diffusivity without density and heat capacity on a compatible basis and at the same state. Electrical resistivity and conductivity are reciprocals only when units, temperature and the intended constitutive model are consistent; anisotropic behavior requires tensors.

NIST’s dimensional-metrology FAQ shows why gauge-material selection depends on expansion, thermal diffusivity, dimensional stability, wear and environmental conditions. A room-temperature expansion coefficient is not universally valid at cryogenic or elevated temperatures.

**Counterexample:** two mating components with mismatched thermal expansion can have significant free strain difference after heating but no predictable stress without an interface mechanics model. The new calculator reports strain only and refuses to invent stress or failure risk.

## Reference capsules for this chapter

- **Free thermal mismatch is not stress** (equation): A scalar free-strain mismatch equals (alpha_a-alpha_b) ΔT if expansion coefficients are constant. Actual stress requires constraint and mechanics.
- **Diffusivity, conductivity and heat capacity differ** (concept): Thermal diffusivity requires conductivity, heat capacity and density under consistent conditions. None is interchangeable without the model and units.
- **Transport can be anisotropic** (concept): Anisotropic crystals and textured parts require directional or tensor property data. Do not collapse a direction into an invariant scalar without rationale.

## Publisher portions used

[NIST-GAGE](https://emtoolbox.nist.gov/faq/faq.asp) · [NIST-RES](https://www.nist.gov/mgi/materials-data-resources)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
