# 03. Feedback, stability, poles and unmodeled disturbances

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

A discrete scalar linear system `x[k+1]=a x[k]+b u[k]` under feedback `u[k]=−K x[k]` has transition `a−bK`. With the autonomous scalar closed loop, its deviations converge toward zero if `|a−bK|<1`. This **nominal model** statement is distinct from disturbance rejection, robust stability, safe actuator behavior, or local nonlinear stability. The model can be inaccurate or have unmodeled delays, and a gain that stabilizes one operating point can destabilize another.

In a two-dimensional linear discrete system, spectral radius of A below one is the usual asymptotic eigenvalue stability condition. The implemented two-by-two eigenvalue tool computes both real and complex conjugate poles and labels this a nominal autonomous system test. It does not handle a general high-order system, parameter uncertainty or actuator saturation. Pole location and oscillatory response should be interpreted with the sampling interval and physical state scaling.

Disturbances enter through unknown pathways as well as declared inputs. Negative feedback can reduce sensitivity to some disturbances but amplify sensor noise in others; some performance and robustness tradeoffs are unavoidable. Commanding high gain is not automatically better. Track both output error and control effort, plus equipment limits, sensor variance, delay and failure modes.

**Counterexample:** a synthetic unstable open-loop scalar has a=1.2 and b=0.5. Gain K=1 gives a closed-loop pole 0.7, nominally stable. If the actuator saturates so that `u=−Kx` is not physically implemented, the pole test is no longer the actual closed-loop dynamics. Conversely, a stable plant can be made unstable by overly aggressive feedback. These counterexamples prevent blanket recommendations based solely on sign or magnitude of gain.

A stability claim about a physical machine requires linearization validity, relevant operating regions, measurement of dynamics, uncertainty, constraints, fail-safe independent protection, and a controlled test procedure. This library does not operate equipment or claim safe deployment.

**Publisher/documentation scope:** [ASTROM-2E](https://press.princeton.edu/books/hardcover/9780691193984/feedback-systems) · [PYCTR-DLQR](https://python-control.readthedocs.io/en/stable/generated/control.dlqr.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
