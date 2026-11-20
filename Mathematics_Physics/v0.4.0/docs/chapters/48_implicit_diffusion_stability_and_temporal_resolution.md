# 48 — Implicit diffusion, unconditional linear stability and temporal-resolution failure cases

**ATLAS FORGE v0.3.0.** Original instructional derivation and pure-Python implementation: `implicit_heat1d_dirichlet` and `tridiagonal_solve`. These are one-dimensional constant-coefficient model computations under fixed temperatures, not experiments on heated materials or validated semiconductor thermal models.

## PDE, units and boundary data

Take the heat/diffusion model \(u_t=\alpha u_{xx}\), where x is position [m], t is time [s], u can represent temperature [K] in a simple conduction model, and alpha is constant thermal diffusivity [m²/s]. With a uniform grid \(x_i=ih\), \(t^n=n\Delta t\), define the dimensionless Fourier number \(r=\alpha\Delta t/h^2\). In an explicit forward-time centered-space method, high spatial frequencies are stable only if \(r\le 1/2\) under the standard 1D Dirichlet assumptions. Implicit methods relax this **stability** restriction but still need time-step refinement for **accuracy**.

## Backward Euler as a tridiagonal implicit system

Using the new-time spatial derivative yields

\[
 \frac{u_i^{n+1}-u_i^n}{\Delta t}=\alpha\frac{u_{i-1}^{n+1}-2u_i^{n+1}+u_{i+1}^{n+1}}{h^2}.
\]

Rearrange to \(-r u_{i-1}^{n+1}+(1+2r)u_i^{n+1}-r u_{i+1}^{n+1}=u_i^n\). Add the fixed boundary contributions to the first/last right-hand sides. The tridiagonal matrix has positive diagonal 1+2r, negative off-diagonal -r, and is strictly diagonally dominant for r>0. It is therefore nonsingular. For a discrete Fourier sine mode with Laplacian eigenvalue \(\lambda_d=-4\sin^2(\pi k/(2N))/h^2\), the amplification is \(G_{BE}=1/(1+4r\sin^2(\pi k/(2N)))\), lying in (0,1] for nonnegative r. Large r strongly damps even modes that may physically persist over a shorter time; numerical stability is not temporal accuracy.

## Crank–Nicolson midpoint averaging

Average the spatial operator between the old and new states:

\[
 \frac{u_i^{n+1}-u_i^n}{\Delta t}=\frac\alpha2\left[(D_{xx}u^{n+1})_i+(D_{xx}u^n)_i\right].
\]

Rearrange to \(-\frac r2u_{i-1}^{n+1}+(1+r)u_i^{n+1}-\frac r2u_{i+1}^{n+1}=(1-r)u_i^n+\frac r2(u_{i-1}^n+u_{i+1}^n)\). The amplification for a discrete sine mode is \(G_{CN}=(1-2r\sin^2(\pi k/(2N)))/(1+2r\sin^2(\pi k/(2N)))\). Its magnitude is ≤1 for all r≥0, but the numerator becomes negative at sufficiently large r, giving alternating signs in stiff high-frequency modes. **Unconditional linear stability does not imply monotonicity or freedom from nonphysical oscillations.** Backward Euler is first-order accurate in time; Crank–Nicolson is second-order for smooth solutions and fixed time steps, subject to regularity and boundary compatibility.

## Manufactured eigenmode benchmark

With fixed-zero boundaries on [0,L], choose \(u(x,0)=\sin(\pi x/L)\). The continuum solution is \(u(x,t)=e^{-\alpha(\pi/L)^2 t}\sin(\pi x/L)\). For a grid with N intervals, the **discrete** lowest sine eigenvalue has magnitude \(4\sin^2(\pi/(2N))/h^2\). Thus, after k steps, the numerical solution should equal the initial discrete sine multiplied by \(G_{BE}^k\) or \(G_{CN}^k\), to rounding error. This isolates implementation correctness from the difference between the discrete and continuous eigenvalues. Compare time-step refinements against the continuum exponential to assess truncation separately.

## Boundary and engineering cautions

The kernel preserves the endpoint values exactly, refuses negative diffusivity and nonfinite inputs, and caps grid size, time steps and Fourier number. It does not model radiation, convection, interface conditions, temperature-dependent properties or heat generation. A slab used to explain processor or transistor heating requires measured thermal properties, multilayer 2D/3D geometry, interface resistance and calibration. A signal that appears physically smooth can still be wrong if an invalid boundary was supplied. This edition's tests are generated numeric trajectories only, not a physical temperature trace.

**Bibliographic orientation only:** MIT OpenCourseWare Numerical Methods for PDEs includes time stepping, stability, heat equations and implicit methods: https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/pages/lecture-notes/. No original publisher files are authenticated or mirrored.
