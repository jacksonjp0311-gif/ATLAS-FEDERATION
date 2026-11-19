# Manufacturing Atlas — Reconstructible knowledge manual v0.1.0

**Canonical ATLAS FORGE federation node; never a parallel project.**

The following chapters are original reference explanations and bounded mathematical models. They are not certified process specifications, a machine safety manual, an authenticated archive of technical standards, or evidence that actual semiconductor chips or computers were fabricated.

# Chapter 01 — From product requirements to datums, inspection plans, and acceptance

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Manufacturing starts with an unambiguous functional requirement. Identify the measurand, coordinate frame, feature, datum precedence, surface condition, allowable range, operating temperature, and acceptance decision rule. Separate a nominal dimension from the allowable interval. A datum is a reference construction, not simply any convenient observed surface. A single distance measurement cannot establish coaxiality, perpendicularity, or form. Every manufacturing operation must leave inspectable evidence of what it produced, what was measured, and what remains unproven.

## Reconstructible law, dimensional contract and assumptions

`Specification → measurable characteristic → calibrated comparison → documented decision`

Inputs/outputs: **categorical / mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For a mating shaft and hole, the feature size and reference temperature must both be declared before a clearance decision can be made. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A design calling only for “high precision” or “standard fit” does not specify reproducible tolerances. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Metrology programme and measurement practice**, https://www.nist.gov/metrology. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 02 — SI length and temperature traceability in precision production

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A reported length is conditional on a measurement system and temperature. In a homogeneous first-order material model, length increases proportionally to the temperature difference and the coefficient of thermal expansion. Derive the approximation by integrating dL/L=α dT for approximately constant α, then truncating exp(αΔT) after its first term. Record instrument calibration, uncertainty, reference environment, repeatability, resolution, operator and date. Traceability attaches to a measurement result through a documented chain; it does not magically attach to a machine merely because its instrument has a calibration label.

## Reconstructible law, dimensional contract and assumptions

`L(T) ≈ L(T_ref)[1+α(T−T_ref)]`

Inputs/outputs: **m, K, K^-1**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

One metre of material with α=12×10^-6 K^-1 changes by approximately 0.24 mm over 20 K under the linear approximation. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Unknown coefficient α, gradients or residual stress can dominate the simple calculation; a predicted growth is not a measured correction. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST metrological traceability frequently asked questions**, https://www.nist.gov/metrology/metrological-traceability. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 03 — Tolerance intervals, clearance/interference, and interchangeable fits

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A manufactured dimension is not a point; it is an admissible interval. The extremal clearance for a hole and shaft comes from the smallest hole paired with the largest shaft, and the largest hole paired with the smallest shaft. Positive C_min guarantees clearance within declared bounds. Negative C_max guarantees interference. A range spanning zero is a transition fit or boundary. Tolerance choice is functional and must consider thermal behavior, roughness, measurement uncertainty, and actual geometric form. This interval reasoning is independent of probabilistic distribution assumptions.

## Reconstructible law, dimensional contract and assumptions

`C_min=H_min−S_max; C_max=H_max−S_min`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Hole [10.02,10.05] mm and shaft [9.97,9.99] mm imply guaranteed [0.03,0.08] mm diametral clearance. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A Monte Carlo estimate cannot replace a worst-case bound unless its probabilistic assumptions and risk target are explicitly accepted. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 04 — Dimensional stack-ups, worst case and correlated uncertainty

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

For features that add algebraically in a dimension loop, each signed interval contributes lower and upper bounds. The worst-case assembled interval is the interval sum, assuming every component can attain its bound jointly. Statistical propagation is different: for a sum of random errors, variance includes covariances between components; the root-sum-square expression is valid only when the off-diagonal covariances are zero. A short assembly measurement cannot identify the true correlation structure among batches, tools, fixture locations, or environmental cycles.

## Reconstructible law, dimensional contract and assumptions

`[Σa_i, Σb_i]; u_sum^2=Σ_iΣ_j Cov(X_i,X_j)`

Inputs/outputs: **mm, mm²**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For intervals [1,3], [-2,-1], [4,5], the net admissible stack is [3,7]. For σ=3 and 4 with zero covariance, σ_total=5. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Treating all correlated thermal growth terms as independent can understate uncertainty and yield an unjustified acceptance decision. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **Doiron and Stoup, uncertainty and dimensional calibrations**, https://www.nist.gov/publications/uncertainty-and-dimensional-calibrations. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 05 — Calibration models, bias, repeatability and residual uncertainty

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A linear calibration line is a regression model, not a certificate. Derive b=Σ(x−x̄)(y−ȳ)/Σ(x−x̄)² and a=ȳ−b x̄. Evaluate residual variation with sample count n−2 and inspect residual versus input. Calibration does not necessarily improve the sensor until a correction is applied and verified. Nonlinear drift, hysteresis, misalignment, thermal dependence, and reference uncertainty are additional error mechanisms not represented in ordinary least squares. A calibration chain may carry uncertainty even when fitted residuals vanish.

