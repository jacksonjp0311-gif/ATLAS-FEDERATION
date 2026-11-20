# Chapter 51 — Manufactured solutions, independent oracles and error budgets

**Edition:** Mathematics & Physics v0.4.0. **Scope:** rigorous, bounded verification of one finite-difference program, not a new general mathematical theorem.

## The crucial separation

A numerical algorithm can solve a *discretized* equation almost exactly while approximating the underlying continuum PDE poorly. Preserve at least four distinct quantities in an investigation: (1) code versus independent oracle, (2) algebraic solver residual, (3) discretization error against a known analytic problem, (4) model-form/measurement uncertainty. These are not interchangeable.

### Continuum manufactured problem

Let `Lx=Ly=1`, homogeneous Dirichlet boundaries, ε constant and choose

\[
V_{\star}(x,y)=\sin(\pi x)\sin(\pi y),\quad
\rho_{\star}(x,y)=2\pi^2\epsilon V_{\star}(x,y).
\]

The derivative `−ε(V_xx+V_yy)=2π² ε V` shows the sine function is an exact continuum solution. The five-point discretization has, for this mode, eigenvalue

\[
\lambda_h=\frac{8}{h^2}\sin^2(\tfrac{\pi h}{2}),\qquad
\lambda_{\rm continuum}=2\pi^2
\]

for `hx=hy=h=1/(n+1)`. Taylor expansion of sine gives `λh=2π²+O(h²)`, hence a second-order potential error after an accurate algebraic solve. This analytic derivation predicts an approximately fourfold reduction when h halves.

### Executed measurements on constructed grids

The v0.4 deterministic numerical oracle observed:

| Interior resolution | Spacing h | L-infinity potential error (V) | Observed reduction |
|:--|--:|--:|--:|
| 7×7 | 0.125 | 0.012950746721879236 | — |
| 15×15 | 0.0625 | 0.003218964440079519 | 4.0233 |
| 31×31 | 0.03125 | 0.0008035776793722249 | 4.0058 |
| 63×63 | 0.015625 | 0.0002008218097049319 | 4.0014 |

The solver reached a very small algebraic residual on each constructed case, yet the continuum error remained nonzero. Therefore asserting a small CG residual as 'true physics' is demonstrably wrong even in this ideally controlled example.

## Independent matrix assembly

A separate `tools/independent_oracle_v04.py` assembles the small-grid matrix by allocating a NumPy dense N×N stencil and using `numpy.linalg.solve`. It does **not** use the reference model's stored four face coefficient arrays or its CG implementation. The oracle compares every potential value, recomputes `||A x−b||`, and independently accumulates boundary flux and area charge. In the recorded initial run, 144 randomized well-posed grids comprised 3,356 voltage comparisons, with maximum absolute difference ≈1.21×10⁻¹¹ V.

This second implementation reduces the probability of the same programming mistake appearing in both paths; because both use the **same physical modeling assumptions** and constructed data, it is not external scientific review or experimental validation.

## Evaluation protocol for future researchers

1. Freeze all inputs, code, random seed, Python/NumPy versions, hash and boundary array representation.
2. Prove data-shape and dimensional consistency, then test operator symmetry and positive energy for representative grids.
3. Check independent dense linear solves on **small** meshes; test explicit failure paths such as overlarge grids and iteration-budget exhaustion.
4. Perform h-refinement against an analytically known continuum solution while keeping solver error much smaller than spatial truncation error.
5. Track flux conservation separately. A solver can conserve its own discretization while solving the wrong continuum equation or employing a bad material model.
6. For actual science, additionally obtain calibrated laboratory measurements, authenticated material parameters, independent replication and an expert review.

## Limitations and sources

The test functions are smooth; no field singularities, junction surface charges, adaptive mesh, anisotropic dielectric, nonlinear Poisson–Boltzmann effects or high-contrast industrial device geometry are represented. These tests do not certify energy-efficient hardware, transistor performance or AI performance. Reference guidance is original mathematics, with topic orientation to MIT OCW 18.086 https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/readings/ . Original publisher document files are not included.
