# 61. Diffusion, mass transport and numerical stability

**Theme:** Materials transport · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Materials processing is controlled partly by species transport across gradients. A foundational continuum model is Fickian diffusion, relating flux to concentration gradient and a diffusivity. In a finite material, boundary conditions and temperature-dependent diffusivity can dominate the predicted profile. An explicit finite-volume model can conserve a stipulated total amount while violating physical plausibility if its time step is unstable. The existing Atlas demonstrates zero-flux finite diffusion with a Courant-style bound. Such a toy model is useful for verifying mathematical transport but not for choosing a semiconductor doping schedule or handling reactive materials.

## Governing relationship and dimensional conventions

`J=-D dc/dx; partial c/partial t=D partial² c/partial x²; explicit stable model D dt/(dx²)≤1/2 in the stated 1D scheme.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

Fick's first law states flux is proportional to the negative gradient. Conservation of species produces the time-dependent diffusion equation when D is constant. A discretized central second derivative leads to an explicit update involving neighboring cells. Positivity and nonoscillatory stability require a time-step restriction, while zero-flux boundaries preserve the integrated quantity in the ideal discrete model. Actual chemical potentials, electrostatic migration, interface reactions, and stress-assisted diffusion alter transport beyond this simplified law.

## Original worked investigation

Set a finite one-dimensional mesh with a localized initial concentration pulse. Evolve it under no-flux boundaries and verify that total modeled moles per area remain unchanged to numerical tolerance. Then repeat with an invalid time step and confirm the reference refuses it rather than reporting a physically meaningless profile.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

No real diffusivity data or silicon fabrication/etching conditions are provided. Numerical mass conservation is necessary but not sufficient for validating material diffusion.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/)
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
