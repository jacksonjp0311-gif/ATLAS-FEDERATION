# Chapter 07: Vectors, inner products and geometric projection

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Vectors encode states, coordinates, gradients and high-dimensional embeddings. An inner product determines lengths and angles and is not merely decorative notation: it defines what orthogonality means in a particular space. Projection decomposes a vector into a component along a direction and an orthogonal remainder. This geometry underlies least squares, PCA, numerical approximation and representation learning.

## Equation, symbols and domain

`⟨u,v⟩=Σ_i u_i v_i; proj_u(v)=(⟨v,u⟩/⟨u,u⟩)u.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Project v=(3,4) onto u=(1,0), obtaining (3,0). Check that the residual (0,4) has zero dot product with u.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

The Euclidean dot product is one possible metric. Different units, indefinite forms or complex inner products require different formulas, and a small residual does not authenticate physical data.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