## Reconstructible law, dimensional contract and assumptions

`y_indicated=a+b x_reference+ε`

Inputs/outputs: **indication / reference units**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Reference values 0,1,2,3 and indications 1,3,5,7 fit b=2, a=1 with zero constructed residual. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Perfect fitted points do not prove an instrument is traceable or accurate away from the calibration range. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST metrological traceability frequently asked questions**, https://www.nist.gov/metrology/metrological-traceability. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 06 — Machine coordinates, spindle kinematics and feed conversion

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Uniform tangential speed defines the spindle relation v_c=πDn after consistent unit conversion. For z cutting edges and feed per tooth f_z, the nominal programmed linear feed is n z f_z. The relation assumes steady rotation and full engagement; it does not identify an experimentally safe feed, tooth breakage threshold, vibration limit, or heat load. Coordinate systems include machine coordinates, work offsets and tool offsets. Any transform must identify origin, handedness, axis direction and units; silent frame changes create systematic dimension errors.

## Reconstructible law, dimensional contract and assumptions

`n[rpm]=1000 v_c[m/min]/(πD[mm]); v_f=n z f_z`

Inputs/outputs: **rpm, mm/min**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

D=10 mm, v_c=100 m/min, z=4, f_z=0.05 mm produces n≈3183 rpm and feed≈637 mm/min in the ideal formula. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Using mm as metres creates a 1000× speed error. Encoder counts do not guarantee actual cutting-edge position under tool deflection. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 07 — Material-removal rate, specific cutting energy and power accounting

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

For a rectangular approximation of engaged material, removing a slice of axial depth a_p and radial width a_e across feed distance v_f per minute yields Q=v_f a_p a_e. The ideal specific-cutting-force approximation converts k_c in N/mm² and Q in mm³/min into watts by dividing by 60,000. Input motor electrical power must exceed cutting power when efficiency is below unity, and other losses contribute. Specific force depends on material, tool geometry, chip thickness and wear. This is an accounting model, not measured cutting conditions.

## Reconstructible law, dimensional contract and assumptions

`Q=v_f a_p a_e; P_cut=k_c Q/60000`

Inputs/outputs: **mm³/min, W**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With a 6,366 mm³/min rate and k_c=1,500 N/mm², the ideal power estimate is about 159 W before drive and auxiliary losses. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A single k_c constant cannot predict chatter, tool fracture, burrs, heat damage, machine bearing loads or unsafe conditions. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 08 — Structural stiffness, elastic compliance and geometric error

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

The Euler–Bernoulli small-deflection cantilever formula comes from integrating the beam bending equation EI wʺ(x)=M(x), with moment varying linearly from applied end load to the fixed support, and enforcing zero displacement and slope at the clamp. Tool holders, machine frames and fixtures deform under load; a nominal coordinate command therefore differs from the realized workpiece geometry. This simplest beam model assumes linear elasticity, a clamped end, no shear deformation, no joint play and constant section. Machine thermal drift and spindle runout are separate contributors.

## Reconstructible law, dimensional contract and assumptions

`δ=F L³/(3EI) for slender linear-elastic cantilever`

Inputs/outputs: **N, m, Pa, m⁴**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

A 10 N load on a 1 m beam with E=200 GPa and I=10^-8 m⁴ gives about 1.67 mm tip deflection. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

The model is unreliable for short thick beams, large deflections, loose fixtures or material failure; its output is not a machine acceptance threshold. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 09 — Lead screws, step resolution, backlash and positioning uncertainty

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

An ideal screw translates one pitch p for each turn. Dividing that rotation into N command steps gives a nominal increment p/N. Backlash is path-dependent deadband: after direction reversal the mechanism may not move until play is taken up. Without state and calibration, a symmetric interval around the ideal command is a conservative representation, not a predicted actual position. Encoder position on the motor side may not capture tool-end motion or structural compliance. Validation requires an external position reference, reversal tests and temperature control.

## Reconstructible law, dimensional contract and assumptions

`Δx=p/N_steps; x∈[x_cmd−b−Δx/2,x_cmd+b+Δx/2]`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Ten commanded turns at 1 mm/turn with 0.02 mm backlash and 200 steps/turn yield an ideal 10 mm and a conservative reachability band of ±0.0225 mm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A 0.005 mm microstep is not proof of ±0.005 mm absolute positioning accuracy. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 10 — Control charts, capability indices and nonstationarity

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A stable process in a defined state can be characterized by the population-like distribution of an inspection characteristic. Three-sigma control limits are used to signal potential special causes, not to assert that all products are conforming. Cp compares specification width with six estimated process standard deviations; Cpk penalizes a displaced mean. These indices have meaning only given process stability, measurement-system adequacy, a justified distribution model and representative data. Treat unstable or distribution-unassessed inputs as unqualified, not as bad-looking capability numbers.

