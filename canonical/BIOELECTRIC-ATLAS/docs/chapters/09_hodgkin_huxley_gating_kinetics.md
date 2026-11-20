# 09. Hodgkin–Huxley voltage-gated sodium and potassium kinetics

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Hodgkin and Huxley formulated time-dependent sodium, potassium and leak currents for the squid giant axon. Their conductances depend on activation/inactivation variables m, h and n. These probabilities evolve according to voltage-dependent first-order transition rates, and the membrane voltage evolves from ionic and applied currents.

## Governing mathematical model

`dx/dt=α_x(V)(1−x)−β_x(V)x; I_Na=gNa m³h(V−ENa); I_K=gK n⁴(V−EK)`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The classical parameterization is in mV, ms, µA/cm², mS/cm² and µF/cm², commonly associated with an experimental temperature around 6.3 °C. Code must not mix those units with the SI-only passive reference without a conversion layer. The voltage reference is modern inside-negative rest around −65 mV; the historical article uses differing original conventions, so maintain a clearly documented translation. For each gate, x_inf=α/(α+β) and τ=1/(α+β). If voltage is held constant during a step, the gate has an exact exponential update that remains within [0,1].

The nominal coefficients (gNa=120, gK=36, gL=0.3 in mS/cm²; ENa=50, EK=−77, EL=−54.387 mV) are an illustrative historical model fit. They are not human cell constants and should not be used to design a medical intervention. A separate solver must respect numerical stability and source-form assumptions.

## Independently checkable worked case

At −65 mV, the model gate fractions are approximately m=0.05293, h=0.59612 and n=0.31768. Compute gate rates and require all to be nonnegative; compare one exact voltage-held gate update with an independently calculated derivative at a very small Δt.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No inference is permitted about human firing thresholds, individual illness, stimulation current or tissue survival from this parameterization.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
