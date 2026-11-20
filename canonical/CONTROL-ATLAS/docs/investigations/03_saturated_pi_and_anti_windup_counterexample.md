# Investigation 03: Saturated PI and anti-windup counterexample

**Origin:** synthetic authored model, no real equipment.

A constructed first-order process receives an unreachable reference followed by a smaller one. The simple PI implementation accumulates integral error if configured without anti-windup. Clamping freezes further integration when error pushes beyond a saturated rail, improving the selected integrated absolute error in this particular test. No generalized optimal-gain theorem follows. Add actuator delay, rate limits, sensor bias, interlocks and failure trace to test real equipment.

**Source:** https://www.mathworks.com/help/simulink/slref/anti-windup-control-using-a-pid-controller.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