## Reconstructible law, dimensional contract and assumptions

`Cp=(USL−LSL)/(6σ); Cpk=min(USL−μ, μ−LSL)/(3σ)`

Inputs/outputs: **dimensionless**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With limits 9 and 11, mean 10, σ=0.2, both Cp and Cpk equal about 1.667 conditional on documented assumptions. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A high Cpk from six handpicked measurements is not evidence of production capability or acceptable safety risk. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Metrology programme and measurement practice**, https://www.nist.gov/metrology. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 11 — Uncertainty-aware inspection, guard bands and explicit non-decisions

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

An acceptance decision combines an indicated value with an uncertainty expansion U and a chosen decision rule. A conservative guard-band decision accepts when the full declared expanded interval lies inside specification, rejects when it lies entirely outside, and otherwise returns indeterminate. The probability of false acceptance is not computed by this rule; it depends on the probabilistic model, prior and coverage basis of U. Record the reference standard, test temperature, calibration chain and feature definition alongside the measurement. Uncertainty does not excuse ignoring systematic error.

## Reconstructible law, dimensional contract and assumptions

`accept if [y−U,y+U] ⊆ [LSL,USL]`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For y=10.9, limits [9,11], U=0.2, the correct conservative decision is indeterminate. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

Measuring 10.99 with a ±0.2 declared interval cannot justify unconditional acceptance solely because 10.99 is below 11. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **Doiron and Stoup, uncertainty and dimensional calibrations**, https://www.nist.gov/publications/uncertainty-and-dimensional-calibrations. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 12 — Process plans, dependency DAGs, checkpoints and rework

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A part can be represented by a directed acyclic graph of operations. Each operation consumes a defined material state and produces a revised state plus evidence, e.g., datum established, surface measured, heat treatment completed. A topological order exists only without cycles. The longest dependency chain gives a lower bound on completion time if unlimited parallel resources are available. Real machines and workers create resource contention, queues, setups, rework and maintenance, so an unconstrained critical path is not a production schedule. Keep the process route reproducible and version controlled.

## Reconstructible law, dimensional contract and assumptions

`finish(v)=duration(v)+max_(u predecessor v) finish(u)`

Inputs/outputs: **min**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

If preparation takes 3 min, dependent machining takes 5 min, independent measurement 7 min, and joining takes 2 min after both, earliest completion is 10 min assuming no shared resource. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A shortest theoretical lead time ignores equipment capacity, logistics, inspection rejection and process yield. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Additive Manufacturing Data Integration and Recommended Practice**, https://www.nist.gov/publications/additive-manufacturing-data-integration-and-recommended-practice. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 13 — Casting/forming geometry, shrinkage, constraints and material evidence

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

An ideal isotropic linear shrinkage fraction s maps a reference pattern dimension into an expected cooled dimension. Real casting solidification, feed systems, thermal gradients and phase changes produce nonuniform deformation and defects. Forming processes additionally involve work hardening, friction, anisotropy, elastic springback and local instability. Reconstructibility requires distinction between a geometry estimate and the actual process qualification. Store the material state, thermal path, measured coupon results, and limits before using a shrinkage factor for an engineering decision.

## Reconstructible law, dimensional contract and assumptions

`L_finished≈L_pattern(1−s)`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

Under an assumed uniform 2% linear shrinkage, a 100 mm pattern yields a predicted 98 mm dimension. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A shrinkage estimate cannot substitute for a validated pattern allowance, casting inspection or material fatigue testing. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 14 — Additive layers, geometric error accumulation and qualification

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

In the simplest layered fabrication model, nominal height equals the number of deposited layers multiplied by nominal layer thickness, with a bounded systematic scale error. This geometric relation does not predict melt-pool dynamics, residual stress, porosity, anisotropy, surface finish or material strength. Additive process qualification requires characterized feedstock, machine state, in-process sensor quality, postprocessing and destructive or nondestructive evaluation as appropriate. Measure dimension and material quality separately. Machine setpoints cannot be transferred uncritically across systems.

## Reconstructible law, dimensional contract and assumptions

`H=N_layers h(1+ε_scale)`

Inputs/outputs: **mm**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For 100 layers of 0.2 mm each and a 1% hypothetical scale error, expected height is 20.2 mm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

