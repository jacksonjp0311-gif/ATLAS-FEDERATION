# 08. System identification: excitation, bias and validation

*Original bounded scientific reference | Assistant-checked source scope | Independent human review: not performed.*

System identification estimates dynamics from observed inputs and outputs. A fitted model is not simply a regression on any available log: experiment design, signal excitation, time alignment, missingness, feedback, nuisance disturbances, noise and model structure determine what is identifiable. MathWorks' workflow explicitly separates data assessment, model selection, model fitting and validation; it advises checking excitation and comparing different structures rather than declaring the best training fit correct.

The Atlas implements a narrow scalar no-intercept model `x[k+1]=a*x[k]+b*u[k]` with the state x known directly and an input u at the correct time. It solves an ordinary least-squares two-parameter normal equation and rejects a singular or poorly excited input/history design. It returns residual sum of squares and parameter estimates, **not** confidence intervals, an identified physical plant, or independent held-out validation. A perfect in-sample RSS can occur in a synthetic noise-free model that shares none of the real system's nonlinearities.

**Excitation counterexample:** with constant state history and input always zero, the data cannot separate a from b; a numerical solver could return arbitrary plausible values. This Atlas refuses. Another failure occurs if a feedback controller automatically responds to unmeasured disturbances; the input may correlate with disturbances, biasing simple least squares. Adding more of the same confounded data does not necessarily fix the model.

A realistic identification protocol begins with a timestamped experimental plan: input ranges and safe excitation, sensor clock accuracy, preparation state, held-out validation windows that cover relevant operating conditions, model selection criteria, residual tests, uncertainty and rollback of incorrect models. Distinguish data used to fit a model from data used to test it. If out-of-sample performance is not available, report the estimate as an in-sample teaching fit only.

System identification is not causal inference by default: model fitting can describe signal dynamics without proving an intervention's effect or mechanism. Causal Atlas should be consulted when changes in operations or treatment assignments are the scientific question.

**Publisher/documentation scope:** [MATH-ID](https://www.mathworks.com/help/ident/gs/system-identification-workflow.html) · [MATH-ID-QUALITY](https://www.mathworks.com/help/ident/gs/about-system-identification.html). These are exact source pointers and original summaries, not redistributed source text or new measurements.
