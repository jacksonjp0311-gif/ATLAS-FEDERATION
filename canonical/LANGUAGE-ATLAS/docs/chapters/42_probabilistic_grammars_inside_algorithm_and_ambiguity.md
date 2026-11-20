# 42. Probabilistic grammars and the difference between likelihood and truth

A context-free grammar lists derivational possibilities. A probabilistic context-free grammar (PCFG) assigns a probability to each production, usually normalized over alternative productions with the same left-hand nonterminal. The grammar defines a generative distribution over derivations, not a universal statement about what speakers may say. A sentence may have multiple derivations with the same surface words, making ambiguity integral to the task.

## Inside recurrence

For a strict Chomsky-normal-form grammar with lexical A→word and binary A→B C productions, let `I(A,i,j)` be the total probability of A deriving token span [i,j). For a one-token span, I sums lexical rule weights with that token. For longer spans, `I(A,i,j)=Σ_{A→B C} p(A→B C)Σ_{k=i+1}^{j−1}I(B,i,k)I(C,k,j)`. Summing over rule choices and split locations preserves multiple parses rather than arbitrarily choosing one. The Viterbi recurrence instead replaces sums over alternatives with a maximum and returns one highest-probability derivation witness.

An unsmoothed parser can underflow in floating point when multiplying very many small probabilities. Production probability estimates from sparse corpora can be biased, and grammar coverage may be poor for idioms, non-concatenative morphology and spontaneous speech. The present `pcfg_inside` restricts inputs to small bounded CNF grammars and valid normalized rule distributions; it does not fit parameters or parse arbitrary human language.

## Constructed demonstration

Create lexical rules N→birds and V→sing, each probability 1, and S→N V probability 1. The two-token sentence has inside probability 1 under this tiny grammar. Replace `sing` with an unlisted token: the probability becomes 0 under the supplied grammar. This means **unlicensed by the grammar**, not that the natural-language sentence is inherently ungrammatical. Add two alternative S derivations to the same surface; the inside probability sums both, while the best derivation retains only the maximum. A model that reports only the best tree loses the ambiguity mass.

## Reconstruct by hand

List all rules and probabilities grouped by left-hand category, confirm row sums, build the triangle of spans of length 1 through n, enumerate every split, and compare inside and Viterbi values. In a multilingual corpus, evaluate grammar coverage and held-out likelihood separately from syntactic adequacy, and inspect examples where alternative analyses remain linguistically reasonable.

**Sources:** Chomsky (1956) on formal grammar classes; Jurafsky and Martin's online language-processing draft for probabilistic grammars. Publisher texts are linked, not copied.
