# Investigation 04. A saturated controller can accumulate hidden integral error

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A synthetic PID trace holds setpoint 10 and measured output 0 for eight samples, using Kp=1, Ki=.5, Kd=0, dt=1 s and actuator bounds [-1,1]. Without antiwindup, the controller integral accumulates despite the actuator being pinned at +1. With the stated conditional-integration clamp, the integral is frozen while the candidate update would deepen saturation. Both traces have clamped physical *commands*, but very different stored controller state. A later reversal in error could therefore lead to different recovery behaviors if a real plant were attached.

The example is **controller arithmetic**, not a closed-loop experiment or automatic tuning result. A different PID implementation might integrate after saturation, use a back-calculation coefficient, filter derivative terms or implement separate tracking antiwindup. None is universally superior without plant-specific evidence and safety constraints.

**Missing evidence:** actuator transfer function, sample time jitter, rate constraints, plant delay, noise and real disturbance tests. **Source:** MathWorks Anti-Windup Control example, selected R2026b documentation.
