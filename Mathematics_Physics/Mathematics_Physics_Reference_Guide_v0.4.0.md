# Mathematics & Fundamental Physics Atlas — Reading Directory v0.1.0

**Goal:** preserve mathematically reconstructible foundations of research instruments, computing hardware, software tools and advanced AI; not an emergency-prepper guide or complete university course.

## 38 original scientific chapters

- [Chapter 01: Proof, axioms, and falsifiable mathematical claims](chapters/01_proof_axioms_and_falsifiable_mathematical_claims.md)
- [Chapter 02: Units, dimensional analysis, and SI definitions](chapters/02_units_dimensional_analysis_and_si_definitions.md)
- [Chapter 03: Numbers, rational arithmetic and precision](chapters/03_numbers_rational_arithmetic_and_precision.md)
- [Chapter 04: Functions, domains, limits and continuity](chapters/04_functions_domains_limits_and_continuity.md)
- [Chapter 05: Derivatives, sensitivities and automatic differentiation](chapters/05_derivatives_sensitivities_and_automatic_differentiation.md)
- [Chapter 06: Integration and conservation over time](chapters/06_integration_and_conservation_over_time.md)
- [Chapter 07: Vectors, inner products and geometric projection](chapters/07_vectors_inner_products_and_geometric_projection.md)
- [Chapter 08: Matrices as composable linear maps](chapters/08_matrices_as_composable_linear_maps.md)
- [Chapter 09: Gaussian elimination and rational certificates](chapters/09_gaussian_elimination_and_rational_certificates.md)
- [Chapter 10: Rank, nullspace and underdetermination](chapters/10_rank_nullspace_and_underdetermination.md)
- [Chapter 11: Least squares and identifiable parameter fitting](chapters/11_least_squares_and_identifiable_parameter_fitting.md)
- [Chapter 12: Eigenvalues, stability and dynamical modes](chapters/12_eigenvalues_stability_and_dynamical_modes.md)
- [Chapter 13: Probability axioms and conditional evidence](chapters/13_probability_axioms_and_conditional_evidence.md)
- [Chapter 14: Random variables, expectation and variance](chapters/14_random_variables_expectation_and_variance.md)
- [Chapter 15: Bayesian updating versus evidence reliability](chapters/15_bayesian_updating_versus_evidence_reliability.md)
- [Chapter 16: Binomial counting and independence assumptions](chapters/16_binomial_counting_and_independence_assumptions.md)
- [Chapter 17: Numerical conditioning and stability](chapters/17_numerical_conditioning_and_stability.md)
- [Chapter 18: Discrete Fourier transform and spectral analysis](chapters/18_discrete_fourier_transform_and_spectral_analysis.md)
- [Chapter 19: Differential equations and initial value problems](chapters/19_differential_equations_and_initial_value_problems.md)
- [Chapter 20: Runge–Kutta methods and local error](chapters/20_runge_kutta_methods_and_local_error.md)
- [Chapter 21: Partial differential equations and boundary conditions](chapters/21_partial_differential_equations_and_boundary_conditions.md)
- [Chapter 22: Optimization, convexity and objective design](chapters/22_optimization_convexity_and_objective_design.md)
- [Chapter 23: Softmax, log-sum-exp and numerical probability](chapters/23_softmax_log_sum_exp_and_numerical_probability.md)
- [Chapter 24: Newtonian mechanics and inertial frames](chapters/24_newtonian_mechanics_and_inertial_frames.md)
- [Chapter 25: Energy, momentum and conservation boundaries](chapters/25_energy_momentum_and_conservation_boundaries.md)
- [Chapter 26: Oscillators, modes and resonance](chapters/26_oscillators_modes_and_resonance.md)
- [Chapter 27: Electric charge, fields and potential](chapters/27_electric_charge_fields_and_potential.md)
- [Chapter 28: Circuit dynamics and RC time constants](chapters/28_circuit_dynamics_and_rc_time_constants.md)
- [Chapter 29: Maxwell equations and wave propagation](chapters/29_maxwell_equations_and_wave_propagation.md)
- [Chapter 30: Thermodynamic temperature and energy scales](chapters/30_thermodynamic_temperature_and_energy_scales.md)
- [Chapter 31: Special relativity and spacetime consistency](chapters/31_special_relativity_and_spacetime_consistency.md)
- [Chapter 32: Quantum state amplitudes and Born measurement](chapters/32_quantum_state_amplitudes_and_born_measurement.md)
- [Chapter 33: Schrödinger equation and Hamiltonian modeling](chapters/33_schr_dinger_equation_and_hamiltonian_modeling.md)
- [Chapter 34: Heisenberg uncertainty and measurement meaning](chapters/34_heisenberg_uncertainty_and_measurement_meaning.md)
- [Chapter 35: Covariance and propagated measurement uncertainty](chapters/35_covariance_and_propagated_measurement_uncertainty.md)
- [Chapter 36: Inverse problems and scientific identifiability](chapters/36_inverse_problems_and_scientific_identifiability.md)
- [Chapter 37: From linear algebra to neural network computation](chapters/37_from_linear_algebra_to_neural_network_computation.md)
- [Chapter 38: Rebuilding an offline scientific computing stack](chapters/38_rebuilding_an_offline_scientific_computing_stack.md)

