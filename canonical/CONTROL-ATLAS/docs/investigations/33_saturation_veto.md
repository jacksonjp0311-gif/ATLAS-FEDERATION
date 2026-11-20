# Investigation 33 — Stable state bound, insufficient actuator authority

The same authored model from Investigation 32 remains state-box invariant according to the ideal closed-loop equation. Shrink the allowable actuator from ±0.25 to ±0.12 while keeping feedback `K=[0.1,0.1]` and state radii `[1,1]`. The worst requested input is `|K0|r0+|K1|r1=0.2`, exceeding 0.12. The tool therefore returns `state_box_invariant_for_every_assumed_model=true`, `actuator_unsaturated_for_every_state_in_box=false`, and `conditional_invariance_and_input_feasibility=false`.

This is an explicit **veto** on the combined certificate. If the hardware saturates, the modeled feedback `u=-Kx` cannot always be implemented. A different nonlinear saturated control law requires new analysis. A low-order optimizer reporting an unconstrained optimal command is not evidence that the actuator can execute that command in time.

No device is driven. The result does not tell an operator what the physical fallback should be; even an output of zero may be hazardous for some processes. NIST SP 800-82r3 stresses integrity and safety in OT operation, but this method is a teaching tool, not a safety instrumented system.
