# Investigation 16 — A factor-of-eight creep-rate change is not eightfold risk

Take hypothetical Norton–Arrhenius parameters A=1e−8 s⁻¹ MPa⁻³, n=3, Q=200 kJ/mol, T=900 K. For 50 MPa the modeled steady creep strain rate is about **3.0863×10⁻¹⁵ s⁻¹**. Doubling stress to 100 MPa multiplies the model rate by eight because n=3. The numerical factor is entailed by an assumed power law, not proof that any metal follows it in service.

**Invalid conclusion:** “therefore the part will fail eight times faster.” Rupture-time, tertiary acceleration, necking, grain-boundary damage, oxidation and stress redistribution are not in this model. Even cumulative constant-rate strain `ε≈εdot t` is not a creep failure criterion. Environmental and load histories can dominate a real application.

A sound report would identify actual material heat, processing, sample size and geometry, creep-test curves, strain gauge calibration, stress and temperature control, duration, fitted parameter covariance, mechanism validity and extrapolation bounds. Without that evidence, a time-to-failure output is intentionally unavailable. The calculator accepts the parameter units explicitly and refuses nonpositive temperature and numerical underflow rather than declaring a truly zero creep rate.

**Outcome:** a bounded kinetics teaching tool and a clear line between calculation and prognostics. Control Atlas (queued) will later address changing stress/temperature over time, but cannot create missing material test evidence.
