# Investigation 12. Designing the next experiment rather than inventing a controller

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

A new industrial process has a variable error and unknown plant dynamics. Which method should an investigator use? The research sequence is: (1) define target and hazard constraints; (2) inspect sensor/actuator bandwidth, time and units; (3) collect input/output data with safe excitation; (4) choose candidate model classes and compare held-out prediction; (5) test controllability and observability; (6) select a control strategy considering constraints and uncertainty; (7) validate with disturbances under independent protection; (8) record failures, rollback capability and model revisions.

If no plant data exist, there is no honest unique tuning answer. A first-order demonstration and scalar LQR can teach equations, but they cannot substitute for physical identification, robust control or a qualified commissioning plan. A larger model does not repair missing sensor paths, and a higher test count does not prove a field system safe.

**Sources:** System Identification Workflow (MathWorks R2026b), Caltech Feedback Systems (Åström–Murray) and Michigan Control tutorials. **Outcome:** research protocol and scoped abstention, no field implementation.
