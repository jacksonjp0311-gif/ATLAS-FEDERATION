# A zero derivative can hide nonlinear uncertainty

**Record:** `linearization-counterexample` · **Type:** equation · **Origin:** formal_derivation

For equally likely X=-1,0,1 and Y=X squared, the derivative at the input mean is zero, but exact enumeration gives output mean 2/3 and variance 2/9.

## Declared relation

```text
E[X]=0; f(E[X])=0; E[X**2]=2/3; Var(X**2)=2/9
```

## Source and inspected portion

[Law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) · A.3 first-order limit; local three-point counterexample

## Assumptions

- The three-point distribution and nonlinear function are declared synthetic mathematics.

## Limitations

- This counterexample disproves universal adequacy of first-order propagation; it does not diagnose every nonlinear model.

Assistant source-portion inspection or explicit local derivation; no independent scientific review or physical replication.
