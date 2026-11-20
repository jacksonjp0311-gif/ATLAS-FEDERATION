# Investigation 02. A feedback pole moves, but actuator safety is unproven

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

The synthetic scalar discrete model has a=1.2 and b=0.5. With no state feedback, the pole has magnitude 1.2 and the ideal autonomous model is unstable. A gain K=1 in `u=-K*x` moves its pole to 0.7, nominally stable. The result says nothing about what happens if the actuator cannot deliver the requested input. If `|u|<=.1`, a large error cannot be corrected by unconstrained linear feedback as modeled. Declaring a safe system based solely on the pole test would change a mathematical label into a real-world claim it does not support.

A real acceptance test must use an identified plant with model uncertainty, actuator saturation, sensor delay, disturbance envelopes and appropriate hardware interlocks. The original synthetic numbers are deliberately chosen; the Atlas makes no claim that a particular motor, factory valve or temperature system has these parameters.

**Refusal:** no optimal gain or safety setting is authorized for an actual device. **Sources:** Åström–Murray, *Feedback Systems* and MIT's scalar LQR context.
