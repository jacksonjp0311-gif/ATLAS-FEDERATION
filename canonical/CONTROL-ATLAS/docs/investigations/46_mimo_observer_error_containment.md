# Investigation 46 — Two-state observer under hard bounded sensor noise

Build a *synthetic* two-state plant with `A=[[.9,.05],[0,.8]]`, observation `C=I2`, observer gain `L=diag(.45,.40)`, initial absolute estimation radii `[.4,.25]`, process disturbance radii `[.03,.05]` and per-sensor measurement noise radii `[.10,.12]`. The error recurrence is `e+= (A-LC)e+w-Lv`, and the bound is `E+=|A-LC|E+W+|L|V`.

The implementation returns a componentwise radius at each sampled step. A separate NumPy implementation reproduces the recurrence for hundreds of random systems. Thousands of randomly selected trajectories consistent with the declared box bounds remained within the intervals; those tests support code correctness, not physical hard-bound evidence. For this example, the infinity row-sum of `|A-LC|` is below one, supplying a simple sufficient stationary error envelope.

Adversarial counterexample: a stable rotating error system can fail the **sufficient** absolute-value row-sum criterion. The code must then return no stationary certificate under that test, not claim that the actual plant is unstable. Another negative case uses an inconsistent measured output: the reading may contradict a bound, but sensor fault, model error and timing remain alternative explanations.

**Unmet conditions:** measured sensor noise floors, calibration, transport delays, actuator applied-input alignment, state normalization and unmodeled dynamics. A calculated observer bound is not a physical safety function.
