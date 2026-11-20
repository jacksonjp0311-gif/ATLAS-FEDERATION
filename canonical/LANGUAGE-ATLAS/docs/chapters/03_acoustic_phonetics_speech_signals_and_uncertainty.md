# Chapter 03. Acoustic phonetics, speech signals and uncertainty

**Area:** Phonetics  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

Acoustic speech consists of time-varying pressure changes, usually measured by a transducer and digitized. Relevant analyses may include time-domain waveforms, spectrograms, spectral envelope, formants, pitch-related periodicity, duration, loudness and noise. No single number fully describes a spoken vowel or consonant. A physical fundamental-frequency estimate depends on the presence of periodic voicing and on the estimator and window; a child, an adult and a speaker with irregular phonation may produce very different signals. Coarticulation and environmental noise limit simplistic phone segmentation.

## Underlying mathematical, grammatical or methodological principle

Sampling converts a continuous signal to a discrete series x[n] at sample rate f_s. For a truly band-limited input and ideal sampling, the Nyquist criterion requires f_s greater than twice the highest signal frequency for unaliased reconstruction. This does not imply speech itself is perfectly band-limited or that a poor microphone records every relevant articulation. The discrete Fourier transform summarizes a finite window's frequency content; time-frequency resolution trades off with window length. A spectrogram's apparent patterns must be tied to a disclosed window, normalization and color scale.

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

Construct a sampled sinusoid mathematically rather than using a real speaker's recording. Calculate sample period 1/f_s and compare hypothetical 500 Hz and 3 kHz components at 8 kHz sampling. Record why this does not characterize intelligibility. Describe how you would collect consented speech and test whether a measured F0 corresponds to a reported pitch.

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

No real audio data, speech-recognition benchmark or recording rights were acquired. Do not infer a person's identity, health or emotion from a toy spectrum. Acoustic measurements require calibration and independently checked labels.

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

- [Speech and Language Processing, Third Edition online draft](https://web.stanford.edu/~jurafsky/slp3/) — Authors August 19, 2026 manuscript release; inspected site contents and edition details
- [Praat phonetic analysis software](https://www.fon.hum.uva.nl/praat/) — Bibliographic software reference for acoustic analysis and measurements; no instrument data acquired
- [International Phonetic Alphabet, current IPA Chart](https://www.internationalphoneticassociation.org/content/chart) — Official IPA chart notation, Council revisions and reproduction terms; current chart rights CC BY-SA 4.0

**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
