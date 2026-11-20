# Chapter 39 — Convolution, spectral multiplication and aliasing

**Area:** Numerics. **Edition:** Computation Atlas v0.2.0. **Evidence origin:** original explanatory material, qualified by the linked publisher sources. Original third-party text is not mirrored.

## Definitions and prerequisites

Linear discrete convolution combines two finite sequences and is central to filtering, impulse responses, polynomial multiplication and imaging. The convolution theorem permits a fast implementation using Fourier-domain multiplication, provided the transform length is large enough to avoid circular wraparound. Naively using an N-point transform for a linear convolution longer than N computes circular convolution and aliases tail terms into earlier samples. Zero-padding is therefore a mathematical requirement, not an optional performance tweak.

## Mathematical contract

(a*b)[k]=Σ_j a[j]b[k−j], where out-of-range indices contribute zero. DFT(a*b)=DFT(a)·DFT(b) for zero-padding length N≥len(a)+len(b)−1.

## Derivation and reasoning

Expanding the DFT of the convolution and exchanging the finite sums yields the product of individual DFTs. The DFT implements periodic extension, so the pointwise product corresponds to circular convolution unless the zero-padded period exceeds the linear result length. With enough padding, circular and linear results coincide within the needed output range.

## Worked reconstruction and independent check

Convolve [1,2,3] with [2,1]. The correct linear result is [2,5,8,3]. The reference method pads to the next power of two, multiplies FFT spectra, inverses and truncates to the linear length. Compare against NumPy's direct convolution rather than another FFT implementation.

## Limitations, falsification, and invalid use

The output of floating-point convolution is approximate. Frequency-domain multiplication can overflow or magnify conditioning problems. For massive sparse kernels, direct/sparse methods may outperform FFT due to overhead. No physical filter response is established without sampling and boundary-condition evidence.

## Cross-domain meaning

This is a mathematical bridge to Cymatics and Signal Atlases, not an implementation of a cross-domain Bitwork router.

## Source orientation and recoverability

- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/pages/lecture-notes/) — original publisher bytes unavailable in this package.
- [MIT OpenCourseWare 18.S191 Introduction to Computational Thinking](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2020/) — original publisher bytes unavailable in this package.

This chapter is a reproducible teaching reference, **not** an independent domain-scientist peer review, live hardware result or universal code proof.
