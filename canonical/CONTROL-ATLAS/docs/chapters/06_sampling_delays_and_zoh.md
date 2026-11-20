# Chapter 06: Sampling, delays, and ZOH

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Ideal sampling theory states that a signal bandlimited below B hertz can in principle be reconstructed without aliasing if the sample rate exceeds `2B`, assuming appropriate anti-aliasing and reconstruction conditions. A safety controller must satisfy more than this. Its closed-loop bandwidth, delays, sensor filters, computation jitter and discretization errors affect stability and performance.

A sampled loop can alias high-frequency sensor disturbances into low-frequency readings. An actuator may hold its previous command between updates, creating a zero-order hold, or may follow interpolation or pulse-width modulation. The difference matters when modeling high-frequency behavior. Modern toolboxes expose multiple continuous-to-discrete conversion assumptions; selecting a method does not identify unmodeled fast modes.

**Worked distinction:** an ideal bandlimited signal with B=4 Hz, sampled at 10 Hz, satisfies `fs>2B`. That says nothing about whether a 10 Hz controller can regulate a high-bandwidth motor safely. Conversely, sampling a supposedly B=5 Hz signal at exactly 10 Hz does not satisfy the strict inequality used by the Atlas. A finite delay and narrow phase margin can defeat an otherwise plausible proportional controller.

A credible digital deployment report needs measured or bounded worst-case scheduling delays, sensor timestamps, actuator response, anti-alias filters, sample/hold behavior and an uncertainty model. The educational `nyquist_information` function returns a condition and its limits; it is not a control design tool.

## Bound reference topics

- **Nyquist strictly applies to a known bandlimited ideal-sampling signal** (`equation`): sampling-bandlimited
- **Sampling above twice bandwidth is not a controller-stability guarantee** (`concept`): sampling-not-control
- **A digital actuator command held between samples is a physical hold assumption** (`concept`): zoh-hold
- **Delays can consume phase margin even for a stable instantaneous plant** (`concept`): delay-phase

## Source pointers

- [MATLAB-ZOH](https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)
- [MATLAB-ALIAS](https://www.mathworks.com/help/signal/ug/aliasing.html)

**Limit:** no new experiments or independent control review.
