# Investigation 21 — Failure to certify with P=I does not mean unstable

For A=diag(0.7,0.9), a candidate P=I gives Q=diag(0.51,0.19), both positive definite, certifying strict decay of V=xᵀP x in the stipulated autonomous 2×2 discrete model. The calculation is a finite-precision diagnostic, not a machine-checked formal proof.

For the different matrix `A=[[0.5,4],[0,0.5]]`, the two eigenvalues equal 0.5, yet P=I does **not** satisfy the strict quadratic decrease test because the cross term causes large transient growth in the Euclidean norm. Saying “therefore A is unstable” would be a logical error: another P can certify it. A failed candidate is *not certified*, not a counterproof of all certificates.

This also illustrates why a nominal eigenvalue check is incomplete for a real controller with saturation or uncertain dynamics. The source-linked record must preserve what property was actually tested and which physical features were excluded. [MIT Lyapunov notes](https://underactuated.mit.edu/lyapunov.html).
