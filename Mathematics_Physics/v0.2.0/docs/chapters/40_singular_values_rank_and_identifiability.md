# Chapter 40: Singular values, rank and identifiability boundaries

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `A=UΣVᵀ; ||δx||/||x|| ≲ κ₂(A) ||δb||/||b|| under suitable assumptions; κ₂=σ₁/σₙ.`

**Reference algorithm:** `math_physics_atlas.v02_models.svd2_diagnostics(matrix, rank_rtol)`

**Units:** Singular values have units of the input-output linear map; condition number is dimensionless only after consistent scaling.

## From fit quality to what is knowable
The singular-value decomposition separates a linear map into input directions, nonnegative gain factors and output directions. For real A, one may write A=UΣVᵀ with orthogonal U,V. If a direction has zero singular value, any movement along its corresponding right singular vector changes no observation. The parameter is unidentifiable from this experiment. If a singular value is small but nonzero, modest measurement errors may cause large parameter errors. Neither more numerical iterations nor an optimistic residual can create missing evidence.

## A hand-checkable 2×2 formula
For A=[[a,b],[c,d]], define p=√((a+d)²+(c−b)²) and q=√((a−d)²+(c+b)²). The two singular values are (p+q)/2 and |p−q|/2 in descending order; their product equals |ad−bc|. Rescale all four coefficients by their maximum magnitude first, then recover magnitudes by the same scale. For the smaller singular value, computing |det(A)|/σ₁ may be preferable when p≈q, although determinant cancellation can still destroy relative accuracy. The exact rank is distinct from estimated numerical rank: σ₂/σ₁≤τ is a *declared tolerance rule*, not a theorem that the underlying system is rank deficient.

## Constructed investigations
A=diag(5,2) maps basis vectors to lengths 5 and 2; its condition number is 2.5. Replacing the second diagonal with 10⁻⁸ creates a fragile inverse: an observation error of order 10⁻⁸ along that axis becomes order one in its parameter. If A=[[1,1],[1,1]], both rows are equal and the null direction (1,−1) is invisible. Rotate a matrix by an orthogonal 90° rotation; singular values should remain unchanged. Compare diagnostic values to an independent LAPACK SVD on random finite 2×2 matrices.

## What not to claim
The compact implementation never computes U or V and cannot solve arbitrary rank-deficient least-squares problems. Computing AᵀA for a large matrix squares its condition number, so do not generalize the 2×2 closed form to a stable large-matrix SVD by naïvely squaring. Missing covariance information, instrument model error, and correlations in observations are separate barriers. A full robust bidiagonal SVD and unit-aware statistical inverse model remain scoped v1 gates.

## Technology continuity link
Rank analysis determines whether a process is measurable, whether sensors are redundant, and whether an AI model has distinguishable parameters. Preserve identifiable parameter combinations rather than publishing unsupported parameter estimates.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Implements only analytic 2×2 singular-value diagnostics; it is NOT a general SVD or pseudoinverse. Small singular values may lose accuracy in determinant cancellation.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
