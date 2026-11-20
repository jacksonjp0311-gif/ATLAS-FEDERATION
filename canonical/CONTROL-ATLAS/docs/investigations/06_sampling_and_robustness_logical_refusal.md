# Investigation 06: Sampling and robustness logical refusal

**Origin:** synthetic authored model, no real equipment.

A 10 Hz sample rate fails the strict ideal sampling condition for a 5 Hz bandlimited signal. An 11 Hz sample rate passes that condition but does not prove any feedback controller stable. Likewise, hypothetical stable-gain bounds .6 and .7 multiply to .42 (<1), a sufficient *conditional* small-gain test; product above 1 is inconclusive about instability. These tools prevent replacing qualified engineering reasoning with generic green status flags.

**Source:** https://www.mathworks.com/help/signal/ug/aliasing.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
