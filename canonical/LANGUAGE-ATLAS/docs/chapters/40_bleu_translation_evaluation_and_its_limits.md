# 40. BLEU evaluates token overlap under explicit reference conditions

Machine translation quality is not a single number. Adequacy, factual fidelity, terminology, register, politeness, cultural meaning, preservation of negation, and usability to real speakers can diverge even when token overlap looks strong. BLEU (Papineni et al., 2002) compares system output n-grams with one or more human reference translations and applies a penalty for very short outputs. It is primarily a **corpus-level** statistic under specified tokenization, reference composition, and smoothing, not a semantic correctness oracle for one sentence.

## Mathematical contract

For order n, count each candidate n-gram's occurrences and clip them to the maximum occurrences of that n-gram in any reference for the corresponding sentence. Accumulate clipped and candidate counts over all sentences to get precision `p_n`. Let c be the total candidate-token length and r the sum of closest reference lengths (tie convention declared). The brevity penalty is `BP=1` for c≥r and `BP=exp(1−r/c)` for 0<c<r. A simple unsmoothed BLEU score of order N is `BP * exp((1/N)Σ_n log(p_n))`, defined as zero when any required p_n is zero. The function has no meaning independent of the tokenizer's unit.

The original 2002 paper introduced a useful automatic evaluation framework. Post's 2018 SacreBLEU paper emphasizes that normalizing and tokenizing data differently makes published scores incomparable. Our `corpus_bleu` is explicitly **not SacreBLEU** and does not implement the WMT signature, reference normalization, or its smoothing options. It only demonstrates the transparent arithmetic on caller-supplied token arrays.

## A falsifying case

A candidate translation containing the exact reference tokens may score 1.0 even if the reference translation itself is culturally inappropriate or false. Conversely, a valid paraphrase can have low n-gram overlap. A one-word candidate may have a nonzero unigram match but a zero four-gram precision under unsmoothed BLEU, and therefore BLEU4=0. None of these outcomes licenses a claim about a model's actual understanding.

## How to reconstruct

Write each reference token sequence, enumerate the candidate's n-grams, apply the per-sentence clipped maximum, aggregate counts, compute closest-reference corpus length, and then report the exact options: tokenization, case treatment, Unicode normalization, references, max order, smoothing, and metric implementation/version. For a serious system comparison, include human judgments on an independently selected sample, preserve error categories such as missing negation or term mistranslation, and avoid training/test leakage.

**Sources:** Papineni et al., *BLEU* (ACL 2002); Matt Post, *A Call for Clarity in Reporting BLEU Scores* (WMT 2018). Only source metadata and scoped explanations are retained; no original paper bytes were mirrored.
