# 05. Passive membrane as capacitor and conductance network

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A lumped passive membrane can be approximated by a capacitor in parallel with an Ohmic leak conductance toward a reversal potential. Kirchhoff current balance gives a first-order differential equation with an exponential analytical solution. This is a building block for understanding time constants and input resistance.

## Governing mathematical model

`C dV/dt = -g(V-E) + I; τ=C/g; V(t)=V_inf+(V0-V_inf)exp(-t/τ)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Specify capacitance in farads, conductance in siemens, voltage in volts, current in amperes and time in seconds. If the injected current is defined positive inward, V_inf=E+I/g for constant forcing and τ=C/g. With several independent parallel channels, the total conductance is the sum and the equilibrium voltage is the conductance-weighted reversal voltage plus I/g_total. A zero-total-conductance system has no finite passive time constant and must not return an invented equilibrium.

This model does not capture excitability, nonlinear gating or spatial conduction. Real cell geometries have membrane and axial access resistance; whole-cell recordings may introduce series resistance and capacitive transients that appear biological if not accounted for. Synthetic parameter sets must be labeled as such.

## Independently checkable worked case

Take C=1 microfarad, g=1 millisiemens and V0=100 mV relative to a zero reversal, I=0. The time constant is 1 ms; after 1 ms the model gives about 36.79 mV. Recalculate by independently solving the linear ODE as a numerical check.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The result is a mathematically defined lumped RC response, not a measured squid axon, a human neuron, or a valid bioelectric stimulation dose.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
