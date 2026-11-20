# Mathematics & Fundamental Physics Atlas — offline reconstruction manual v0.3.0

This manual preserves the original v0.1 human science reference **verbatim**, then appends the successive chapter content from v0.2 and v0.3. The original source files and test history remain unchanged. None of these constructed calculations imply physical field validation, legal reuse of third-party publisher bytes, or independent scientific acceptance.

---

# Mathematics & Fundamental Physics Atlas v0.1.0 — Reconstructible Scientific Reference

James Paul Jackson research program · November 15, 2026 · ATLAS FORGE Common Contract 1.0

**Contents:** thirty-eight original chapters, twenty-two authored executable reconstruction exercises, ten public bibliographic references, explicit model validity boundaries and source-rights debt.

**Scientific status:** a first educational research edition, not a complete archive of all mathematics or physics, an independent peer-reviewed paper or a validated instrument design.

## Complete chapter index

- 01_proof_axioms_and_falsifiable_mathematical_claims.md
- 02_units_dimensional_analysis_and_si_definitions.md
- 03_numbers_rational_arithmetic_and_precision.md
- 04_functions_domains_limits_and_continuity.md
- 05_derivatives_sensitivities_and_automatic_differentiation.md
- 06_integration_and_conservation_over_time.md
- 07_vectors_inner_products_and_geometric_projection.md
- 08_matrices_as_composable_linear_maps.md
- 09_gaussian_elimination_and_rational_certificates.md
- 10_rank_nullspace_and_underdetermination.md
- 11_least_squares_and_identifiable_parameter_fitting.md
- 12_eigenvalues_stability_and_dynamical_modes.md
- 13_probability_axioms_and_conditional_evidence.md
- 14_random_variables_expectation_and_variance.md
- 15_bayesian_updating_versus_evidence_reliability.md
- 16_binomial_counting_and_independence_assumptions.md
- 17_numerical_conditioning_and_stability.md
- 18_discrete_fourier_transform_and_spectral_analysis.md
- 19_differential_equations_and_initial_value_problems.md
- 20_runge_kutta_methods_and_local_error.md
- 21_partial_differential_equations_and_boundary_conditions.md
- 22_optimization_convexity_and_objective_design.md
- 23_softmax_log_sum_exp_and_numerical_probability.md
- 24_newtonian_mechanics_and_inertial_frames.md
- 25_energy_momentum_and_conservation_boundaries.md
- 26_oscillators_modes_and_resonance.md
- 27_electric_charge_fields_and_potential.md
- 28_circuit_dynamics_and_rc_time_constants.md
- 29_maxwell_equations_and_wave_propagation.md
- 30_thermodynamic_temperature_and_energy_scales.md
- 31_special_relativity_and_spacetime_consistency.md
- 32_quantum_state_amplitudes_and_born_measurement.md
- 33_schr_dinger_equation_and_hamiltonian_modeling.md
- 34_heisenberg_uncertainty_and_measurement_meaning.md
- 35_covariance_and_propagated_measurement_uncertainty.md
- 36_inverse_problems_and_scientific_identifiability.md
- 37_from_linear_algebra_to_neural_network_computation.md
- 38_rebuilding_an_offline_scientific_computing_stack.md

---

# Chapter 01: Proof, axioms, and falsifiable mathematical claims

**Discipline:** Logical foundations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Mathematics distinguishes stipulated axioms from derived statements and empirical predictions. A proof is a finite chain of sound inferences in a specified logical system, not an attractive example or a statistical sample. To reconstruct knowledge, preserve assumptions, definitions, exact statement, proof steps and a counterexample when assumptions fail. Computers can verify many small claims exhaustively, but a finite test cannot prove a theorem about an unbounded domain.

## Equation, symbols and domain

`For implication P ⇒ Q, prove all valid P entail Q, or construct P∧¬Q.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For all integers n, verify algebraically that n(n+1) is even by noting neighboring integers have opposite parity. Testing the first million integers alone would not prove the universal statement.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Logical validity depends on the chosen assumptions and semantics; an empirical physical model must also face measurement. An executable unit test certifies a specific implementation on selected values, not universal correctness.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 02: Units, dimensional analysis, and SI definitions

**Discipline:** Metrology. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Units encode the type of physical quantity. SI defining constants provide a repeatable common basis for measuring length, time, mass, electrical charge, temperature and amount of substance. Dimensional homogeneity is necessary for a physical relation, but it is not sufficient to prove one: two incorrect formulas may have identical units. Distinguish exact defining constants from experimental constants such as the gravitational constant.

## Equation, symbols and domain

`[force]=kg·m·s^-2; [energy]=kg·m²·s^-2; [power]=kg·m²·s^-3.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Derive that a force of one newton acting through one meter of displacement transfers one joule in the aligned ideal case, then divide by one second to obtain one watt.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A dimensionally correct model can still omit losses or wrong physical mechanisms. Instrument calibration and provenance remain independent evidence requirements.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 03: Numbers, rational arithmetic and precision

**Discipline:** Computational foundations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Integer and rational numbers support exact symbolic calculations; binary floating-point arithmetic represents a finite subset of real numbers. Scientific programs must decide when exactness matters, especially for conservation and discrete coefficients. Fractions prevent a balancing or linear-algebra proof from being undermined by roundoff. Numerical algorithms must separately track overflow, cancellation, conditioning and finite precision.

## Equation, symbols and domain

`p/q∈ℚ, q≠0; floating-point x̂=x(1+δ) under a bounded operation model.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Solve 3x=1 exactly as one third. A binary float approximates that value and cannot generally preserve equality 3x=1 as an exact rational identity.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Exact arithmetic may be computationally expensive; floating-point can be more appropriate for measured physical values with uncertainty. No representation turns a measured input into an exact constant.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares


---

# Chapter 04: Functions, domains, limits and continuity

**Discipline:** Calculus. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

A function maps inputs in a declared domain to outputs, while a limit specifies the behavior near a point rather than merely at it. Continuity permits controlled passage from input approximations to output approximations under appropriate bounds. Mathematical analysis provides tools to reason about stability, convergence and nonlinear response. Software should reject inputs outside domains such as logarithms of nonpositive arguments.

## Equation, symbols and domain

`lim_(x→a) f(x)=L means ∀ε>0 ∃δ>0: 0<|x-a|<δ ⇒ |f(x)-L|<ε.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Use f(x)=x² and a=2. Factor |x²-4|=|x-2||x+2| to bound the output difference when x is sufficiently close to two.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A continuity proof applies to its specified domain and topology. Finite tests near one input cannot establish global continuity or physical behavior.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **MIT OpenCourseWare 18.01SC Single Variable Calculus, Fall 2010:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ — scope: One-variable differentiation, integration, limits and fundamental theorem learning topics


---

# Chapter 05: Derivatives, sensitivities and automatic differentiation

**Discipline:** Calculus. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Derivatives quantify local sensitivity and power optimization, gradient-based learning and control. Polynomial differentiation follows from the binomial expansion and the limit definition. Finite differences approximate slopes without symbolic derivatives but suffer truncation and roundoff errors. Automatic differentiation applies the chain rule through a computational graph and is distinct from symbolic simplification or finite differencing.

## Equation, symbols and domain

`f′(x)=lim_(h→0)[f(x+h)-f(x)]/h.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For f(x)=x², derive f′(x)=2x and compare a centered finite difference with step h at x=2. Explain why making h arbitrarily tiny in floating point eventually becomes unreliable.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A derivative can fail to exist at a kink; noisy sampled sensor data may not have a meaningful instantaneous derivative. Local gradients do not determine global optimum.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **MIT OpenCourseWare 18.01SC Single Variable Calculus, Fall 2010:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ — scope: One-variable differentiation, integration, limits and fundamental theorem learning topics


---

# Chapter 06: Integration and conservation over time

**Discipline:** Calculus. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Integration accumulates a varying rate into a total. It connects physical power to energy, velocity to displacement, probability density to probability and differential equations to trajectories. The fundamental theorem of calculus connects an accumulated integral with a derivative when appropriate regularity holds. Numerical quadrature approximates integrals when antiderivatives are unavailable.

## Equation, symbols and domain

`∫_a^b f(x)dx = F(b)-F(a) when F′=f.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Integrate f(t)=t² over [0,3] by its antiderivative t³/3 to obtain nine. Reconstruct the same result with Simpson quadrature for an even partition.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Finite sampling and interpolation introduce numerical error; discontinuities and singularities demand extra care. Integrating an invented power profile does not establish measured energy.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.01SC Single Variable Calculus, Fall 2010:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/ — scope: One-variable differentiation, integration, limits and fundamental theorem learning topics


---

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


---

# Chapter 08: Matrices as composable linear maps

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Matrices represent linear maps between finite-dimensional vector spaces. Matrix multiplication composes maps; transpose changes coordinate relationships under a chosen real inner product. Associativity makes chains of transformations possible but matrix multiplication is not generally commutative. AI workloads rely extensively on matrix products, making the derivation and data layout important for rebuilding model execution.

## Equation, symbols and domain

`(AB)_(ij)=Σ_k A_(ik)B_(kj); (AB)v=A(Bv).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Multiply a 1×2 row [1,2] by a 2×1 column [3,4] to obtain 11. Reverse the order and observe that the result is a 2×2 matrix, not the same scalar.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Dimensions must be checked before multiplication; numeric precision and memory layout matter for large computation. Matrix multiplication alone cannot infer scientific causation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 09: Gaussian elimination and rational certificates

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Gaussian elimination transforms a linear system into a form whose solution is easy to recover. Pivoting and rank expose inconsistent or underdetermined systems. Exact rational elimination can certify a small system without rounding, which is useful when preserving symbolic conservation laws. Numerical solvers for large floating systems require scaling and stable pivot strategies, not arbitrary exact fractions.

## Equation, symbols and domain

`Ax=b; row operations E_i preserve the solution set when E_i is invertible.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Solve 2x+y=5 and x−y=1. Subtract or eliminate to obtain x=2,y=1. Substitute into both original equations to verify zero rational residual.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A singular matrix may have no solution or infinitely many; a unique-solution routine must refuse. Equality tests in floating point should use meaningful tolerances and uncertainty.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 10: Rank, nullspace and underdetermination

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Rank counts independent constraints; nullspace describes directions left unconstrained. The rank-nullity theorem provides a dependency test for linear models, scientific inference and network conservation. In a chemical reaction matrix, the nullspace gives mathematically balanced coefficient families. In inverse problems, nontrivial nullspaces show why multiple parameter sets can explain the same observations.

## Equation, symbols and domain

`rank(A)+nullity(A)=number of columns of A.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Use a 1×2 matrix [1,1]. Its rank is one, so its nullspace has dimension one: vectors (t,−t). A single linear equation therefore cannot identify two independent unknowns.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Numerical rank depends on tolerance and conditioning; an exact symbolic rank does not validate measured coefficients or identify a causal mechanism.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 11: Least squares and identifiable parameter fitting

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Noisy observations often cannot satisfy a proposed linear model exactly. Least squares chooses parameters that minimize squared residuals under a declared metric. Differentiating the quadratic objective yields normal equations, but solving them can amplify conditioning problems. Physical parameter identification also needs independent calibration, representative data and a justified error model.

## Equation, symbols and domain

`min_x ||Ax-b||²; for full-rank A, AᵀAx=Aᵀb.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Fit a straight line to (0,1),(1,3),(2,5). The model y=1+2x yields zero residual. With a perturbed point, compute the new residual and distinguish fit quality from evidence of a mechanism.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Normal equations square the condition number; professional fitting often uses QR or SVD. A low error may reflect leakage or insufficiently diverse data, not correct physics.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions


---

# Chapter 12: Eigenvalues, stability and dynamical modes

**Discipline:** Linear algebra. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Eigenvalues describe how a linear transformation acts along special directions. In differential-equation systems they classify exponential growth, decay and oscillation under a linear model. In AI they appear in optimization curvature, covariance spectra, propagation stability and dimensionality reduction. A numerical eigenvalue requires a model and a source of coefficients; one large eigenvalue does not automatically mean a system is unstable under every discretization.

## Equation, symbols and domain

`Av=λv; dynamical modes of x′=Ax depend on eigenvalues of A.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For diagonal A=diag(−1,−2), the dynamical system x′=Ax has two decaying modes. Replace one diagonal entry by +1 and explain which initial-state component grows.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Nonnormal matrices can amplify disturbances transiently even when eigenvalues indicate eventual decay. Nonlinear dynamics and uncertain coefficients need separate evaluation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability


---

# Chapter 13: Probability axioms and conditional evidence

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Probability is a mathematical description of uncertainty under a specified sample space and measure. Conditional probability updates knowledge about events but does not establish a measurement model. Bayesian calculations combine priors and likelihoods; their quality depends on how these inputs were obtained. A future AI system must distinguish mathematical normalization from statistical calibration and causal validity.

## Equation, symbols and domain

`P(A|B)=P(A∩B)/P(B) for P(B)>0.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

