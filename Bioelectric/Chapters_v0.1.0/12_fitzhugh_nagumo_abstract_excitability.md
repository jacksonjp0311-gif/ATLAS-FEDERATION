# 12. FitzHugh–Nagumo dimensionless excitability dynamics

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A reduced two-variable excitable-system model can reproduce qualitative phase-plane behavior while omitting the specific molecular channels of Hodgkin–Huxley. A typical FitzHugh–Nagumo reference contains a fast excitation variable v and a slow recovery variable w. Its variables and time parameters are dimensionless unless a specific validated scaling is supplied.

## Governing mathematical model

`dv/dt = v−v³/3−w+I; dw/dt=ε(v+a−bw)`

**Source orientation:** FITZHUGH-1961 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1366333/`), DOI 10.1016/S0006-3495(61)86902-6. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Unlike membrane voltage in volts, FHN v is a dimensionless state coordinate. Converting an FHN trajectory directly to a measured neuronal action potential is invalid without an experimentally calibrated transformation. The model is integrated with classical fourth-order Runge–Kutta using a small bounded step. The result is a reproducible nonlinear dynamical system that can demonstrate excitability and oscillator intuition without guessing channel conductances.

An independent solver should evaluate the derivative separately and compare a one-step RK4 result to two half-steps. Any numerical check must record a, b, epsilon, drive, initial state and integration step. Out-of-range values or nonfinite dynamics should halt rather than be interpreted as extreme biology.

## Independently checkable worked case

Start from (v,w)=(-1,0), a=0.7,b=0.8,epsilon=0.08 and dt=0.01. Compare the RK4 result with two steps of dt=0.005 to better than the documented local tolerance. Change the drive and observe a different trajectory.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

This is a generic excitable dynamical reference, not a model of human nervous function, diagnosis, consciousness or therapeutic stimulation.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
