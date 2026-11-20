# Chapter 43: Heat equation, diffusion stability and bounded temperature fields

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `∂T/∂t=α∂²T/∂x²; Tᵢⁿ⁺¹=(1−2r)Tᵢⁿ+r(Tᵢ₋₁ⁿ+Tᵢ₊₁ⁿ), r=αΔt/Δx²≤1/2.`

**Reference algorithm:** `math_physics_atlas.v02_models.heat1d_dirichlet(initial, alpha, dx, dt, steps)`

**Units:** x [m], t [s], thermal diffusivity α [m²/s], temperature difference [K]; Fourier number αΔt/Δx² dimensionless.

## Governing physical assumption
For a homogeneous medium with constant volumetric heat capacity and conductivity, Fourier conduction plus energy balance leads to ∂T/∂t=α∂²T/∂x², where α=k/(ρc_p) has units m²/s. For a nonuniform or phase-changing medium this simplified equation is no longer sufficient; additional material functions and boundary fluxes are required. The atlas kernel uses a temperature *difference* relative to a fixed-temperature reference so that both end points can be represented as zero without confusing 0 K with an ordinary room boundary.

## Finite-difference reconstruction
On a uniform grid xᵢ=iΔx, the centered approximation to ∂²T/∂x² is (Tᵢ₋₁−2Tᵢ+Tᵢ₊₁)/Δx². With forward Euler time stepping, define r=αΔt/Δx² and obtain Tᵢⁿ⁺¹=(1−2r)Tᵢⁿ+rTᵢ₋₁ⁿ+rTᵢ₊₁ⁿ. If 0≤r≤1/2, these are nonnegative weights summing to one. Each interior update is a convex combination, so a nonnegative initial profile with fixed-zero boundaries remains nonnegative and cannot generate a new maximum. This discrete maximum-principle argument both motivates the numerical stability limit and exposes a physical constraint test. It is stronger than merely looking for non-finite numbers.

## Exact separable manufactured solution
For T(x,0)=sin(πx/L), T(0,t)=T(L,t)=0, set T(x,t)=X(x)G(t) to obtain G′/G=αX″/X=−α(π/L)². Therefore T(x,t)=sin(πx/L)exp[−α(π/L)²t]. At L=1 m and α=0.1 m²/s, the center decays as exp(−0.1π²t). Sample N=40 intervals and r=0.25, integrate 60 steps, compare the whole numerical field with this continuous reference. The difference is discretization error; refining Δx while keeping r fixed should reduce it. An independent oracle checks 100 finite eigenmode cases.

## Negative controls
When r>1/2, a grid-scale alternating mode can grow with the explicit update even though the continuous heat equation smooths disturbances. The kernel rejects that region rather than delivering a plausible but unstable plot. It also rejects nonzero boundary values, inconsistent grid size, negative diffusivity and nonfinite inputs. A stable numerical profile does not validate the chosen k, ρ or c_p for an actual material; preserve empirical provenance separately.

## Technology continuity link
Diffusion models are useful for IC thermal design, process control, precision machining and battery management. Engineers must extend them to heterogeneous materials and real boundary conditions before applying results to equipment.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** One-dimensional constant-diffusivity linear conduction with fixed-zero Dirichlet boundaries only; refuses Fourier number >1/2. Not a calibrated materials-property or heat-transfer prediction.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
