# Chapter 53 — Nonlinear elliptic equilibrium, discrete monotonicity and damped Newton

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Status:** original numerical-analysis exposition, executable finite reference, not experimental evidence.

## 1. Problem statement and exactly what the program solves

The numerical reference solves the one-dimensional **dimensionless** Dirichlet problem

\[
-\alpha\,u''(x)+\beta\sinh u(x)=f(x),\quad 0<x<\ell,\quad
u(0)=u_L,\;u(\ell)=u_R, \quad\alpha>0,\;\beta\ge0.
\]

Here `u` is a dimensionless normalized potential. `alpha`, `beta`, and `f` are stipulated dimensionless model inputs. They are not inferred permittivity, measured doping or contact parameters. This simple monotone equilibrium is a mathematically controlled *subproblem*, not a coupled electron-hole transport system. The code restricts `3<=n<=1024`, `|u|<=20` and other documented numerical ranges. Such limits are **software guards**, not physical constants.

At interior points `x_i=i h`, `h=ell/(n+1)`, central differencing gives

\[
F_i(\mathbf u)=\frac{\alpha}{h^2}(2u_i-u_{i-1}-u_{i+1})
+\beta\sinh(u_i)-f_i=0.
\]

The boundary values occupy the missing `u_0` and `u_{n+1}` positions. The assembled Jacobian is tridiagonal:

\[
J_{ii}=2\alpha/h^2+\beta\cosh(u_i),\qquad
J_{i,i\pm1}=-\alpha/h^2.
\]

A finite-domain Jacobian is symmetric positive definite under the stated positive `alpha`, nonnegative `beta` and Dirichlet boundaries: its quadratic form is the weighted sum of squared first differences (including endpoints) plus a nonnegative diagonal contribution. This guarantees a uniquely solvable **Newton linear step**, not convergence of an undamped Newton iteration from arbitrary starting conditions.

## 2. Controlled Newton globalization

Each iteration constructs a true nonlinear residual, solves `J Δu = -F`, and searches for a step `lambda=1,1/2,...,2^-25` that reduces the maximum residual while keeping `|u|<=20`. A successful step updates `u`; otherwise the routine reports `line_search_failed`. Exceeding the iteration budget yields `maxiter_exceeded`, never an invented converged state. The output includes `iterations`, `residual_linf`, a stated tolerance and the count of rejected line-search steps.

The initial state is the linear interpolation between the two Dirichlet endpoints. Linear solves use a small pure-Python tridiagonal elimination. `rtol`/`atol` bound the **algebraic nonlinear equation residual** in the supplied normalization. They do not bound the error in true physical voltage without an independently specified dimensional model.

## 3. Flux balance is a second, separate observable

Summing the discrete equation over `i=1..n` and multiplying by `h` telescopes the interior differences:

\[
\underbrace{\alpha\frac{u_1-u_L}{h}}_{\text{left outward flux}}
+\underbrace{\alpha\frac{u_n-u_R}{h}}_{\text{right outward flux}}
+\beta h\sum_{i=1}^{n}\sinh(u_i)
=h\sum_{i=1}^{n}f_i.
\]

A deviation from this discrete balance signals an implementation or algebraic-solve defect. A *small* balance residual is not evidence that the continuum model or material parameters match nature.

## 4. Independent reference investigations

1. **Exact constant state.** Choose `u_L=u_R=c` and `f_i=beta*sinh(c)`. Because all second differences vanish, the exact discrete solution is `u_i=c`. This tests boundary handling and the nonlinear term.
2. **Exact linear state.** With `beta=0`, `f=0`, any affine interpolation is the exact discrete solution. This detects incorrect endpoint signs.
3. **Continuum manufactured sine.** Take `u*(x)=sin(pi*x)` on `ell=1`, homogeneous endpoints and `f(x)=alpha*pi^2*sin(pi*x)+beta*sinh(sin(pi*x))`. The solved grid should approach the **continuum** field at second order; this tests spatial truncation rather than only convergence of Newton's method.
4. **Deliberate non-convergence.** Set `maxiter=1` on a nontrivial profile. Return `converged=false` and the original residual; do not label the tentative iterate a physical prediction.

The source tree ships all four tests, an additional randomized SciPy root comparison, and an independent Decimal/quad oracle for the adjacent exponential-fit kernel.

## 5. Counterexamples and scope restrictions

A converged nonlinear solve can still represent the wrong physical carrier statistics. Degenerate semiconductors require Fermi–Dirac treatment; depletion approximations, interface traps, contact barriers, temperature variation and quantum confinement can all invalidate a simple symmetric `sinh(u)` closure. Even for this mathematical equation, a tiny residual at a coarse grid does not establish a small continuum error. Deliberately keep these distinct: **implementation**, **discrete solution**, **continuum approximation**, **physical model**, **experimental observation**.

**Source navigation (not authenticated full texts):** TU Wien semiconductor equations, https://iue.tuwien.ac.at/phd/sharma/node-The-Basic-Semiconductor-Equations.html ; COMSOL semiconductor theory and solver convergence, https://www.comsol.com/support/learning-center/article/improving-convergence-of-semiconductor-models-69861 . This chapter is independently authored; no external source PDF was acquired, copied, or authenticated.
