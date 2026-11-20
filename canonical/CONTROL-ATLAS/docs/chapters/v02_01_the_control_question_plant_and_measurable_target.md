# 01. The control question, plant, and measurable target

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A controller is only meaningful relative to a physical or simulated **plant**, a desired **output**, a control input that can actually be applied, and disturbances and limits that can occur. A question such as “make the valve stable” does not define a measurable acceptance condition. Specify which measured variable should remain near which reference trajectory, what disturbance matters, what time scale is relevant, and which actuator and sensor are available. A controller can regulate a controlled output successfully while damaging equipment or increasing energy consumption elsewhere.

Basic notation: `x` is internal state; `u` is the commanded input; `y` is the measured or modeled output; `r` is the reference; `d` is a disturbance. In linear state-space representation, a locally valid model may be written `dot(x)=A x+B u+E d`, `y=C x+D u`. The matrices describe a declared model in given state coordinates. The user should not infer `A`, `B` and `C` from the hardware's name or from a chart screenshot. Different parameterizations can describe the same input-output behavior but give different internal-state interpretations.

Control design is a contract on **time** and **measurement**. An actuator can saturate, exhibit backlash, introduce delay, or respond asymmetrically. A sensor can drift, saturate, quantize, filter, or have a latency longer than the intended loop period. An unknown time base can reverse cause and effect in telemetry. Without calibrated measurements, claims of “99% improvement” can be false even when simulation errors shrink.

Declare four types of evidence separately: analytical identities; simulated behavior under stated models; recorded signals from actual equipment; independently validated closed-loop outcomes. A stable eigenvalue is an analytical model fact, not real plant stability. A well-fitted regression may still omit crucial dynamics. An author-created simulation is not a field trial. The control engineer needs versioned control code, equipment configuration and a rollback plan before any physical implementation.

**Worked framing:** a hypothetical thermal chamber should regulate measured air temperature after a door opening, subject to heater power, chamber heat capacity, fan dynamics, sensor delay and overtemperature protection. A first-order plant can be a starting approximation, not permission to disable independent hardware interlocks. A Control Atlas result should name the missing physical variables before suggesting tuning.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [CTMS-METHODS](https://ctms.engin.umich.edu/CTMS/index.php?aux=Home). These are exact source pointers and original summaries, not redistributed source text or new measurements.
