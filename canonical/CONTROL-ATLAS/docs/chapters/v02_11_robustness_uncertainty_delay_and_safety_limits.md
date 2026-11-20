# 11. Robustness, uncertainty, delay and safety limits

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Nominal stability is a mathematical fact about a particular model. Robust stability concerns whether the controlled system remains stable for a declared set of plausible model perturbations. Robust performance additionally concerns tracking and disturbance responses under those perturbations. Neither follows solely from the fact that a nominal state matrix has eigenvalues inside the unit circle. Real systems experience gain variation, nonlinear friction, temperature-dependent parameters, timing delay, actuator saturation and sensor drift.

A first-order model can fail when a time delay dominates response. Controller gains tuned against a zero-delay model may increase oscillation or produce overshoot after delay is introduced. Similarly, nominal state feedback may demand unlimited input even though the motor/valve/controller has finite range or rate. The mismatch is a change in the implemented closed loop, not a violation of linear mathematics. Robust controller design requires a stated uncertainty family and the correct physical constraints.

A stability margin report should include measurement and model frequency ranges, gain/phase conventions, identified delay, sample frequency, actuator limits, variability among operating conditions, sensor noise, and validation against held-out response data. A single Bode plot is not a guarantee: phase wraps, noise and unmodeled resonances can distort estimates. A controller with no explicit fallback or independent safety limit should not be promoted into equipment operation based on synthetic testing.

The current release does not compute generic H-infinity controllers, structured singular values, root-locus tuning, Nyquist encirclements, nonlinear Lyapunov proofs, safety certificates, or time-delay margins. Those are documented future references. It does compute basic nominal poles, two-state reachability and one scalar LQR gain. The output labels prevent downstream AI users from silently upgrading this into robust-system certification.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [MICH-PID](https://ctms.engin.umich.edu/CTMS/index.php?example=Introduction&section=ControlPID). These are exact source pointers and original summaries, not redistributed source text or new measurements.
