# A common offset does not average away

**Record:** `shared-offset-average` · **Type:** equation · **Origin:** formal_derivation

With an uncertain common offset independent of independent reading noise, averaging reduces the noise contribution but leaves the offset variance.

## Declared relation

```text
Var(mean) = u_b**2 + sigma**2/n
```

## Source and inspected portion

[Law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) · A.3; local model x_i=mu+b+epsilon_i

## Assumptions

- Var(b)=u_b^2; Var(epsilon_i)=sigma^2; all stated independence conditions hold.

## Limitations

- This is a model identity, not a diagnosis of a particular sensor.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
