# Investigation 39 — A safe-looking sampled tube does not prove safe operation

**Origin:** authored 12-step interval simulation and overapproximate bound. Model `x[k+1]=0.6 x[k]+0.2 u_applied[k]+w[k]`, controller `requested=-0.4 h[k]`, observer gain L=0.55, initial estimate h[0]=0.1 and error radius 0.05. Disturbances satisfy |w|<=0.01 and |v|<=0.01 by stipulation. The actuator magnitude limit is 0.4, slew limit 0.1 per sample, lag alpha=0.6, with initial applied input zero. The state limit is |x|<=1.

The interval tube propagates physical state, observer state and actuator separately, rather than substituting h for x. Over the twelve sampled steps, all returned physical intervals lie inside the model's state bound. This does **not** make the tube invariant beyond twelve steps, show what happens between samples, prove that actual w and v satisfy the stipulated limits, or establish a physical hardware safety function. The model omits parametric variation, state-dependent sensor degradation and unmodeled dynamics.

Under a deliberately tightened state limit of 0.04, the returned interval fails containment; the correct status is insufficient mathematical evidence under that model, **not** a demonstration of physical equipment failure. When actuator response fraction is changed from 0.6 to 0.01, the state tube changes. Ignoring this actuator dynamic can invalidate predicted behavior.

Independent NumPy-generated trajectories drawn inside the stipulated bounds remain inside the conservative computed intervals for the tested seeds; this is an implementation regression test, not a proof of real-world validity. The interval hull loses correlations between physical state and estimate, so it can reject some systems that would actually satisfy tighter constraints. That conservatism must be reported without silently changing the envelope.

**Sources:** Mayne et al. 2006, robust output feedback with invariant tubes; MIT underactuated notes on reachable sets and robust MPC. The local method is a finite scalar interval calculation, not an implementation of their complete robust MPC algorithms.
