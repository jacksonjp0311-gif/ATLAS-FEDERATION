# Chapter 42: Adaptive nonlinear ODE integration and local error estimation

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `y′=f(t,y); e≈|y_(h/2,h/2)−y_h|/15 for an RK4 pair under smoothness and asymptotic assumptions.`

**Reference algorithm:** `math_physics_atlas.v02_models.nonlinear_rk4_adaptive(rhs, t0, y0, t1)`

**Units:** t in seconds, y in problem-specific units, f in y units per second; absolute error tolerance in y units.

## From physical laws to trajectories
A state equation y′=f(t,y) plus an initial condition defines an initial-value problem under the usual regularity conditions. The fourth-order Runge–Kutta method computes four slopes: k₁=f(t,y), k₂=f(t+h/2,y+hk₁/2), k₃=f(t+h/2,y+hk₂/2), k₄=f(t+h,y+hk₃). Their weighted sum gives y_{n+1}=y_n+h(k₁+2k₂+2k₃+k₄)/6. Fixed h is often wasteful in smooth regions and inaccurate near rapid changes. Adaptive integration estimates how a shorter step changes the answer.

## Richardson step doubling
Assume a smooth nonstiff solution and the RK4 local truncation error behaves like C h⁵. One full step has leading error C h⁵. Two consecutive half steps accumulate approximately C h⁵/16. Thus the difference between the two estimates is approximately 15C h⁵/16. Dividing by 15 estimates the fine path error. Adding (y_fine−y_full)/15 is a fifth-order Richardson correction in the asymptotic regime. Choose the next h in proportion to (tolerance/error)^(1/5), bounded between conservative shrinking and growth factors. Every step checks that time advances and the derivative remains finite. Both the initial state and absolute tolerances have physical units.

## Worked logistic example
With growth rate 1 s⁻¹, y′=y(1−y) and y(0)=0.1, separation of variables yields log(y/(1−y))=t−log 9, so y(t)=1/(1+9e^(−t)). At t=2 s the solution is approximately 0.45085306. Generate a finite numerical trace at several tolerances and compare to the analytic formula. A separate oracle checks 120 seeded initial conditions and horizons. Do not label this an observed biological growth curve; it is a constructed differential equation with stipulated parameters.

## Negative experiments and limits
For y′=−1000y, the explicit RK4 stability region places restrictions on h even if a step starts with small apparent state variation. An adaptive local-error controller is not a trustworthy stiff integrator; seek an implicit method with a stability analysis. Discontinuous right-hand sides, impulses, unknown initial states and event-triggered changes require separate modeling. When a budget is exhausted, raise an error; silently returning a partial trajectory would falsely report a completed simulation.

## Technology continuity link
This small solver supports offline models of thermal response, chemical kinetics, population systems and controller dynamics. Document the RHS, tolerances, units, step acceptance and exact comparison case so future users can reproduce the numerical process.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Step-doubling local tolerance is not a proof of global error or stiff-system stability. Refuses invalid initial/time domains and step-budget exhaustion.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
