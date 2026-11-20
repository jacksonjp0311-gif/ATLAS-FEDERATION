# 08. Cable-step stability, conservation and discretization errors

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A numerical simulation of a physical equation has its own stability conditions. Even if the continuum PDE is passive, choosing a time step beyond the explicit solver’s stability bound can create artificial oscillation or growth. Finite-step numerical evidence must therefore include the method, resolution and error constraints.

## Governing mathematical model

`Δt ≤ C/(degree_max g_ax+g_leak) (sufficient nonnegative weights)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For a leak-free sealed chain, sum of C(V_i−V_ref) remains constant under exact arithmetic because every axial edge current appears once with a positive and once with a negative sign. This invariance provides a strong finite numerical test independent of a particular waveform. With leak, the sum decays toward the reversal; with injected currents, the total changes according to the supplied net current.

A convergence study must compare results at decreasing Δt and increasing spatial resolution, while retaining actual geometry and boundary conditions. The simple implemented model keeps the number of nodes finite and does not infer any real tissue size. It rejects input-current lists of the wrong length, negative conductances, nonfinite voltages and time steps beyond its declared bound.

## Independently checkable worked case

Initialize five random node voltages; evolve with leak 0, no applied current and an admissible time step. After each step, sum all voltages and verify conservation to floating-point tolerance. Deliberately choose a step larger than the bound and require refusal, not a fictitious oscillatory “spike.”

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Stability of a numerical integrator does not prove a biological system stable or a model parameter set experimentally valid.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
