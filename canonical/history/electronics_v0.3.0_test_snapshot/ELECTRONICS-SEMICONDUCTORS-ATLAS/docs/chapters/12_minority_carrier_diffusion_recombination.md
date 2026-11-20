# 12. Minority-carrier diffusion, recombination and discrete conservation

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Minority-carrier diffusion, recombination and discrete conservation. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`D u\x27\x27-u/τ=0; L_D=√(Dτ); F=-D du/dx; F_R-F_L+Σ_i (h u_i/τ)=0`

**Units:** m²/s, s, m, m⁻³, m⁻²s⁻¹. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

For low-level injected excess carrier density u(x), assume spatially uniform D>0, a fixed lifetime τ>0, no field and no generation. Continuity at steady state becomes D u''−u/τ=0 with injection/recombination boundary values u(0)=u_L, u(L)=u_R. The exact analytic solution is u(x)=u_L sinh((L−x)/L_D)/sinh(L/L_D)+u_R sinh(x/L_D)/sinh(L/L_D), L_D=sqrt(Dτ). For L/L_D≫1, compute ratios with scaled exponentials to avoid overflow.

On N equal cells, (2+h²/(Dτ))u_i−u_(i−1)−u_(i+1)=0. The tridiagonal matrix has positive diagonal and nonpositive off-diagonals and admits a positive inverse under the prescribed conditions. Summing its finite-volume continuity rows gives F_R−F_L+Σ h u_i/τ=0 exactly up to floating rounding. The boundary fluxes represent the carrier supply needed to balance bulk recombination.

## Independently executable algorithm

Reconstruct `minority_diffusion_profile` by Thomas elimination; confirm nonnegative interior for nonnegative boundaries and validate the telescoping flux balance independently of the tridiagonal residual. Compare each profile to the hyperbolic analytic solution. Double the grid from N=20 to 40 to 80 and check an approximately fourfold reduction in maximum interior error at fixed physical parameters.

## Worked scientific investigation

Choose D=0.002 m²/s, τ=10⁻⁷ s, L=10⁻⁵ m, u_L=1 normalized density and u_R=0.1. Compare N=20/40/80 discrete solutions against the analytic sinh solution. Report peak errors and net recombination and boundary fluxes with units. Changing τ changes L_D; a fitted lifetime cannot be inferred from an arbitrarily chosen synthetic profile.

## Failure conditions and counterexamples

The fixed-lifetime linear law is not valid for strong injection, nonlinear SRH/Auger/radiative recombination, field-assisted processes or spatially varying materials. Do not relabel exact numerical conservation as experimental calibration.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.
