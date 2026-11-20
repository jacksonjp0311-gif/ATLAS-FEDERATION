# Control Atlas authored review questions (development, not hidden AI benchmark)

1. What is the difference between stability of a declared scalar recurrence and plant safety?
2. When is first-order exact ZOH equivalent to its continuous model?
3. Why does a zero-order hold assumption need an actuator specification?
4. What are two cases where a shorter sample interval can worsen controller operation?
5. How do controllability and observability differ, and what do rank tests assume?
6. Why is an absolute determinant tolerance sensitive to units and scaling?
7. When can a PI integrator wind up during saturation?
8. What is actually demonstrated by a clamp-versus-none IAE simulation?
9. Why is a low modeled tracking error not evidence of safety?
10. How can a Kalman filter be confidently biased?
11. What are Q and R in the scalar Kalman model, and how must they be obtained?
12. What does a finite-horizon scalar Riccati recursion optimize?
13. Why does clipping an unconstrained LQR action invalidate its optimality claim?
14. What does satisfying Nyquist for a stated bandlimited signal fail to prove?
15. What does a failed sufficient small-gain test imply?
16. What data are needed for a real plant identification study?
17. How would you verify an industrial loop without violating its safety constraints?
18. What source qualification must a context package retain?
19. Why are control-theory models not automatically safe agent orchestration rules?
20. What work remains deferred until all thirty domains are built?


## v0.2 extension material

# Control Atlas authored scientific checks (not a hidden or independent AI benchmark)

1. What are plant, sensor, actuator and disturbance in a stated physical control question?
2. How does exact first-order ZOH differ from explicit Euler under coarse sampling?
3. Why can nominal discrete pole stability fail to predict safe physical operation?
4. What exactly does full rank of a two-state controllability matrix establish?
5. Why does observability rank not guarantee accurate noisy state estimation?
6. How can PID integral windup arise during actuator saturation?
7. How does derivative-on-measurement differ from derivative-on-setpoint?
8. Why should signal frequency be stored separately from controller sample rate and discrete-time radians/sample?
9. What is aliasing for a 70Hz input sampled at 100Hz?
10. Why does perfect in-sample ARX fit not validate a physical plant?
11. Why can feedback cause bias in naive system identification?
12. What is the difference between scalar unconstrained LQR and MPC?
13. What does a Kalman variance mean when sensor bias is unmodeled?
14. How should a model report actuator constraints and time delay?
15. What evidence distinguishes residual anomaly from root-cause identification?
16. Which equipment safety interlocks remain independent of model software?
17. How do exact record revisions preserve scientific qualifications?
18. What evidence would be necessary before testing live control on a real machine?
19. When should the Atlas return an unresolved answer instead of a controller gain?
20. Why is routing/Bitwork development explicitly deferred in this project?


## v0.3.0 authored development questions (not held-out evaluation)

1. Why is a stable nominal pole insufficient for a controller with uncertain parameters?
2. When is evaluating the corners of a coefficient rectangle an exact robust criterion?
3. Why does a standard confidence interval not automatically establish a hard parameter bound?
4. How does one sample of feedback delay change the scalar characteristic equation?
5. Why does failing with P=I not prove a stable nonnormal matrix unstable?
6. Why is an eigentest based on floating-point numbers not formally verified proof?
7. Can |S|+|T| be assumed equal to one? What identity is correct?
8. Why does a single frequency value not yield gain margin or phase margin?
9. Why does lag-one autocorrelation alone fail to establish model residual whiteness?
10. What independent data are needed to validate a closed-loop plant model?
11. What does a stale sensor flag establish and what does it not establish?
12. Why must a safe fallback be defined by the actual plant rather than assumed to be zero?
13. Which empirical tests and standards would be required before deploying a control loop?
14. Why are content versions and safety acceptance separate axes?


## v0.4 adversarial control questions (visible development prompts, not independent held-out benchmarks)

