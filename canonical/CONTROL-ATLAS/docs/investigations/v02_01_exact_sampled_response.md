# Investigation 01. Exact sampled response versus unstable approximation

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A hypothetical system follows the specified first-order model `tau*dy/dt+y=K*u`, with gain K=2, time constant tau=3 s, zero initial state and a unit step. There are no measured physical signals. The continuous analytical response at three seconds is `2*(1-exp(-1))`. For a zero-order held input sampled every half-second, the exact discrete state uses `a=exp(-1/6)`, `b=2*(1-a)` and six input holds. The discrete result matches the analytic response to floating-point precision. This is a controlled internal numerical identity, not a plant identification or a controller-quality assessment.

A naive implementation might instead use explicit Euler with a sample interval much larger than the time constant, so its discrete coefficient `a_E=1-dt/tau` can fall outside the unit circle even though the original continuous first-order plant is stable. The correct investigation must distinguish an unstable numerical approximation from an unstable physical system. Check the chosen hold type and sample timing rather than treating every discretization as equivalent.

**Evidence needed for a real device:** timestamps, actuator hold policy, actual sampled input/output signals, sensor calibration, unknown dead-time and operating conditions. **Refusal:** the calculator cannot infer whether a real heating chamber responds as a first-order plant. **Sources:** SciPy `cont2discrete` documentation and Åström–Murray, *Feedback Systems* chapter scope.
