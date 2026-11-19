# 59. Coupled Gummel iteration, damping, and failure reporting

## Block splitting is a numerical choice

The Poisson and two continuity equations form a nonlinear coupled boundary-value problem. A simple reconstructible iteration separates them: (1) initialize potential from linear interpolation between prescribed contacts; (2) solve the electron and hole conservative tridiagonal systems at that fixed potential; (3) solve the potential tridiagonal system using the resulting charge; (4) damp the potential update; (5) repeat until *both* the nonlinear residual and the update meet tolerances.

With provisional \(u^{(k+1),*}\), use \(u^{(k+1)}=u^{(k)}+\omega(u^{(k+1),*}-u^{(k)})\), where \(0<\omega\leq 1\). Fix the two potential boundary values after each update. The iteration is not generally contractive; too much bias, too little Debye screening, unrealistic contacts or extreme doping may make it diverge or oscillate. Damping improves but does not certify convergence.

## Distinguish residuals and mathematical claims

Compute three separate errors at the final state: 

\[R_{P,i}=\frac{\lambda^2}{h^2}(2u_i-u_{i-1}-u_{i+1})-(p_i-n_i+C_i),\]

\[R_{n,i}=F_{n,i+1/2}-F_{n,i-1/2},\quad R_{p,i}=F_{p,i+1/2}-F_{p,i-1/2}.\]

These discrete residuals are not estimates of the *continuum* error. Manufactured analytic solutions, mesh refinement and independent dense solvers check different failure modes. A successful single-grid residual can coexist with a wrong unit scale, incorrect physical boundary conditions or significant discretization bias. Each reported result therefore includes an iteration count, a convergence flag, maximum Poisson residual, both particle-flux variation residuals, and a global Gauss balance. Failure must raise a typed error with the reason and must not return the last iterate as accepted.

## Initial conditions and contact constraints

This reference solver treats a steady state rather than a time evolution: there is no initial physical carrier distribution. The numerical *initial guess* is not an experimentally observed state. The two species have fixed contact densities, not current-controlled injection. The implementation assumes zero carrier generation/recombination; to model a diode with traps or illumination one must add \(G-R\) source terms and define their units and material parameters explicitly. Without those, treating its current–voltage values as manufactured diode measurements would be an invalid scientific inference.

## Rebuild protocol

Run the reference model on a symmetric equilibrium with all contacts equal and zero doping. Increase the potential bias in small increments, preserving the previous solution only as a numerical warm start if the solver implementation explicitly supports it. For every case, confirm the two contact conditions, nonnegative densities, independent charge-balance residual, and step-size convergence. Force `maxiter=1` on a nontrivial case and require rejection; introduce NaN, negative density and illegal geometry and require rejection. This supplies falsification opportunities instead of only golden-path examples.