The layer-height calculation cannot certify load-bearing performance or quality of a laser-melted part. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Measurement Science for Additive Manufacturing Program**, https://www.nist.gov/programs-projects/measurement-science-additive-manufacturing-program. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 15 — Surface texture, sampling limits, contact function and roughness

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Surface texture influences contact, friction, lubrication, leakage and electrical interconnect behavior. A discrete absolute-deviation calculation summarizes a profile sample relative to a fitted mean. It is not a complete realization of an official surface-roughness standard: filtering, evaluation length, probe radius, sampling spacing, directionality and spatial form all matter. Flatness and roughness are different measurements. Use explicitly stated bandwidth and instrument condition before comparing reported Ra values. Reconstruction requires both an algorithm and an independent measurement method.

## Reconstructible law, dimensional contract and assumptions

`R_a,discrete=(1/N)Σ|z_i−z̄|`

Inputs/outputs: **m**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

For samples [0,+1 µm,−1 µm], the simple mean-removed average absolute height is 2/3 µm. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A low Ra does not establish surface flatness, low fatigue crack risk, electrical cleanliness or seal compatibility. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST dimensional measurement services**, https://www.nist.gov/programs-projects/dimensional-measurement-services. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 16 — Heat balances in machines, toolrooms and thermal processes

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A lumped thermal capacity C linked to ambient through thermal resistance R and heated by constant P obeys C dT/dt=P−(T−T_ambient)/R. Solve this linear ODE to obtain the exponential response with τ=RC and equilibrium T_∞=T_ambient+PR. Thermal state changes machine dimensions, material stiffness, electronics and measurement. The model is appropriate only when internal temperature gradients are negligible relative to the boundary resistance. Store energy balances, sensor uncertainty and environmental history.

## Reconstructible law, dimensional contract and assumptions

`T(t)=T_∞+[T(0)−T_∞] exp[−t/(RC)]`

Inputs/outputs: **K, W, J/K**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

With T(0)=310 K, ambient 300 K, P=5 W, R=2 K/W and C=10 J/K, T is already at 310 K and remains constant. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A lumped response cannot predict tool-tip gradients, thermal deformation, flash temperatures or chemical thermal processes. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Metrology programme and measurement practice**, https://www.nist.gov/metrology. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 17 — Manufacturing dependencies for semiconductor devices and precision instruments

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

Semiconductor fabrication depends on material purification, crystal structure and wafer geometry, surface cleaning, thin-film control, selective pattern transfer, doping control, contact metallurgy, contamination management and electrical process monitoring. These are coupled manufacturing and metrology problems, not simply electronic circuit equations. Optical overlay and layer thickness can require uncertainty budgets far below the scale of common mechanical processes. Preserve physics and chemistry derivations, process-state transitions and qualified original references, but do not pretend a tutorial contains enough information to produce verified integrated circuits.

## Reconstructible law, dimensional contract and assumptions

`Process evidence = material state + tool state + environment + metrology + traceable data`

Inputs/outputs: **qualitative**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

A layer-thickness measurement is only meaningful alongside reference material, spot sampling, temperature, calibration, model and stated uncertainty. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A successful transistor simulation does not validate cleanroom lithography, chemistry, yield, safe chemical handling or fabricated logic timing. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST Accuracy and Traceability in Dimensional Measurements (microlithography)**, https://www.nist.gov/publications/accuracy-and-traceability-dimensional-measurements. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# Chapter 18 — Manufacturing a reconstructible computer: dependency closure and verification

**ATLAS FORGE / Manufacturing / exact content edition 0.1.0**  
**Scientific role:** original reconstructible derivation and bounded reference calculation  
**Evidence maturity:** authored explanation and finite constructed tests; no certified machine, authenticated original publisher file or external peer review.

## Why this knowledge must survive

A computable engineering design becomes reconstructible when each transformation has evidence of dimensional conformity, material state, connection identity, power, timing and failure handling. A computer-architecture module can specify arithmetic and state transitions, but it also needs a material and manufacturing route for connectors, conductors, insulating layers, switches, enclosures and test instruments. Manufacturing supplies repeatable interfaces and acceptance tests, not just a process list. Link exact Atlas record revisions for units, materials, semiconductors, electrical power, timing and algorithms. Only physical trials can demonstrate that an actual processor and instrument function.

## Reconstructible law, dimensional contract and assumptions

`materials → metrology → tool → part → assembly → circuit → processor → software`

Inputs/outputs: **qualitative**. The symbolic statement is meaningful only with its declared coordinate frame, sign convention, reference conditions and assumptions. Preserve full-precision inputs in machine-readable files; avoid silently mixing millimetres and metres. Store a model revision separately from a measured experimental datum. A machine can execute a reference equation perfectly while the modeled process fails to correspond to the physical system.

## Worked constructed investigation

