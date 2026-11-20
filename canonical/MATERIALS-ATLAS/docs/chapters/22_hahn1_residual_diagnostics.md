# 22. Hahn1 copper: what a certified numerical fit does and does not establish

**Status:** descriptive reanalysis of the existing NIST Hahn1 local checked transcription. No new physical measurement or original upstream transport-byte acquisition is claimed.

## Separate the three evidence layers

**Layer 1 — source-reported observations.** NIST publishes 236 temperature/response pairs for the Hahn1 copper thermal-expansion benchmark. The Atlas stores the numeric values in original published order as a checked transcription. The predictor temperature is in kelvin; the numerical response scale remains unresolved in our inspected material. A local SHA-256 identifies our transcription, not the original upstream bytes.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

**Layer 3 — physical validity and prediction.** To use the fit to predict expansion in a real specimen, we would need to establish response units, reference specimen and processing conditions, the model's physical applicability, measurement uncertainty, calibration, and temperature range. The Atlas does not infer any of these from the fact that a residual sum of squares matches.

## Why bin the residuals?

The v0.3 calculator sorts the 236 observations by temperature and partitions them into a declared number of equal-count groups (2–20). It reports each bin's temperature span, count, mean residual and root-mean-square residual, along with the overall residual mean and RSS. Binning can expose a temperature-dependent bias that a single RSS conceals, but it depends on the chosen number of bins and can hide patterns. It is a descriptive visualization in numeric form, not a hypothesis test or independent holdout evaluation.

The tool also reports a correlation between adjacent residuals **after temperature sorting**. This is *not* a time-series autocorrelation because sorted temperature order does not represent acquisition time. The distinction is critical: calling a temperature-neighbor statistic evidence of instrument drift would overstate what the available metadata support.

## Limits and useful follow-up

We do not claim a new fitted parameter set, an independent temperature sweep, an error model for the physical experiment, or a validated extrapolation. The publisher data are an in-sample benchmark. A defensible next study would obtain the original upstream data bytes and source metadata, resolve response units, predeclare an out-of-sample or independent-specimen comparison, and quantify uncertainty from measurement and model inadequacy. This domain can provide an analysis checklist and computational reference while marking those steps open.

**Sources:** NIST e-Handbook copper Hahn1 example: https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd641.htm ; NIST StRD certified values: https://www.itl.nist.gov/div898/strd/nls/data/LINKS/v-hahn1.shtml ; NIST model diagnostics: https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd644.htm . The cited pages are publisher material; the Atlas calculation is original reanalysis.