With prior probability 0.5, P(test+|H)=0.9 and P(test+|¬H)=0.1, calculate posterior P(H|test+)=0.9. Change the base rate and recompute.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

An invented prior and likelihood are not empirical frequencies. Conditioning on a zero-probability event requires a more careful formalism, not division by zero.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares


---

# Chapter 14: Random variables, expectation and variance

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Expectation summarizes a distribution’s mean while variance measures spread around that mean. Neither is a substitute for bounds on rare events. Independence is a property of joint distributions and cannot be inferred from separate measurements. Reliable AI evaluation preserves the true sampling scheme, correlated sources and the difference between observed data and simulated samples.

## Equation, symbols and domain

`E[X]=Σ_x x p(x); Var(X)=E[(X−E[X])²].`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For a fair binary variable with values zero and one, compute expectation 0.5 and variance 0.25. Change the probability of one to 0.9 and recompute.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A mean alone cannot predict safety, tail behavior or worst-case cost. Heavy-tailed distributions may lack finite variance, making some standard formulas invalid.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 15: Bayesian updating versus evidence reliability

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Bayesian inference offers a consistent way to combine beliefs and likelihood under a model. Evidence likelihood must be defined with respect to competing hypotheses, not assigned because a result appears plausible. Reusing dependent observations as independent evidence can double count information, producing unwarranted confidence. This is relevant for multi-agent reasoning where several reports may share the same original source.

## Equation, symbols and domain

`Posterior odds = prior odds × likelihood ratio.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

A test with sensitivity 0.9 and false-positive rate 0.1 produces likelihood ratio nine for a positive result. Start with prior odds 1:1 and recover posterior 9:1, then document that these parameters were stipulated.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Incorrect prior odds, test calibration, dependence or selection bias can dominate conclusions. Posterior numerical precision does not establish causation.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares


---

# Chapter 16: Binomial counting and independence assumptions

**Discipline:** Probability. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

The binomial distribution counts successes in independent and identically distributed Bernoulli trials. It provides a baseline for uncertainty calculations and simple stochastic simulations. When physical conditions or human behaviors are correlated, a binomial model can understate uncertainty. A reconstructible probability reference states the number of trials, success definition, sampling independence and event probability explicitly.

## Equation, symbols and domain

`P(K=k)=C(n,k)p^k(1−p)^(n−k).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For two independent fair trials, exactly one success occurs with probability 2×0.5×0.5=0.5. If trials are perfectly correlated, the same calculation is invalid.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Repeating an experiment does not guarantee independence, and unknown success probabilities should not be declared exact merely because software accepts them.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 17: Numerical conditioning and stability

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Numerical conditioning concerns how small changes in inputs can affect a mathematically exact output; numerical stability concerns how the algorithm propagates its own rounding. These are separate ideas. A well-implemented solver cannot rescue a fundamentally ill-conditioned inverse problem without additional information. Source-level tests must include near-singular and out-of-domain cases, not only easy integer examples.

## Equation, symbols and domain

`κ(A)=||A||||A⁻¹|| when A is invertible; sensitivity scales with conditioning.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Consider a system whose two equations become almost identical. Tiny measurement noise may cause large parameter swings, even while the residual of a fitted solution appears small.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A small residual is not a guarantee of accurate parameters. Calculating an inverse explicitly is often less stable than solving via a factorization.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares


---

# Chapter 18: Discrete Fourier transform and spectral analysis

**Discipline:** Signal mathematics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Fourier analysis decomposes sampled signals into oscillatory components and supports filtering, communication, spectroscopy and model diagnostics. The discrete transform assumes finite sampled data and a particular normalization. Parseval’s theorem relates total squared signal magnitude to total spectral magnitude under matching conventions. Frequency resolution and aliasing depend on the sampling rate and duration, which cannot be recovered from an unlabeled vector alone.

## Equation, symbols and domain

`X_k=Σ_(t=0)^(N−1) x_t exp(−2πikt/N).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For samples [1,0,−1,0], compute the DFT and compare Σ|x|² to (1/N)Σ|X|². Record the sample interval before assigning physical frequencies.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A correct discrete spectrum does not prove the presence of a physical oscillator; windowing, noise and aliasing can create ambiguous peaks.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability


---

# Chapter 19: Differential equations and initial value problems

**Discipline:** Differential equations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Differential equations connect rates of change to a system’s current state. An initial condition selects a trajectory from a family of solutions. Existence and uniqueness require conditions such as local Lipschitz behavior; not every nonlinear model has a unique global solution. For physical reconstruction, preserve differential equations, parameter units, boundary/initial data and numerical method separately.

## Equation, symbols and domain

`y′=a y+b; y(t)=(y0+b/a)e^(at)−b/a for a≠0.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For y′=−y and y(0)=1, derive y(t)=e^(−t). Verify at t=1 with an independent numerical solver and compare the residual.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A differentiable fitted trajectory does not prove the proposed physical mechanism. Model coefficients from a past environment may not apply after material or equipment changes.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 20: Runge–Kutta methods and local error

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Runge–Kutta schemes approximate solutions by evaluating rates at multiple intermediate points. For sufficiently smooth problems, classical RK4 has fourth-order global accuracy as the step shrinks under suitable conditions. Stiff systems can behave poorly with explicit schemes despite small local residuals, so solver selection matters as much as step size. Numerical convergence should be tested against analytic cases and independent implementations.

## Equation, symbols and domain

`RK4: y_(n+1)=y_n+h(k1+2k2+2k3+k4)/6.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Use y′=−0.5y with y(0)=1 and t=1. Compare RK4 using 10, 20 and 40 steps with the analytic e^(−0.5) result and examine convergence.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

No fixed step count provides a universal guarantee for an unknown differential equation. Hidden discontinuities, stiffness and unbounded forcing can invalidate a simple error estimate.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 21: Partial differential equations and boundary conditions

**Discipline:** Differential equations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Partial differential equations model spatially distributed physical quantities. The same equation can describe different systems depending on boundary and initial conditions. Conservation-law derivations often yield flux-divergence forms, while constitutive relations determine material parameters. Finite differences must respect stability, boundary flux and domain geometry to avoid producing physically false results.

## Equation, symbols and domain

`∂u/∂t=D∂²u/∂x² for one-dimensional constant-D diffusion.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Discretize a three-cell diffusion profile with no-flux boundaries, and verify the sum stays constant for a stable explicit timestep under the declared coefficient.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A stable numerical solution may still use a wrong diffusion coefficient or ignore convection, reactions or electric fields. No semiconductor process recipe follows from this model.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability
- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles


---

# Chapter 22: Optimization, convexity and objective design

**Discipline:** Optimization. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Optimization converts a declared objective and constraints into a mathematical search. Convexity provides useful global guarantees when assumptions hold; outside convex settings gradient descent can reach local minima or saddle points. In AI training, a low mathematical loss need not correspond to useful or safe behavior, so optimization targets must be validated independently. Numerical step-size choices affect convergence.

## Equation, symbols and domain

`For positive-definite Q: minimize 0.5 xᵀQx−bᵀx; gradient Qx−b.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For Q=diag(2,2), b=(2,4), the minimum occurs at x=(1,2). Verify a bounded gradient descent sequence approaches that solution.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A strongly convex quadratic example is not a proof about neural network training or real-world utility. Constraints, metric weights and source data determine the actual objective.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 23: Softmax, log-sum-exp and numerical probability

**Discipline:** Optimization. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Softmax transforms finite logits into a normalized positive distribution. Subtracting the maximum avoids overflow without changing the ratio; the transformation illustrates algebraic invariance that improves numerical stability. In machine learning, model outputs after softmax are not automatically calibrated probabilities of truth. Data, training and evaluation design determine whether the scores are predictive.

## Equation, symbols and domain

`softmax_i(z)=exp(z_i−m)/Σ_j exp(z_j−m), m=max(z).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Compute softmax on [1000,1001] by first subtracting 1001, giving exp(−1)/(exp(−1)+1) and 1/(exp(−1)+1). Compare with [0,1].

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

High softmax confidence can accompany incorrect predictions. Temperature scaling or calibrations are empirical procedures and not inferred by normalization alone.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods
- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares


---

# Chapter 24: Newtonian mechanics and inertial frames

**Discipline:** Classical physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Classical mechanics provides a foundation for machine design, robotics and motion measurement. Newton’s laws apply in inertial frames under their classical scope. Position, velocity and acceleration carry different physical units, and time integration connects them. Real systems include forces and constraints that must be measured before a constant-acceleration formula can be trusted.

## Equation, symbols and domain

`F=ma; x(t)=x0+v0t+0.5at² for constant a.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

At x0=0,v0=1 m/s,a=2 m/s²,t=3s, compute x=12m and v=7m/s. Explain which forces would have to remain constant for this idealization to apply.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

At relativistic velocities or in non-inertial frames, ordinary formulas require correction. A calculated trajectory without calibrated forces and timing is not an observed motion.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions
- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026


---

# Chapter 25: Energy, momentum and conservation boundaries

**Discipline:** Classical physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Energy and momentum conservation provide necessary checks on mechanical systems. Conservation is applied to a named boundary, and real transfer can occur as work, heat, radiation or mass flow. Equating all energy input to kinetic energy while omitting losses invents performance. A clear ledger helps reconstruct machinery and efficient computation infrastructure from validated measurements.

## Equation, symbols and domain

`K=0.5mv²; ΔE_system=E_in−E_out under declared control boundary.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

A 1kg point mass moving at 2m/s has kinetic energy 2J. If friction dissipates one joule from an idealized system, mechanical kinetic energy cannot remain unchanged without another energy input.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A zero residual can be achieved by construction even with fictitious inputs. Conservation does not identify every loss path or validate a particular engine.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 26: Oscillators, modes and resonance

**Discipline:** Classical physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Simple harmonic motion links restoring force to oscillation frequency and conserved mechanical energy. It appears in vibrations, circuits, sensor design and approximation of stable equilibria. Resonance under forcing depends on damping and the source spectrum, not merely the undamped natural frequency. A structural or sensor model requires verified mass, stiffness and boundary conditions.

## Equation, symbols and domain

`m x″+k x=0, ω=sqrt(k/m), E=0.5mv²+0.5kx².`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For m=1kg,k=4N/m, the ideal angular frequency is 2rad/s. At displacement 0.5m and zero velocity, the elastic potential is 0.5J.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Material nonlinearities, damping, multiple modes, and resonant failure limits are omitted from the ideal model. No safe structural design follows from a single frequency.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions
- **MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011:** https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/ — scope: Initial value problems, linear ODE, Fourier, dynamics, numerical solution and stability


---

# Chapter 27: Electric charge, fields and potential

**Discipline:** Electromagnetism. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Electrical forces and potential energy arise from charges and electromagnetic fields. A field is defined locally and must be measured or computed from a complete boundary-value problem. Scalar voltage differences alone do not tell how a device behaves under load. Conductors, dielectrics, contact surfaces and time variation matter for real electronics.

## Equation, symbols and domain

`F=qE for a point charge in a specified static field; U=qV.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For a hypothetical positive charge q=1C in uniform E=2N/C, calculate force magnitude 2N. Then identify why an electric field assumption is essential to the example.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Continuum electrostatics ignores microscopic quantum effects and cannot certify safe wiring or field exposure. SI electric permittivity is experimentally adjusted, not an exact independent defining constant.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 28: Circuit dynamics and RC time constants

**Discipline:** Electromagnetism. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Lumped electrical circuits provide a model between field theory and computing hardware. Resistance and capacitance describe certain linear approximations, while transients require a differential equation. Charge conservation and Ohm’s law give an exponential relaxation for an ideal RC branch. Real components have tolerances, parasitic elements, breakdown and temperature dependence.

## Equation, symbols and domain

`V(t)=V0 e^(−t/RC), τ=RC for ideal capacitor discharge.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For R=1000ohm and C=0.001F, time constant is one second. From 10V at t=1s, the ideal voltage is 10/e volts.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

The equation is not a circuit construction guide or a safe discharge procedure. A correct RC trajectory does not establish isolation, grounding or electrical approval.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions


---

# Chapter 29: Maxwell equations and wave propagation

**Discipline:** Electromagnetism. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Maxwell’s equations unify electric and magnetic fields and describe waves under classical assumptions. Differential relations express source densities and local changes; integral forms relate field flux and circulation to charge and current. Applying boundary and material conditions is necessary before predicting propagation. The speed of electromagnetic waves in vacuum connects electromagnetic constants and the exact SI speed of light definition.

## Equation, symbols and domain

`∇·E=ρ/ε0, ∇·B=0, ∇×E=−∂B/∂t, ∇×B=μ0J+μ0ε0∂E/∂t.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