## Offline reproduction and source accountability

[Full human-readable manual](DEPTH_MANUAL_v0.1.0.md) · [Twenty-two constructed experiments](CASEBOOK.md) · [Source/rights register](SOURCE_REGISTER.md) · [Scientific gap matrix](COVERAGE_MATRIX.md) · [Validation](VALIDATION_v0.1.0.md)

Run `python -m math_physics_atlas` and `python -m unittest discover -s tests -q`. The optional NumPy crosschecks require NumPy, but the core code needs only Python 3.10+.

The Bitwork router is deferred until all content domains are established. The original thirty-domain candidate list remains unchanged.

## v0.2.0 original scientific extension

- [Chapter 39: Householder QR and stable least-squares reconstruction](chapters/39_householder_qr_and_stable_least_squares.md)
- [Chapter 40: Singular values, rank and identifiability boundaries](chapters/40_singular_values_rank_and_identifiability.md)
- [Chapter 41: Radix-two FFT, spectral sampling and aliasing tests](chapters/41_radix2_fft_sampling_and_spectral_oracles.md)
- [Chapter 42: Adaptive nonlinear ODE integration and local error estimation](chapters/42_adaptive_nonlinear_ode_and_local_error.md)
- [Chapter 43: Heat equation, diffusion stability and bounded temperature fields](chapters/43_heat_equation_ftcs_diffusion_and_stability.md)
- [Chapter 44: Wave equation, leapfrog propagation and electromagnetic scope](chapters/44_wave_equation_leapfrog_cfl_and_field_limits.md)

Six new constructed cases: [v0.2 casebook](V02_CASEBOOK.md). The v0.1 manual, old tests, records and sources are preserved, not retroactively rewritten.

## v0.3.0 — reconstruction mathematics and engineering bridge

- [Chapter 45: Rectangular SVD by one-sided Jacobi](chapters/45_rectangular_svd_one_sided_jacobi_and_rank.md)
- [Chapter 46: Pseudoinverse least squares and identifiability](chapters/46_pseudoinverse_least_squares_identifiability.md)
- [Chapter 47: Electrostatic Poisson model and discrete Gauss balance](chapters/47_poisson_electrostatics_finite_difference_gauss_law.md)
- [Chapter 48: Implicit diffusion and temporal accuracy](chapters/48_implicit_diffusion_stability_and_temporal_resolution.md)

Four new constructed investigations: [v0.3 casebook](V03_CASEBOOK.md). Code: `math_physics_atlas/v03_models.py`. Independent checks: `tools/independent_oracle_v03.py`. All previous chapter files, edition records and tests remain intact in the active package or frozen history.


## v0.4.0 — matrix-free two-dimensional electrostatics and numerical evidence

- [Chapter 49: Conservative 2D Poisson and dielectric face flux](chapters/49_conservative_2d_poisson_and_dielectric_flux.md)
- [Chapter 50: Matrix-free Jacobi-preconditioned conjugate gradient](chapters/50_matrix_free_preconditioned_conjugate_gradient.md)
- [Chapter 51: Manufactured solutions and error separation](chapters/51_manufactured_solutions_discretization_and_residuals.md)
- [Chapter 52: Dielectric interfaces and the semiconductor handoff](chapters/52_dielectric_interfaces_units_and_semiconductor_handoff.md)

Additional original constructed cases: [v0.4 casebook](V04_CASEBOOK.md). Core standard-library implementation: `math_physics_atlas/v04_models.py` and `math_physics_atlas/v04_cases.py`. Optional independent NumPy dense reference: `python tools/independent_oracle_v04.py`. Source/citation status, experiments, and scientific v1 gates remain explicitly separate from code tests. **Original thirty domain queue and Bitwork scheduling are unchanged.**
