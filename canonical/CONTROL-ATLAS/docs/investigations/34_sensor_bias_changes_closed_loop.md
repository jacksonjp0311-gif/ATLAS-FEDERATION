# Investigation 34 — A proof for x is not a proof for x-hat

The mathematical invariant-set certificate assumes exact state feedback. In a constructed simulator, the state evolves as `x'=A x+B u+w`, but the command uses `u=-K(x+bias)` subject to a clamp. A second run with identical underlying plant and disturbance sequence adds an artificial sensor bias after the sixth sample; the commands and state trajectories differ.

These series are not physical data. The simulator cannot determine whether a real anomalous reading comes from a physical state shift, sensor offset, numerical drift or a malicious manipulation. It only demonstrates that an unmodeled estimation error can alter feedback. The robust-box method refuses to return a proof when full state feedback is not affirmed; a robust observer-controller proof would need to model estimation error, clock delay and disturbance coupling.

**Evidence request for a real investigation:** independent reference sensors, sensor calibration, time stamps, actuator response, control-law version, sensor fusion assumptions and safety-logic responsibility. NIST SP 800-82r3 provides an operational integrity context. No fault diagnosis or security incident is inferred from this synthetic case.
