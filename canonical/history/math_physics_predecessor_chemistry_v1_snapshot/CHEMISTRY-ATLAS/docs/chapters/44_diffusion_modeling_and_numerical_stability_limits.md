# 44. Diffusion modeling and numerical stability limits

**Field:** Transport · **Version:** v0.2.0 · **Scientific status:** original educational reference; cited publisher portions inspected, original publisher bytes not archived. No real experiment.

## Principles and physical scope

Diffusion couples microscopic transport to concentration gradients, making it relevant to corrosion, mixing, materials aging and semiconductor processing. Fick's first law is a constitutive approximation for one species in a medium under defined conditions; the coefficient D can depend strongly on temperature, composition, phase, defects and electric fields. A finite-volume discretization can demonstrate how concentration profiles spread while conserving total amount under no-flux boundaries. But a stable numerical result is not proof of a calibrated diffusivity or the absence of side reactions. Scientific continuity requires the governing equation, boundary conditions, grid resolution, time-step stability criterion, initial profile and a separate record of how D was measured.

## Equation and definitions

`J=−D∂c/∂x, ∂c/∂t=D∂²c/∂x². Explicit 1D timestep requires λ=DΔt/(Δx)²≤1/2 for the simplest uniform diffusion scheme.`

Inputs and reference states must be declared. The algebra alone cannot establish source data validity, experimental behavior or physical safety.

## Derivation and why the relationship holds

Integrate conservation on each cell and approximate fluxes through faces; with constant D and equal spacing, the update is c_i^(new)=c_i+λ(c_(i−1)−2c_i+c_(i+1)). For reflective zero-flux boundaries, the edge neighbor is replaced by the boundary cell's own concentration. Internal face fluxes cancel pairwise when summing every cell, providing an exact discrete conservation invariant up to roundoff. The coefficient λ≤1/2 gives nonnegative convex weights in 1D; exceeding it can produce oscillatory or negative numerical values even though the PDE is diffusive.

## Reconstruct without external AI

Initialize five abstract cells [0,0,1,0,0] mol/m³, set Δx=1 m and D=0.1 m²/s, and advance with Δt=1 s for 20 steps. Verify total integral remains 1 mol/m². Then try Δt=10 s: the library should refuse the unstable coefficient rather than silently produce misleading concentrations.

These examples are invented, not laboratory readings. Reproduce them by hand and compare only within the declared model domain.

## Failure case and missing evidence

No real fabrication furnace, diffusion depth, thermal budget, or wafer contamination is inferred. Complex interfaces, non-Fickian transport, moving phases and source terms require different models and validated material parameters.

## Source provenance and rights

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — Uncertainty and calibration scope for reconstructed measurements

**Not retained:** original publisher documents, real chemical samples, source tables and independent domain review.
