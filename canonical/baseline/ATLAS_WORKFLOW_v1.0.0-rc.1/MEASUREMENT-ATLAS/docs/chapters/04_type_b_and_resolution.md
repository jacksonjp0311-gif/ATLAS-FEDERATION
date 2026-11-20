# Type B information and resolution models

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Describe the information, not just a divisor

Type B evaluation uses relevant non-series information such as earlier results, specifications or certificates. A bound is not a standard deviation until a distribution or other justified interpretation has been assigned. [TN4: 4.1–4.6](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty)

For the declared symmetric rectangular model with half-width a, u=a/√3. The corresponding symmetric triangular model gives a/√6. A certificate that reports expanded uncertainty U and its coverage factor k can support u=U/k within its stated interpretation. Do not assume an unstated k or replace a justified distribution with whichever gives a smaller uncertainty. [TN4: 4.2 and 4.6](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-4-type-b-evaluation-standard-uncertainty)

## Resolution is a different object

Resolution describes detectable indication changes and may vary with operating conditions. [VRES: 4.14](https://jcgm.bipm.org/vim/en/4.14.html)

**Atlas derived example:** suppose a display rounds to the nearest step q=0.02 mm and the residual rounding error is explicitly modeled as uniform over [−q/2,q/2]. Substituting a=q/2 in the rectangular formula gives u=q/√12≈0.0057735 mm. Neither the digits nor q alone establish the uniform assumption. A truncating display would require a different centering/correction model.

## Prevent double counting

For each budget entry, record the underlying effect and where its numerical estimate came from. If repeated readings already reflect the same quantization effect, blindly adding another independent resolution term may double count it. Treat that warning as a model-review question, not an automatic instruction to remove a term.

**Stop condition:** a certificate or specification does not identify whether a quoted number is a bound, standard uncertainty, expanded uncertainty, or acceptance limit.


## Exact reference records

- [Type B information sources](../records/type-b-information.md)
- [Uniform bounded uncertainty](../records/uniform-bounds.md)
- [Triangular bounded uncertainty](../records/triangular-bounds.md)
- [Convert a reported uncertainty multiplier](../records/certificate-multiplier.md)
- [Quantization uncertainty needs an explicit model](../records/quantization-assumption.md)
- [Resolution is not total uncertainty](../records/resolution-meaning.md)
