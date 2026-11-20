# Investigation 32 — An invariant box under bounded disturbance

**Question:** Can a fixed two-state feedback law keep every state within a chosen box under stipulated plant and disturbance uncertainty? In the authored example, the state radii are `[1,1]`, disturbances are bounded by `[0.05,0.05]`, and feedback is `K=[0.1,0.1]`. The six independent plant intervals provide 64 vertices. For each vertex, the tool bounds `|x'_i|≤Σ_j |A_ij-B_i K_j|r_j+d_i` and compares with the chosen state radii. It separately checks `|u|≤|K0|r0+|K1|r1≤0.25`.

The construction produces a conditional mathematical certificate under an exact sampled LTI model and true full-state feedback. It uses no plant data, actuator device or physical sensor. The maximum bounds are not confidence intervals learned from measurements; they result from stipulated input intervals. If those intervals are false, the certificate does not apply.

An independent test enumerates all 64 parameter corners and four state-box corner signs across seeded synthetic models. It compares the worst observed one-step bound to the original algorithm, without pretending the random tests are a physical experiment. An invariance result can be used to organize a test plan, but only a qualified process-specific review can establish applicability and operational risk.

**Reproduce:** `python -m control_atlas invariance-casebook`. **Source:** MIT [Robust and Stochastic Control](https://underactuated.mit.edu/robust.html), invariant-set discussion.
