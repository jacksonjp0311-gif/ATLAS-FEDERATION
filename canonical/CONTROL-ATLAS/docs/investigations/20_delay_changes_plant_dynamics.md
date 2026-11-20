# Investigation 20 — A one-sample delay reverses the stability result

A constructed discrete plant has a=1.5, b=1, K=1.2. Without feedback delay the characteristic pole is `1.5−1.2=0.3`, stable in the ideal linear scalar model. With feedback based on x[k−1], the characteristic equation is `z²−1.5z+1.2=0`. Its complex roots have magnitude `√1.2≈1.095445`, outside the unit circle.

The counterexample exposes a key architecture risk: assuming local-model decision time equals actual sensor-to-actuator response time. A model that passes without delay may fail even with one exact sample delay. It does **not** establish the stability of random, multiple-period, packet-loss or asynchronous delays. Record per-message timestamps, jitter, synchronized clocks, actuator timing and dropouts; select a model aligned to observed dynamics.

**Run:** `python -m control_atlas robust-casebook`. Published networked-delay research considers much broader structures than this algebraic example; [networked delay/dropout study](https://www.sciencedirect.com/science/article/pii/S0016003213001920) abstract is only background.
