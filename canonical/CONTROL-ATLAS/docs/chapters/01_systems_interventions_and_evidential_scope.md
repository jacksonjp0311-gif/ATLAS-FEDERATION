# Chapter 01: Systems, interventions, and evidential scope

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

Control engineering starts by identifying a **plant** (system being influenced), measurable outputs, controllable actuators, goals, disturbances, sensor latency and hard safety limits. For example, a temperature loop requires a thermal mass, heater/fan limits, sensing locations and thermal coupling assumptions. A symbolic transfer function can describe a limited operating region but does not certify that those assumptions hold during operation.

A controller is a policy mapping measured state or tracking error to an action. In negative feedback, the controller uses error between setpoint and measured output to correct a disturbance. The loop may reduce sensitivity to some uncertainties, yet it can amplify high-frequency noise, excite unmodeled modes or destabilize if sign, gain or delays are wrong. A controller is not necessarily safe merely because its output approaches the requested setpoint in a simulation.

The Atlas documents models, hypotheses and design methods as source-linked records. It never drives physical equipment. Its public casebook is a set of authored synthetic tests; no PLC, factory machine, robot, device, agent or other live plant was operated. An AI may use these records as context but cannot treat retrieved text as executable instructions, and the deferred Bitwork routing system is separate.

**Evidence gate:** A real control recommendation needs identified dynamics or credible first-principles model, actual actuator/sensor constraints, testing across relevant operating states, disturbance and uncertainty analysis, interlocks, qualified review and a recorded change-control plan. Without those, the appropriate result is a model-level explanation or an unresolved decision.

## Bound reference topics

- **A feedback question requires plant, actuator, sensor, target and operating range** (`concept`): feedback-question
- **A simulated controlled plant is not a test of real equipment** (`concept`): model-vs-hardware
- **Controller success claims require explicit model and disturbance scope** (`concept`): controller-evidence
- **Control Atlas methods must not be mistaken for a live Atlas or Bitwork router** (`method`): non-routing-domain

## Source pointers

- [FBS-WIKI](https://fbswiki.org/)
- [FBS-PRESS](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems)

**Limit:** no new experiments or independent control review.
