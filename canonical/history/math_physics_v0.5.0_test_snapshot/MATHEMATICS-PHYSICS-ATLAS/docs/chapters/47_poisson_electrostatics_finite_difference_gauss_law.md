# 47 — Reconstructing one-dimensional electrostatic Poisson equations and Gauss-law checks

**ATLAS FORGE v0.3.0.** An educational 1D constant-permittivity electrostatic boundary-value model, not a semiconductor process simulation, transistor compact model, charge transport model, physical measurement or certified high-voltage calculator. Reference: `poisson1d_dirichlet` and `tridiagonal_solve` in `math_physics_atlas/v03_models.py`.

## From a conservation law to a differential equation

For static electric fields, Maxwell-Gauss law in matter is \(\nabla\cdot\mathbf D=\rho_f\), where \(\mathbf D=\epsilon\mathbf E\) under a linear isotropic constitutive law and \(\mathbf E=-\nabla V\). When variation is only in x and epsilon is a positive constant, the governing equation becomes

\[
  -\epsilon\,\frac{d^2V}{dx^2}=\rho_f(x),\quad 0<x<L,
\]

with Dirichlet electrode potentials \(V(0)=V_L\) and \(V(L)=V_R\). Units: \(\epsilon\) F/m = C/(V·m), charge density \(\rho\) C/m³, V volt, x meter, E V/m and D C/m². The equation is only valid within its electrostatic, constant-dielectric, one-dimensional assumptions. Semiconductor charge density generally depends on mobile carriers and potential, requiring a *nonlinear coupled Poisson–transport or quantum system*, not this direct linear solve.

## Derivation of the centered finite-difference stencil

Let \(x_i=ih\) for i from 0 to N+1, with h=L/(N+1). Taylor expand smooth V around \(x_i\): \(V(x_i\pm h)=V_i\pm h V_i'+h^2 V_i''/2\pm h^3 V_i'''/6+h^4V_i^{(4)}/24+\cdots\). Adding the two expansions cancels odd terms. Thus \(V_i''\approx (V_{i-1}-2V_i+V_{i+1})/h^2\), with local truncation error of order h² when V has bounded fourth derivative. The discrete equation is

\[
 -V_{i-1}+2V_i-V_{i+1}=\frac{\rho_i h^2}{\epsilon}.
\]

Move the known boundary values into the first and last entries of the right-hand side; the unknown interior potentials solve a tridiagonal system with diagonal 2 and off-diagonal -1. Thomas forward elimination and back substitution take O(N) operations and O(N) storage. The positive-definite Dirichlet operator admits a unique discrete solution for epsilon>0. The solver refuses nonpositive epsilon, nonfinite values, invalid geometry, and pivots too small relative to scale.

## An exact manufactured charge-slab test

Choose uniform charge \(\rho(x)=\rho_0\) and arbitrary boundary potentials. Twice integrating gives

\[
  V(x)=V_L+(V_R-V_L)\frac{x}{L}+\frac{\rho_0}{2\epsilon}x(L-x).
\]

Because the centered second difference is *exact for a quadratic*, interior grid values should match that polynomial to roundoff, not merely to O(h²). For L=1 m, epsilon=1 F/m (deliberately artificial), rho=2 C/m³, and both boundaries zero, the solution is V(x)=x(1-x) volt, peaking at 0.25 V at the midpoint. These arbitrary teaching constants are **not** realistic vacuum permittivity or a validated device geometry. Run the same case using physical-scale epsilon with matching physically plausible charge values to verify unit arithmetic, without inferring a material's behavior.

## Discrete Gauss balance as a conservation check

Define face field \(E_{i+1/2}=-(V_{i+1}-V_i)/h\) and displacement \(D_{i+1/2}=\epsilon E_{i+1/2}\). Then \(D_{i+1/2}-D_{i-1/2}=h\rho_i\). Summing over all interior cells telescopes: \(D_{N+1/2}-D_{1/2}=h\sum_i\rho_i\). The implementation records the numerical Gauss balance residual separately from the maximum pointwise Poisson residual. This is a discrete identity of the assumed model. A tiny residual **does not** establish that true physical charge density, permittivity or boundary conditions were measured correctly.

For nonconstant smooth fields, use a manufactured sine potential V=sin(pi x/L), with rho=epsilon(pi/L)^2 sin(pi x/L). On grids N=15,31,63,127, the maximum error should decrease by approximately a factor of four each time h is halved. A failure of this refinement trend indicates an implementation or convergence problem.

## Why this is a semiconductor prerequisite, not a semiconductor simulator

A semiconductor must additionally model carrier statistics, band structure, dielectric interfaces, mobility, drift-diffusion currents, recombination, contacts and doping distributions. At equilibrium or under bias, rho can depend strongly on V and other fields. The Atlas's future Electronics & Semiconductors edition should use this verified finite-difference operator as a reference component and then introduce coupled constitutive laws and experimental validation; **do not silently relabel the present constant-epsilon slab as a diode or transistor**.

**External publisher orientation, not archived original files:** MIT OpenCourseWare Numerical Methods for PDEs, sections on Poisson and elliptic finite differences: https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/pages/lecture-notes/ and MIT's publicly linked course overview https://math.mit.edu/classes/18.336/index.html. No publisher PDF, source hash or reuse clearance is claimed by this chapter.
