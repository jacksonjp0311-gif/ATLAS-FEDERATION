# 27. Transformation kinetics: isothermal laws and temperature-history traps

## What the model says

A standard phenomenological form for an isothermal transformed fraction is `X(t)=1−exp[−(k t)^n]`, often associated with Johnson–Mehl–Avrami–Kolmogorov-type kinetics under selected nucleation and growth assumptions. `k` has units s⁻¹, `n` is dimensionless, time is seconds, and `X` is between zero and one. The form is *not* a universal law of microstructural evolution. Different process routes, nucleation mechanisms, impingement, spatial distributions and incubation effects can produce different kinetics.

For target fraction `0<X<1`, invert to `t=[−ln(1−X)]^(1/n)/k`. The calculator requires a strictly interior desired fraction; an exact fraction one occurs asymptotically in the ideal model and must not be reported as a finite termination time. A nonpositive kinetic rate or exponent is invalid.

## Constructed example

For assumed `k=0.001 s⁻¹` and `n=2`, half transformation occurs at approximately **832.55 seconds**. Applying the forward equation to this time returns 0.5 within floating-point rounding. The chosen parameters are not from a real alloy and cannot be used to specify a furnace recipe. The example is an algebraic verification, not evidence for a physical half-transformation time.

## What must be learned experimentally

A reproducible kinetic claim needs the starting phase fractions, sample composition and history, quench and aging protocol, actual specimen thermal profile, measurement method (DSC, dilatometry, microscopy, diffraction, etc.), segmentation calibration, uncertainty and replicate data. Fit parameters must be estimated with a documented temperature and composition range. Multiple mechanisms can fit a short transformation curve; a high R² is not enough to establish the kinetic model. Nucleation barriers, diffusion constraints and competing reactions may change throughout the process.

## Critical failure: using an isothermal model for a cooling curve

A continuous-cooling transformation is a **history-dependent** problem. A measured TTT curve is not automatically a CCT curve, and simply adding separate isothermal fractions is generally unjustified. If the thermal path changes, a validated state-evolution model or direct nonisothermal evidence is required. This Atlas does not implement Scheil additivity, latent-heat-coupled process simulation or microstructure prediction. The model returns fractions only under the specifically declared fixed-temperature parameterization.

**Connections:** Chapter 04 (processing and defects), Chapter 15 (diffusion and kinetics), Chapter 20 (phase equilibria), and Control Atlas (eventual temperature-program models, not yet built). The v1 content deliberately separates an executable arithmetic function from actual heat-treatment qualification.
