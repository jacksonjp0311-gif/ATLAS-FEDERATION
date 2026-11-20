# Chapter 56 — Independent nonlinear oracles, error separation and the physical-model handoff

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Program objective:** preserve enough steps, boundary assumptions, tests and source status for a future researcher to recreate and falsify numerical claims offline.

## 1. Four different verification layers

A verified equation implementation must separate the following questions:

1. **Code and arithmetic.** Does the finite algorithm compute the requested discrete quantities for authored inputs? Assert dimensions, finite arithmetic, sign conventions, exact algebraic identities and known solutions.
2. **Discrete nonlinear solve.** Does the returned vector satisfy the discretized equations? Assemble the residual separately and compare with a distinct solver or algorithm. Compare roots, not merely a duplicated helper function.
3. **Continuum approximation.** How does the discretization error change with mesh refinement? Manufacture a smooth analytic field, derive its source term in the **continuum** equation, then refine the grid with solver error controlled more tightly than truncation error.
4. **Physical interpretation.** Does the selected PDE, closure and parameter set predict controlled measurements? That requires independent physical observations, instrument calibration, uncertainty propagation, accepted source provenance and outside replication. This edition has **no such evidence**.

Passing layers 1–3 cannot be described as passing layer 4. Nor can a `SciPy` comparison be described as independent scientific peer review: it is a second **software implementation** of an authored mathematical case.

## 2. Independent offline oracle methods

The v0.5 optional oracle uses three intentionally different computational routes:

- **SciPy hybrid nonlinear root finder and NumPy dense matrix assembly:** compare 100 independently assembled finite nonlinear systems against the reference tridiagonal damped-Newton algorithm. Record every compared potential and the maximum numerical discrepancy.
- **Python Decimal with 70 digits:** evaluate `B(z)=z/(exp(z)-1)` on 215 finite values, including near-zero and high-magnitude inputs; measure relative differences under a documented range.
- **SciPy quadrature:** integrate the Scharfetter–Gummel cell's exponential integrating factor on 160 independent edge fixtures; compare the integral-based flux with the Bernoulli formula.

These are **synthetic cases** selected using a fixed seed. They do not simulate thermal noise, contact resistance, fabrication variability, lattice scattering, interfacial trapping or quantum confinement.

## 3. Independent manufactured continuum benchmark

The one-dimensional continuum equation with `u*(x)=sin(pi*x)` and source

\[
f(x)=\alpha\pi^2\sin(\pi x)+\beta\sinh(\sin(\pi x))
\]

is a constructive check of second-order central differencing. The exact continuous field is known. Record `||u_h-u*||_infinity` on `n=15,31,63` interior nodes and verify an approximately fourfold error reduction with each halving of `h`. Also record `||F(u_h)||_infinity`, because a tiny nonlinear algebraic residual does not imply a tiny spatial truncation error.

## 4. Conservation and physical charge bookkeeping

The discrete Poisson–Boltzmann balance in Chapter 53 is an exact telescoping algebraic relation for an exact discrete root. It is useful for detecting a sign error and for preventing silent conservation failures. Yet conservation alone is not calibration: multiple incorrect closures conserve exactly. A proposed physical model must track **density units**, positive elementary charge sign, thermal voltage and the particular electron/hole quasi-Fermi conventions. Fixed doping profiles and Boltzmann statistics require measurement and assumptions that this library deliberately does not invent.

## 5. Release-level requirements and escalation

Preserve original exact-version data records; do not mutate predecessors. Treat `related_to` navigation as different from scientific support. Version the canonical node manifest, common registry, compiled schema and new exact record/relation revisions. An incremental release must list changed/added file hashes and exact predecessor full-ZIP SHA; reject unexpected deletion, ZIP path traversal or mismatched restore. Publish source-tree and fresh-restoration regression reports separately, plus a strict original publisher-byte source audit. Preserve v0.4 tests on an unmodified frozen predecessor snapshot.

A future Electronics & Semiconductors Atlas must extend this bridge to **coupled electron/hole continuity equations**, recombination, contacts, interface conditions, convergence under strong fields, experimental material parameters and measured device results. Reusing a mathematical subroutine is not evidence that a transistor or AI hardware was rebuilt.

**Source navigation and disclosure:** TU Wien and COMSOL public documentation linked in Chapters 53–55; there is no independently authenticated publisher-file transport in this research increment. The human-readable chapter, original Python reference and tests are program-authored material; no copyrighted original document is mirrored.
