# Chapter 38 — Discrete Fourier transform and radix-two FFT

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

The discrete Fourier transform (DFT) expresses a finite sequence in a frequency basis of complex exponentials. The direct computation has quadratic arithmetic cost in sequence length. The radix-two fast Fourier transform (FFT) recursively decomposes even and odd indices into smaller transforms, yielding O(n log n) operations for n a power of two. Both compute the same mathematical DFT, aside from numerical rounding. Fourier coefficients are not automatically physical resonant modes: sample rate, windowing, boundary conditions and measurement geometry affect interpretation.

## Mathematical contract

X_k=Σ_(n=0)^(N−1) x_n exp(−2πikn/N). The inverse is x_n=(1/N)Σ_k X_k exp(+2πikn/N). For N=2^m, radix-two FFT work is O(N log₂N).

## Derivation and reasoning

Split the DFT sum into terms with even index 2j and odd index 2j+1. Both subsets are transforms of length N/2. The odd transform is multiplied by a twiddle factor exp(−2πik/N); combining one pair of N/2 transforms costs O(N). Thus T(N)=2T(N/2)+O(N), yielding O(N log N). The inverse changes the exponential sign and divides by N.

## Worked reconstruction and independent check

Take [1,2,3,4]; calculate its four complex DFT coefficients by hand and recover the input using the inverse transform. Compare the pure-Python iterative FFT with NumPy's FFT on seeded complex arrays. The tests include round trips, real and imaginary components, and several powers of two.

## Limitations, falsification, and invalid use

Non-power-of-two lengths require another FFT variant or padding. Rounding can accumulate; tiny imaginary residuals after real-valued convolution do not imply a physical imaginary signal. No claim of instrument frequency calibration is made.

## Cross-domain meaning

Signal and Cymatics Atlases depend on correct transform mathematics, but the FFT itself does not establish a physical mechanism or measured acoustic resonance.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
