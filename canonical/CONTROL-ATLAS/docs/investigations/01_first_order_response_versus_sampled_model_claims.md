# Investigation 01: First-order response versus sampled-model claims

**Origin:** synthetic authored model, no real equipment.

First-order step with tau=10 s reaches about 63.2% of the step by t=10 s. Exact ZOH for tau=5 s, gain=2 and dt=.5 s gives a=e^-0.1 and b=2(1-a). This checks the *stipulated model*, not real machine dynamics. If a second unmodeled pole or delay exists, the same response data may not support these calculations for future excitation. Require measured frequency/step data, actuator calibration, latency and independent holdout disturbances before using for control.

**Source:** https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
