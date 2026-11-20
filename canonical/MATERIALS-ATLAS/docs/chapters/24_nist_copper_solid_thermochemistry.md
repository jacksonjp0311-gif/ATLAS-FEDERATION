# 24. Copper thermochemistry from a bounded publisher fit

**Source type:** NIST Chemistry WebBook SRD 69, copper condensed-phase Shomate coefficients (Chase 1998 compilation; data reviewed June 1977). **Inspection:** publisher HTML and selected display rows, 2026-11-12. **Status:** computational reproduction of a *compiled, fitted representation*; not a new calorimetry experiment. [Publisher record](https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS).

## Define the material and the quantity

The fitted solid-phase entry is for elemental copper, Cu (CAS 7440-50-8), not a named alloy or a particular lot. The independent variable is thermodynamic temperature **T in kelvin**. Its published fit applies to **298–1358 K**. The response quantities are molar heat capacity at constant pressure, Cp in J/(mol K); molar enthalpy relative to 298.15 K, H−H(298.15) in kJ/mol; and molar entropy S in J/(mol K). These are *thermodynamic compilation quantities*, not Hahn1's experimental thermal-expansion response and not generic engineering material constants.

## The numerical contract

Set t=T/1000 and evaluate the Shomate family with the publisher's selected solid coefficients:

- Cp=A+B t+C t²+D t³+E/t²
- H−H(298.15)=A t+(B/2)t²+(C/3)t³+(D/4)t⁴−E/t+F−H
- S=A ln(t)+B t+(C/2)t²+(D/3)t³−E/(2t²)+G

[Public derivative: the source coefficient set is withheld pending NIST SRD69 redistribution clearance.] The coefficient precision shown by NIST is finite; it does not establish a coefficient covariance or combined material uncertainty budget.

[Public derivative: selected publisher display rows and their numerical reproduction results are withheld pending NIST SRD69 redistribution clearance. This comparison is unavailable in this edition.]

## A useful independent identity

For thermodynamic consistency within the fit, `dH/dT=Cp`, after the kJ-to-J conversion, and `dS/dT=Cp/T`. The v1 numerical oracle integrates Cp independently and differentiates the compiled expressions. It tests the mathematical implementation, not the empirical validity of the coefficients. [Public derivative: the dataset-derived numerical example is withheld pending redistribution clearance.] This is not a latent-heat measurement.

## Refusal and source boundaries

The calculator rejects a temperature outside 298–1358 K rather than extrapolating. It does not transition to the liquid coefficients at the solidus, infer alloy heat capacity from elemental copper, or treat this enthalpy series as thermal expansion. Report the phase, domain, units, reference state, source version, and coefficient-display precision with each result. A fit that matches rounded NIST rows can still be inappropriate for a real component with impurity, cold work, temperature gradients, or unknown service conditions.

**Cross-links:** Chapter 14 (temperature-dependent properties), Chapter 22 (fit residuals), Chapter 29 (decision ledger). `python -m materials_atlas v1-cases` reproduces the explicit published-row checks.
