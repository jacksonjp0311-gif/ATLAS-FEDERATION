# 12. Constrained control and model predictive planning

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

Model predictive control (MPC) repeatedly optimizes a finite-horizon control sequence under a model and constraints, applies the first action, and resolves as new state information becomes available. The mechanism is general but guarantees depend on objective, terminal conditions, model uncertainty, constraint feasibility, estimator accuracy and solver behavior. Merely simulating a model for several steps is not MPC; nor is a scalar LQR gain with clamping automatically an optimal constrained controller.

A realistic constrained plant has input limits, state constraints, rate constraints and sometimes mixed-integer operating modes. The optimization can become infeasible if no available actuation can satisfy all constraints, particularly with delayed or changed dynamics. A controller that silently returns any finite input after an infeasible problem may be unsafe. The correct behavior includes explicit feasibility status, fallback rules and independent enforcement of hard physical limits.

Our bounded LQR and PID demonstrations intentionally remain separate from an MPC implementation. They illustrate two key failure modes: an unconstrained optimal gain can request an impossible input; and a saturated integrator can accumulate error in ways that harm recovery. A future research implementation should not be adopted without measured model validity, solver timing budgets, infeasibility traces, adversarial disturbances and explicit shutdown policy.

Study questions: Can an MPC objective express an equipment safety requirement that is not modeled as a constraint? What happens if a late sensor packet arrives after the optimization horizon was formed? How should a controller distinguish an infeasible model from a temporarily unavailable sensor? These are design questions, not problems that adding more model parameters automatically solves.

**Publisher/documentation scope:** [MIT-LQR](https://underactuated.mit.edu/lqr.html) · [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems). These are exact source pointers and original summaries, not redistributed source text or new measurements.
