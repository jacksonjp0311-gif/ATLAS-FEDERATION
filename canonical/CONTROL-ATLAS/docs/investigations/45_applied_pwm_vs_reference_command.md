# Investigation 45 — A commanded signal is not an applied input

Consider a controller that commands an input of 10 arbitrary units, but the actuator magnitude, slew and response rate allow only 0.1 at the next sampled instant. Existing Control v0.6 formulas distinguish requested, clipped, slew-limited and applied values. The experiment is *synthetic*, but its central error mode is grounded in how real actuator limits affect dynamic control.

The new OpenMCT parser uses the explicitly logged `PWM` column for an input-output model and retains `REF` as the reference. The data-paper description confirms both appear in the physical log. If a regression instead uses REF while the actuator has lag or saturation, it is estimating a different relationship from the one assumed by the underlying plant equation. An observer can only cancel the input term in its error dynamics if it uses the same **known applied input** as the plant.

For real validation, compare the controller command, physical PWM, measured speed, sample time, actuator model and load changes. A channel label is not independent proof that a driver performed its action. A safety-rated independent interlock is a distinct system, not supplied by a Python clamp. No hardware was commanded during this release.
