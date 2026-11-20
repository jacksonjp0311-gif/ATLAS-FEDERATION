# Five reproducible synthetic causal cases

All counts, mechanisms and graphs here are original constructed examples. None is a measurement, participant dataset or independently reproduced experiment. Run `python -m causal_atlas casebook` to obtain exact fractions and explicit limits.

## 1 A better process looks worse in the aggregate

| Job group | Process | Jobs | Passing jobs | Pass rate |
|---|---|---:|---:|---:|
| Easy | Existing | 80 | 64 | 0.80 |
| Easy | New | 20 | 18 | 0.90 |
| Difficult | Existing | 20 | 4 | 0.20 |
| Difficult | New | 80 | 24 | 0.30 |

Crude existing-process rate: `(64+4)/100 = 0.68`. Crude new-process rate: `(18+24)/100 = 0.42`. The crude difference is −0.26.

Using a target with equal easy and difficult shares gives existing rate `(0.80+0.20)/2 = 0.50` and new rate `(0.90+0.30)/2 = 0.60`: difference +0.10.

The fully stipulated binary model uses `P(difficult)=1/2`, `P(new|easy)=1/5`, `P(new|difficult)=4/5`, and the four pass probabilities in the table. Exact intervention evaluation returns the same +0.10 difference. This agreement is guaranteed by the authored model and its complete specification; it is not a causal conclusion from the counts alone.

A real application must justify the recorded job categories, treatment definition, sufficient adjustment and target mix. Randomization or another defensible identification design could supply evidence that this teaching example does not contain. No sampling interval is claimed.

## 2 Selection creates association

A and B are independent fair binary variables. Select records where C is their logical OR. Before selection, `P(A=1|B=1)=1/2`. Among selected records, `P(A=1|B=0,C=1)=1`, whereas `P(A=1|B=1,C=1)=1/2`. No arrow from A to B was introduced. This is an exact property of this synthetic mechanism.

## 3 Conditioning on the pathway

In the supplied graph `A -> M -> Y`, conditioning on M blocks the chain. M is a descendant of A, so it fails this package's sufficient total-effect back-door criterion. This does not implement or adjudicate all direct-effect strategies.

## 4 Missing treatment support

Delete the existing-process row for difficult jobs but retain positive target weight for difficult jobs. Standardization refuses the input instead of inventing the missing group rate. With zero target weight the missing group is irrelevant to that newly restricted target.

## 5 An unobserved common cause

Supply `U -> A`, `U -> Y`, and `A -> Y`, but list only A and Y as observed. No observed back-door adjustment set is returned. The result is scoped to this criterion and this graph. It is not a general impossibility theorem.

## Sources and implementation

The literature links and exact inspected locators appear in SOURCE_REGISTER.md. The numerical cases are defined in `causal_atlas/cases.py` and evaluated by `causal_atlas/models.py`. Conditional outcome probabilities and do-intervention probabilities remain separate operations.


## v1 additional casebook

Seven runnable advanced cases now live under `examples/` and `causal_atlas/advanced_cases.py`: two-decision g-formula, staggered group-time comparisons, binary interventional mediation, two-unit interference, stratum transport, independent-binomial descriptive uncertainty, and an attributed historical Berkeley aggregate reanalysis. Use `python -m causal_atlas advanced-casebook` to emit all outputs. Only Berkeley uses observed historical counts; the other six are constructed numerical models. Their preconditions and unresolved causal identification remain attached to each result. See [investigations 07–13](REFERENCE_GUIDE.md#investigations) and [real data provenance](REAL_DATA_REPRODUCTION.md).
