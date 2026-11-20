# Chapter 40 — Exact linear equations, rank and pivoting

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

A system Ax=b represents linear constraints. Gaussian elimination applies invertible row operations to find an equivalent echelon system; back-substitution then recovers solutions where pivots exist. In exact rational arithmetic, an invertible square matrix yields a unique solution and a zero residual certificate. A singular matrix may have no solutions or infinitely many, neither of which should be silently represented by a guessed inverse. Numerical floating-point elimination additionally needs pivot strategies and condition analysis because small pivots can amplify rounding.

## Mathematical contract

Elementary row operation preserves the solution set. For square nonsingular A, x=A^(−1)b, and exact residual r=Ax−b=0. Rank(A)=n is sufficient for uniqueness in an n×n system.

## Derivation and reasoning

Swapping rows, adding a scalar multiple of one row to another, or scaling a row by a nonzero scalar preserves the simultaneous-equation solution set. Gauss–Jordan eliminates every nonpivot coefficient and normalizes pivots to one. When no nonzero pivot exists in a required column, the supplied square matrix is singular and the unique-solution contract fails. Exact arithmetic avoids cancellation error but increases integer numerator/denominator size.

## Worked reconstruction and independent check

Solve 2x+y=5 and x−y=1, obtaining x=2, y=1. Then solve with coefficients 1/10 and 3 using Fraction strings to preserve decimal intent. The reference also refuses [[1,2],[2,4]] under a uniqueness contract. Compare non-singular integer systems against SciPy at moderate condition numbers.

## Limitations, falsification, and invalid use

Exact rational solutions can be extremely expensive for large systems. `Fraction(0.1)` captures an already-rounded float, whereas `Fraction("0.1")` represents one tenth exactly. A zero residual in the model does not prove that measured coefficients came from a valid scientific experiment.

## Cross-domain meaning

This supports Causal regression and Control linear systems, but their model identification, input units and physical uncertainty are independent evidence obligations.

## Source orientation and recoverability

- [MIT 18.06 Linear Algebra, course syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) — original publisher bytes unavailable in this package.
- [Python documentation, fractions — Rational numbers](https://docs.python.org/3/library/fractions.html) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