A testable tool-chain packet lists drawing, bill of materials, tolerances, fixtures, calibration chain, process route, test vector, environmental bounds and unresolved supply dependencies. The reference computation is reproduced by the standard-library package `manufacturing_atlas.models`; applicable functions are exercised by `tests/test_models.py` and the versioned casebook. Numerical evidence supports the finite arithmetic under the declared assumptions, rather than any empirical performance claim.

## Counterexample and limits

A CAD model, simulator, or executable reference algorithm alone is not a demonstrated hardware reconstruction. For acceptance, record what could falsify the conclusion, which measurements would test it, how uncertainty enters, and which operating regimes are excluded. Retain negative outcomes instead of silently adjusting the model to fit them.

## Experimental verification and restoration contract

A future laboratory should: (a) establish instrument identity and traceable reference with uncertainty; (b) acquire repeated observations at declared temperature and environmental state; (c) compare observed quantities against the predicted result with an independent calculation; (d) perform perturbation and reversal checks; (e) preserve raw logs, calibration IDs, data rights, date, and computed checksums. **None of those laboratory measurements have been conducted by this Atlas chapter.**

## Source and rights

Bibliographic orientation: **NIST manufacturing research and reference programmes**, https://www.nist.gov/manufacturing. This original summary does not reproduce publisher text or authenticate downloadable source bytes. Any normative industrial standard requires its own licensed copy and edition control.

## Cross-domain relevance

This chapter supplies mathematical and measurement prerequisites for reconstructing mechanical tools, production processes, semiconductors, electrical interfaces, and computing systems. Its knowledge record is linked by exact immutable revision in the shared ATLAS FORGE federation.


---

# New Manufacturing v0.2.0 original chapters 19–30

# Chapter 19: Why covariance must be positive semidefinite

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`u_y² = aᵀ Σ a, and Σ must be symmetric PSD`

## Scientific derivation and engineering reasoning

An uncertainty budget is not just a set of individual standard deviations and pairwise correlations. Every physically possible covariance matrix must be symmetric positive semidefinite (PSD): for every real vector a, aᵀΣa≥0. If this condition fails, the matrix assigns a negative variance to some linear combination of measurands and cannot represent a valid multivariate uncertainty model. Checking each |Cov(i,j)|≤σiσj is necessary but not sufficient for three or more correlated quantities.

A bounded symmetric Jacobi eigenvalue method can evaluate the small matrices encountered in educational tolerance stackups. Validate finite entries, symmetry and a scale-aware nonnegative eigenvalue condition; then propagate uncertainty with the quadratic form. Because real metrology can be extremely ill-conditioned, distinguish solver tolerance from physical measurement uncertainty. A numerical eigenvalue tolerance must not be misrepresented as proof that the source covariance estimates were calibrated.

Constructed counterexample: Σ=[[1,.9,.9],[.9,1,−.9],[.9,−.9,1]] has admissible pairwise magnitudes yet a negative eigenvalue and must be rejected. Valid test: two standard deviations 3 and 4 with zero covariance give u=5. With covariance +0.5 between two unit-standard-deviation contributors, the uncertainty of their sum is √3. Correlations should be inferred from appropriate paired observations, not chosen to make a tolerance stackup pass.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.covariance_budget_psd`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Measurement covariance must be estimated from real calibration/control data, currently absent.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 20: Inspection guard bands and conditional false acceptance

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`P(accept | actual x)=Φ((USL−g−x)/σ)−Φ((LSL+g−x)/σ)`

## Scientific derivation and engineering reasoning

A tolerance limit is a condition on the actual measurand; a measuring instrument returns an uncertain observation. If accepting every reading inside [LSL,USL] creates unacceptable risks near the boundaries, a decision rule may require readings in a narrower interval [LSL+g,USL−g]. Under a synthetic zero-bias Gaussian instrument-error model with known σ, a specific true part value x has a calculable probability of producing an accepted reading.

That conditional probability is **not** P(true conforming | observed reading), which would require a prior distribution of true part values and a calibrated likelihood. Confusing the two is a serious inferential error. The user must provide an explicit decision rule, expanded or standard uncertainty convention, and treatment of asymmetry, drift and calibration bias.

Constructed case: true x=0, specification ±1, sigma=1, g=0 gives acceptance probability 0.682689492. Increasing guard band lowers that conditional probability. For a truly nonconforming item x=1.5 and sigma=.2, compute a finite false-accept chance even though the nominal part lies outside specification; the result is illustrative and not a manufacturing acceptance certificate.

Actual decision rules require measured uncertainties, a reference instrument, calibration, process distribution, product risk requirements and a documented rejection/indeterminate category.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.normal_inspection_acceptance_risk`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

This probability presumes Gaussian unbiased errors and a specified actual value; no observed error distribution is supplied.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 21: Process stability is a prerequisite to capability

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`Cp=(USL−LSL)/(6s), Cpk=min(USL−μ,μ−LSL)/(3s)`

