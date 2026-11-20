# Investigation 15 — Isothermal fraction inversion versus a real heat-treatment schedule

Consider a purely invented isothermal transformation with rate parameter `k=0.001 s⁻¹` and exponent `n=2`. Applying `X=1−exp[−(kt)^n]`, solving for X=0.5 gives **832.554611 s**. Substituting this time in the forward equation reproduces the fraction. This is exact algebra under a stipulated model, not a measured steel or polymer kinetic response.

Now imagine an operator changes temperature during the hold. The formerly fitted k is not guaranteed to apply: nucleation, growth, diffusivity, activation energy and phase pathways may differ at each temperature. The same final elapsed time does not guarantee the same final fraction. Applying the old isothermal formula to a nonisothermal cycle is an *unverified extrapolation*, not a small computational error.

To make a real heat-treatment decision, obtain a time-temperature history, representative microstructure, composition, nucleation constraints, phase fraction measurement method and quality, actual process kinetics, confidence bounds and possibly TTT/CCT measurements. A process controller's set-point log is not necessarily the specimen thermal record.

The Atlas calculator returns a conditional fraction only. It refuses exact fraction 1 when solving for finite time because this ideal law approaches 1 asymptotically. This protects evidence boundaries rather than inventing a finish time. Real heat-treatment qualification must use calibrated kinetics and relevant standards.
