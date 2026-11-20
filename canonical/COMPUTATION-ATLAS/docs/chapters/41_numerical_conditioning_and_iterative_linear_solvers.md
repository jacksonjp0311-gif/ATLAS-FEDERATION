# Chapter 41 — Numerical conditioning and iterative linear solvers

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Solving Ax=b with finite-precision arithmetic requires consideration of sensitivity. The condition number measures how a small perturbation of the matrix or right-hand side can change the solution. A solver can have a small residual ||Ax−b|| yet a large forward error when A is ill-conditioned. Iterative methods such as Jacobi, Gauss–Seidel and conjugate gradient use repeated updates, often exploiting sparsity. Their convergence depends on properties such as diagonal dominance or positive definiteness and cannot be promised for arbitrary inputs.

## Mathematical contract

Residual r_k=b−Ax_k; forward error e_k=x_k−x*. Condition estimate for nonsingular A: ||e||/||x*|| ≲ κ(A)(||δA||/||A||+||δb||/||b||) under suitable small-perturbation conditions.

## Derivation and reasoning

An approximate solution is validated by the residual but interpreted with a condition estimate. For positive definite quadratic energy, conjugate gradient can use Krylov subspaces and orthogonality to converge rapidly under good conditioning; exact arithmetic may terminate in at most n steps, while floating point complicates the ideal theorem. Sparse matrix–vector products can dominate computation and data movement rather than scalar multiplication count.

## Worked reconstruction and independent check

Take A=[[1,1],[1,1+ε]] with ε small. Compare the numerical solution after slightly perturbing b. Record residual and difference from an exact Fraction calculation. Vary ε through several orders of magnitude and show why a tiny residual alone is insufficient.

## Limitations, falsification, and invalid use

The current v0.2 code implements only bounded exact elimination, not a full sparse iterative solver or condition estimator. The chapter is conceptual and its mathematical claims require independent source review before a safety-critical application.

## Cross-domain meaning

Future Control and Measurement integrations must carry sensor uncertainty, physical units and condition numbers along with numerical estimates.

## Source orientation and recoverability

- [MIT 18.06 Linear Algebra, course syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) — original publisher bytes unavailable in this package.
- [Python decimal module: rounding, context and arithmetic](https://docs.python.org/3/library/decimal.html) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
