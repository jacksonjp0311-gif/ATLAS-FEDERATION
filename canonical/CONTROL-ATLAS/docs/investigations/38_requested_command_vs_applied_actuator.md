# Investigation 38 — The difference between an issued command and an actuator state

**Origin:** original actuator model, no hardware, motor or valve test. Suppose the controller requests input 10 in a generic unit. The actuator can accept magnitude at most 1, change by at most 0.2 per sample, and its modeled discrete response fraction is alpha=0.5. At the current sample the applied input equals zero.

The intended command is 10. The magnitude target becomes 1. The slew target becomes 0.2. The *applied next-sample input* becomes **0.1**. All four values are different. The plant consumes the *previous applied input* during this present step, not the new applied target unless the timing equation is changed. An LQR or PI regulator optimized under u=10 immediately applied would be predicting an entirely different plant.

If the slew limit is zero, the actuator state remains unchanged regardless of the requested command. If alpha equals one, the next applied state reaches the already limited target. These are arithmetic results of the assumed actuator model; they do not identify actual lag, friction, backlash, deadband or mechanical failure.

**Failure mode:** report that the controller “acted” merely because a command was logged. The relevant evidence is actual actuator position/force/flow with timestamp and uncertainty. Without it the control loop's input remains unverified. The final control record explicitly refuses physical actuation approval.

**Source:** Newton and Kroo, AIAA 2023 published abstract on actuator rate-limit effects; MIT/Åström feedback references. The specific scalar model and example are newly authored.
