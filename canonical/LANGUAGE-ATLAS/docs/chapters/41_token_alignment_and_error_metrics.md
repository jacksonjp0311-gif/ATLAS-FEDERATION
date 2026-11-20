# 41. Alignment error rates depend on segmentation and evidence

Speech recognition, transcription and historical comparison frequently align two sequences. A sequence is not necessarily a sequence of English words: it may be graphemes, phonemes, morphemes, gloss tokens or segments defined by an annotation project. The unit determines both interpretation and error counts. Standard edit distance minimizes substitutions, insertions and deletions under fixed costs; one alignment may be optimal among multiple alternatives.

## Dynamic programming

For reference tokens `r_1…r_m` and hypothesis tokens `h_1…h_n`, define `D(i,0)=i` and `D(0,j)=j`. Recurrence: `D(i,j)=min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+[r_i≠h_j])`. A reverse traceback produces one optimal path and records matches, substitutions, deletions and insertions. Under the usual definition, word error rate is `(S+D+I)/N_ref`, where N_ref is the number of reference words; with N_ref=0, the normalized rate is undefined, not zero. WER can exceed one when insertions dominate.

`aligned_edit_distance` implements this teaching calculation with an explicit finite grid cap and returns one witness. It neither detects the speaker's intended words nor authenticates the reference. Text normalization, language-specific word boundaries, transcription conventions and punctuation affect all results. A signed-language movement sequence or simultaneous non-manual feature tier is not faithfully represented by one token stream.

## Example

For reference `['i','like','cats']` and hypothesis `['i','adore','cats']`, one substitution yields distance 1 and error rate 1/3. The result says nothing about whether “adore” conveys acceptable meaning in the context. Two equally valid transcripts may differ in word segmentation and appear to have errors even when the sound signal is similar. A linguistic atlas must preserve the transcription scheme and source audio/video rights where permitted.

## Evidence requirements

A real ASR or documentation evaluation should preserve the source recording and permitted access, time alignment, speaker/dialect context, reference annotators, disagreements, normalization rules, and boundaries used by the metric. Errors from small datasets or unrepresentative domains cannot be scaled to all speakers. A low token error rate can hide catastrophic errors on names, medication instructions, negation or consent conditions.

**Sources:** Jurafsky and Martin *Speech and Language Processing* online draft (selected publisher overview); Unicode UAX #29; existing Atlas segmentation and morphology references. No actual audio/transcription dataset was imported.
