# Investigation 15 — Zero rational residual does not validate measured coefficients

**Origin:** authored 2×2 system solved by exact Gaussian elimination. For [[2,1],[1,−1]]x=[5,1], the unique solution is x=[2,1] and the exact rational residual is zero. Replace matrix rows with almost equal rows, then perturb the right side slightly: large changes in the solution may result even when residual remains small. That is poor conditioning of the mathematical problem, not necessarily an implementation bug.

**Reproduce:** use `gaussian_solve_exact` for exact rational matrices, and compare with a floating-point solver on a nonsingular ill-conditioned example. Record both residual and condition estimate. The numerical example contains no physical sensor measurements, and its source coefficients are author-chosen.
