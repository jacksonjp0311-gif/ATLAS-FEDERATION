# 02. Continuous-time responses and exact sampled holds

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A first-order model `tau dy/dt + y=K u` has time constant `tau>0`, static gain `K` and output `y`. With a constant step input held after t=0 and known initial y0, its exact continuous response is `y(t)=K u+(y0−K u)exp(−t/tau)`. Under this *single model*, the difference from the final value has decayed to 1/e after one time constant. It does not establish an actual device's response after one step because many physical systems include delay, higher-order dynamics, nonlinearities and disturbances.

Sampling changes the implementation. Under a **zero-order hold**, input u[k] stays constant during each interval of length Δt; the corresponding exact first-order difference equation is `y[k+1]=a y[k]+b u[k]`, with `a=exp(−Δt/tau)` and `b=K(1−a)`. Explicit Euler would give `a≈1−Δt/tau`, which can become unstable at coarse sampling even if the original continuous model is stable. This is a numerical-approximation defect, not a change in physical plant stability. The SciPy reference documents ZOH separately from Euler, backward difference and Tustin methods.

The Control package supplies analytic scalar solutions and the exact ZOH coefficients and iterates. It does **not** fit a real time constant, compensate sensor delay, simulate dead-time, or choose a safe controller for a device. Users must provide model units and sample timing. It rejects nonpositive time constants and sampling intervals, nonfinite inputs and excessive step sequences.

**Verification example:** set K=2, tau=3 s, Δt=.5 s, u[k]=1, y0=0. The exact discrete model has `a=exp(−1/6)` and `b=2(1−a)`. After six input holds, y[6]=2(1−exp(−1)) matches the continuous response at t=3 s. An independent SciPy `cont2discrete` calculation checks the same coefficients. The result is a unit test of the mathematical model, not experimental identification.

An input record should include sampling hardware clock, hold policy, actuator mapping, sensor filter, input/output data units, and evidence that the first-order approximation is applicable. Without those details, future context consumers may apply an algebraically correct equation in the wrong system.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [SCIPY-ZOH](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
