# 51. A credible bounded-feedback claim needs evidence for every envelope

Control proofs commonly begin with mathematical assumptions such as “process disturbance is bounded by W,” “measurement noise is bounded by V,” “actuator lag has response fraction alpha,” and “the plant dynamics are described by a,b.” These assumptions are not validated merely because the resulting inequality is true. The next verification layer must measure or justify the bounds, document drift and different operating modes, and establish what constitutes a failure to stay inside them.

## Minimum evidence packet

For the plant: identify the physical system, parameter sources, units, operating modes, sampling schedule, disturbance measurements, transient conditions, nonlinearities, hysteresis, and known delay. For the actuator: separate command, clamped target, measured applied position/force, magnitude limit, rate limit, dynamics, fault response and interlocks. For the sensor: physical quantity, calibration, drift, timestamp, freshness, quantization, noise and bias limits and missing data. For the estimator: update order, correct input-history representation, initial error distribution or set, observer gain, uncertainty propagation and mismatch monitoring. For constraints: distinguish process quality targets from physical protective limits and separate sampled constraints from intersample risks.

A statistical standard deviation does not provide a hard worst-case bound. Conversely, a worst-case interval does not assign a probability to its endpoints. If a source only gives 3σ under a Gaussian model, its finite bound status must remain unresolved: Gaussian tails are unbounded under the idealized model. Robust interval arithmetic may overapproximate reachability because state, estimate and past action are correlated. This is a conservative rejection hazard, not license to shrink the envelope without a valid derivation.

## Validation sequence

First check dimension and timing consistency. Then reproduce model calculations with a second numerical implementation and independent adversarial test cases. Check the smallest positive and largest allowed disturbances, gain changes, saturation and slew, initial state error, and measured-versus-predicted applied command. Compare estimator predictions against independent measurements. Test in a non-actuating replay/simulation environment and only under separately reviewed approval move toward bench validation. Safety-rated interlocks and failure recovery design are **not** provided by this Atlas.

The broader ATLAS FORGE sequence remains all thirty knowledge domains first, then the Bitwork/routing architecture, followed by integrated, independently authored retrieval/answer-quality studies and computer transfer. None of the mathematical models here establish that the routing system already works or improves AI performance.

**Sources:** MIT *Underactuated Robotics* state estimation and robust control notes; Mayne et al. 2006 output-feedback constrained-control abstract; NIST SP 800-82 Revision 3 final safety/security overview. This chapter is an authored evidence protocol, not a standards certification.
