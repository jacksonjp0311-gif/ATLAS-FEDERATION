# Chapter 39: Householder QR and stable least-squares reconstruction

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `A=QR, QᵀQ=I; if A has full column rank, Rx=Qᵀb; ||Ax−b||₂ minimized.`

**Reference algorithm:** `math_physics_atlas.v02_models.qr_least_squares(matrix, rhs)`

**Units:** A: measurement response per parameter; b: measured response; x: parameter units.

## Why a reconstructible solver matters
A future researcher fitting a sensor response, calibrating instruments, or estimating the parameters of a physical law needs a linear inverse method whose errors can be diagnosed. Least-squares finds an x minimizing the squared Euclidean residual ||Ax−b||². The formal normal equations AᵀAx=Aᵀb are correct as exact mathematics but are a dangerous implementation choice: under the 2-norm, κ₂(AᵀA)=κ₂(A)² for a full-rank A. Squaring the condition number discards effective precision just when measurements are nearly dependent. This chapter gives a compact alternative suitable for an offline Python implementation.

## Derivation from geometry
Let m≥n and A∈ℝ^{m×n} have linearly independent columns. The matrix A can be transformed by an orthogonal Q into an upper trapezoidal R. Since ||Qᵀv||₂=||v||₂, minimization of ||Ax−b||₂ is equivalent to minimization of ||[R;0]x−Qᵀb||₂. The first n rows give a triangular system Rx=c₁ and the remaining rows contribute an irreducible residual ||c₂||₂. A Householder vector v=u−αe₁, where u is the active column and α=−sign(u₁)||u||₂, produces H=I−2vvᵀ/(vᵀv). H is symmetric and HᵀH=I because H²=I. Apply H to each trailing column and to b, without storing the full Q. Back substitution completes the algorithm. The sign convention avoids subtracting almost equal magnitudes when constructing v.

## Worked reconstruction and checks
Use four rows [1,t] for t=1,2,3,4 and measured responses [3,5,7,9]. The unique affine map b(t)=1+2t has parameters x=[1,2]. A correct solver yields a residual near machine rounding. Perturb one response and verify Aᵀ(Ax−b)≈0; this normal-equation residual is an *optimality check*, not the chosen solve algorithm. Independently compare parameters to an SVD-based LAPACK least-squares implementation on seeded finite inputs. Preserve the full design matrix, parameter units, and the residual vector: a tiny residual alone does not show that the underlying physical model is right.

## Failure investigation and bounded scope
If columns are equal, A has rank one; infinitely many parameter vectors can fit the same prediction. Refuse this input rather than returning a fabricated unique coefficient vector. Strongly scaled or nearly rank-deficient inputs can have large forward errors even when orthogonal transformations are stable. The diagnostic threshold for declaring numerical rank is a computational policy, not a measurement of scientific truth. This reference implementation handles bounded m≤128 and n≤32, m≥n, finite real values, and no pivoted or rank-revealing QR. Robust full SVD, statistical errors-in-variables, and confidence intervals remain follow-on work.

## Technology continuity link
QR supports spectrum inversion, metrology, linear regression, fitting physical constants, and AI feature regression. Archive equations, numerical decisions, and residual checks together; no proprietary library is required to execute the bounded reference model.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Full-column-rank only: rank loss, underdetermined inputs and extreme scaling are rejected. Residual does not establish parameter identifiability under noise.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
