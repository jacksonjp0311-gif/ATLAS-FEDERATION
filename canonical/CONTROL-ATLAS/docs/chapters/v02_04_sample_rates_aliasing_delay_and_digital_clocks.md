# 04. Sample rates, aliasing, delay and digital clocks

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A digital control system records and acts at discrete times. The sample interval Δt and sample rate fs=1/Δt are not mere file metadata: they determine the discrete model, ability to observe changes and delay from sensing to actuation. If the sensor or controller clock slips, a model designed for uniform sampling may mis-estimate state or provide control too late. Sampling jitter, packet delays and asynchronous loops require their own verification.

For an ideal sinusoid of frequency f sampled exactly at rate fs, frequencies separated by multiples of fs can produce the same sample sequence, and a positive-frequency alias may be folded into `[0,fs/2]`. For instance a 70-Hz sinusoid sampled at 100 Hz has an alias magnitude of 30 Hz. The scalar `alias_frequency` function shows this arithmetic and explicitly refuses to identify the original physical frequency from samples. It does not undo aliasing or model finite-window spectral leakage, quantization, or nonuniform sampling. Proper anti-alias analog filtering is needed when the sampled input contains frequencies above the measurement bandwidth.

Time delay affects the phase relationship of plant and controller and can erode stability margins. A one-sample computational delay is not equivalent to no delay; a networked actuation path may have jitter and dropped commands. Increasing sampling frequency without sufficient CPU time, sensor bandwidth or anti-alias filtering can increase load without improving control quality.

**Practical test plan:** timestamp *both* command and measurement at acquisition and arrival; use calibrated clocks; record sample interval distribution and burst gaps; measure disturbance-bandwidth and sensor response; compare offline replay under real latency to assumed delay; monitor overruns and failover behavior. A frequency-domain margin estimate based on a nominal delay-free transfer function cannot be used for a controller with unmeasured network delay.

A source record should preserve units in hertz, seconds, sample index and radians/sample separately. Mixing these conventions is a serious, preventable error, especially when interpreting phase and frequency plots.

**Publisher/documentation scope:** [SCIPY-ZOH](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html) · [MATH-ALIAS](https://www.mathworks.com/help/daq/making-quality-measurements.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
