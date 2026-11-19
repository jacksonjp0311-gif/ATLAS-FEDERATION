# 06. Parallel channel conductances and current conservation

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The total membrane current is the sum of capacitive, leak and channel currents. When each channel is approximated as Ohmic at one operating point, the conductance-weighted equilibrium follows directly from Kirchhoff’s current law. Current direction conventions must be explicit to avoid sign errors.

## Governing mathematical model

`0 = Σ_k g_k(E_k-V) + I; V*=(Σg_k E_k+I)/Σg_k`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For fixed conductances, the conductance sum is nonnegative and strictly positive for a finite equilibrium. If all conductances are zero, V is not identified by the equilibrium equation. Changes in one channel conductance change both the time constant and steady voltage. In living tissue, voltage-gated channels make g depend on voltage and time, so a single fixed conductance equilibrium may be invalid.

A model can pass numerical tests while using unrealistic dimensions or ignoring gradients maintained by ATP-driven pumps. To avoid false confidence, require a list of which currents were modeled, whether the state is dynamic, the selected time reference, and the error bounds for input current and conductance parameters. Keep the original ion model and the numerical solver as distinct reproducibility claims.

## Independently checkable worked case

For two channels with g=(2,1) S and E=(−0.1,+0.2) V, equilibrium is zero. Add 0.2 A inward to the g=2 S, E=−0.1 V system and its equilibrium also becomes zero. These numbers are dimension-checking fixtures, not actual biological conductances.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Do not infer tissue health, identity of the active channel, action-potential threshold or safety limits from this linearized example.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
