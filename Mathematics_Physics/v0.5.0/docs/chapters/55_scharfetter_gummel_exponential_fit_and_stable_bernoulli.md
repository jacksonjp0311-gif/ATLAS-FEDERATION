# Chapter 55 — Scharfetter–Gummel exponential fitting and stable Bernoulli evaluation

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Focus:** a single conservative 1D flux edge, with an independently testable exact constant-field solution.

## 1. Why an ordinary centered flux can fail

For a simple nondegenerate carrier particle flux along a one-dimensional edge, stipulate

\[
J=-D\left(\frac{dn}{dx}-n\frac{du}{dx}\right),
\]

where `n>=0` is a number density (m^-3), `D>0` a diffusion coefficient (m^2/s), and `u` a dimensionless field potential. `J` has units m^-2 s^-1 (number per unit area per second). This is an **electron-like particle-flux sign convention**; an electron **electrical current** has the opposite sign and carries the charge multiplier. A hole flux uses a different sign convention. No contact or recombination model is assumed.

If `u` changes steeply across a cell, a centered difference in `n` and `u` may produce nonphysical oscillations or a failure to preserve exact thermal equilibrium. The Scharfetter–Gummel construction instead solves the local first-order differential equation exactly on a cell with **constant `D`** and a **linear `u` profile**.

## 2. Integrating-factor derivation

Let `h` denote cell-edge width and `delta=u_R-u_L`. Rearrange the flux equation as

\[
\frac{d}{dx}\big(n e^{-u}\big)=-\frac{J}{D}e^{-u}.
\]

Integrating from left to right with linearly interpolated `u(x)=u_L+delta*x/h` yields

\[
J=\frac{D}{h}\left[B(-\delta)n_L-B(\delta)n_R\right],
\quad B(z)=\frac{z}{e^z-1},\;B(0)=1.
\]

It follows algebraically that `B(-z)=B(z)+z`. With equal potentials, `delta=0`, the flux reduces to Fick's law `J=D(n_L-n_R)/h`. Under a local Boltzmann equilibrium `n_R=n_L*exp(delta)`, the two terms cancel **exactly in the mathematical formula**. Floating-point computations have roundoff, so tests require an explicit numeric tolerance.

## 3. Computing B(z) without avoidable overflow or cancellation

Directly computing `exp(z)-1` near zero loses significant digits. For `|z|<<1`, use the Taylor expansion

\[
B(z)=1-\frac{z}{2}+\frac{z^2}{12}-\frac{z^4}{720}+\frac{z^6}{30240}+O(z^8).
\]

For moderate `z`, use `expm1(z)` in the denominator. For large positive `z`, evaluate `z exp(-z)/(1-exp(-z))`; for large negative `z`, evaluate `-z/(1-exp(z))`. The v0.5 pure-Python implementation explicitly accepts `|z|<=150`, refuses nonfinite inputs, and does not promise arbitrary-precision accuracy beyond that range.

## 4. Worked edge investigations

**Zero-field diffusion:** `u_L=u_R=0`, `n_L=7`, `n_R=3`, `D=0.1 m^2/s`, `h=0.5 m`. The formula gives `J=0.8 m^-2 s^-1` when `n` is represented as numbers per m^3. These numbers are an invented arithmetic fixture, not a proposed device parameter set.

**Equilibrium cancellation:** `u_L=0`, `u_R=1`, `n_L=1`, `n_R=e`. Because `n_R/n_L=e^{u_R-u_L}`, the exact edge flux is zero. Test both edges in the reverse orientation: `J(R->L)=-J(L->R)`.

**Adversarial jump:** `delta=120`. Direct `exp(delta)` risks loss of numerical resolution. The bounded Bernoulli implementation retains `B(-delta)-B(delta)=delta` to machine precision while avoiding a naive catastrophic subtraction for the Bernoulli function itself.

## 5. From edge flux to future carrier continuity

A full finite-volume semiconductor discretization would enforce cell balance, for example `J_{i+1/2}-J_{i-1/2}=h(G-R)` after correctly selecting sign and charge conventions, plus a self-consistent Poisson equation, electron and hole statistics, material-dependent mobilities/diffusion, contacts and interface physics. **The present reference does not solve that coupled system.** It preserves the edge flux as a separate, validated mathematical primitive that Electronics & Semiconductors may reuse when its own source and measurement gates are met.

**Source orientation:** TU Wien basic semiconductor equations, https://iue.tuwien.ac.at/phd/sharma/node-The-Basic-Semiconductor-Equations.html ; COMSOL semiconductor drift–diffusion/Poisson overview, https://www.comsol.com/semiconductor-module . These links are bibliographic pointers, not preserved authenticated publisher files.
