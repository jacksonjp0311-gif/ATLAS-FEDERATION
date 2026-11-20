# Chapter 05: State-space reachability and observation

**Evidence status:** authored educational explanation linked to selected source pages, not independent science/hardware validation.

For a linear time-invariant state-space system, `x[k+1]=A x[k]+B u[k]`, `y[k]=C x[k]`, controllability asks whether permitted inputs can transfer the modeled state, and observability asks whether modeled internal states can be reconstructed from output history under assumptions. The general algebraic tests involve the controllability matrix `[B, AB, ..., A^(n−1)B]` and observability matrix stacking `[C; CA; ...; CA^(n−1)]`.

The v0.1 calculator specializes to exactly **two states, one input and one output**. It reports determinants of `[B,AB]` and `[C;CA]`, and compares absolute determinants against a caller-provided numeric threshold. A nonzero determinant is a mathematical full-rank condition in exact arithmetic. Near-singular matrices are numerically delicate, and absolute determinant tolerance changes under state scaling: this tool is a teaching calculation, not a condition-number-aware diagnostic for a calibrated system.

**Failure example:** measure only one output of a two-state system with an unstable hidden state; satisfactory output tracking does not prove all states remain bounded. Similarly, a controller cannot stabilize an uncontrollable unstable mode by wishing for a higher gain. Before trusting an observer, identify sensor geometry, units, noise and actual process dynamics. A model chosen by an agent is not validated merely by matching a short input/output trace.

Code records must remain paired with rank assumptions and explicit state-space units. The generic Forge retrieval layer should return those qualifications to an AI, not only the single boolean `controllable`.

## Bound reference topics

- **Controllability depends on A and B, not an attractive controller name** (`equation`): controllability
- **Observability depends on A and C, not merely repeated sensor readings** (`equation`): observability
- **Numerical rank thresholds depend on scaling and matrix conditioning** (`concept`): rank-tolerance
- **A visible output can hide unobservable internal instability** (`concept`): unobserved-modes

## Source pointers

- [PY-CTRB](https://python-control.readthedocs.io/en/latest/generated/control.ctrb.html)
- [PY-OBSV](https://python-control.readthedocs.io/en/latest/generated/control.obsv.html)
- [FBS-WIKI](https://fbswiki.org/)

**Limit:** no new experiments or independent control review.
