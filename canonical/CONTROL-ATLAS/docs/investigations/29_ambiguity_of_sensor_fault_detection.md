# Investigation 29 — Innovation covariance and identical sensor readings with different causes

A constructed two-sensor innovation vector ν=[2,0] has covariance S=[[4,1],[1,1]]. The normalized squared innovation νᵀS⁻¹ν is **4/3**. If the off-diagonal covariance were falsely treated as zero, the result would instead be 1. Covariance structure is not a decorative metadata field; it changes the calculation.

This statistic is not a fault-class label. A single measurement y=10 can arise from actual state x=10 with zero bias or x=8 with bias 2. Both are perfectly consistent with the same reported sensor value. The library explicitly returns `not_identified_by_this_measurement` rather than guessing whether a machine changed or a sensor drifted.

A proper diagnostic investigation would compare an independently calibrated sensor, inspect actuator and timestamp evidence, incorporate a physically justified state observer and excitation, and account for communication or adversarial data issues. NIST's OT integrity guidance treats anomaly monitoring and system assurance as additional engineering layers, not proof of a root cause.
