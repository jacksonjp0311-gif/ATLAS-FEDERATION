# Investigation 33 — A cheap segment substitution is not historical evidence

**Origin:** authored input segments [p,a,t] and [f,a,t]. The caller declares substitution p→f cost .25 and every other substitution cost 1, while insertion/deletion each cost 1. Dynamic programming returns minimum .25 with a matching alignment witness. An ordinary unweighted Levenshtein distance would return 1.

Changing the cost table changes the result. The score may be useful for prioritizing candidate correspondences but does not prove phonetic similarity, relatedness or a historical sound change. A scientific investigation needs multiple reliable lexical items, validated transcriptions, a documented comparison model and alternatives including loanwords and chance resemblance.

The test includes an exact witness-cost check. **No authentic wordlist or cognate adjudication was loaded.**
