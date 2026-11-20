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