In charge-free vacuum, combine curl equations to motivate a wave equation with propagation speed c=1/sqrt(μ0ε0). Explain why vacuum ε0 and μ0 derived from adjusted constants are no longer separately exact.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Actual antennas, waveguides, dielectric losses and quantum material responses need additional constitutive models and measurements. No RF transmitter construction or exposure assessment is provided.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010:** https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/ — scope: Electrostatics, electricity, circuits, magnetic fields, Maxwell wave principles
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 30: Thermodynamic temperature and energy scales

**Discipline:** Thermodynamics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Temperature gives a natural energy scale through Boltzmann’s constant in thermal equilibrium models. Statistical mechanics connects microscopic states to bulk thermodynamics under ensembles and assumptions about independence or interactions. A scale kBT is not a promise that every particle has exactly that energy. Physical materials can be quantum degenerate or out of equilibrium, making classical approximations inadequate.

## Equation, symbols and domain

`E_thermal scale≈k_B T; β=1/(k_B T).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

At T=300K, compute kBT with the exactly defined SI constant 1.380649×10^-23J/K, then convert the result to electronvolts.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A thermal-energy scale is not a measured material heat capacity, reaction barrier or safe equipment limit. Temperature gradients require non-equilibrium treatment.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 31: Special relativity and spacetime consistency

**Discipline:** Relativity. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Special relativity constrains measurements of time, length, momentum and energy across inertial frames. It becomes essential near light speed and for particle and electromagnetic physics. The Lorentz factor diverges as speed approaches c, while classical formulas are reasonable low-speed approximations. A physics reference should distinguish exact equations in a model from numerical values of particle properties obtained experimentally.

## Equation, symbols and domain

`γ=1/sqrt(1−v²/c²), |v|<c.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

At v=0 calculate γ=1. At v=0.6c, compute γ=1.25. Compare qualitatively with the classical low-velocity limit.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

No general relativity, gravitational curvature, accelerated frames or measured high-energy experiment is simulated. Never evaluate a real-valued γ with |v|≥c.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **OpenStax University Physics Volume 1, 2016:** https://openstax.org/books/university-physics-volume-1/pages/1-introduction — scope: Classical mechanics, units, conservation laws, energy and relativity introductions
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 32: Quantum state amplitudes and Born measurement

**Discipline:** Quantum physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Quantum mechanics uses complex amplitudes to predict measurement probabilities. A state vector is not a classical probability list: phases matter for interference even though a single basis measurement records amplitude magnitudes squared. Normalization ensures probabilities sum to one. This framework is necessary to understand semiconductor electronic structure and future quantum technologies, but abstract probabilities do not demonstrate quantum hardware.

## Equation, symbols and domain

`P(i)=|ψ_i|²/Σ_j |ψ_j|² for finite state coordinates.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For amplitudes [1,i], compute equal probabilities after normalization. Replace i with -i: the same measurement probabilities result in this basis, even though phase relationships may affect later interference.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Physical amplitudes require a defined Hilbert space, apparatus and measurement basis. A two-component simulation cannot certify quantum computing, entanglement generation or device fidelity.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.04 Quantum Physics I, Spring 2016:** https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/ — scope: Wavefunctions, measurement, Schrödinger equation, quantum state operators
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 33: Schrödinger equation and Hamiltonian modeling

**Discipline:** Quantum physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

The Schrödinger equation connects quantum-state evolution to a Hamiltonian representing the system. Stationary eigenstates and their energies depend on boundary conditions and interactions. Electron behavior in materials also requires many-body approximations and measured validation. The formal equation is foundational for understanding chemical bonding, semiconductor bands and computational quantum models.

## Equation, symbols and domain

`iℏ∂ψ/∂t=Hψ; Hψ=Eψ for stationary states.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For a two-state diagonal Hamiltonian with energies E1 and E2, reason that each basis component accumulates phase exp(−iEt/ℏ). The magnitude squared of each isolated component remains constant.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Without a specified physical Hamiltonian and boundary conditions, the equation alone predicts no measured material property. Many-electron and decoherence effects are omitted.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.04 Quantum Physics I, Spring 2016:** https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/ — scope: Wavefunctions, measurement, Schrödinger equation, quantum state operators
- **NIST CODATA Recommended Fundamental Constants, 2022 adjustment:** https://physics.nist.gov/cuu/Constants/ — scope: NIST versioned fundamental physical constants; distinguish exact SI defining constants from adjusted measurements


---

# Chapter 34: Heisenberg uncertainty and measurement meaning

**Discipline:** Quantum physics. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Quantum uncertainty bounds arise from noncommuting observables and the mathematical structure of state variances. This is not a statement that laboratory equipment is merely too imprecise: the bound applies to state preparation and measurement distributions in quantum theory. Actual instrumentation contributes additional classical uncertainty and systematic error, which needs a separate budget.

## Equation, symbols and domain

`Δx Δp ≥ ℏ/2 for compatible position/momentum observables.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

For a chosen position standard deviation Δx, use the bound to determine the minimum allowed momentum standard deviation. Explain why an instrument calibration cannot simply remove the quantum relation.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A product bound does not identify a unique state or particle trajectory. Applications must specify operators, state preparation, units and conditions.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 8.04 Quantum Physics I, Spring 2016:** https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/ — scope: Wavefunctions, measurement, Schrödinger equation, quantum state operators
- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions


---

# Chapter 35: Covariance and propagated measurement uncertainty

**Discipline:** Metrology. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

Measurement results require uncertainty as well as a numerical estimate. When inputs are correlated, a propagation formula that ignores covariance can be misleading. This matters for scientific knowledge that must survive multiple instrument generations and software implementations. The uncertainty budget should retain calibration, resolution, physical model and statistical sampling information rather than a guessed final percentage.

## Equation, symbols and domain

`For z=ab, u_z²≈b²u_a²+a²u_b²+2abCov(a,b).`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Let a=2±0.1, b=3±0.2 with zero covariance. Then z=6 and propagated standard uncertainty is sqrt(0.09+0.16)=0.5. Repeat with known positive covariance.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

This is a first-order local approximation. Large nonlinear uncertainty, dependence on unknown common sources and non-Gaussian distributions require more advanced methods.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions
- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026


---

# Chapter 36: Inverse problems and scientific identifiability

**Discipline:** Numerical computation. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

An inverse problem infers hidden causes or parameters from observations. Even exact observations may be insufficient when multiple parameter sets produce identical outputs. Rank and nullspace analysis make the problem visible in linear settings. Regularization supplies additional assumptions and can improve numerical behavior, but it does not magically create measurement evidence. This issue appears in tomography, model training and system diagnostics.

## Equation, symbols and domain

`Given y=F(θ), uniqueness of θ requires injectivity over the admissible model domain.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Observe y=x1+x2=5. Both (2,3) and (1,4) fit exactly; a second independent observation is necessary to identify both unknowns without a prior.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

A unique numerical minimum may be induced by regularization rather than by data. Report prior assumptions and identifiable observables separately.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Engineering Metrology and Uncertainty Guidelines:** https://www.nist.gov/pml/nist-technical-note-1297 — scope: Source-scoped uncertainty budgets, sensitivity, covariance and reporting conventions


---

# Chapter 37: From linear algebra to neural network computation

**Discipline:** AI foundations. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

A neural network can be understood as a composition of affine maps and nonlinear activation functions. Matrix operations provide the bulk computation, while derivatives propagate sensitivity during training. The mathematical representation is portable across CPU, GPU and other architectures if numerical formats and operator definitions are preserved. A successful calculation, however, does not show that the trained system understands science or generalizes to unseen data.

## Equation, symbols and domain

