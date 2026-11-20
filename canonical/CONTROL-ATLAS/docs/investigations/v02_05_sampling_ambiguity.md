# Investigation 05. A 70 Hz oscillation appears at 30 Hz after sampling

**Origin: constructed scientific teaching case or procedural review; no device was controlled.**

An ideal sinusoid at 70 Hz sampled at fs=100 Hz is represented by an alias frequency magnitude of 30 Hz. The samples alone can be compatible with a lower-frequency sinusoid under a suitable phase relationship. The Atlas computes the folded frequency but does not estimate the original physical frequency, resolve phases or recover information removed by undersampling.

A control engineer attempting to suppress a mechanical resonance from an aliased accelerometer trace could target the wrong mode. The solution begins with measuring actual sensor bandwidth, analog anti-alias filtering, clock jitter and sampling rates before fitting a model. An FFT of a short or gapped time series can also exhibit leakage and other artifacts not represented in this one-line formula.

**Refusal:** this package does not identify a physical resonance or reconstruct a unique signal. **Source:** MathWorks Making Quality Measurements antialiasing guidance.
