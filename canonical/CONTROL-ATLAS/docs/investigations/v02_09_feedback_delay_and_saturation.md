# Investigation 09. Modeling a delay matters more than a larger gain

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A feedback design can appear well behaved in a simulated first-order plant with instantaneous sensing and actuation, then oscillate when a physical sensor and valve introduce dead-time. A sample arriving late is not equivalent to a timely state reading. Saturation can also break the assumed linear law, so eigenvalue checks of an unconstrained model no longer describe the actual controller.

This investigation is deliberately a **design audit rather than an implemented delay simulator**. It enumerates data needed to test a real system: command/response timestamp traces, actuator rate limits, sensor filtering, nonlinear operating regions, sample drops and protected fallback behavior. It refuses to infer a robust stability margin without such information, even if a nominal pole calculator returns “stable.”

**Sources:** Åström–Murray feedback scope, Michigan control tutorials and MathWorks antiwindup example. **Outcome:** risk and evidence list, no physical action.
