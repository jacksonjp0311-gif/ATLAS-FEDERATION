# Investigation 36 — Why a hundred successful rollouts do not certify a bounded set

An experimenter simulates an original two-state model with disturbances alternating among `[+0.05,0]`, `[−0.05,0]`, `[0,+0.05]`, `[0,−0.05]`. The trajectories stay finite. This is useful to test that the implementation does not numerically explode on those cases. It does not check every initial state, disturbance sequence, interval-parameter combination, sensor-bias pattern or actuator condition.

A universal invariant-set certificate requires inequalities covering **all** modeled states and disturbances in the set. The exact corner-based method can prove this conditional mathematical statement for a rectangular 2×2 class. But it cannot prove its own uncertainty bounds were measured correctly. Conversely, a single synthetic violation under assumptions can falsify an overly broad numerical claim, even though it does not show that actual equipment will fail.

The study should label distinct evidence: code tests, separate numerical algorithms, model-specific mathematical proof, experimental system identification, operator safety review and deployed behavior. None can be replaced with a number of rendered charts or agent-generated explanations. **No actual process was controlled** in this work.
