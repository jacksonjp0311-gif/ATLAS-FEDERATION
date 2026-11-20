# 02. Doping, equilibrium carrier mass action and intrinsic concentration

**ATLAS FORGE / Electronics & Semiconductors v0.1.0 — original source-linked reconstruction**

Evidence class: original educational technical synthesis; finite software checks on constructed inputs. **Not laboratory data, chip fabrication, industrial qualification or independent scientific peer review.**

## Physical or mathematical statement

n-p=N_D-N_A; n*p=n_i^2; n=(D+sqrt(D^2+4*n_i^2))/2 for D>=0.

The model requires consistent sign conventions, material parameters, boundary conditions and SI units. Every symbol must be tied to a physical definition: carriers m^-3. Units are integral to the mathematical model; converting from centimeters to meters without transforming carrier densities changes predicted results by powers of ten.

## Reconstructing the method

mass_action_carriers(net_doping_m3,intrinsic_concentration_m3) with stable minority concentration.

A future researcher should first recover the SI definitions, verify finite numerical reference cases, write a minimal implementation using only standard arithmetic, check limiting behavior against an independent analytic calculation and then introduce measurements with a traceable calibration budget. Validate internal consistency (charge, current, units, positivity, conservation) before fitting unknown parameters.

## Assumptions and boundaries

Assumes nondegenerate equilibrium, fully ionized dopants, no deep traps and a specified intrinsic concentration.

Computational correctness is the lowest evidence tier. A scientific device model additionally requires known material properties, geometry, temperature, boundary conditions and calibrated measurements. In a full carrier-transport model, diffusion and drift compete; a small solver residual is not proof of an accurate continuous physical model. Edge cases can violate equilibrium, Boltzmann statistics, continuum transport, ideal contacts or neglected parasitics.

## Worked reconstruction exercise

Reimplement the relevant function in `electronics_atlas/models.py` from the equation rather than copying the output; compare with a second analytic form, boundary limit or independent arithmetic oracle. Repeat with input scaled by powers of ten and record which quantities have units and which are dimensionless. Every example is constructed and records no real wafer or circuit observation.

## Source and provenance

Reference card: `OPENSTAX-DOPING`. Original publisher documents are **not** preserved locally in this edition. Linked sources are bibliographic orientation; the derivation and wording of this chapter are authored for ATLAS FORGE. Independent source-to-formula review and external hardware validation remain uncompleted gates.

## Cross-domain dependencies

- Mathematics & Fundamental Physics: charge, fields, differential equations and uncertainty
- Chemistry and Materials: impurities, defects, dielectric materials, carrier concentrations
- Computation and Energy: Boolean semantics, switching energy, reliability constraints

**Failure rule:** If an assumption or required unit is unknown, mark the numerical prediction unvalidated instead of treating a plausible number as physical evidence.