`Layer map y=σ(Wx+b); gradients follow the chain rule and matrix transposes.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Take a one-layer model with W=[[2,0]], b=[1], input x=[3,4] and identity activation, yielding output seven. Compute derivative of output with respect to x.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

Loss functions, data, numerical precision and training dynamics require independent evaluation. This chapter neither trains a foundation model nor measures AI benchmark improvement.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **MIT OpenCourseWare 18.06 Linear Algebra, Spring 2010:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — scope: Matrix theory, elimination, linear maps, eigenvalues, orthogonality and least squares
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

# Chapter 38: Rebuilding an offline scientific computing stack

**Discipline:** Knowledge continuity. **Release:** Mathematical and Physical Sciences Atlas 0.1.0. **Evidence:** original educational synthesis under stated source scope; no original publisher file or physical measurement acquired.

## Scientific meaning and prerequisite concepts

The purpose of the Atlas is to preserve enough mathematics and physics to rebuild scientific tools and advanced AI without depending on today’s cloud providers. Human-readable derivations must accompany executable algorithms, exact provenance and failure examples. Source URLs are useful but cannot replace authenticated original transport bytes. Future readers need to recreate the reasoning, verify it on independent measurements and connect it to computing architecture, compilers and materials science.

## Equation, symbols and domain

`Verified source bytes + units + derivations + executable tests + uncertainties + rights → qualified reusable reference.`

Each numerical value has a mathematical space, unit or dimensionless convention. A model result is conditional on declared boundaries and inputs. Mathematical identities are different from empirically confirmed physical laws.

## Derivation and reproducible reasoning

Start from the stated definitions, inspect any conservation or continuity condition, and transform the expression using valid algebra under those assumptions. Exact integer/rational methods give strong finite certificates where applicable, whereas numerical methods need truncation, rounding and stability checks. A later researcher must be able to distinguish the proof from the measured quantity that would make the model predictive. Keep the full parameter values and units, not just a plotted conclusion.

## Worked reconstruction, with independent checks

Reproduce a rational solve, Simpson integration, RK4 ODE and a two-level Born probability using plain Python, then identify the missing source or instrument data for a real physical case.

Recalculate first by hand, then reproduce with the bounded Python kernel if a corresponding method exists. Use a deliberate negative example to test refusal or uncertainty. This example was authored for the Atlas and is not a physical experiment.

## Boundary, counterexample and uncertainty

This first edition is an intentionally scoped scientific reference. It is not a university-equivalent complete corpus, original experimental result, working processor or fully offline archive of publisher literature.

The software cannot certify calibrated instruments, physical hardware behavior, or a new scientific discovery. Original published tables and course materials were not copied; preserve legally reusable source material and provenance separately when actually acquired.

## Publisher references, bibliographic only

- **BIPM, SI Brochure Ninth Edition, revised June 2026:** https://www.bipm.org/en/si-brochure-9 — scope: Official SI defining constants and unit descriptions, complete brochure revision 4.01 June 2026
- **NIST Digital Library of Mathematical Functions, version 1.2.8 (September 2026):** https://dlmf.nist.gov/ — scope: Official mathematical introduction, algebraic/analytic methods, special functions and numerical methods


---

## Reproducible constructed cases
# Mathematics & Physics v0.1.0 — Original Constructed Casebook

**Evidence label:** 22 project-authored finite examples. These are not experimentally measured physics or an AI performance benchmark. Reproduce with `python -m math_physics_atlas` and independent arithmetic.

## Case 01: Exact rational 2x2 solution

**Domain:** Unique square linear system. **Passed original program check:** True.

```json
{
  "solution_fractions": [
    "2",
    "1"
  ],
  "solution_floats": [
    2.0,
    1.0
  ],
  "exact_residual_zero": true,
  "scope": "unique square rational linear system, not general overdetermined fitting"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 02: Matrix multiplication

**Domain:** Linear maps only; input dimensions matter. **Passed original program check:** True.

```json
[
  [
    11.0
  ]
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 03: Orthogonal projection

**Domain:** Euclidean inner product. **Passed original program check:** True.

```json
{
  "projected": [
    3.0,
    0.0
  ],
  "perpendicular_residual": [
    0.0,
    4.0
  ],
  "coefficient": 3.0,
  "orthogonality_residual": 0.0
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 04: Least squares straight line

**Domain:** Full column rank, normal equations only. **Passed original program check:** True.

```json
{
  "parameters": [
    1.0,
    2.0
  ],
  "squared_residual": 0.0,
  "normal_equation_residual": [
    0.0,
    0.0
  ],
  "limitations": [
    "Normal equations square the condition number; use stable QR/SVD on real data",
    "No physical model or independent fitted dataset verified"
  ]
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 05: Polynomial derivative

**Domain:** Power rule for polynomials. **Passed original program check:** True.

```json
[
  3.0,
  8.0
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 06: Central finite difference

**Domain:** Discretization and rounding error. **Passed original program check:** True.

```json
4.000000000004
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 07: Exact polynomial integral

**Domain:** Antiderivative formula. **Passed original program check:** True.

```json
9.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 08: Simpson cubic integral

**Domain:** Uniform even intervals; polynomials of degree up to three. **Passed original program check:** True.

```json
4.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 09: Exponential ODE

**Domain:** Constant coefficient scalar ODE. **Passed original program check:** True.

```json
0.7357588823428847
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 10: RK4 ODE convergence

**Domain:** Finite step stability not proven for arbitrary ODEs. **Passed original program check:** True.

```json
{
  "numerical_y": 0.6065306597142194,
  "analytic_reference": 0.6065306597126334,
  "steps": 100,
  "scope": "scalar linear yprime=ay+b with constant a,b, no general ODE guarantees"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 11: Parseval DFT identity

**Domain:** Finite discrete transform with specified normalization. **Passed original program check:** True.

```json
{
  "time_energy": 2.0,
  "frequency_energy": 2.0,
  "scope": "Parseval energy, unnormalized forward DFT, no physical sampling or aliasing assessment"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 12: One bit entropy

**Domain:** Shannon discrete probabilities, not physical disorder. **Passed original program check:** True.

```json
1.0
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 13: Bayesian evidence update

**Domain:** User-chosen likelihoods, no true outcome inference. **Passed original program check:** True.

```json
{
  "posterior_H1": 0.9,
  "evidence_probability": 0.5,
  "scope": "chosen prior and likelihood, not real event validation"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 14: Binomial count

**Domain:** Independent identical Bernoulli trials. **Passed original program check:** True.

```json
0.5
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 15: Stable softmax

**Domain:** Probability transform, not calibrated model confidence. **Passed original program check:** True.

```json
[
  0.5,
  0.5
]
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 16: Quadratic gradient descent

**Domain:** Strongly convex strictly diagonal dominant Hessian. **Passed original program check:** True.

```json
{
  "solution": [
    1.0,
    2.0
  ],
  "objective": -5.0,
  "gradient_norm": 0.0,
  "scope": "strictly diagonally dominant symmetric positive quadratic only; other objectives need separate solvers"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 17: Constant acceleration kinematics

**Domain:** One dimensional classical motion. **Passed original program check:** True.

```json
{
  "position_m": 12.0,
  "velocity_m_s": 7.0,
  "scope": "one-dimensional constant acceleration in chosen inertial frame; no air drag or relativistic correction"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 18: Spring potential energy

**Domain:** Lossless linear spring within elastic range. **Passed original program check:** True.

```json
{
  "energy_J": 0.5,
  "angular_frequency_rad_s": 2.0,
  "scope": "ideal linear lossless spring, no forced/driven dynamics, validated material stress or safety"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 19: RC exponential decay

**Domain:** Ideal components, no hardware approval. **Passed original program check:** True.

```json
{
  "voltage_V": 3.6787944117144233,
  "time_constant_s": 1.0,
  "scope": "ideal RC discharge, lumped model, no actual wiring/voltage safety approval"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 20: Photon energy

**Domain:** Vacuum photon, not a measured absorption spectrum. **Passed original program check:** True.

```json
{
  "energy_J": 3.972891714297857e-19,
  "energy_eV": 2.479683968664005,
  "scope": "single photon in vacuum; not a particular material absorption spectrum"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 21: Quantum Born probabilities

**Domain:** Abstract normalized two-level state. **Passed original program check:** True.

```json
{
  "probabilities": [
    0.5,
    0.5
  ],
  "original_norm_squared": 2.0,
  "scope": "finite dimensional pure state Born rule, no claim of quantum computer or measurement"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.

## Case 22: Product uncertainty

**Domain:** Linear error propagation with zero covariance. **Passed original program check:** True.

```json
{
  "value": 6.0,
  "standard_uncertainty": 0.5,
  "scope": "first-order uncertainty approximation with caller supplied covariance, no calibrated measurements"
}
```

An identical software result is a necessary mathematical regression check, not empirical proof of the underlying physical model.



## Source and rights register
# Mathematics & Fundamental Physics Atlas v0.1.0 — source navigation

**Source grade:** ten bibliographic/selected-page references, zero authenticated publisher original file bytes. Original written lessons are independent educational syntheses, not mirrors of publisher materials. MIT OCW and OpenStax reuse rights are source-/edition-specific.

## BIPM-SI

- Official link: https://www.bipm.org/en/si-brochure-9
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## NIST-CODATA

- Official link: https://physics.nist.gov/cuu/Constants/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## NIST-DLMF

- Official link: https://dlmf.nist.gov/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## NIST-UNCERTAINTY

- Official link: https://www.nist.gov/pml/nist-technical-note-1297
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## MIT-LA

- Official link: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## MIT-CALCULUS

- Official link: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## MIT-ODE

- Official link: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## MIT-PHYS

- Official link: https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## MIT-QUANTUM

- Official link: https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**

## OPENSTAX-PHY

- Official link: https://openstax.org/books/university-physics-volume-1/pages/1-introduction
- Scope: selected public publisher description and foundational terminology for the associated chapters
- Source original bytes locally authenticated: **no**
- Independent scientific peer review: **no**
- Reproduction rights for original publisher resources: **not independently cleared**



## Scientific survival charter
# ATLAS FORGE — Human Knowledge Survival Charter

**Edition 1.0 · 13 November 2026 · Foundational design contract**  
**Owner's standard:** Construct the collection as though it might be the last usable store of humanity's knowledge. **This is an aspiration and an acceptance criterion, not a claim that the existing collection already holds all human knowledge.**

## 1. The standard

A useful surviving library must allow future readers—human or machine—to recover **what a proposition means**, **why it was believed**, **how its supporting observation was obtained**, **how to reproduce the calculation or experiment**, **where its limits lie**, and **how it interacts with knowledge elsewhere**. Merely saving abstracts, embedding vectors, URLs, or a popular conclusion cannot preserve a scientific civilization's reasoning. An equation without symbols and units can be useless or dangerous; a measured number without instrument, sample and conditions is not transferable; a source summary without attribution cannot be corrected when the original disappears.

The library must work in stages of resource scarcity. At the lowest level a reader has only a filesystem and a UTF-8 text viewer. The next level has a standard Python interpreter and a modest CPU. Higher levels may use relational databases, specialized solvers, GPU models and search indexes. No critical theorem, provenance declaration, or document location may *require* proprietary cloud authentication, a vector index, or a language model to be decoded. Bitwork-powered routing, when built at the end of the 30-domain content program, will accelerate retrieval but must not be the only path to knowledge.

## 2. Every domain's minimum scientific package

A finished content domain needs original explanatory chapters and navigable source cards, but **volume is insufficient**. A chapter should cover: the question, definitions and physical/mathematical objects, variables and units, relevant historical foundations, assumptions, derivation or causal mechanism, observation/experiment or computational method, an independently reproducible numerical or procedural example, competing or contradictory views, uncertainty, invalid use cases, and connections to other chapters. Algorithms need versioned source code and known tests; a simulation must identify its assumptions and seed. A failure case is part of the knowledge, not noise to delete.

It should be possible for an apprentice to begin with basic prerequisites, build a working understanding, and tell what additional data would be needed to solve a real problem. **No fabricated confidence, novelty, measurement, or peer review.** If a gap prevents an answer, preserve the gap and the experiment that would resolve it. Verified, refuted, contradicted, plausible, and unknown claims remain distinguishable.

We preserve at least three distinct representations: readable **UTF-8 Markdown**, machine-readable **canonical JSON/JSONL** with explicit schema and qualified links, and executable **plain Python** or well-specified pseudocode where computational knowledge is essential. Tabular datasets should use documented field names, units, missing-value semantics and reproducible parsing. Non-text scientific media require an accessible descriptive equivalent (equations, alt text, dimensions and metadata) without falsely claiming the textual description reproduces their full data.

## 3. Evidence ranks are not ratings of truth

Evidence is recorded by access and validation capability, not compressed to one misleading percentage:

- **L0 — Citation or unresolved locator.** A source is named; its bytes and exact passages may be unavailable. Useful as a lead, **not independently recoverable**.
- **L1 — Source-scoped notes.** A selected passage, metadata or publisher abstract was reviewed and paraphrased. Original file still may be missing and rights remain external.
- **L2 — Locally retained source bytes with provenance and permitted rights.** Include canonical origin, retrieval date, SHA-256, parser version, license and exact inspected portion. A hash proves bytes, not accuracy.
- **L3 — Reproduced analysis against an authentic documented dataset.** Include original raw bytes where legally permitted, transformation scripts, outputs and discrepancies; still distinct from conducting the original laboratory experiment.
- **L4 — Independently corroborated science.** Separate scientific teams, data or high-quality methodological reviews support the claim under specified conditions; evidence and disagreement must be retained. This cannot be conferred by passing unit tests.

These levels describe *specific claims and sources*, not entire domains. A repository may have L3 mathematical code and only L0 primary research. **Never display L2–L4 without the applicable supporting files and reviewer attribution.** A paper's two different webpages may be one experiment; don't count them as two replications. Raw observations are retained separately from normalized derived values.

## 4. Reproducibility and recovery requirements

Every tagged release should have a self-consistent tree manifest, hash list, schemas, environment requirements, tests, known failures, an offline reading index and a `RESTORE` guide. Preserve immutable previous revisions and add explicit supersession/contradiction relationships instead of editing history to look consistent. The release should be extracted on a clean machine and verified without network access. A knowledge reader must be able to inspect the original chapters even when packages cannot install. A Python-only audit should enumerate source gaps, verify hashes and report potential dependence on online services.

Record the algorithms of human knowledge production: how to form hypotheses; design fair comparisons; calibrate an instrument; collect raw data; distinguish association from causation; quantify uncertainty; falsify claims; and update records after contradictory evidence. Preservation cannot be purely static. Scientific progress requires an *audit of corrections*.

Redundancy is not equal to backup. The final deployment plan should include three separately verified copies, more than one geographic/storage failure domain, periodic fixity checks, read-only archives, documented encryption/key custody where needed, durable software versions and periodic migration of fragile file formats. This program **has not implemented that final off-site archival infrastructure**; the charter specifies its eventual acceptance test. An untested copy is not a verified restore.

## 5. Human and AI pathways

For a human: start with a domain map, prerequisites, explanation, practical worked example, full source citation and failure scenarios. For an AI: return a **bounded citation package** containing a claim, exact source and revision, units and applicability, assumptions and uncertainty, contradiction links and abstention reason. A retrieval score is not scientific credibility. Retrieved documents remain untrusted data, never executable tool instructions or permission grants. A useful result can be **we don't know**, together with a testable plan to learn it.

Memory and self-improvement must be evaluated on independently authored held-out tasks, with precommitted rubrics and budgets, appropriate baseline, truthful uncertain outcomes, effect size and cost, plus tests against contamination and regressions. A cached answer that sounds convincing does not establish learning. Do not use this archive's own teaching tests as a hidden benchmark for models it has taught.

## 6. Build order and discipline

The thirty-domain roadmap governs **content order**. Signal and Cymatics are preserved companion nodes; Measurement, Causal, Materials, Control and Agent are the content domains already built to differing maturity. Subsequent domains will build their complete depth before being considered ready. Agent Atlas is moving toward a scoped v1, followed by Computation Atlas. **Bitwork routing comes only after all thirty domain libraries' content editions**, then comparative integration/evaluation and desktop transfer. Do not opportunistically change the router during corpus authoring. The shared Forge contract must remain versioned and source-closed.

Release labels are always two-dimensional: `content_scope_ready` and `scientific_or_deployment_accepted`. We can call the bounded content edition 1.0 while still honestly retaining unresolved independent review, third-party source acquisition, and live AI measurements. The survival standard means each remaining dependency is **visible and recoverable**, not silently presumed solved.

## 7. What this archive cannot yet claim

As of this charter, it is **not humanity's comprehensive knowledge**, is **not offline-complete for the primary sources it cites**, is **not independently peer-reviewed**, and has **not deployed its final cross-domain routing or distributed backup system**. In particular, many source cards link to web material whose original bytes are not archived. This is a critical survivability debt, not a superficial TODO. Resolve it with appropriately licensed copies, durable identifiers, bibliographic facts and original explanatory reconstruction where reuse rights are restricted.

**Acceptance phrase:** *Every important conclusion must survive with its proof path, limits, and a way to learn more—not merely its words.*

**References:** Library of Congress, *Recommended Formats Statement 2025–2026*, particularly datasets and open character-based formats (https://www.loc.gov/preservation/resources/rfs/data.html); Sutton and Barto, *Reinforcement Learning: An Introduction*, second edition (MIT Press, 2018); OpenTelemetry agent trace conventions; primary sources referenced in each Atlas node. This charter is original project policy, not an international preservation standard or proof of completeness.



---

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


---

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


---

# Chapter 41: Radix-two FFT, spectral sampling and aliasing tests

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `X[k]=Σₙ₌₀ᴺ⁻¹ x[n]e^(−2πikn/N); x[n]=(1/N)Σₖ X[k]e^(+2πikn/N).`

**Reference algorithm:** `math_physics_atlas.v02_models.fft_radix2(samples, inverse)`

**Units:** Input samples carry signal units; DFT has input units under unnormalized forward definition, and frequencies require an explicit sample interval.

## Why a fast transform is more than an optimization
A discrete Fourier transform rewrites an evenly sampled finite sequence as a weighted sum of complex exponentials. It supports spectral diagnosis, filters, convolution, digital communications and the linear algebra used inside AI systems. The direct formula has N² complex multiply-adds. For N=2ᵐ, the Cooley–Tukey decomposition splits even- and odd-index samples into two length N/2 transforms and combines them using roots of unity. Its operation count scales with N log₂N, making large experiments feasible without a specialized scientific stack.

## Derive the butterfly
Take x[2j] and x[2j+1]. Then X[k]=E[k]+ωᴺᵏ O[k], where ωᴺ=e^(−2πi/N), and E,O are the DFTs of the even and odd subsequences. Because ωᴺ^(k+N/2)=−ωᴺᵏ, X[k+N/2]=E[k]−ωᴺᵏ O[k]. The butterfly therefore combines two half-size transforms with a single phase multiplier. Iterative bit reversal places the leaves in the order needed to perform these in-place butterflies from length 2 to N. The inverse conjugates the sign of the exponent and divides by N. State your normalization: the unnormalized forward transform obeys Σ|x[n]|²=(1/N)Σ|X[k]|² (Parseval identity).

## Reconstruct and inspect
For x=[0,1,0,0], each sample is zero except n=1, so X[k]=e^(−2πik/4)=[1,−i,−1,+i]. The inverse returns the original impulse. A single complex sinusoid with k=3 and N=16 gives one nonzero bin of magnitude 16; a real cosine splits into symmetric positive/negative frequency bins. A separate NumPy FFT checks 200 seeded arrays and the inverse reconstruction. The benchmark reports absolute errors and case counts; it does not establish CPU performance against optimized native libraries.

## Aliasing and leakage are scientific limitations
If a continuous signal has frequency f and a sampler takes values every Δt, f and f+k/Δt can generate indistinguishable samples for integer k. The Nyquist bound |f|<1/(2Δt) is a sampling condition, not an FFT error message. Finite time windows leak energy across bins when a tone does not fit an integer number of cycles. An FFT cannot reconstruct frequencies or phases that acquisition discarded. With no sample interval, X[k] is only a sequence of coefficients, not a physical spectrum in hertz.

## Technology continuity link
Keep the transform convention, units, sampling metadata, numerical test vectors, anti-alias requirements and counterexamples. These are the minimum ingredients for rebuilding spectrum analyzers, digital oscilloscopes and fast convolution.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Only power-of-two N≤4096 and finite scalar samples. Sampling cannot distinguish frequencies separated by integer multiples of sample rate.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.


---

# Chapter 42: Adaptive nonlinear ODE integration and local error estimation

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `y′=f(t,y); e≈|y_(h/2,h/2)−y_h|/15 for an RK4 pair under smoothness and asymptotic assumptions.`

**Reference algorithm:** `math_physics_atlas.v02_models.nonlinear_rk4_adaptive(rhs, t0, y0, t1)`

**Units:** t in seconds, y in problem-specific units, f in y units per second; absolute error tolerance in y units.

## From physical laws to trajectories
A state equation y′=f(t,y) plus an initial condition defines an initial-value problem under the usual regularity conditions. The fourth-order Runge–Kutta method computes four slopes: k₁=f(t,y), k₂=f(t+h/2,y+hk₁/2), k₃=f(t+h/2,y+hk₂/2), k₄=f(t+h,y+hk₃). Their weighted sum gives y_{n+1}=y_n+h(k₁+2k₂+2k₃+k₄)/6. Fixed h is often wasteful in smooth regions and inaccurate near rapid changes. Adaptive integration estimates how a shorter step changes the answer.

## Richardson step doubling
Assume a smooth nonstiff solution and the RK4 local truncation error behaves like C h⁵. One full step has leading error C h⁵. Two consecutive half steps accumulate approximately C h⁵/16. Thus the difference between the two estimates is approximately 15C h⁵/16. Dividing by 15 estimates the fine path error. Adding (y_fine−y_full)/15 is a fifth-order Richardson correction in the asymptotic regime. Choose the next h in proportion to (tolerance/error)^(1/5), bounded between conservative shrinking and growth factors. Every step checks that time advances and the derivative remains finite. Both the initial state and absolute tolerances have physical units.

## Worked logistic example
With growth rate 1 s⁻¹, y′=y(1−y) and y(0)=0.1, separation of variables yields log(y/(1−y))=t−log 9, so y(t)=1/(1+9e^(−t)). At t=2 s the solution is approximately 0.45085306. Generate a finite numerical trace at several tolerances and compare to the analytic formula. A separate oracle checks 120 seeded initial conditions and horizons. Do not label this an observed biological growth curve; it is a constructed differential equation with stipulated parameters.

## Negative experiments and limits
For y′=−1000y, the explicit RK4 stability region places restrictions on h even if a step starts with small apparent state variation. An adaptive local-error controller is not a trustworthy stiff integrator; seek an implicit method with a stability analysis. Discontinuous right-hand sides, impulses, unknown initial states and event-triggered changes require separate modeling. When a budget is exhausted, raise an error; silently returning a partial trajectory would falsely report a completed simulation.

## Technology continuity link
This small solver supports offline models of thermal response, chemical kinetics, population systems and controller dynamics. Document the RHS, tolerances, units, step acceptance and exact comparison case so future users can reproduce the numerical process.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Step-doubling local tolerance is not a proof of global error or stiff-system stability. Refuses invalid initial/time domains and step-budget exhaustion.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.


---

# Chapter 43: Heat equation, diffusion stability and bounded temperature fields

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `∂T/∂t=α∂²T/∂x²; Tᵢⁿ⁺¹=(1−2r)Tᵢⁿ+r(Tᵢ₋₁ⁿ+Tᵢ₊₁ⁿ), r=αΔt/Δx²≤1/2.`

**Reference algorithm:** `math_physics_atlas.v02_models.heat1d_dirichlet(initial, alpha, dx, dt, steps)`

**Units:** x [m], t [s], thermal diffusivity α [m²/s], temperature difference [K]; Fourier number αΔt/Δx² dimensionless.

## Governing physical assumption
For a homogeneous medium with constant volumetric heat capacity and conductivity, Fourier conduction plus energy balance leads to ∂T/∂t=α∂²T/∂x², where α=k/(ρc_p) has units m²/s. For a nonuniform or phase-changing medium this simplified equation is no longer sufficient; additional material functions and boundary fluxes are required. The atlas kernel uses a temperature *difference* relative to a fixed-temperature reference so that both end points can be represented as zero without confusing 0 K with an ordinary room boundary.

## Finite-difference reconstruction
On a uniform grid xᵢ=iΔx, the centered approximation to ∂²T/∂x² is (Tᵢ₋₁−2Tᵢ+Tᵢ₊₁)/Δx². With forward Euler time stepping, define r=αΔt/Δx² and obtain Tᵢⁿ⁺¹=(1−2r)Tᵢⁿ+rTᵢ₋₁ⁿ+rTᵢ₊₁ⁿ. If 0≤r≤1/2, these are nonnegative weights summing to one. Each interior update is a convex combination, so a nonnegative initial profile with fixed-zero boundaries remains nonnegative and cannot generate a new maximum. This discrete maximum-principle argument both motivates the numerical stability limit and exposes a physical constraint test. It is stronger than merely looking for non-finite numbers.

## Exact separable manufactured solution
For T(x,0)=sin(πx/L), T(0,t)=T(L,t)=0, set T(x,t)=X(x)G(t) to obtain G′/G=αX″/X=−α(π/L)². Therefore T(x,t)=sin(πx/L)exp[−α(π/L)²t]. At L=1 m and α=0.1 m²/s, the center decays as exp(−0.1π²t). Sample N=40 intervals and r=0.25, integrate 60 steps, compare the whole numerical field with this continuous reference. The difference is discretization error; refining Δx while keeping r fixed should reduce it. An independent oracle checks 100 finite eigenmode cases.

## Negative controls
When r>1/2, a grid-scale alternating mode can grow with the explicit update even though the continuous heat equation smooths disturbances. The kernel rejects that region rather than delivering a plausible but unstable plot. It also rejects nonzero boundary values, inconsistent grid size, negative diffusivity and nonfinite inputs. A stable numerical profile does not validate the chosen k, ρ or c_p for an actual material; preserve empirical provenance separately.

## Technology continuity link
Diffusion models are useful for IC thermal design, process control, precision machining and battery management. Engineers must extend them to heterogeneous materials and real boundary conditions before applying results to equipment.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** One-dimensional constant-diffusivity linear conduction with fixed-zero Dirichlet boundaries only; refuses Fourier number >1/2. Not a calibrated materials-property or heat-transfer prediction.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.


---

# Chapter 44: Wave equation, leapfrog propagation and electromagnetic scope

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `u_tt=c²u_xx; uᵢⁿ⁺¹=2uᵢⁿ−uᵢⁿ⁻¹+λ²(uᵢ₋₁ⁿ−2uᵢⁿ+uᵢ₊₁ⁿ), λ=cΔt/Δx≤1.`

**Reference algorithm:** `math_physics_atlas.v02_models.wave1d_dirichlet(displacement, c, dx, dt, steps)`

**Units:** displacement u [application units], wave speed c [m/s], x [m], t [s]; Courant cΔt/Δx dimensionless.

## Field equations and their reduction
A one-dimensional scalar wave u_tt=c²u_xx represents transverse-string displacement, simple acoustic potential or a component of a propagating field only under additional assumptions. Maxwell's equations in a homogeneous source-free vacuum give ∇×E=−∂B/∂t and ∇×B=μ₀ε₀∂E/∂t. Taking the curl of Faraday's law and applying ∇×(∇×E)=∇(∇·E)−∇²E with ∇·E=0 yields ∂²E/∂t²=c²∇²E, c=1/√(μ₀ε₀) in the vacuum constitutive model. The reduction is not equivalent to validating a full electromagnetic solver: vector polarizations, boundary conditions, sources and material constitutive laws have been removed.

## Centered-time and centered-space stencil
Approximating the second time derivative by (uᵢⁿ⁺¹−2uᵢⁿ+uᵢⁿ⁻¹)/Δt² and second spatial derivative by (uᵢ₋₁ⁿ−2uᵢⁿ+uᵢ₊₁ⁿ)/Δx² gives the leapfrog update. To initialize with zero velocity, Taylor-expand u(x,Δt)=u(x,0)+(Δt²/2) c²u_xx(x,0)+O(Δt³); the first discrete step carries half the spatial second-difference coefficient. A Fourier mode e^(ik iΔx) has amplification governed by cos(ωΔt)=1−2λ²sin²(kΔx/2). Real ω for all resolved modes requires λ=cΔt/Δx≤1. A bound on grid growth is not a validation of physical boundary reflections.

## Worked eigenmode with real units
For a length-L region with u=0 at each endpoint, u(x,0)=sin(πx/L) and u_t(x,0)=0, separation of variables gives u(x,t)=sin(πx/L)cos(cπt/L). With L=1 m, grid Δx=1/40 m and λ=0.5, evolve 40 discrete steps and compare against the analytic field. The small phase error should reduce with refinement. Change λ to 1.1: the code must reject the step before producing unbounded numerical oscillations. A separate oracle compares 100 randomized finite grids and wave speeds; there are no antennas, oscilloscopes or radiation measurements involved.

## Physical and numerical cautions
An actual FDTD Maxwell calculation would require staggered E and H components, consistent permittivity and permeability, source injection, absorbing boundaries, magnetic/electric energy checks, mesh convergence, and measured validation. At a material interface the simple constant-c wave equation is insufficient. Do not infer semiconductor device performance, radio transmitter range, or electromagnetic compliance from this scalar toy model. Explicitly preserve the numerical reduction and its limits.

## Technology continuity link
Understanding wave propagation and discrete stability is a prerequisite for reconstructing signal timing, acoustics, optics, radio and numerical field computation. This is a teachable foundation, not a production field simulator.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 8.02SC Electricity and Magnetism, Fall 2010](https://ocw.mit.edu/courses/8-02sc-physics-ii-electricity-and-magnetism-fall-2010/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Scalar 1D wave with fixed-zero ends and zero initial velocity; not a Maxwell field solver, transmission-line impedance model, or radiation prediction.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.


---

# 45 — Reconstructing rectangular singular-value decomposition with one-sided Jacobi rotations

**ATLAS FORGE Mathematics & Fundamental Physics, v0.3.0.** Original educational chapter; not a claim of a new algorithm, peer-reviewed mathematics, or experimental physics. Implementation: `math_physics_atlas/v03_models.py::jacobi_svd`; independent comparison: `tools/independent_oracle_v03.py`. Supports 1–32 rows and columns, finite real double-precision inputs, with convergence and reconstruction refusals.

## Mathematical objective and scope

For a real matrix \(A\in\mathbb R^{m\times n}\), an SVD is \(A=U\Sigma V^T\), where the singular values \(\sigma_1\ge\cdots\ge\sigma_r\ge0\), \(r=\min(m,n)\), measure the magnitudes of orthogonally independent input-output directions. For full-rank matrices, the nonzero columns \(u_i\) and \(v_i\) satisfy \(Av_i=\sigma_i u_i\) and \(A^Tu_i=\sigma_i v_i\). The Euclidean condition number for full rank is \(\kappa_2(A)=\sigma_1/\sigma_r\). If \(\sigma_r=0\), algebraic rank is smaller and a finite full-rank condition number does not exist.

Do not confuse the **algebraic rank** of an exact real matrix with **numerical rank** under finite precision. This edition reports the latter using the declared relative threshold \(\sigma_i > \tau\sigma_1\), with \(\tau\) passed into the model. Values near the threshold can change classification under noise and roundoff. Moreover, SVD factors have sign ambiguities, and factors within a repeated singular-value subspace can be rotated; comparisons must use singular values, reconstruction residuals and subspaces, not demand identical matrix entries for U and V.

## Why Jacobi orthogonalization avoids normal equations

The normal-equations route forms \(A^TA\), whose 2-norm condition number is \(\kappa_2(A)^2\) when A is full rank. Squaring an already large conditioning ratio magnifies roundoff in small singular directions. In one-sided Jacobi, start with columns of A and an identity right-rotation accumulator V. For a column pair \(p,q\), let \(\alpha=\langle a_p,a_p\rangle\), \(\beta=\langle a_q,a_q\rangle\), \(\gamma=\langle a_p,a_q\rangle\). Seek a planar rotation making the new column dot product vanish. With \(\zeta=(\beta-\alpha)/(2\gamma)\), choose a cancellation-avoiding tangent

\[
 t=\frac{\operatorname{sign}(\zeta)}{|\zeta|+\sqrt{1+\zeta^2}},\quad c=\frac{1}{\sqrt{1+t^2}},\quad s=ct.
\]

Then \(a'_p=c a_p-s a_q\), \(a'_q=s a_p+c a_q\). Apply the identical column rotation to V. Sweep all pairs, stopping when \(|\gamma|/(\sqrt{\alpha}\sqrt{\beta})\) is small enough for every nonzero pair; reject after a finite sweep budget. Since the tall matrix's right transformations remain orthogonal, its resulting column norms are approximations to singular values, and its normalized nonzero columns are the left singular directions. For \(m<n\), perform the tall calculation on \(A^T\), then exchange the left and right factors on output.

The implementation rescales by the maximum absolute entry before accumulating products, avoids explicitly forming \(A^TA\), orders singular values descending, and checks scaled Frobenius reconstruction and active-column orthogonality. It **does not** provide full orthonormal nullspace bases when singular values are zero: zero singular modes deliberately have zero columns on one factor. It is a *thin reconstruction and rank diagnostic*, not a replacement for production LAPACK.

## Constructed investigation: rank-one system

Take \(A=\begin{bmatrix}1&2\\2&4\\3&6\end{bmatrix}\). Columns are linearly dependent, so \(\operatorname{rank}(A)=1\). The nonzero singular value is \(\sqrt{70}\), since \(\operatorname{tr}(A^TA)=70\) and the second eigenvalue vanishes. Running `jacobi_svd` should return a large value near \(8.366600265\), a small value near zero, and a numerical rank of one. Check \(\|A-U\Sigma V^T\|_F/\|A\|_F\), not the arbitrary signs of U or V.

Construct the transpose and verify that the singular values are invariant. Repeat with a full-rank rectangular random matrix against an independent NumPy/LAPACK oracle. Finally, set \(A=\operatorname{diag}(1,10^{-14})\) with rank tolerance \(10^{-10}\). The mathematical rank is two, but the **chosen numerical rank is one**. This is not an algorithm failure—it reveals the predeclared cutoff and the need for source uncertainty and resolution analyses.

## Reconstruction steps and failure boundaries

An independent implementation needs: bounded real-array parsing; explicit orientation of wide matrices; Euclidean inner products and stable length; plane-rotation arithmetic; sweep convergence and failure signaling; right-rotation accumulation; singular-value ordering; reconstruction and orthogonality certificates; and an explicit rank convention. Do not emit a singular-vector direction as empirically identifiable if its singular value is near noise. Reject nonfinite matrices, ragged arrays, unsupported size, incorrect tolerances, and nonconvergence. This small implementation has not been tested for huge dynamic ranges, distributed matrices, complex matrices, sparse scaling, or adversarial floating-point cases. When accurate general-purpose SVD is operationally required, independently evaluate production libraries and their numerical error contracts.

**External bibliographic orientation, not archived publisher bytes:** Netlib's official LAPACK `DGESVD` routine documents the standard real SVD contract and factor ordering: https://www.netlib.org/lapack/explore-html/d1/d7f/group__gesvd_gac6bd5d4e645049e49bb70691180abf07.html. MIT numerical methods teaching material provides further context: https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/. The Atlas does not reproduce or authenticate original publisher source files from either URL.


---

# 46 — SVD pseudoinverse, identifiable parameters and threshold-sensitive least squares

**Edition v0.3.0.** Original mathematical reconstruction using the `svd_least_squares` reference implementation. Numerical checks only; no calibrated inverse physical experiment, model-performance guarantee, or independent scientific peer review.

## What equation is actually solved?

Given \(A\in\mathbb R^{m\times n}\) and \(b\in\mathbb R^m\), solve \(\min_x\|Ax-b\|_2\). If the system is inconsistent, residual zero is impossible. If columns are dependent or \(m<n\), solutions may not be unique. Form the thin decomposition \(A\approx\sum_i\sigma_i u_i v_i^T\). For a selected positive singular set \(\mathcal I=\{i:\sigma_i>\tau\sigma_1\}\), define a **truncated pseudoinverse**

\[
  A_\tau^+ b=\sum_{i\in\mathcal I}v_i\,\frac{u_i^T b}{\sigma_i}.
\]

For the exact SVD with only nonzero singular values retained, this gives the least-squares solution with minimum Euclidean norm. Truncation at a larger numerical threshold instead regularizes small singular directions and can add bias. In each direction, the coefficient \((u_i^Tb)/\sigma_i\) shows that small singular values magnify noise. This is not evidence that the underlying measured parameter is real or unique.

## Derive the normal-equation stationarity condition

Let \(f(x)=\frac12\|Ax-b\|_2^2\). Its gradient is \(\nabla f(x)=A^T(Ax-b)\); a least-squares stationary point satisfies \(A^T(Ax-b)=0\). This necessary and sufficient condition holds for the unconstrained convex quadratic, even if the parameter is non-unique. In exact arithmetic \(A^TAx=A^Tb\) could be solved, but forming \(A^TA\) squares the condition number. QR is appropriate for full-column-rank overdetermined systems; SVD exposes loss of rank and provides a principled minimum-norm selection. Always distinguish objective-optimal residuals from scientifically identifiable parameters.

## Worked example and alternative hypotheses

For \(A=\begin{bmatrix}1&2\\2&4\\3&6\end{bmatrix}\) and \(b=(1,2,3)^T\), every \(x\) with \(x_1+2x_2=1\) fits perfectly. The minimum-norm solution lies parallel to \((1,2)\): \(x=(1/5,2/5)\). The solutions \((1,0)\) and \((-1,1)\) generate the same observations but represent different parameter hypotheses. A correct small residual alone cannot determine which physical mechanism is true. Where physical units differ across parameters, unweighted Euclidean minimum norm may itself be scientifically inappropriate: nondimensionalization, measurement weights and explicit priors are needed.

For \(A=[\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}]\), \(b=(4,5)^T\), the minimum-norm solution is \((4,5,0)^T\). Compare this with arbitrary nullspace shifts \((4,5,c)^T\), all with the same prediction. The reference solver handles both over- and underdetermined bounded real systems. It intentionally reports numerical rank and the cutoff used.

## Tests and falsification

Compare independent NumPy least-squares outputs on fixed-seed rectangular matrices, including exactly dependent columns. Assert finite residuals, check \(\|Ax-b\|\), verify the stationarity condition for full-rank untruncated cases, and explicitly test cutoff sensitivity. Counterexamples must include a rank-one design and a matrix with a singular value below \(\tau\sigma_1\). A pathological high dynamic range or nonconverging rotation problem is a refusal, not a successful demonstration of the solver.

## Forward link to scientific computing and AI

Least squares appears in instrument calibration, inverse field problems, parameter estimation, feature regression and neural network training approximations. The transfer is mathematical, not proof of useful intelligence: reproducible AI research must additionally specify training data, generalization, evaluation, leakage control, compute cost and independent baselines. The Atlas's evidence register must never label these constructed examples as hardware experiments or intelligence gains.

**Source orientation:** LAPACK DGESVD official reference: https://www.netlib.org/lapack/explore-html/d1/d7f/group__gesvd_gac6bd5d4e645049e49bb70691180abf07.html. Source page referenced by URL only; no authenticated original transport file stored.


---

# 47 — Reconstructing one-dimensional electrostatic Poisson equations and Gauss-law checks

**ATLAS FORGE v0.3.0.** An educational 1D constant-permittivity electrostatic boundary-value model, not a semiconductor process simulation, transistor compact model, charge transport model, physical measurement or certified high-voltage calculator. Reference: `poisson1d_dirichlet` and `tridiagonal_solve` in `math_physics_atlas/v03_models.py`.

## From a conservation law to a differential equation

For static electric fields, Maxwell-Gauss law in matter is \(\nabla\cdot\mathbf D=\rho_f\), where \(\mathbf D=\epsilon\mathbf E\) under a linear isotropic constitutive law and \(\mathbf E=-\nabla V\). When variation is only in x and epsilon is a positive constant, the governing equation becomes

\[
  -\epsilon\,\frac{d^2V}{dx^2}=\rho_f(x),\quad 0<x<L,
\]

with Dirichlet electrode potentials \(V(0)=V_L\) and \(V(L)=V_R\). Units: \(\epsilon\) F/m = C/(V·m), charge density \(\rho\) C/m³, V volt, x meter, E V/m and D C/m². The equation is only valid within its electrostatic, constant-dielectric, one-dimensional assumptions. Semiconductor charge density generally depends on mobile carriers and potential, requiring a *nonlinear coupled Poisson–transport or quantum system*, not this direct linear solve.

## Derivation of the centered finite-difference stencil

Let \(x_i=ih\) for i from 0 to N+1, with h=L/(N+1). Taylor expand smooth V around \(x_i\): \(V(x_i\pm h)=V_i\pm h V_i'+h^2 V_i''/2\pm h^3 V_i'''/6+h^4V_i^{(4)}/24+\cdots\). Adding the two expansions cancels odd terms. Thus \(V_i''\approx (V_{i-1}-2V_i+V_{i+1})/h^2\), with local truncation error of order h² when V has bounded fourth derivative. The discrete equation is

\[
 -V_{i-1}+2V_i-V_{i+1}=\frac{\rho_i h^2}{\epsilon}.
\]

Move the known boundary values into the first and last entries of the right-hand side; the unknown interior potentials solve a tridiagonal system with diagonal 2 and off-diagonal -1. Thomas forward elimination and back substitution take O(N) operations and O(N) storage. The positive-definite Dirichlet operator admits a unique discrete solution for epsilon>0. The solver refuses nonpositive epsilon, nonfinite values, invalid geometry, and pivots too small relative to scale.

## An exact manufactured charge-slab test

Choose uniform charge \(\rho(x)=\rho_0\) and arbitrary boundary potentials. Twice integrating gives

\[
  V(x)=V_L+(V_R-V_L)\frac{x}{L}+\frac{\rho_0}{2\epsilon}x(L-x).
\]

Because the centered second difference is *exact for a quadratic*, interior grid values should match that polynomial to roundoff, not merely to O(h²). For L=1 m, epsilon=1 F/m (deliberately artificial), rho=2 C/m³, and both boundaries zero, the solution is V(x)=x(1-x) volt, peaking at 0.25 V at the midpoint. These arbitrary teaching constants are **not** realistic vacuum permittivity or a validated device geometry. Run the same case using physical-scale epsilon with matching physically plausible charge values to verify unit arithmetic, without inferring a material's behavior.

## Discrete Gauss balance as a conservation check

Define face field \(E_{i+1/2}=-(V_{i+1}-V_i)/h\) and displacement \(D_{i+1/2}=\epsilon E_{i+1/2}\). Then \(D_{i+1/2}-D_{i-1/2}=h\rho_i\). Summing over all interior cells telescopes: \(D_{N+1/2}-D_{1/2}=h\sum_i\rho_i\). The implementation records the numerical Gauss balance residual separately from the maximum pointwise Poisson residual. This is a discrete identity of the assumed model. A tiny residual **does not** establish that true physical charge density, permittivity or boundary conditions were measured correctly.

For nonconstant smooth fields, use a manufactured sine potential V=sin(pi x/L), with rho=epsilon(pi/L)^2 sin(pi x/L). On grids N=15,31,63,127, the maximum error should decrease by approximately a factor of four each time h is halved. A failure of this refinement trend indicates an implementation or convergence problem.

## Why this is a semiconductor prerequisite, not a semiconductor simulator

A semiconductor must additionally model carrier statistics, band structure, dielectric interfaces, mobility, drift-diffusion currents, recombination, contacts and doping distributions. At equilibrium or under bias, rho can depend strongly on V and other fields. The Atlas's future Electronics & Semiconductors edition should use this verified finite-difference operator as a reference component and then introduce coupled constitutive laws and experimental validation; **do not silently relabel the present constant-epsilon slab as a diode or transistor**.

**External publisher orientation, not archived original files:** MIT OpenCourseWare Numerical Methods for PDEs, sections on Poisson and elliptic finite differences: https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/pages/lecture-notes/ and MIT's publicly linked course overview https://math.mit.edu/classes/18.336/index.html. No publisher PDF, source hash or reuse clearance is claimed by this chapter.


---

# 48 — Implicit diffusion, unconditional linear stability and temporal-resolution failure cases

**ATLAS FORGE v0.3.0.** Original instructional derivation and pure-Python implementation: `implicit_heat1d_dirichlet` and `tridiagonal_solve`. These are one-dimensional constant-coefficient model computations under fixed temperatures, not experiments on heated materials or validated semiconductor thermal models.

## PDE, units and boundary data

Take the heat/diffusion model \(u_t=\alpha u_{xx}\), where x is position [m], t is time [s], u can represent temperature [K] in a simple conduction model, and alpha is constant thermal diffusivity [m²/s]. With a uniform grid \(x_i=ih\), \(t^n=n\Delta t\), define the dimensionless Fourier number \(r=\alpha\Delta t/h^2\). In an explicit forward-time centered-space method, high spatial frequencies are stable only if \(r\le 1/2\) under the standard 1D Dirichlet assumptions. Implicit methods relax this **stability** restriction but still need time-step refinement for **accuracy**.

## Backward Euler as a tridiagonal implicit system

Using the new-time spatial derivative yields

\[
 \frac{u_i^{n+1}-u_i^n}{\Delta t}=\alpha\frac{u_{i-1}^{n+1}-2u_i^{n+1}+u_{i+1}^{n+1}}{h^2}.
\]

Rearrange to \(-r u_{i-1}^{n+1}+(1+2r)u_i^{n+1}-r u_{i+1}^{n+1}=u_i^n\). Add the fixed boundary contributions to the first/last right-hand sides. The tridiagonal matrix has positive diagonal 1+2r, negative off-diagonal -r, and is strictly diagonally dominant for r>0. It is therefore nonsingular. For a discrete Fourier sine mode with Laplacian eigenvalue \(\lambda_d=-4\sin^2(\pi k/(2N))/h^2\), the amplification is \(G_{BE}=1/(1+4r\sin^2(\pi k/(2N)))\), lying in (0,1] for nonnegative r. Large r strongly damps even modes that may physically persist over a shorter time; numerical stability is not temporal accuracy.

## Crank–Nicolson midpoint averaging

Average the spatial operator between the old and new states:

\[
 \frac{u_i^{n+1}-u_i^n}{\Delta t}=\frac\alpha2\left[(D_{xx}u^{n+1})_i+(D_{xx}u^n)_i\right].
\]

Rearrange to \(-\frac r2u_{i-1}^{n+1}+(1+r)u_i^{n+1}-\frac r2u_{i+1}^{n+1}=(1-r)u_i^n+\frac r2(u_{i-1}^n+u_{i+1}^n)\). The amplification for a discrete sine mode is \(G_{CN}=(1-2r\sin^2(\pi k/(2N)))/(1+2r\sin^2(\pi k/(2N)))\). Its magnitude is ≤1 for all r≥0, but the numerator becomes negative at sufficiently large r, giving alternating signs in stiff high-frequency modes. **Unconditional linear stability does not imply monotonicity or freedom from nonphysical oscillations.** Backward Euler is first-order accurate in time; Crank–Nicolson is second-order for smooth solutions and fixed time steps, subject to regularity and boundary compatibility.

## Manufactured eigenmode benchmark

With fixed-zero boundaries on [0,L], choose \(u(x,0)=\sin(\pi x/L)\). The continuum solution is \(u(x,t)=e^{-\alpha(\pi/L)^2 t}\sin(\pi x/L)\). For a grid with N intervals, the **discrete** lowest sine eigenvalue has magnitude \(4\sin^2(\pi/(2N))/h^2\). Thus, after k steps, the numerical solution should equal the initial discrete sine multiplied by \(G_{BE}^k\) or \(G_{CN}^k\), to rounding error. This isolates implementation correctness from the difference between the discrete and continuous eigenvalues. Compare time-step refinements against the continuum exponential to assess truncation separately.

## Boundary and engineering cautions

The kernel preserves the endpoint values exactly, refuses negative diffusivity and nonfinite inputs, and caps grid size, time steps and Fourier number. It does not model radiation, convection, interface conditions, temperature-dependent properties or heat generation. A slab used to explain processor or transistor heating requires measured thermal properties, multilayer 2D/3D geometry, interface resistance and calibration. A signal that appears physically smooth can still be wrong if an invalid boundary was supplied. This edition's tests are generated numeric trajectories only, not a physical temperature trace.

**Bibliographic orientation only:** MIT OpenCourseWare Numerical Methods for PDEs includes time stepping, stability, heat equations and implicit methods: https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/pages/lecture-notes/. No original publisher files are authenticated or mirrored.


# Addendum — original v0.4.0 Physics & Mathematics Chapters 49–52



---

# Chapter 49 — Conservative 2D Poisson reconstruction and dielectric flux

**Edition:** ATLAS FORGE Mathematics & Physics v0.4.0. **Status:** original explanatory chapter, mathematically motivated finite-grid software reference; not experimentally calibrated.

## Reconstruction objective and prerequisites

Recover a two-dimensional approximation to electrostatic potential, given a positive scalar permittivity field, charge density and fixed boundary potentials. This directly supports future learning about electrostatic components, dielectrics and semiconductor-device potential solvers, but is **not** a semiconductor-device simulator. Prerequisites: SI units, gradient/divergence, Dirichlet boundary data, five-point differences, and linear algebra.

In a prescribed, static, linear isotropic material, **E** = −∇V and **D** = ε **E**. Gauss's constitutive statement ∇·**D** = ρ gives

\[
-\nabla\cdot(\epsilon(x,y)\nabla V)=\rho(x,y).
\]

ε has units F/m, V volts, E V/m, D C/m², ρ C/m³. A two-dimensional computational slice assumes invariance in the unmodeled third dimension; integrated area charge and perimeter displacement flux therefore have units **C/m per unit depth**, not total coulombs.

## Mesh and derivation

For a rectangle 0≤x≤Lx, 0≤y≤Ly with `nx × ny` unknown interior grid nodes, define `hx=Lx/(nx+1)` and `hy=Ly/(ny+1)`. Boundary nodes receive prescribed voltages. At an interior node P, approximate face permittivity by the harmonic mean `ε_E=2 ε_P ε_(i+1,j)/(ε_P+ε_(i+1,j))`, analogously W,N,S. Use centered face gradients; with positive scalar ε, each face weight is positive:

\[
 a_E=\epsilon_E/h_x^2,\quad a_W=\epsilon_W/h_x^2,\quad
 a_N=\epsilon_N/h_y^2,\quad a_S=\epsilon_S/h_y^2.
\]

The discrete equation is

\[
(a_E+a_W+a_N+a_S)V_P-a_EV_E-a_WV_W-a_NV_N-a_SV_S=\rho_P.
\]

Known boundary potentials are moved to the right-hand side as `+a_face*V_boundary`; the coefficient matrix retains its diagonal face weights. This is not the same as imposing a row of zeros for a boundary: the latter can destroy the intended SPD property of the **interior-only** matrix.

On shared interior faces, a single face coefficient appears symmetrically on both sides. For every nonzero interior vector x, the discrete energy is a sum of positive weighted neighbor differences plus positive boundary-face terms `a_face*x_P²`. With fixed Dirichlet data on all four sides, this establishes positive definiteness for the modeled operator (up to floating-point breakdown). No sign-indefinite nonlinear material response is admitted.

## Algorithm and data contract

Call `poisson2d_problem(nx,ny,Lx,Ly,epsilon,rho,boundary)` from `math_physics_atlas.v04_models`. `epsilon` and the boundary can be a finite numeric scalar, callable `(x,y)`, or full boundary-inclusive 2D node array. `rho` also accepts an interior-only array. The model explicitly checks shape, finite values, bounds, permittivity positivity and coefficient representation. Only grids 2–64 interior points along each axis, at most 4096 unknowns, are permitted in this reference implementation. The operator is applied matrix-free in O(nx*ny) memory and work per iteration.

A solved 2D field is stored as `(ny+2)×(nx+2)` row-major voltages with edge values preserved. Reproducibility requires the grid, physical lengths, ε field, ρ field, all four Dirichlet edges, solver tolerances and iteration limit; quoting only the matrix or a final plot is insufficient.

## Discrete Gauss accounting

With `F=-ε∇V`, the conservation statement is `∇·F=ρ`; summing interior discrete equations cancels interior-face fluxes. The total external flux per unit depth is the sum, over boundary-adjacent faces, of

\[
 F_{\rm outward}\,\Delta s=\epsilon_{\rm face}\,\frac{V_{\rm interior}-V_{\rm boundary}}{h_{\rm normal}}\,\Delta s.
\]

It must match `Σ ρ_(i,j) hx hy`, up to algebraic residual and roundoff. This checks **discrete charge accounting**, not physical accuracy or actual boundary-charge measurement.

## Worked investigation

Take `Lx=Ly=1 m`, `ε=1 F/m` (deliberately mathematical rather than a realistic material), four zero-voltage boundaries, and `ρ(x,y)=2π² sin(πx)sin(πy) C/m³`. The exact continuum solution is `V=sin(πx)sin(πy)` volts. The computer first assembles the discrete equation from the chosen mesh; solving that equation to a tiny residual still leaves a positive grid-truncation error. Chapter 51 measures the latter independently at four grid sizes.

## Failure cases, open physics, sources

Invalid ε≤0, NaNs, unsupported boundary types, wrong array shapes, overflow and excessive grid sizes are rejected. Zero-iteration or under-budget conjugate-gradient solves must *never* be marked scientifically converged. Neumann/periodic boundaries, anisotropic or nonlinear dielectric tensors, sharp curved interfaces, mobile charge carriers, traps, temperature effects, real device contacts, quantum corrections, time-dependent electrodynamics, experimental validation and semiconductor fabrication process data are outside scope.

**Source orientation only:** MIT OpenCourseWare 18.086 readings (finite differences, fast Poisson, conjugate gradients): https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/readings/ . Primary publisher document bytes not downloaded or rights-authenticated here. This chapter is original synthesis, not a copy of the course text.



---

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



---

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



---

# Chapter 52 — Dielectric interfaces, SI metrology and the semiconductor handoff

**Edition:** Mathematics & Physics v0.4.0. **Status:** a reconstructible linear-electrostatics reference and an explicit map of *missing* semiconductor knowledge.

## Physical meaning before computation

The electrostatic model takes ε(x,y) as **already known**. It does not infer ε from measurements and it does not predict how charge carriers redistribute in silicon. For a linear scalar dielectric, ε=εr ε0. The NIST 2022 CODATA recommendation for vacuum permittivity is approximately `ε0 = 8.8541878188 × 10^−12 F/m` with a nonzero published standard uncertainty; it is *not* an exact fixed SI constant. Material relative permittivity εr varies with composition, frequency, temperature, fields and measurement protocol. A numerical grid value is not a calibration certificate.

The fundamental equations preserved in this node are

\[
\mathbf E=-\nabla V,\qquad \mathbf D=\epsilon\mathbf E,
\qquad \nabla\cdot\mathbf D=\rho.
\]

For an interface without free surface charge, the **normal displacement** is continuous; electric field need not be continuous when ε differs. A dielectric interface with a prescribed free sheet charge or polarization discontinuity requires additional jump conditions not covered by assigning a piecewise ε grid alone.

## Why harmonic face averaging is a useful first approximation

In one dimension consider two adjacent half-cells of width h/2 with ε1, ε2. At steady state, the same displacement passes through both segments. Their voltage drops add:

\[
\Delta V=-(D/\epsilon_1)(h/2)-(D/\epsilon_2)(h/2)
=-D\,h/\epsilon_{\rm face}.
\]

Solving gives `εface=2ε1ε2/(ε1+ε2)`, the harmonic average used in the v0.4 reference. This preserves shared-face flux cancellation. It assumes an axis-aligned interface and an isotropic, linear medium; on curved or oblique interfaces the modeling error needs a separate investigation. For a prescribed interface sheet charge, this simple average without a jump/source term is insufficient.

## Worked exercise: two dielectrics and fixed perimeter voltage

Take a unit rectangle with prescribed `V=x` along all boundary edges and set ε=1×10⁻¹¹ F/m for x<0.5 and 6×10⁻¹¹ F/m for x≥0.5. Let ρ=0. Construct a 13×11 interior grid with `poisson2d_problem`, solve with `solve_poisson2d_cg`, and check the integrated residual `Φboundary−Qinterior`. The computed potential is generally **not exactly V=x** throughout: the change in ε redistributes gradient so normal displacement can be continuous across internal faces. This is a synthetic dielectric-interface test, not an actual materials experiment.

A stronger future investigation should construct an analytic two-layer one-dimensional-in-x solution with piecewise slopes satisfying `ε1 E1=ε2 E2` at an aligned interface, compare exact face charge, and examine error when the interface does not align with the computational grid. This v0.4 reference does not claim those convergence properties yet.

## Reconstructible semiconductor bridge: what is still missing

Even a perfect electrostatic Poisson solver alone cannot reconstruct a transistor. The next Electronics & Semiconductors Atlas requires (at minimum):

- Semiconductor crystal structure and measured band structure; intrinsic carrier concentration and statistical mechanics with temperature.
- Doping, ionized impurity populations, Poisson-carrier coupling, electron and hole continuity equations, mobility/diffusion and recombination mechanisms.
- Contacts, electrochemical potential, Schottky/ohmic interfaces, gate oxide geometry, breakdown and interface traps; circuit-level boundary conditions.
- Material and process metrology, lithography, thin-film deposition, doping/anneal, manufacturing tolerances and test instruments.
- Mesh convergence, uncertainty propagation, calibration against actual measured devices and peer-reviewed source transport/rights verification.

Treat the v0.4 solver as a **numerical prerequisite**, not a semiconductor model or validated tool for device design. The original thirty-domain priority queue remains immutable. Complete domain libraries before any Bitwork routing or integrated desktop transfer.

## Evidence ledger and source provenance

- NIST CODATA permittivity entry: https://physics.nist.gov/cgi-bin/cuu/Value?ep0 (publisher value and uncertainty only; no authenticated publisher file bytes archived).
- NIST CODATA research overview: https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022 .
- OpenStax University Physics Vol. 2, Gauss law: https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law (orientation only; original publisher file not mirrored).

All original formulas and explanations in this chapter are AI-assisted synthesis prepared for ATLAS FORGE. The model has **zero field experiments, zero independently authenticated primary-source publisher transport files, and no external scientific peer review**.



---

# Mathematics & Physics Atlas — original scientific increment v0.5.0

# Chapter 53 — Nonlinear elliptic equilibrium, discrete monotonicity and damped Newton

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Status:** original numerical-analysis exposition, executable finite reference, not experimental evidence.

## 1. Problem statement and exactly what the program solves

The numerical reference solves the one-dimensional **dimensionless** Dirichlet problem

\[
-\alpha\,u''(x)+\beta\sinh u(x)=f(x),\quad 0<x<\ell,\quad
u(0)=u_L,\;u(\ell)=u_R, \quad\alpha>0,\;\beta\ge0.
\]

Here `u` is a dimensionless normalized potential. `alpha`, `beta`, and `f` are stipulated dimensionless model inputs. They are not inferred permittivity, measured doping or contact parameters. This simple monotone equilibrium is a mathematically controlled *subproblem*, not a coupled electron-hole transport system. The code restricts `3<=n<=1024`, `|u|<=20` and other documented numerical ranges. Such limits are **software guards**, not physical constants.

At interior points `x_i=i h`, `h=ell/(n+1)`, central differencing gives

\[
F_i(\mathbf u)=\frac{\alpha}{h^2}(2u_i-u_{i-1}-u_{i+1})
+\beta\sinh(u_i)-f_i=0.
\]

The boundary values occupy the missing `u_0` and `u_{n+1}` positions. The assembled Jacobian is tridiagonal:

\[
J_{ii}=2\alpha/h^2+\beta\cosh(u_i),\qquad
J_{i,i\pm1}=-\alpha/h^2.
\]

A finite-domain Jacobian is symmetric positive definite under the stated positive `alpha`, nonnegative `beta` and Dirichlet boundaries: its quadratic form is the weighted sum of squared first differences (including endpoints) plus a nonnegative diagonal contribution. This guarantees a uniquely solvable **Newton linear step**, not convergence of an undamped Newton iteration from arbitrary starting conditions.

## 2. Controlled Newton globalization

Each iteration constructs a true nonlinear residual, solves `J Δu = -F`, and searches for a step `lambda=1,1/2,...,2^-25` that reduces the maximum residual while keeping `|u|<=20`. A successful step updates `u`; otherwise the routine reports `line_search_failed`. Exceeding the iteration budget yields `maxiter_exceeded`, never an invented converged state. The output includes `iterations`, `residual_linf`, a stated tolerance and the count of rejected line-search steps.

The initial state is the linear interpolation between the two Dirichlet endpoints. Linear solves use a small pure-Python tridiagonal elimination. `rtol`/`atol` bound the **algebraic nonlinear equation residual** in the supplied normalization. They do not bound the error in true physical voltage without an independently specified dimensional model.

## 3. Flux balance is a second, separate observable

Summing the discrete equation over `i=1..n` and multiplying by `h` telescopes the interior differences:

\[
\underbrace{\alpha\frac{u_1-u_L}{h}}_{\text{left outward flux}}
+\underbrace{\alpha\frac{u_n-u_R}{h}}_{\text{right outward flux}}
+\beta h\sum_{i=1}^{n}\sinh(u_i)
=h\sum_{i=1}^{n}f_i.
\]

A deviation from this discrete balance signals an implementation or algebraic-solve defect. A *small* balance residual is not evidence that the continuum model or material parameters match nature.

## 4. Independent reference investigations

1. **Exact constant state.** Choose `u_L=u_R=c` and `f_i=beta*sinh(c)`. Because all second differences vanish, the exact discrete solution is `u_i=c`. This tests boundary handling and the nonlinear term.
2. **Exact linear state.** With `beta=0`, `f=0`, any affine interpolation is the exact discrete solution. This detects incorrect endpoint signs.
3. **Continuum manufactured sine.** Take `u*(x)=sin(pi*x)` on `ell=1`, homogeneous endpoints and `f(x)=alpha*pi^2*sin(pi*x)+beta*sinh(sin(pi*x))`. The solved grid should approach the **continuum** field at second order; this tests spatial truncation rather than only convergence of Newton's method.
4. **Deliberate non-convergence.** Set `maxiter=1` on a nontrivial profile. Return `converged=false` and the original residual; do not label the tentative iterate a physical prediction.

The source tree ships all four tests, an additional randomized SciPy root comparison, and an independent Decimal/quad oracle for the adjacent exponential-fit kernel.

## 5. Counterexamples and scope restrictions

A converged nonlinear solve can still represent the wrong physical carrier statistics. Degenerate semiconductors require Fermi–Dirac treatment; depletion approximations, interface traps, contact barriers, temperature variation and quantum confinement can all invalidate a simple symmetric `sinh(u)` closure. Even for this mathematical equation, a tiny residual at a coarse grid does not establish a small continuum error. Deliberately keep these distinct: **implementation**, **discrete solution**, **continuum approximation**, **physical model**, **experimental observation**.

**Source navigation (not authenticated full texts):** TU Wien semiconductor equations, https://iue.tuwien.ac.at/phd/sharma/node-The-Basic-Semiconductor-Equations.html ; COMSOL semiconductor theory and solver convergence, https://www.comsol.com/support/learning-center/article/improving-convergence-of-semiconductor-models-69861 . This chapter is independently authored; no external source PDF was acquired, copied, or authenticated.


# Chapter 54 — Boltzmann equilibrium charge, thermal voltage and nondimensionalization

**Edition:** Mathematics & Fundamental Physics v0.5.0. **Evidence status:** constructed models only. **Purpose:** preserve a reconstructible chain from electrostatics to a limited equilibrium charge closure.

## 1. Physical equation and sign conventions

An electrostatic potential `V` in volts gives electric field `E=-grad(V)`. In a uniform linear dielectric of permittivity `epsilon` in farads per metre,

\[
-\nabla\cdot(\epsilon\nabla V)=\rho
= q\,[N_D^+-N_A^-+p-n],
\]

where `q>0` is elementary charge, `n,p` are electron and hole number densities (m^-3) and ionized dopants also have units m^-3. The carrier terms multiply charge `q` to yield C/m^3. The formula alone does not determine `n,p`; separate carrier statistics and continuity/transport laws are necessary. A solver that takes `rho` as independently specified has **not yet coupled** mobile charge self-consistently.

In a simplified, nondegenerate, isothermal equilibrium with a common reference concentration `n0`, one may stipulate

\[
U_T=k_B T/q,\qquad u=V/U_T,\qquad
n=n_0e^u,\quad p=n_0e^{-u},
\]

so `p-n=-2n0*sinh(u)`. The charge equation is then

\[
-\epsilon U_T u_{xx} +2qn_0\sinh u=qC(x),\qquad C=N_D^+-N_A^-.
\]

This is a **special equilibrium closure** at fixed temperature and specified reference statistics. Real semiconductor electron and hole densities depend on band edges, quasi-Fermi levels, contact conditions, and temperature. The two exponentials are not a complete semiconductor device model.

## 2. Nondimensionalization before coding

Choose a positive reference length `L0`, normalized coordinate `x*=x/L0`, and an arbitrary positive reference charge-density scale `rho*` (C/m^3). Divide the previous equation by `rho*`:

\[
-\alpha\,\partial_{x*}^2u +\beta\sinh u=f(x*),\quad
\alpha=\frac{\epsilon U_T}{\rho_* L_0^2},\quad
\beta=\frac{2qn_0}{\rho_*},\quad
f=\frac{qC}{\rho_*}.
\]

All three coefficients are now dimensionless, as assumed by the standalone Python kernel. The code's `length` is the length in units of `L0`, not raw metres; using dimensional `epsilon` directly as `alpha` is an error. To return to physical voltage, multiply the dimensionless result by `U_T`. To return to electric field, compute `-U_T/L0` times the dimensionless gradient. The v0.5 software **does not automate this physical conversion** because it has no authenticated material parameters or calibration.

## 3. Worked constructed problem

Let `ell=1`, `alpha=1`, `beta=0.4`, `u_L=u_R=0`. Select the exact continuum field `u*(x)=sin(pi*x)`. Its source is

\[
f(x)=\pi^2\sin(\pi x)+0.4\sinh(\sin(\pi x)).
\]

Discretize by the centered second difference, solve the nonlinear system with damped Newton, and compare every interior node against the known `u*(x_i)`. Halving the grid spacing should reduce the leading second-order truncation error by approximately four, **when the nonlinear residual is sufficiently small**. This uses a manufactured forcing—not a measured doping distribution—and cannot validate an external sample of silicon.

## 4. Energy and uniqueness of the discrete model

The finite-dimensional objective

\[
\mathcal{E}(u)=\frac{\alpha}{2h^2}\sum_{i=0}^{n}(u_{i+1}-u_i)^2
+\beta\sum_{i=1}^n\cosh u_i-\sum_{i=1}^n f_i u_i
\]

has interior gradient equal to the finite-difference equation, with Dirichlet endpoints held fixed. Its Hessian is the SPD Jacobian from Chapter 53. This provides a useful *mathematical* structure and a clean numerical diagnostic. Energy minimization does not make the assumed carrier-density closure experimentally correct.

## 5. Missing experiment and uncertainty ledger

To use the numerical kernel for a physical semiconductor, a future researcher must establish material composition and phase, dopant activation, carrier temperature, charge trapping, relative dielectric function and uncertainty, boundaries/contacts, band structure and the density-of-states regime. Measured I–V curves, C–V curves or spatial profiles require authentic instrument calibration, uncertainty estimates and independently reproduced fit diagnostics. This reference contains none of those measurements.

**Source navigation only:** TU Wien, https://iue.tuwien.ac.at/phd/sharma/node-The-Basic-Semiconductor-Equations.html ; COMSOL semiconductor interface documentation, https://doc.comsol.com/6.4/doc/com.comsol.help.semicond/semicond_ug_semiconductor.6.02.html . No original publisher transport bytes or approved offline mirror are included.


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