## Scientific derivation and engineering reasoning

Capability indices compare tolerance width and observed variation. The indices Cp and Cpk are meaningful for a stable, adequately characterized process distribution, not automatically for arbitrary data. Cpk incorporates offset of the process mean from tolerance center. NIST explicitly separates process stability assessment from capability; a trend, tool drift, subgroup mixing or autocorrelation can invalidate ordinary summary assumptions.

The reference function therefore requires declarations of both stability and distribution evidence. If either is absent, it refuses to produce Cp/Cpk. Even when both declarations are present, it labels the result conditional and not independently authenticated: self-asserted flags are not calibrated instruments or reviewed stability plots.

A reproducible capability investigation needs sample order and subgroup rationale, sample size, controlled conditions, measurement-system repeatability, autocorrelation and a process-change log. Use a sample standard deviation with n−1 denominator, record mean and holdouts, and do not infer a six-sigma guarantee from a small convenience sample.

Constructed case: 20 values near 10 within limits [9,11] produce numerical Cp/Cpk under declared evidence, while the same data without stability evidence return HOLD. An identical repeated value has zero sample variance, which is not evidence of perfect manufacturing: the function explicitly refuses that inference.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.stable_process_capability`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Actual stability and distribution are not proved by boolean declarations; outside review remains required.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 22: Finite-sample yield is not guaranteed reliability

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`p_hat=k/n; Wilson 95% lower bound < 1 even when k=n`

## Scientific derivation and engineering reasoning

A batch with all passing tested units is not proven to have 100% yield. For n independent Bernoulli trials with k observed passes, the score-based Wilson interval gives bounded confidence limits for the unknown pass fraction. It remains finite at k=0 and k=n, unlike naive p±z√(p(1−p)/n) which collapses to zero width at these extremes.

The interval assumes representative, independent, identically distributed trials and a specified pass/fail definition. It does not address convenience sampling, clustered wafer defects, shared systematic process errors, instrument false acceptance, untested field conditions, or burn-in lifetime. Sample correlation can cause the nominal interval to substantially understate uncertainty.

Constructed result: k=n=100 yields a point estimate of 1.0 but a Wilson 95% lower confidence limit around 0.963, not 1.0. With no tested samples, the calculation is undefined and must be refused rather than returning a comforting default.

When qualifying semiconductor or additive-manufactured components, report which population was sampled, what pass criteria were used and whether each unit's outcome was independently observable. Retain nonconforming parts, root-cause records and uncertainty intervals alongside successes.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.wilson_yield_interval`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Wilson confidence requires independent representative observations; no physical trial data are included.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 23: An unbroken metrology chain needs real evidence

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`measurand → instrument → lab reference → SI realization, each with uncertainty`

## Scientific derivation and engineering reasoning

A measurement is traceable through a documented chain of comparisons, each carrying a defined quantity, uncertainty and competent calibration source. The chain is a graph of certificates and reference standards, not a marketing claim attached to a measuring tool. At each edge preserve the measured standard, procedure, uncertainty budget, date, environmental control, correction factor and interval before recalibration.

The software checks a declared chain for missing parent records, cycles, missing units, absent uncertainties, expired dates and malformed SHA-256 strings. It still returns `documentation_present_not_source_authenticated` when all metadata looks complete. That distinction is essential: a syntactically plausible 64-character checksum does not prove the original certificate bytes were inspected, or that its issuer was competent.

Constructed case: a gauge references a lab certificate, which references a root standard. The metadata has consistent units, valid dates and checksum strings. The graph is structurally complete, but no actual certificate was retrieved or signed; hence external authentication remains false. A missing parent or expired certificate blocks the declared chain.

For genuine metrological evidence, inspect authentic documents, certificate signatures, measurement logs and accredited competence, and preserve their exact bytes and cryptographic hashes separately from interpretation records.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.traceability_chain_audit`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

The tool is a metadata integrity audit, not NIST accreditation or a device calibration.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 24: Datum frames connect drawings to measured coordinates

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`[X,Y]ᵀ = t + s R(θ)[x,y]ᵀ`

## Scientific derivation and engineering reasoning

Part dimensions become meaningful only relative to defined datums and coordinate systems. A planar rigid-body transform rotates a point through angle θ and translates it by t. Optionally, an isotropic scale factor can represent a declared calibration correction. Rotation is orthogonal: RᵀR=I and preserves lengths when scale=1. The inverse transform applies Rᵀ to the translated observation and divides by scale.

The model checks finite coordinates and a positive scale, and the independent oracle uses a separately assembled NumPy rotation matrix. It does not identify a coordinate transform from noisy observations, which would require calibration targets and an uncertainty model. A perfect numerical inverse of a declared transform cannot prove a machine's actual axes are perpendicular, free of backlash, or stable with temperature.

Constructed test: point (1,0), 90° rotation and translation (3,5) gives (3,6) within floating rounding. Random inverse-transform cases recover the original coordinates. If inspection results are compared without consistent frames, an otherwise conforming part can be falsely rejected or a bad part falsely accepted.

Future manufacturing releases should add measured 3D transformations, squareness, probe offsets, artefact registration and coordinate covariance, all with authentic calibration evidence.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.datum_rigid_transform_xy`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

