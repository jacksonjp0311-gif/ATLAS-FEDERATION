# Investigation 25 — One harmless-looking gain matrix, one ill-conditioned direction

**Origin:** constructed 2×2 algebraic example. No real dynamic system or control hardware.

Supply G=[[1,−1.99],[−1.99,1]] and K=I. Then M=I+GK=[[2,−1.99],[−1.99,2]]. Its singular values are **3.99 and 0.01**, and condition number **399**. The program's S=(I+GK)⁻¹ and T=I−S satisfy S+T=I within floating-point tolerance.

The near-singular direction is a useful warning: looking at individual entries, or a single scalar “loop gain,” misses directional sensitivity. But this calculation contains no poles or frequency sweep; it cannot show whether a dynamic plant is internally stable or robustly stable. Singular values at one frequency cannot replace a system model, actuator saturation checks or a site-specific safety case.

**Reproduce:** `mimo_2x2_return_difference(G,K)` in `control_atlas.advanced`. An independent NumPy SVD and inverse agree on randomized 2×2 models in the release oracle. **Next evidence:** obtain transfer/state-space dynamics, operating point, calibrated units, bandwidth, latency and full-frequency uncertainty before making a physical stability claim.
