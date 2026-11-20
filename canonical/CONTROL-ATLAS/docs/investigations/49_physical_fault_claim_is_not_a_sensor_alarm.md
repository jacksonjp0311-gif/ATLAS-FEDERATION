# Investigation 49 — The observer says “inconsistent”; the engineer must ask why

A two-state observer predicts a sensor value within componentwise intervals based on a declared state estimate and absolute noise bounds. A measured value outside that envelope is **evidence that at least one assumption was violated**. It does not isolate a sensor failure. The actual cause could be an actuator delivering a different input, timing drift, out-of-distribution process disturbance, changed plant dynamics, sensor bias or untrusted telemetry.

Run `two_sensor_consistency` with an expected state `[1,2]`, identity C, error radius `[.1,.1]`, measurement noise radius `[.1,.1]`, and sensor values `[10,2]`. The first channel is incompatible; the second may be compatible. The output sets `root_cause_identified=false`. The interface has no network or device-control side effects.

A proper field investigation would request independent calibrated sensors, actuator feedback, waveform history, network timing, firmware changes, environment and model confidence. It would preserve a contradiction without automatically correcting or overriding a real controller. NIST's final operational-technology guidance explicitly separates performance, reliability, and safety requirements. This Atlas is a research reference; it is neither a safety-rated controller nor a hardware fault classifier.
