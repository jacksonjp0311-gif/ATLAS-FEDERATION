# 10. Removable singularities in Hodgkin–Huxley rate equations

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Classic Hodgkin–Huxley activation-rate formulas contain factors of the form x/(1−exp(−x/a)). At x=0 a naive floating-point evaluation gives 0/0, even though the physical mathematical limit exists. Software that inserts an arbitrary epsilon or returns zero can produce a discontinuous gating rate and invalid dynamics.

## Governing mathematical model

`lim_{x→0} x/(1−exp(−x/a)) = a`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use expm1 where possible to compute exp(x)−1 accurately for small arguments, and a series expansion around the removable singularity. For gate m this occurs near −40 mV, and for gate n near −55 mV under the conventional rest-normalized voltage representation. A strictly positive temperature is required for any thermodynamic extension, and the rate model should reject unreasonable voltage extrapolations instead of producing infinities.

Calculate convergence by evaluating values on either side of the singularity and checking smooth approach to the analytical limit. Preserve independent identity tests, not just two hardcoded voltage values. Numerical methods must not be mistaken for independently verified biophysics; the target historical equation still depends on experimental context and translation of voltage reference conventions.

## Independently checkable worked case

At −40 mV, the m activation rate has the finite limit 1/ms; at −55 mV, n activation is 0.1/ms. Perturb either voltage by ±10⁻⁵ mV and verify the rate approaches the same finite limit smoothly, rather than throwing or becoming zero.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

A mathematically stable rate calculation does not establish that any particular ion channel behaves according to the squid model.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
