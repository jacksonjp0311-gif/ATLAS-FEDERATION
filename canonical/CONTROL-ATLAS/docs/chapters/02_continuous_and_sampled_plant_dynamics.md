# Chapter 02: Continuous and sampled plant dynamics

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A standard teaching plant is `τ ẏ = -y + K u`, with time constant τ>0 and constant input u. For a settled step to final value, `y(t)=y∞+(y0−y∞)exp(−t/τ)`. This is not a measured response curve and excludes dead time, nonlinearity, hidden poles and measurement noise. In this limited model, at `t=τ` the state has completed about 63.2% of the difference between initial and final values.

For piecewise constant inputs held over a sample period Δ, the exact discrete update is `y[k+1]=a y[k]+b u[k]`, with `a=exp(−Δ/τ)` and `b=K(1−a)`. This zero-order-hold conversion follows by integrating the first-order differential equation. It is not the same as Euler approximation `a≈1−Δ/τ`, which can produce misleading behavior at large Δ. MathWorks documents the ZOH convention for conversion of continuous LTI models to sampled systems. A real digital controller also has conversion, sampling jitter, computational latency, quantization, scheduling and delay; none are present in the toy update.

**Failure experiment:** sample one measured system at two rates, then claim that the faster rate always gives a better controller. With unknown high-frequency dynamics or noise, higher sampling can amplify bandwidth demands. Without measured sensor/actuator dynamics and processing delay, the model cannot predict real loop performance.

**Reusable packet:** provide τ, K, operating point, perturbation range, hold convention, Δ, actuator and sensor units, and whether parameters are observed, fitted or guessed. The calculator returns exactly this bounded model—not an unrestricted continuous-to-discrete converter.

## Bound reference topics

- **The exact first-order stable response assumes one real pole and no disturbance** (`equation`): firstorder-response
- **Exact first-order ZOH depends on held-constant input between samples** (`equation`): zoh-response
- **Continuous-time dynamics and sampled dynamics require an explicit hold convention** (`concept`): continuous-vs-discrete
- **Exact model discretization does not identify the actual plant** (`concept`): unknown-plant

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MATLAB-ZOH](https://www.mathworks.com/help/control/ref/dynamicsystem.c2d.html)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)

**Limit:** no new experiments or independent control review.
