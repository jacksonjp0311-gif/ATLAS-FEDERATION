# 04. Abrupt p-n junction potential and depletion width

**ATLAS FORGE / Electronics & Semiconductors v0.1.0 — original source-linked reconstruction**

Evidence class: original educational technical synthesis; finite software checks on constructed inputs. **Not laboratory data, chip fabrication, industrial qualification or independent scientific peer review.**

## Physical or mathematical statement

V_bi=V_T ln(N_A N_D/n_i^2); W=sqrt((2*epsilon/q)*(1/N_A+1/N_D)*(V_bi-V_a)).

The model requires consistent sign conventions, material parameters, boundary conditions and SI units. Every symbol must be tied to a physical definition: V, m, m^-3, F/m. Units are integral to the mathematical model; converting from centimeters to meters without transforming carrier densities changes predicted results by powers of ten.

## Reconstructing the method

built_in_potential and depletion_width in physical SI units.

A future researcher should first recover the SI definitions, verify finite numerical reference cases, write a minimal implementation using only standard arithmetic, check limiting behavior against an independent analytic calculation and then introduce measurements with a traceable calibration budget. Validate internal consistency (charge, current, units, positivity, conservation) before fitting unknown parameters.

## Assumptions and boundaries

Depletion approximation ignores finite junction grading, interface traps, degeneracy, injection and breakdown; V_bi-V_a must be positive.

Computational correctness is the lowest evidence tier. A scientific device model additionally requires known material properties, geometry, temperature, boundary conditions and calibrated measurements. In a full carrier-transport model, diffusion and drift compete; a small solver residual is not proof of an accurate continuous physical model. Edge cases can violate equilibrium, Boltzmann statistics, continuum transport, ideal contacts or neglected parasitics.

## Worked reconstruction exercise

Reimplement the relevant function in `electronics_atlas/models.py` from the equation rather than copying the output; compare with a second analytic form, boundary limit or independent arithmetic oracle. Repeat with input scaled by powers of ten and record which quantities have units and which are dimensionless. Every example is constructed and records no real wafer or circuit observation.

## Source and provenance

Reference card: `OPENSTAX-DEVICES`. Original publisher documents are **not** preserved locally in this edition. Linked sources are bibliographic orientation; the derivation and wording of this chapter are authored for ATLAS FORGE. Independent source-to-formula review and external hardware validation remain uncompleted gates.

## Cross-domain dependencies

- Mathematics & Fundamental Physics: charge, fields, differential equations and uncertainty
- Chemistry and Materials: impurities, defects, dielectric materials, carrier concentrations
- Computation and Energy: Boolean semantics, switching energy, reliability constraints

**Failure rule:** If an assumption or required unit is unknown, mark the numerical prediction unvalidated instead of treating a plausible number as physical evidence.
