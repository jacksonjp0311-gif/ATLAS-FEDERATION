# Chapter 41: Radix-two FFT, spectral sampling and aliasing tests

**Edition:** Mathematics & Fundamental Physics v0.2.0 (original project research).  **Evidence class:** mathematical derivations plus bounded numerical simulations only. No independent scientific peer review or original publisher document archived.

**Reconstruction equation:** `X[k]=Σₙ₌₀ᴺ⁻¹ x[n]e^(−2πikn/N); x[n]=(1/N)Σₖ X[k]e^(+2πikn/N).`

**Reference algorithm:** `math_physics_atlas.v02_models.fft_radix2(samples, inverse)`

**Units:** Input samples carry signal units; DFT has input units under unnormalized forward definition, and frequencies require an explicit sample interval.

## Why a fast transform is more than an optimization
A discrete Fourier transform rewrites an evenly sampled finite sequence as a weighted sum of complex exponentials. It supports spectral diagnosis, filters, convolution, digital communications and the linear algebra used inside AI systems. The direct formula has N² complex multiply-adds. For N=2ᵐ, the Cooley–Tukey decomposition splits even- and odd-index samples into two length N/2 transforms and combines them using roots of unity. Its operation count scales with N log₂N, making large experiments feasible without a specialized scientific stack.

## Derive the butterfly
Take x[2j] and x[2j+1]. Then X[k]=E[k]+ωᴺᵏ O[k], where ωᴺ=e^(−2πi/N), and E,O are the DFTs of the even and odd subsequences. Because ωᴺ^(k+N/2)=−ωᴺᵏ, X[k+N/2]=E[k]−ωᴺᵏ O[k]. The butterfly therefore combines two half-size transforms with a single phase multiplier. Iterative bit reversal places the leaves in the order needed to perform these in-place butterflies from length 2 to N. The inverse conjugates the sign of the exponent and divides by N. State your normalization: the unnormalized forward transform obeys Σ|x[n]|²=(1/N)Σ|X[k]|² (Parseval identity).

## Reconstruct and inspect
For x=[0,1,0,0], each sample is zero except n=1, so X[k]=e^(−2πik/4)=[1,−i,−1,+i]. The inverse returns the original impulse. A single complex sinusoid with k=3 and N=16 gives one nonzero bin of magnitude 16; a real cosine splits into symmetric positive/negative frequency bins. A separate NumPy FFT checks 200 seeded arrays and the inverse reconstruction. The benchmark reports absolute errors and case counts; it does not establish CPU performance against optimized native libraries.

## Aliasing and leakage are scientific limitations
If a continuous signal has frequency f and a sampler takes values every Δt, f and f+k/Δt can generate indistinguishable samples for integer k. The Nyquist bound |f|<1/(2Δt) is a sampling condition, not an FFT error message. Finite time windows leak energy across bins when a tone does not fit an integer number of cycles. An FFT cannot reconstruct frequencies or phases that acquisition discarded. With no sample interval, X[k] is only a sequence of coefficients, not a physical spectrum in hertz.

## Technology continuity link
Keep the transform convention, units, sampling metadata, numerical test vectors, anti-alias requirements and counterexamples. These are the minimum ingredients for rebuilding spectrum analyzers, digital oscilloscopes and fast convolution.

## Source, rights and verification boundary
This chapter is original educational derivation and demonstration, not copied course text. Bibliographic scope: [MIT OpenCourseWare 18.335J, Introduction to Numerical Methods (2019) — bibliographic source only](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/pages/calendar/). The publisher resource was not downloaded, rights-authenticated, or used as an independent empirical validation. **Refusal/limitation:** Only power-of-two N≤4096 and finite scalar samples. Sampling cannot distinguish frequencies separated by integer multiples of sample rate.

**Verification route:** run `python -m unittest discover -s tests -q` and `python tools/independent_oracle_v02.py`; retain seed, full inputs, environment, numerical residuals, and all failed cases.
