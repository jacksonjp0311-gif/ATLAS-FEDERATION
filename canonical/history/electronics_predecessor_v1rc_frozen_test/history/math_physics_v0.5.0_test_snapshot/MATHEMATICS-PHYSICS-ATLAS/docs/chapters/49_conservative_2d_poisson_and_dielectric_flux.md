# Chapter 49 — Conservative 2D Poisson reconstruction and dielectric flux

**Edition:** ATLAS FORGE Mathematics & Physics v0.4.0. **Status:** original explanatory chapter, mathematically motivated finite-grid software reference; not experimentally calibrated.

## Reconstruction objective and prerequisites

Recover a two-dimensional approximation to electrostatic potential, given a positive scalar permittivity field, charge density and fixed boundary potentials. This directly supports future learning about electrostatic components, dielectrics and semiconductor-device potential solvers, but is **not** a semiconductor-device simulator. Prerequisites: SI units, gradient/divergence, Dirichlet boundary data, five-point differences, and linear algebra.

In a prescribed, static, linear isotropic material, **E** = −∇V and **D** = ε **E**. Gauss's constitutive statement ∇·**D** = ρ gives

\[
-\nabla\cdot(\epsilon(x,y)\nabla V)=\rho(x,y).
\]

ε has units F/m, V volts, E V/m, D C/m², ρ C/m³. A two-dimensional computational slice assumes invariance in the unmodeled third dimension; integrated area charge and perimeter displacement flux therefore have units **C/m per unit depth**, not total coulombs.

## Mesh and derivation

For a rectangle 0≤x≤Lx, 0≤y≤Ly with `nx × ny` unknown interior grid nodes, define `hx=Lx/(nx+1)` and `hy=Ly/(ny+1)`. Boundary nodes receive prescribed voltages. At an interior node P, approximate face permittivity by the harmonic mean `ε_E=2 ε_P ε_(i+1,j)/(ε_P+ε_(i+1,j))`, analogously W,N,S. Use centered face gradients; with positive scalar ε, each face weight is positive:

\[
 a_E=\epsilon_E/h_x^2,\quad a_W=\epsilon_W/h_x^2,\quad
 a_N=\epsilon_N/h_y^2,\quad a_S=\epsilon_S/h_y^2.
\]

The discrete equation is

\[
(a_E+a_W+a_N+a_S)V_P-a_EV_E-a_WV_W-a_NV_N-a_SV_S=\rho_P.
\]

Known boundary potentials are moved to the right-hand side as `+a_face*V_boundary`; the coefficient matrix retains its diagonal face weights. This is not the same as imposing a row of zeros for a boundary: the latter can destroy the intended SPD property of the **interior-only** matrix.

On shared interior faces, a single face coefficient appears symmetrically on both sides. For every nonzero interior vector x, the discrete energy is a sum of positive weighted neighbor differences plus positive boundary-face terms `a_face*x_P²`. With fixed Dirichlet data on all four sides, this establishes positive definiteness for the modeled operator (up to floating-point breakdown). No sign-indefinite nonlinear material response is admitted.

## Algorithm and data contract

Call `poisson2d_problem(nx,ny,Lx,Ly,epsilon,rho,boundary)` from `math_physics_atlas.v04_models`. `epsilon` and the boundary can be a finite numeric scalar, callable `(x,y)`, or full boundary-inclusive 2D node array. `rho` also accepts an interior-only array. The model explicitly checks shape, finite values, bounds, permittivity positivity and coefficient representation. Only grids 2–64 interior points along each axis, at most 4096 unknowns, are permitted in this reference implementation. The operator is applied matrix-free in O(nx*ny) memory and work per iteration.

A solved 2D field is stored as `(ny+2)×(nx+2)` row-major voltages with edge values preserved. Reproducibility requires the grid, physical lengths, ε field, ρ field, all four Dirichlet edges, solver tolerances and iteration limit; quoting only the matrix or a final plot is insufficient.

## Discrete Gauss accounting

With `F=-ε∇V`, the conservation statement is `∇·F=ρ`; summing interior discrete equations cancels interior-face fluxes. The total external flux per unit depth is the sum, over boundary-adjacent faces, of

\[
 F_{\rm outward}\,\Delta s=\epsilon_{\rm face}\,\frac{V_{\rm interior}-V_{\rm boundary}}{h_{\rm normal}}\,\Delta s.
\]

It must match `Σ ρ_(i,j) hx hy`, up to algebraic residual and roundoff. This checks **discrete charge accounting**, not physical accuracy or actual boundary-charge measurement.

## Worked investigation

Take `Lx=Ly=1 m`, `ε=1 F/m` (deliberately mathematical rather than a realistic material), four zero-voltage boundaries, and `ρ(x,y)=2π² sin(πx)sin(πy) C/m³`. The exact continuum solution is `V=sin(πx)sin(πy)` volts. The computer first assembles the discrete equation from the chosen mesh; solving that equation to a tiny residual still leaves a positive grid-truncation error. Chapter 51 measures the latter independently at four grid sizes.

## Failure cases, open physics, sources

Invalid ε≤0, NaNs, unsupported boundary types, wrong array shapes, overflow and excessive grid sizes are rejected. Zero-iteration or under-budget conjugate-gradient solves must *never* be marked scientifically converged. Neumann/periodic boundaries, anisotropic or nonlinear dielectric tensors, sharp curved interfaces, mobile charge carriers, traps, temperature effects, real device contacts, quantum corrections, time-dependent electrodynamics, experimental validation and semiconductor fabrication process data are outside scope.

**Source orientation only:** MIT OpenCourseWare 18.086 readings (finite differences, fast Poisson, conjugate gradients): https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/readings/ . Primary publisher document bytes not downloaded or rights-authenticated here. This chapter is original synthesis, not a copy of the course text.