A mathematical frame transform is not a physically calibrated CMM or machine-tool coordinate system.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 25: A feasible process plan is not an optimal factory schedule

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`start_i >= max(end_dependencies,resource_free_time); end_i=start_i+duration_i`

## Scientific derivation and engineering reasoning

A real production route is a dependency graph with both precedence and finite resource constraints. A simple topological critical path determines a lower bound on completion time but can underestimate makespan when two operations compete for the same spindle, metrology station or operator. Resource-constrained scheduling must assign start and end times without violating prerequisites or machine occupancy.

The reference uses deterministic list scheduling on a DAG with each resource treated as unary. The recurrence starts each task no earlier than both its latest predecessor completion and its assigned resource's previous availability. It explicitly reports that the result is feasible, **not provably optimal**. It ignores changeover costs, worker constraints, maintenance, urgent jobs, yield, rework, batch setups and machine breakdowns.

Constructed example: a cutting task A=3 minutes and B=4 minutes share one station. Their combined occupied time is at least 7 minutes regardless of precedence. With a separate inspection task C depending on A, C may overlap B only if it uses a different resource. Deterministic schedules must be checked independently against resource occupancy and precedence, not trusted because a list of operations exists.

A future planner should include measured process time distributions, scrap probabilities, safety and energy constraints before scheduling an actual factory.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.resource_bounded_schedule`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Schedule outputs are not shop-floor safety authorization or throughput forecasts.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 26: Mass and energy constraints are reconstruction invariants

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`m_in=m_part+m_scrap+m_recoverable+Δinventory; P=energy/time`

## Scientific derivation and engineering reasoning

Conservation laws offer a way to detect inconsistency before constructing a process. For an operation with measured stock mass m_in, finished part mass m_part, chips/scrap m_scrap and recoverable material m_rec, the remainder must be recorded as inventory, residue, loss or measurement discrepancy. Mass balance does not say the process is efficient, safe or qualified; it only exposes missing accounting.

Existing Manufacturing v0.1 models provide bounded cutting power and removed-volume calculations under hypothetical uniform chip-load assumptions. Mechanical input power must exceed ideal cutting power when efficiency is below one. Combining energy estimates with a resource schedule supports a synthetic lower-bound budget, but machine acceleration, auxiliary loads, lubrication, spindle idle power and thermal dissipation are not included.

Worked scenario: a declared material density times removal volume gives removed mass. Independently compute material removal rate from feed and geometry and multiply by specific cutting energy, then divide by efficiency for an illustrative input-power lower bound. A mismatch beyond declared uncertainty triggers investigation; no numeric output authorizes an actual spindle speed.

The continuity ledger must connect material identity, specimen geometry and measured mass to the measurement chain. No physical material was cut or measured in this Atlas edition.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_atlas.models.cutting_estimate; resource_bounded_schedule`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Reference energy and mass relationships are not validated machine setpoints or real tool performance.

Bibliography card: `NIST-AM-QUAL`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 27: Evidence-carrying process plans refuse unsupported completion

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`ready_i = inputs_present ∧ required_evidence_present ∧ all_dependencies_ready`

## Scientific derivation and engineering reasoning

A process graph can list perfectly plausible steps but still be impossible to execute. Each stage needs input artifacts, outputs, prerequisite stages and a declared set of evidence types. The evidence-gated planner propagates missing inputs and missing evidence through the dependency graph, returning HOLD rather than inventing a completed manufacturing step. This is the major integration principle connecting ATLAS FORGE's scientific library with reconstructible operations.

The result has two independent dimensions. **Structural completeness** means the required item names and evidence declarations exist according to the supplied metadata. **Scientific/physical certification** requires authentic measurements, competent reviewers and physical inspections and is never inferred by this method. A recorded hash or a user-supplied certificate label cannot turn a synthetic plan into an authenticated fabricated component.

Constructed case: raw stock feeds inspection with required calibration and measurement evidence. If calibration is present but measurement absent, inspection HOLDs and all downstream dependent stages remain blocked. If both are provided only as synthetic metadata, the planner can be structurally complete, but `independently_certified` remains false.

Graph cycles, unknown inputs, duplicate produced artifacts and malformed metadata are errors, not states silently skipped. This provides an executable audit scaffold for the future Manufacturing-to-Computer Architecture handoff.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Recorded evidence metadata does not authenticate a lab, physical part or safety control.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 28: Manufacturing prerequisites for silicon gates and integrated circuits

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`materials→geometry→fabrication→metrology→device IV/CV→cell delay→logic`

