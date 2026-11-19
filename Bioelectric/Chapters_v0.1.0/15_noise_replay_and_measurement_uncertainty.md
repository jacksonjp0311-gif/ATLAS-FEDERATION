# 15. Noise, calibration uncertainty and reproducible signal traces

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Measurement uncertainty has multiple sources: calibration reference, amplifier drift, thermal noise, digitizer resolution, model inadequacy and environmental interference. A numerical trace can be perfectly reproducible while a real instrument is not. An evidence record must therefore distinguish a random seed and generated noise samples from raw, calibrated laboratory observations.

## Governing mathematical model

`u_c=√Σu_i² for independent (uncorrelated) standard uncertainties`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Root-sum-square combination is valid for independent standard uncertainties or when covariance terms are legitimately zero. With correlated measurements, add the covariance terms; a simple RSS function must not pretend to handle correlation. Synthetic Gaussian noise with a fixed seed supports test replays but does not establish a real biological noise spectrum, PSD, Johnson noise temperature, amplifier 1/f behavior or electrode artifact distribution.

A robust measurement dossier would include instrument model and serial, calibration status, measurement chain, temperature, source impedance, bandwidth, gain, ADC reference, sample-rate uncertainties, and raw unprocessed samples. The Atlas provides a checklist, not the evidence. Calibration receipts from qualified laboratories are necessary for external engineering acceptance.

## Independently checkable worked case

Combine independent uncertainties 3 and 4 in the same physical units; u_c=5. Generate two artificial noise traces using the same seed and standard deviation and verify identical SHA-256. Change seed and verify digest difference. Label the trace synthetic.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Numerical seed repeatability is not experimental repeatability. This edition does not provide verified biomedical instrumentation, medical diagnostic sensitivity or measured noise covariance.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
