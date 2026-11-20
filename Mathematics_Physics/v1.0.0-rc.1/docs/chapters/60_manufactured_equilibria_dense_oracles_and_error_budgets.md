# 60. Manufactured equilibria, independent oracles, and error budgets

## Exact discrete coupled solution

Choose \(u(x)=a+bx\), \(n(x)=N e^{u(x)}\), and \(p(x)=P e^{-u(x)}\), with \(N,P>0\). Prescribe \(C(x_i)=n(x_i)-p(x_i)\) at interior nodes, and set all six contact values to these analytic functions. Then \(-\lambda^2 u''=0\) and \(p-n+C=0\) at each node. The Scharfetter–Gummel flux vanishes on every edge because each exponential carrier ratio exactly cancels the Bernoulli factors. This provides an **exact discrete manufactured equilibrium** for any finite supported grid, independent of calibrating a real crystal.

Try both signs of \(b\), unequal \(N,P\), and very fine meshes. Compare every state value, not only the terminal current. This solution is not evidence that a real semiconductor realizes the imposed doping function or boundary concentrations. It is a proof obligation for the discrete signs and implementation.

## A separately coded nonlinear oracle

Construct \(3m\) unknowns \((u_1,\ldots,u_m,n_1,\ldots,n_m,p_1,\ldots,p_m)\). Assemble the residual directly with a different vectorization and pass it to a dense SciPy nonlinear root solver. The reference implementation uses explicit tridiagonal Gummel steps, whereas the oracle solves the combined dense system through a separate algorithm. Compare every potential and carrier concentration at 60 deterministic seeded, small, moderately biased problems, and record the largest absolute difference and independently evaluated residual. Both implementations share the same mathematical model; agreement is *algorithmic corroboration*, not independent physical evidence.

## Four distinct uncertainty classes

(1) **Roundoff:** floating-point cancellation and finite mantissas; compare with analytic or arbitrary precision when practical. (2) **Algebraic error:** residual/termination accuracy of the finite nonlinear system. (3) **Discretization error:** mismatch between a mesh solution and a continuum model; use manufactured non-affine solutions and refinement rates, which this particular coupled release still needs beyond the exactly affine equilibrium. (4) **Model and measurement error:** uncertain permittivity, doping, mobility, contact boundary processes, carrier statistics, recombination, temperature and interface traps. The first three are not substitutes for the fourth.

## Falsification and release gate

A historical regression test must keep its original inputs, source tree and assertions. A fresh archive replay must reproduce the current candidate suite, and a SHA-256-inventory must prove previous immutable records remain unchanged. If the exact archive cannot be reconstructed or source permissions are unknown, those gates remain open. A successful collection test does not sign a peer review or certify source files never retrieved. The v1 candidate is a bounded scientific *content and software* artifact until source-authentication and expert-review gates can be genuinely closed.
