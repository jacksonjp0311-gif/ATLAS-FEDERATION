# Investigation 30 — Perfect training fit, worse later prediction

A constructed 32-step scalar ARX history starts with dynamics x+=.8x+.2u for its first 24 samples. The later eight steps instead use x+=.95x+.2u. The training model fits the first segment to near machine precision; its later one-step prediction RMS is about **0.129** because the true synthetic system changed. This is mathematical evidence that training fit alone cannot establish future prediction quality.

The implementation uses a chronological hold-later segment, not an external trial. The validation residuals use the **observed** prior state at each step. It therefore does not test multi-step model rollout accuracy, closed-loop stability, or real machine drift. It also refuses a constant-state/zero-input history with insufficient excitation rather than presenting arbitrary fit coefficients.

This example suggests a data-collection protocol: define a target operating envelope, record independent process disturbances and times, reserve later data by regime/shift, log actual vs commanded actuator values, and compare residuals under alternative models. In a real closed-loop process, ordinary least squares may still be biased by feedback; held-out time does not identify causation by itself.
