# 11. Time integration of the HH membrane with explicit scope limits

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The HH system combines one membrane voltage equation and three first-order gating equations. Numerical integration choices matter: very large explicit steps can generate fictitious firing, negative gate fractions or numerical instability. A reproducible implementation must specify its integration method, time units, parameter domain and result trace format.

## Governing mathematical model

`C_m dV/dt=I_in−I_Na−I_K−I_l; gated x(t+Δt)=x_inf+(x−x_inf)e^{−Δt/τ}`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The reference integrates V with bounded explicit Euler and gates by their exact voltage-held exponential solution. This is a numerical splitting scheme, not an analytically exact solution of the coupled nonlinear HH system. The implementation requires Δt≤0.025 ms, finite bounded synthetic injected current, a defined initial state and a finite step budget. A comparison to a smaller step or a separate numerical integrator can reveal discretization error.

The model's current values are declared in µA/cm² and capacitance in µF/cm², so mV/ms emerges correctly. Gating fractions remain in [0,1] if the rates and step are valid. The initial historical −65 mV rest state has only a small residual drift under the rounded leak parameters; this is not a failure of the arithmetic. Outputs are labeled simulated squid membrane traces rather than measurement or medical advice.

## Independently checkable worked case

Run 500 steps at 0.01 ms from the classical rest gate equilibrium and require all voltages and gate fractions to remain finite. Repeat with identical inputs and compare complete traces for exact deterministic replay. Deliberately request Δt=0.2 ms and require rejection.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The original source had experimental support for squid giant axon physiology. This Atlas reimplementation itself has no direct biological experiment, temperature-corrected human tissue model or clinical validation.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
