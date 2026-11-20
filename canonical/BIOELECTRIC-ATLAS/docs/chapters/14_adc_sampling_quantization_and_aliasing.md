# 14. Sampling, Nyquist limits and ADC error models

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Bioelectric signals are often sampled with electronic instruments, but the sampling process can distort or misrepresent the underlying analog waveform. An ideal uniform ADC maps a bounded voltage range into discrete integer codes. Quantization error, clipping and aliasing must be documented independently from biological interpretation.

## Governing mathematical model

`ΔV=(V_max−V_min)/(2^N−1); |quantization error|≤ΔV/2 for unclipped ideal nearest-code samples`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For an N-bit ideal code range [0,2^N−1], the encoder maps the analog input to the nearest code and reports any out-of-range clipping. A data report should preserve sample rate, voltage units, offset, transfer function, ADC resolution, reference accuracy and calibration. A realistic front end also needs anti-alias filtering, noise, input impedance, isolated supplies and electrical safety, none of which is implemented by a numerical quantizer.

Aliasing occurs because sample sequences depend on frequency modulo the sample rate. The synthetic sinusoid at 17 Hz sampled at 100 Hz is indistinguishable from a 117 Hz sinusoid at those sample instants. This does not mean the underlying analog signals are identical. A high sample rate alone does not guarantee measurement quality if anti-alias filtering or reference voltage is incorrect.

## Independently checkable worked case

Quantize an unclipped 0–1 V sample using 10 bits and require reconstruction error below half an ideal code step. Compare 200 samples of 17 Hz and 117 Hz sines at 100 samples/s and observe nearly identical discrete values.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Sampling examples are simulated and not equipment calibration or human-body electrophysiology measurements. Mains-connected or body-connected measurement circuit construction is out of scope.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
