# Investigation 05 — Reanalyzing NIST Hahn1 copper thermal-expansion observations

**Data origin:** NIST reported experimental data; reproduced analysis with a local, checked text transcription. **No new physical measurements.**

NIST Hahn1 contains 236 temperature and response pairs. The observed predictor range is 14.13 to 851.61 K. Both the NIST Statistical Reference Datasets collection and the e-Handbook associate the data with a copper thermal-expansion study by Thomas Hahn; they are not independent experimental replications. The units and magnitude scale of the reported response are not established to a level sufficient for engineering length predictions in this package.

## Step-by-step protocol

1. Confirm source identity and column semantics: the handbook presentation lists coefficient versus kelvin, while the Dataplot file displays temperature then response as numeric pairs. The local normalized TSV columns are explicitly `temperature_k`, `response_as_published`.
2. Preserve row order, row count, original decimal token precision and provenance. Here the 236 rows were transcribed from a publisher text view because direct source-byte retrieval was blocked. The TSV's SHA-256 authenticates the local transcription alone.
3. Define the seven-parameter NIST model: `y=(b0+b1*T+b2*T^2+b3*T^3)/(1+b4*T+b5*T^2+b6*T^3)`.
4. Evaluate the model at the **published certified coefficients**, compute `RSS = Σ[y_i-f(T_i;b)]²` and `RSD = sqrt(RSS/(236-7))`.
5. Compare with NIST certified `RSS=1.5324382854`, `RSD=0.081803852243`, residual degrees freedom 229. Do not silently rescale the response or convert the coefficient to reciprocal kelvin.
6. Run the separate SciPy least-squares oracle with Levenberg–Marquardt and trust-region reflective numerical algorithms. It initializes near the certified coefficients and is not a global-search proof.
7. Preserve assumptions, lack of source-level uncertainty, missing original byte hash and absence of physical replication in the exported AI context.

## Numerical outcome

`python -m materials_atlas published-hahn1` calculates RSS about **1.53243828536062**, differing from the certified number by about **3.94×10⁻¹¹**, and RSD about **0.08180385224272**. The checks use predeclared absolute tolerances of 5×10⁻⁹ and pass. The separately executed SciPy fits also return the same benchmark within that tolerance.

## Interpretation

The agreement supports transcription/model consistency. It does not establish material identity, uncertainty, data rights to relicense NIST's publications, or an ability to predict expansion for another copper lot. These records must not be represented as instrument calibration or engineering material qualification. The NIST handbook shows that a visually plausible quadratic-over-quadratic rational curve can still leave patterned residuals; diagnostics and an adequate measurement model matter.

**Publisher links:** [Hahn1 data](https://itl.nist.gov/div898/handbook/datasets/HAHN1.DAT), [Handbook background](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd641.htm), [StRD certified values](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/v-hahn1.shtml), [certification method](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/c-hahn1.shtml), [quadratic-model diagnostic](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd644.htm).
