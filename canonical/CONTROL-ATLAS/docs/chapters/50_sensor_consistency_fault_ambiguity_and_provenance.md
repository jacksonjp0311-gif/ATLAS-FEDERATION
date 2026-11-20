# 50. Sensor inconsistency is evidence of a model contradiction, not a component verdict

A measured signal is a sample of a physical process, filtered by a sensor, acquisition system, timestamp, calibration and communication path. An unexpected reading may arise from a faulty sensor, unmodeled plant dynamics, material/process changes, a stale timestamp, an actuator not following commands, a unit conversion error, or a disturbance larger than assumed. A monitoring system must distinguish a *detected inconsistency* from a *diagnosed cause*.

## Scalar bounded-consistency gate

If the estimated state is h with a documented absolute error bound E, and sensor noise has a documented absolute limit V, the expected measurement interval is `[h-E-V, h+E+V]` for `y=x+v`. A reading outside this interval demonstrates that at least one assumed relation or bound is inconsistent with the observation, ignoring rounding and model arithmetic. It does **not** tell us which assumption failed. This holds regardless of whether a sensor defect is a likely hypothesis; statistical diagnosis requires a different study design and often redundant measurements.

For example, with h=0.1, E=0.04 and V=0.02, y=0.13 is inside the declared interval `[0.04,0.16]`. A reading y=0.30 is outside and lies 0.14 model units above the upper bound. The appropriate output is a scoped contradiction plus a list of unresolved causes, not “replace the sensor.” A nominal Kalman filter innovation covariance uses a probabilistic noise model; it cannot automatically substitute for a hard maximum noise envelope. Overconfidence about either uncertainty type can make a controller's risk assessment invalid.

## Practical fault-inquiry procedure

Define the physical quantity and units, time alignment, sampling rate and sensor location before computing a residual. Check sample freshness, calibration revision, data-handling path and process conditions. Validate the actuator's applied state separately from requested command logs. If a discrepancy persists, collect independent measurements or controlled tests to distinguish sensor failure, actuation failure and plant disturbance. A disagreement can be reproduced synthetically under more than one mechanism, and a controller should not escalate to physical intervention solely because a model consistency test failed.

For industrial operational technology, NIST SP 800-82 Revision 3 (final, September 2023) addresses the distinct performance, safety and security needs of systems that interact with the physical world. NIST Revision 4 was only an initial public draft as of November 2026. The Atlas should not describe a draft as the current final standard.

**Source scope:** NIST final SP 800-82r3 https://csrc.nist.gov/pubs/sp/800/82/r3/final and Revision 4 initial public draft https://csrc.nist.gov/pubs/sp/800/82/r4/ipd ; MIT *Underactuated Robotics* estimation chapter https://underactuated.csail.mit.edu/ . Official publisher overview and sections, not a certified system audit. No network/PLC device access in this package.
