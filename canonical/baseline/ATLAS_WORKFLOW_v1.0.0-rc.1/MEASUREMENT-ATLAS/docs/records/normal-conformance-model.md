# Conformance probability needs a declared distribution

**Record:** `normal-conformance-model` · **Type:** equation · **Origin:** source_reported

Conformance probability integrates a justified post-measurement distribution over the specification interval.

## Declared relation

```text
p_c = integral_[L,U] g(y | data) dy
```

## Source and inspected portion

[Measurement uncertainty in conformity assessment](https://www.bipm.org/documents/20126/2071204/JCGM_106_2012_E.pdf/fe9537d2-e7d7-e146-5abb-2649c3450b25) · §7.1–7.2, equations (4)–(6), printed p.13

## Assumptions

- The supplied distribution represents the stated state of knowledge.

## Limitations

- An uncertainty number alone is insufficient to select that distribution.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical certification.