## Scientific derivation and engineering reasoning

A reconstructible semiconductor device requires a stack of physical dependencies: starting substrate identity, purity and defect characterization; thin-film growth or deposition; repeatable pattern alignment; material removal; dopant distribution and activation; contact formation; interconnect; electrical probing; packaging; and thermal/environmental testing. Every transition changes geometry, composition or electrical performance, and each needs appropriate instruments and controls.

The Electronics node now preserves bounded MOS/diode/logic equations and an 8-bit program interpreter. Those are insufficient to establish physical silicon: fabricated device I–V/C–V curves, oxide thickness, doping profiles, contact resistance, gate transfer curves, setup/hold distributions, noise margins and yield are all absent. The manufacturing evidence graph should list these requirements as explicit blocked gates, not treat a model simulation as an observed device.

Current NIST research emphasizes overlay and critical-dimension metrology for multilayer semiconductor fabrication, highlighting the measurement dependency between layout and functioning devices. The corresponding bibliographic source card is navigational; no authenticated NIST original file was locally archived.

The intended future experiment is a safety-reviewed, independently performed fabrication/measurement program with raw instrument files and release criteria. This edition intentionally avoids asserting any wafer process recipe or chemically hazardous tool configuration as tested or safe.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate; electronics-atlas method prerequisites`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Physical fab processes and calibrated device measurements have not been performed.

Bibliography card: `NIST-CHIPS-OVERLAY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 29: Repairs must regenerate qualification evidence

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`postrepair acceptance = spec ∧ traceable_measurement ∧ evidence_of_changed_components`

## Scientific derivation and engineering reasoning

Technological continuity requires maintenance and rebuilding as much as first-time manufacturing. When a machine component is replaced, a formerly calibrated assembly may no longer meet its previous accuracy, alignment, stiffness or thermal specifications. Repair is a state transition that should invalidate dependent qualifications unless fresh evidence confirms applicable performance.

A repair trace starts from symptoms and out-of-tolerance observations, records replaced components and their provenance, updates geometric and uncertainty budgets, then schedules controlled post-repair measurements against appropriate references. The validity of prior inspection data must be reviewed. For example, changing a measuring probe tip affects offset and possibly uncertainty, while replacing a leadscrew can change backlash and axis response.

The graph does not assume all repairs require a full factory requalification or that a single passing dimension proves success. It identifies which evidence types depend on the changed component. A future competence-reviewed policy must set specific criteria for releasing machinery to service.

Constructed test: a repair step requests a new calibration record and an alignment measurement. Without either, the subsequent inspection step is blocked even if the prior drawing and parts list exist. This is a software demonstration of evidence dependencies, not an instruction to operate repaired equipment.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate; covariance_budget_psd`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Maintenance planning is not machine safety certification or control-system functional-safety testing.

Bibliography card: `NIST-CALIBRATION-GMP13`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.


---

# Chapter 30: An auditable chain from physical parts to computing

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`reconstructible claim = science_reference ∧ manufacturing_evidence ∧ hardware_measurement ∧ verified_computation`

## Scientific derivation and engineering reasoning

ATLAS FORGE's eventual claim is stronger than storing manuals: a future team should be able to reconstruct useful technology from starting materials and verify it along the way. This chapter packages a deliberately incomplete *end-to-end challenge* that spans scientific source knowledge, material and machine readiness, fabrication evidence, electronics and an observable program result.

The current Electronics release demonstrates a bounded 8-bit stored-program interpreter that can compute and store a result. The challenge's software layer can execute that same program and verify the final accumulator and memory bytes. But the manufacturing branch has no actual wafer, calibrated measuring equipment, fabricated registers, clock or physical computer. Accordingly the evidence-gated manufacturing steps must remain on HOLD while the software computation passes.

A future real-world attempt should provide authentic source files and rights, bill of materials, tool and instrument calibration, raw process logs, measured semiconductor I–V/C–V, verified noise and clock timing margins, manufactured circuit photos/layout and a program execution trace from the actual device. Each artifact must be accompanied by a machine-readable hash, provenance and independently reviewed authenticity.

The challenge should report separate stages rather than one aggregate success bit: `software_reference_passed`, `process_metadata_complete`, `physical_manufacture_verified`, and `independent_review_completed`. Only the first can currently be true. This is the difference between a hypothetical reconstruction blueprint and demonstrated technological continuity.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_evidence_gate; electronics_atlas.v1_scoped_models.EightBitAccumulator`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

No physical reconstructed computer or certified manufacturing facility is part of this release.

Bibliography card: `NIST-AM-QUAL`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.

