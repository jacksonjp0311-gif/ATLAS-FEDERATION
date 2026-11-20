# Investigation 26 — A common certificate is sufficient; a failed candidate is not an instability verdict

For a synthetic discrete-time family with A11∈[.5,.6], A12,A21∈[−.03,.03], A22∈[.3,.4], and P=I, the program checks all **16** matrix-box vertices and finds a strictly positive minimum eigenvalue of Q=P−AᵀPA. The worst is approximately **0.634697**. Under the exact linear model, the convexity argument supports a common quadratic decrease statement across the entire independent-entry box; this is not an interval-arithmetic verification of actual equipment.

Now replace the family with a single A=[[.8,1],[0,.8]]. Its eigenvalues are both .8, so it is asymptotically stable, yet P=I fails the sufficient test. The program correctly reports *candidate not certified*. Calling the plant unstable would be wrong. Another P may certify it. A real controller with saturation, delays or correlated uncertain coefficients is outside this test's scope.

**Adversarial question:** does numerical vertex checking prove robustness under every industrial disturbance? **Answer:** no. The guarantee is conditional on the exact bounded discrete-time matrix family, verified modeling assumptions, and numerical tolerance. Separate physical uncertainty identification, disturbance and interlock engineering remain necessary.
