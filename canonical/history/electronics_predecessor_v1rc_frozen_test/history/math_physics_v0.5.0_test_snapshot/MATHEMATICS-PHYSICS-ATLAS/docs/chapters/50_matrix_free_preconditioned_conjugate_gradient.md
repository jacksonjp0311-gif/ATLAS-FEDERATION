# Chapter 50 — Matrix-free preconditioned conjugate gradient with explicit failure status

**Edition:** Mathematics & Physics v0.4.0. **Evidence:** finite software/numerical comparisons; no algorithmic universality claim.

## What problem is solved?

For the symmetric positive-definite *interior Dirichlet* Poisson operator, solve `A x = b` without allocating a dense N×N matrix. On a 64×64 interior grid N=4096, a dense double matrix would occupy roughly 134 MB, versus O(N) vectors and four face-weight arrays for the five-point application. This is a bounded reference implementation, not a benchmark against commercial sparse solvers.

The preconditioner is the diagonal `M=diag(A)`. Because ε is strictly positive and all face weights positive, every M diagonal entry is positive. Preconditioning reduces differing scales, but this simple M does **not** guarantee mesh-independent iteration counts for large aspect ratios or highly contrasting dielectrics. More capable multigrid and incomplete-factorization methods remain future work.

## Derive the recurrence

Start from `x0=0`, `r0=b−A x0`, `z0=M^{-1}r0`, `p0=z0`. For each iteration k compute

\[
\alpha_k=\frac{r_k^T z_k}{p_k^T A p_k},\quad
x_{k+1}=x_k+\alpha_kp_k,\quad
r_{k+1}=r_k-\alpha_k A p_k,
\]

and then `z_(k+1)=M^-1 r_(k+1)`,

\[
\beta_k=\frac{r_{k+1}^Tz_{k+1}}{r_k^Tz_k},\quad
p_{k+1}=z_{k+1}+\beta_kp_k.
\]

For an SPD A in exact arithmetic, the search directions are A-conjugate and the method minimizes the quadratic error over growing Krylov subspaces. In floating-point arithmetic, recurrence identities can drift. This implementation recomputes a true residual periodically and before claiming convergence, checks finite arithmetic and refuses a nonpositive `p^T A p` breakdown.

## Stopping contract and numerical scale

The explicit criterion is `||b−Ax||₂ <= max(atol, rtol*||b||₂)`, evaluated using the actual current iterate; `rtol>0` or `atol>0` must be specified. `maxiter` is bounded at 40,000. Reaching the limit returns `converged=False`, `status=maxiter_exceeded`, the true residual and potential field. It is **not** silently promoted to a valid physical solution. Because `||b||` has units inherited from the assembled equation, relative and absolute tolerances must be interpreted within that unit system. A tiny relative residual does not, by itself, certify a small physical error when the inverse operator is ill-conditioned.

## Reference reconstruction

```python
from math_physics_atlas.v04_models import poisson2d_problem, solve_poisson2d_cg
p=poisson2d_problem(16, 12, 1.0, 0.8, 8.8541878188e-12, 0.0,
                    lambda x,y: x)
s=solve_poisson2d_cg(p, rtol=1e-10, maxiter=2000)
assert s['converged']
print(s['iterations'], s['relative_residual'])
```

On a variable-ε grid, the reference suite checks A symmetry and positive discrete quadratic energy independently using deterministic vectors, compares a dense independently assembled NumPy solution, then separately checks the boundary-charge balance. The Python reference has no SciPy runtime dependency; SciPy is used only by some optional external comparisons.

## Counterexample: false convergence

Choose a nonsymmetric patterned charge distribution on a 14×11 grid. Stop after only one iteration with a much tighter tolerance than the first step can meet. The system must report `maxiter_exceeded`, not `converged`. A reported end-state field cannot be used to infer a voltage or current unless the algebraic residual, mesh convergence, constitutive assumptions, and experimental calibration have all been assessed separately.

## Complexity and limits

One matrix-vector multiplication costs O(N), and iterative storage O(N). Convergence depends on spectral distribution, boundary types, physical coefficient contrast, mesh dimensions and stopping tolerance; **this reference does not estimate an uncertainty distribution or solve any nonlinear carrier continuity equation**. It does not claim full-precision formal guarantees, parallel scalability or production reliability.

**Source orientation only:** SciPy `sparse.linalg.cg` documentation at https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html documents the SPD assumption, relative/absolute tolerance convention, non-convergence status and preconditioning purpose. No third-party source code is bundled or authenticated.
