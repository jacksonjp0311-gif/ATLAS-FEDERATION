# Pontius inverse interval replay

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## Model and source

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

The [NIST example](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd61a.htm) describes a single-use interval. Physical units remain unspecified source load units. Original upstream bytes remain unavailable, even after two download attempts in this checkpoint.

## Fixed comparison

Targets and half-integer tolerance were written before the first local interval computation. This is an authored prospective numerical check, not a blind or independently authored evaluation. The target digest is `c90495800126a1a524b0dbf5b30c4d363214f660bc71969ec9a43bd17eedca9c`.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

The estimate and lower endpoint match within that tolerance; the upper endpoint does not. The cause is unestablished. This report does not assign it to publisher error, a particular rounding rule, data changes or software defects. The comparison remains `computed_with_publisher_discrepancies`.

## Separate numerical algorithm

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

This comparison reduces the chance of a shared implementation mistake but is not independent human review. It also cannot establish the physical validity of the statistical assumptions.

## Preserve the evidence

The publisher upper bound and recomputed upper bound are separate common-contract records joined by `contradicts`. The unchanged context assembler can retain them together. Old source records, thresholds and case bytes remain intact; the new target file is separately hashed.

```powershell
py -3 -m measurement_atlas inverse-interval
```

The command exits successfully when the computation succeeds, while its JSON explicitly reports publisher disagreement. Success of the program is not success of every scientific comparison. See [v0.6 source discrepancies](SOURCE_DISCREPANCIES.md) and [method assumptions](COVERAGE_METHODS.md).
