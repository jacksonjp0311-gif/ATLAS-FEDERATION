# 58. Scharfetter–Gummel flux, M-matrices and positivity

## Derivation on one edge

Let \(u\) vary linearly and \(D\) be positive and constant across an edge \([x_i,x_{i+1}]\) of length \(h\). Take the electron number flux \(F=-D(n'-nu')\). The integrating-factor identity \((n e^{-u})'=-F e^{-u}/D\) shows that an exact edge integration yields

\[F_{i+1/2}=\frac{D}{h}\{B(-\Delta u)n_i-B(\Delta u)n_{i+1}\},\qquad
B(z)=\frac{z}{e^z-1},\quad B(0)=1.\]

For holes use \(-u\): \(F_{p,i+1/2}=D_p h^{-1}[B(\Delta u)p_i-B(-\Delta u)p_{i+1}]\). The Bernoulli relation \(B(-z)=B(z)+z\) is algebraically exact. Numerically, evaluate \(B\) near zero through a Taylor series or `expm1` to avoid catastrophic cancellation, and use stable rearrangements at moderately large positive or negative arguments.

## Building the tridiagonal system

Set consecutive finite-volume fluxes equal at every interior node. For electron unknown \(n_i\), with \(a=\Delta u_{i-1/2}\), \(b=\Delta u_{i+1/2}\), the coefficients are

\[-B(-a)n_{i-1}+[B(a)+B(-b)]n_i-B(b)n_{i+1}=0.\]

The hole system substitutes \(-u\) for \(u\). Contact concentrations move to the right side of the linear system, whose off-diagonal entries are nonpositive and whose inverse has nonnegative entries for the connected Dirichlet chain. A positive prescribed contact therefore yields nonnegative interior density, subject to finite arithmetic and the admitted parameter bounds. This discrete *M-matrix* structure is why merely applying central differences to a drift term can produce negative densities where exponential fitting does not.

## Exact equilibrium checks

If \(n_{i+1}=n_i e^{\Delta u}\), the electron flux is exactly zero in exact arithmetic; for holes the zero-flux ratio is \(p_{i+1}=p_i e^{-\Delta u}\). Use both checks, including negative slopes and contact-density asymmetry. Do not claim that equal electron and hole densities imply charge neutrality when dopants are present: Poisson must also hold.

## Stress tests and boundaries

The reference implementation bounds nodal voltage jumps and rejects overflow, nonfinite densities, unphysical negative concentrations and near-singular linear pivots. A positive density on a synthetic grid is not by itself evidence of the physical validity of Boltzmann statistics. At very high doping, degeneracy, scattering, interface effects and field-dependent mobility matter; a simple equilibrium Einstein relation can fail. The original Scharfetter–Gummel 1969 IEEE paper is a bibliographic scientific reference with rights governed by IEEE. Its original bytes are **not** mirrored here or represented as authenticated.

## Reproduction

Set constant \(u\), prescribe density endpoints, and verify that the solution is affine in \(x\) and the flux is constant. Next set a monotonic \(u\) and construct exponential contact ratios: both edge fluxes should vanish. Apply extreme valid but asymmetric contacts and verify positivity and constant flux, then deliberately exceed the allowed potential magnitude and confirm explicit rejection. A separate SciPy dense-root comparison tests the fully coupled result, but it does not become an experimental device measurement.
