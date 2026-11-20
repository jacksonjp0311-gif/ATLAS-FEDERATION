# Chapter 54 — Boltzmann equilibrium charge, thermal voltage and nondimensionalization

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Evidence status:** constructed models only. **Purpose:** preserve a reconstructible chain from electrostatics to a limited equilibrium charge closure.

## 1. Physical equation and sign conventions

An electrostatic potential `V` in volts gives electric field `E=-grad(V)`. In a uniform linear dielectric of permittivity `epsilon` in farads per metre,

\[
-\nabla\cdot(\epsilon\nabla V)=\rho
= q\,[N_D^+-N_A^-+p-n],
\]

where `q>0` is elementary charge, `n,p` are electron and hole number densities (m^-3) and ionized dopants also have units m^-3. The carrier terms multiply charge `q` to yield C/m^3. The formula alone does not determine `n,p`; separate carrier statistics and continuity/transport laws are necessary. A solver that takes `rho` as independently specified has **not yet coupled** mobile charge self-consistently.

In a simplified, nondegenerate, isothermal equilibrium with a common reference concentration `n0`, one may stipulate

\[
U_T=k_B T/q,\qquad u=V/U_T,\qquad
n=n_0e^u,\quad p=n_0e^{-u},
\]

so `p-n=-2n0*sinh(u)`. The charge equation is then

\[
-\epsilon U_T u_{xx} +2qn_0\sinh u=qC(x),\qquad C=N_D^+-N_A^-.
\]

This is a **special equilibrium closure** at fixed temperature and specified reference statistics. Real semiconductor electron and hole densities depend on band edges, quasi-Fermi levels, contact conditions, and temperature. The two exponentials are not a complete semiconductor device model.

## 2. Nondimensionalization before coding

Choose a positive reference length `L0`, normalized coordinate `x*=x/L0`, and an arbitrary positive reference charge-density scale `rho*` (C/m^3). Divide the previous equation by `rho*`:

\[
-\alpha\,\partial_{x*}^2u +\beta\sinh u=f(x*),\quad
\alpha=\frac{\epsilon U_T}{\rho_* L_0^2},\quad
\beta=\frac{2qn_0}{\rho_*},\quad
f=\frac{qC}{\rho_*}.
\]

All three coefficients are now dimensionless, as assumed by the standalone Python kernel. The code's `length` is the length in units of `L0`, not raw metres; using dimensional `epsilon` directly as `alpha` is an error. To return to physical voltage, multiply the dimensionless result by `U_T`. To return to electric field, compute `-U_T/L0` times the dimensionless gradient. The v0.5 software **does not automate this physical conversion** because it has no authenticated material parameters or calibration.

## 3. Worked constructed problem

Let `ell=1`, `alpha=1`, `beta=0.4`, `u_L=u_R=0`. Select the exact continuum field `u*(x)=sin(pi*x)`. Its source is

\[
f(x)=\pi^2\sin(\pi x)+0.4\sinh(\sin(\pi x)).
\]

Discretize by the centered second difference, solve the nonlinear system with damped Newton, and compare every interior node against the known `u*(x_i)`. Halving the grid spacing should reduce the leading second-order truncation error by approximately four, **when the nonlinear residual is sufficiently small**. This uses a manufactured forcing—not a measured doping distribution—and cannot validate an external sample of silicon.

## 4. Energy and uniqueness of the discrete model

The finite-dimensional objective

\[
\mathcal{E}(u)=\frac{\alpha}{2h^2}\sum_{i=0}^{n}(u_{i+1}-u_i)^2
+\beta\sum_{i=1}^n\cosh u_i-\sum_{i=1}^n f_i u_i
\]

has interior gradient equal to the finite-difference equation, with Dirichlet endpoints held fixed. Its Hessian is the SPD Jacobian from Chapter 53. This provides a useful *mathematical* structure and a clean numerical diagnostic. Energy minimization does not make the assumed carrier-density closure experimentally correct.

## 5. Missing experiment and uncertainty ledger

To use the numerical kernel for a physical semiconductor, a future researcher must establish material composition and phase, dopant activation, carrier temperature, charge trapping, relative dielectric function and uncertainty, boundaries/contacts, band structure and the density-of-states regime. Measured I–V curves, C–V curves or spatial profiles require authentic instrument calibration, uncertainty estimates and independently reproduced fit diagnostics. This reference contains none of those measurements.

**Source navigation only:** TU Wien, https://iue.tuwien.ac.at/phd/sharma/node-The-Basic-Semiconductor-Equations.html ; COMSOL semiconductor interface documentation, https://doc.comsol.com/6.4/doc/com.comsol.help.semicond/semicond_ug_semiconductor.6.02.html . No original publisher transport bytes or approved offline mirror are included.
