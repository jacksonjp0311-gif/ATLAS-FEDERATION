# Investigation 41 — Probabilistic noise and hard limits are different evidence classes

**Question:** A sensor datasheet reports a standard deviation of 0.01 units. Can we use that as `V=0.01` in a deterministic observer error certificate?

**Answer:** Not without a justified physical bound. If the model assumes Gaussian noise with standard deviation 0.01, samples can exceed any finite multiple of the standard deviation with nonzero probability. A 1σ envelope is not a strict maximum. The error recurrence `E_next=|a-L|E+W+|L|V` provides deterministic containment only when W and V are actual hard bounds (or conservative engineering bounds established by other evidence) and their time/order assumptions are true.

For a=0.8, L=0.6, W=0.02 and hard V=0.01 the calculated limiting radius is 0.0325. If V=0.01 is *only* a standard deviation, the same algebra may compute a number but a deterministic worst-case certificate is not justified. The proper output is an unvalidated model condition, and the system should request a qualified noise model and application-specific uncertainty statement. Intermittent sensor bias, saturation or stale measurements introduce separate faults not covered by the Gaussian/noise distinction.

The Atlas stores the difference between a confidence interval, a standard deviation and a hard uncertainty set, rather than compressing all three into one confidence badge. This complements Measurement Atlas, whose accepted method outputs carry their own degrees of freedom and assumptions.

**Source:** MIT *Underactuated Robotics*, State Estimation/Filtering coverage; original deterministic set-membership derivation. No sensor has been calibrated here.
