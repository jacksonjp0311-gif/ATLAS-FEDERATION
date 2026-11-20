# Chapter 44: Wave equation, leapfrog propagation and electromagnetic scope

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `u_tt=c²u_xx; uᵢⁿ⁺¹=2uᵢⁿ−uᵢⁿ⁻¹+λ²(uᵢ₋₁ⁿ−2uᵢⁿ+uᵢ₊₁ⁿ), λ=cΔt/Δx≤1.`

**Reference algorithm:** `math_physics_atlas.v02_models.wave1d_dirichlet(displacement, c, dx, dt, steps)`

**Units:** displacement u [application units], wave speed c [m/s], x [m], t [s]; Courant cΔt/Δx dimensionless.

## Field equations and their reduction
A one-dimensional scalar wave u_tt=c²u_xx represents transverse-string displacement, simple acoustic potential or a component of a propagating field only under additional assumptions. Maxwell's equations in a homogeneous source-free vacuum give ∇×E=−∂B/∂t and ∇×B=μ₀ε₀∂E/∂t. Taking the curl of Faraday's law and applying ∇×(∇×E)=∇(∇·E)−∇²E with ∇·E=0 yields ∂²E/∂t²=c²∇²E, c=1/√(μ₀ε₀) in the vacuum constitutive model. The reduction is not equivalent to validating a full electromagnetic solver: vector polarizations, boundary conditions, sources and material constitutive laws have been removed.

## Centered-time and centered-space stencil
Approximating the second time derivative by (uᵢⁿ⁺¹−2uᵢⁿ+uᵢⁿ⁻¹)/Δt² and second spatial derivative by (uᵢ₋₁ⁿ−2uᵢⁿ+uᵢ₊₁ⁿ)/Δx² gives the leapfrog update. To initialize with zero velocity, Taylor-expand u(x,Δt)=u(x,0)+(Δt²/2) c²u_xx(x,0)+O(Δt³); the first discrete step carries half the spatial second-difference coefficient. A Fourier mode e^(ik iΔx) has amplification governed by cos(ωΔt)=1−2λ²sin²(kΔx/2). Real ω for all resolved modes requires λ=cΔt/Δx≤1. A bound on grid growth is not a validation of physical boundary reflections.

## Worked eigenmode with real units
For a length-L region with u=0 at each endpoint, u(x,0)=sin(πx/L) and u_t(x,0)=0, separation of variables gives u(x,t)=sin(πx/L)cos(cπt/L). With L=1 m, grid Δx=1/40 m and λ=0.5, evolve 40 discrete steps and compare against the analytic field. The small phase error should reduce with refinement. Change λ to 1.1: the code must reject the step before producing unbounded numerical oscillations. A separate oracle compares 100 randomized finite grids and wave speeds; there are no antennas, oscilloscopes or radiation measurements involved.

## Physical and numerical cautions
An actual FDTD Maxwell calculation would require staggered E and H components, consistent permittivity and permeability, source injection, absorbing boundaries, magnetic/electric energy checks, mesh convergence, and measured validation. At a material interface the simple constant-c wave equation is insufficient. Do not infer semiconductor device performance, radio transmitter range, or electromagnetic compliance from this scalar toy model. Explicitly preserve the numerical reduction and its limits.

## Technology continuity link
Understanding wave propagation and discrete stability is a prerequisite for reconstructing signal timing, acoustics, optics, radio and numerical field computation. This is a teachable foundation, not a production field simulator.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010](https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Scalar 1D wave with fixed-zero ends and zero initial velocity; not a Maxwell field solver, transmission-line impedance model, or radiation prediction.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
