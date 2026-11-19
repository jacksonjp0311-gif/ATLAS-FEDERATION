# Published numerical values do not always agree

**Case:** NIST Pontius load-cell calibration · Checked 12 November 2026

The same published observations were fitted with an independent implementation using centered/scaled Decimal arithmetic. The initial comparison used handbook displays with half-last-digit tolerances. Six comparisons exceeded those tolerances. Those original targets and failures remain in the package; none was relaxed to make a test pass.

A subsequent check used NIST StRD certified numerical regression statistics, which state a multiple-precision calculation rounded to fifteen significant digits. All 11 checked StRD quantities match within half of the last displayed decimal unit (or exactly for residual degrees of freedom). This second source was selected after observing the first disagreement: it is transparent verification, not a blinded study.

## Comparisons exceeding handbook display rounding

| Model | Quantity | Handbook | Recomputed | Original absolute tolerance |
|---|---|---:|---:|---:|
| linear | beta_0 | 0.00614969 | 0.00614968421052632 | 5e-09 |
| linear | residual_sd | 0.0021712694 | 0.00217127259605675 | 5e-11 |
| linear | lack_of_fit_F | 214.7464 | 214.746923653909 | 5e-05 |
| quadratic | beta_0 | 0.000673618 | 0.000673565789473684 | 5e-10 |
| quadratic | beta_2 | -3.16081e-15 | -3.16081871345029e-15 | 5e-21 |
| quadratic | residual_sd | 0.0002051768 | 0.000205177424076185 | 5e-11 |

## Interpretation

The differences are small and do not reverse the qualitative lesson that a quadratic describes this case better than a straight line under its assumptions. Their cause has not been established. Do not attribute them to a specific software bug, transcription change or author error without additional evidence.

Two separate Atlas claim records retain the handbook and certified intercepts, connected by a `contradicts` relation. The existing context assembler therefore carries the conflict and source closure together. No retrieval-engine change was made.

Sources: [handbook linear fit](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd613.htm), [handbook quadratic fit](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd617.htm), [StRD certified values](https://www.itl.nist.gov/div898/strd/lls/data/LINKS/v-Pontius.shtml), [certification method](https://www.itl.nist.gov/div898/strd/lls/data/LINKS/c-Pontius.shtml).

This is a source-consistency finding and reproducible numerical check, not a new physical law, laboratory certificate or independent physical replication.
