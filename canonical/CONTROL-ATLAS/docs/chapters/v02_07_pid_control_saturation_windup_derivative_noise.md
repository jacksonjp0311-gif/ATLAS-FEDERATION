# 07. PID control, saturation, windup, derivative noise

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Proportional-integral-derivative (PID) control combines a term proportional to tracking error, accumulated error and a rate term. It is widely useful but is not one universal algorithm: continuous/discrete implementation, error/measurement derivative choice, integral discretization, filtering, setpoint weighting and output saturation matter. A gain tuple with no sample time, actuator limits or derivative convention is underspecified.

Integral action can drive steady errors toward zero under suitable plant conditions, but an actuator with hard limits cannot produce any demanded command. If the integrator accumulates while the actuator remains saturated, the stored integral may delay recovery after the setpoint changes. MathWorks documents distinct clamping and back-calculation antiwindup policies; they are not interchangeable. Derivative action can amplify measurement noise and is commonly filtered or taken on measurement rather than setpoint to avoid derivative kick.

The Atlas's `pid_saturated_demo` applies a simple **conditional integration clamp** to supplied setpoint and measurement sequences, with derivative on measurement. It returns P, I, D, raw command, saturated command and a saturation flag. It **does not simulate a physical plant or close a feedback loop against measured device data**. Comparing traces with and without clamping demonstrates only internal controller arithmetic. The implementation is intentionally not an industrial PID tuning assistant.

**Teaching counterexample:** with a large positive error and a command constrained to ±1, an unconstrained integral term can grow without bound over repeated samples while the actual output stays at +1. Conditional integration prevents further accumulation when it would deepen saturation, but cannot determine whether the chosen gains are stable for an unknown plant. Actuator backlash, rate limits and dynamic dead-time remain outside the trace.

A real PID review must preserve controller sample time, controller form, saturation/tracking logic, derivative filtering, sensor calibration and placement, setpoint policy, disturbance tests and independent safety interlocks. No user should send these test commands directly to a real valve or heater.

**Publisher/documentation scope:** [MATH-PID-AW](https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html) · [MICH-PID](https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID). These are exact source pointers and original summaries, not redistributed source text or new measurements.
