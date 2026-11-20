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
