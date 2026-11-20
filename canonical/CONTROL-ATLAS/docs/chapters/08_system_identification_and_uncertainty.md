# Chapter 08: System identification and uncertainty

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

A system-identification study attempts to infer a model from inputs and observed outputs. Even if the dataset is accurate, different models may fit the same limited trajectory. For example, a first-order process response observed over a narrow timespan may not reveal an ignored slow thermal mode or a delay. A single closed-loop trace may make actuator changes correlated with disturbances, complicating inference about the open-loop plant.

The experiment design must define excitation range, the steady operating point, measurement units, sampling clock, disturbance history and candidate model class. Parameter uncertainty should include instrument calibration, sensor drift, saturation, unmodeled modes, noise assumptions, and any prior engineering constraints. A fitted mean squared error is not a guarantee of correct uncertainty bounds, physical interpretation, robustness or ability to stabilize the actual machine.

A reasonable sequence is to collect timestamped excitation/response data under supervised and safe operating conditions; fit multiple physically plausible models; compare residuals and holdout behavior; challenge the models with independent disturbance cases; and conduct bounded sensitivity analysis for the intended controller. If an identification experiment cannot be done without violating production safety constraints, that is a limitation, not a reason to invent parameter values.

The current Control Atlas deliberately **does not fit plants from data**. All demo coefficients are supplied. This separation is an engineering safety boundary: a mathematical solver may work perfectly on a false or incomplete plant model.

## Bound reference topics

- **Identifiability requires informative excitation and an explicit candidate model** (`concept`): excitation-identification
- **Disturbance and controller action can confound a closed-loop identification** (`concept`): confounding-control
- **A good fitted response is not physical-model validation** (`concept`): fit-not-validity
- **Compare fitted dynamics on holdout inputs and disturbances** (`method`): heldout-disturbance

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [MATLAB-DISC](https://www.mathworks.com/help/control/ug/continuous-discrete-conversion-methods.html)

**Limit:** no new experiments or independent control review.