1. Why does S+T=I at one algebraic frequency point not prove dynamic internal stability?
2. What does a small return-difference singular value mean and what can it not establish?
3. Prove the matrix convexity step behind fixed-P box-vertex sufficiency.
4. Give a stable discrete matrix for which P=I fails the Lyapunov decrease test.
5. What changes if parameter bounds are correlated instead of an independent box?
6. Why do finite-horizon Riccati gains require Q/Qf PSD and R>0?
7. Explain the difference between an unconstrained LQR optimum and a physically admissible action.
8. Why does failure to find a grid plan not prove continuous constrained infeasibility?
9. Which terminal set/robustness conditions are absent from this simple grid search?
10. Derive NIS=nu^T S^-1 nu and state the conditions needed for a chi-square interpretation.
11. Why can a normal-looking NIS coexist with a false sensor reading?
12. Show two state/bias hypotheses yielding identical scalar measurement.
13. What information must be collected before a fault can be isolated to one sensor?
14. Why is an ARX model's training RMS unrelated to free-running multi-step accuracy?
15. How can a feedback loop bias ordinary least-squares identification?
16. What must a sensor timestamp provenance record include to support online monitoring?
17. Which NIST SP 800-82 revision was final in November 2026, and what was still a draft?
18. Why is software numerical agreement not equivalent to real hardware-in-loop stability evidence?
19. What safe-state and interlock claims require independent operational approval?
20. When must a downstream agent abstain instead of suggesting a gain or device command?


## v0.5 developer-authored adversarial questions (not held-out)

1. Why is a nominal pole test weaker than a robust positively invariant set proof?
2. Derive the two-state row bound for bounded disturbances and exact linear feedback.
3. Why are 64 corners enough for independent 2×2 A/B intervals in this convex worst-case bound?
4. Which correlations of uncertainty would invalidate the independent parameter rectangle interpretation?
5. Give a model where the candidate state box passes but the actuator amplitude vetoes use.
6. Why does actuator slew-rate control require an augmented model?
7. Why is an output of zero not universally a physical safe shutdown?
8. Show how biased observations change the effective closed-loop state transition.
9. Why is a finite successful rollout not proof of universal invariance?
10. What experimental evidence justifies a future disturbance bound?
11. How should an AI distinguish mathematical model proof from empirical plant validation?
12. What remains unverified when a numerical oracle agrees at machine precision?
13. Which source supports bounded disturbance modeling, and what exact portion was checked?
14. Is Control v0.5 an accepted scientific v1 or a working content checkpoint?


## v0.6 adversarial questions (authored development review, not independent held-out test)

1. What difference between a requested input and applied actuator state appears after saturation, slew and lag?
2. Why does a deterministic observer error radius not follow from a Gaussian standard deviation alone?
3. Which exact input time index enters the plant and the Luenberger observer?
4. Derive e[k+1]=(a-L)e[k]+w[k]-L v[k] from the declared plant and observer.
5. Why does |a-L|<1 not imply zero observer error with bounded nonzero disturbances?
6. When does a finite-horizon reachable tube become an invariant set? (It does not automatically.)
7. How can interval dependence make a conservative finite tube fail to certify a physically viable controller?
8. Does a model-inconsistent measurement determine which component failed? Explain alternative causes.
9. How should an AI handle an unsupported sensor noise bound or missing actuator lag?
10. What tests would distinguish true plant model error from sensor timestamp drift?
11. Why is a physical interlock distinct from a constraint checked in an offline mathematical model?
12. Which external acceptance gates remain open before Control scoped v1, Bitwork routing and eventual desktop transfer?


## v1 adversarial review items (authored, not independently held out)

1. Why is an externally published experiment not automatically an experiment replayed by this Atlas?
2. What cannot be inferred from time/RPM records labeled with constant nominal PWM?
3. Why does fitting `b*u+c` fail when u is constant?
4. Why is a source Git blob hash not proof of a sensor's calibration?
5. What is the difference between REF and PWM in the OpenMCT log?
6. How should a GUI reconstruct times from DT_ms rather than impose nominal timing?
7. When does DMM_SAMPLE_ID duplication invalidate a naive current standard error?
8. How are one-step and free-run RMSE different, and why is random adjacent-row splitting questionable?
9. Under what conditions is `(A-LC)e+w-Lv` a valid observer error recurrence?
10. Why is `max_row_sum |A-LC|<1` only sufficient, not necessary, for model contraction?
11. Can an out-of-range sensor reading identify whether the sensor or model was wrong?
12. Which NIST OT edition is final as of November 2026, and what is still draft?
13. Which real experiments or documented bounds must be obtained before control v1 scientific acceptance?
14. What must remain deferred under the all-30-domains-first owner instruction?
