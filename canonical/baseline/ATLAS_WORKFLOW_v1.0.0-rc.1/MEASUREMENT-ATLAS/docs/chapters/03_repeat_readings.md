# Repeat readings and shared effects

[Reference index](../REFERENCE_GUIDE.md) · Content edition 0.5.0


## Design before averaging

Repeatability holds a stated procedure, operator, system and setting fixed over a short interval. Reproducibility deliberately changes specified conditions and reports those changes. [VREP: 2.20](https://jcgm.bipm.org/vim/en/2.20.html) [VREPRO: 2.24](https://jcgm.bipm.org/vim/en/2.24.html)

The existing Type A mean routine uses the sample standard deviation divided by √n under independent, stable reading assumptions. Those conditions are supplied by the experimenter, not established by a successful function call. [TNA: A.4, equations A-4 and A-5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)

## A derived counterexample to automatic averaging gains

Let each reading be xᵢ=μ+b+εᵢ. Declare a common uncertain offset b with standard uncertainty 0.2 mm and independent reading noise εᵢ with standard deviation 0.1 mm. For four readings, direct covariance propagation gives

`Var(mean) = 0.2² + 0.1²/4 = 0.0425 mm²`.

The standard uncertainty is approximately 0.20616 mm. Treating all errors as independent would give a much smaller number and erase the common offset. Increasing the count to 100 leaves about 0.20025 mm, not 0.01 mm. This result is a direct derivation under the invented model, not sensor data.

## Proposed collection worksheet

Retain raw readings and their acquisition order, object and instrument IDs, operator, timestamps, environmental conditions, and excluded readings with reasons. Flag changes of setting or reference within a series. A time-series plot or a study design can motivate a covariance model; the present package does not automatically diagnose independence.

**Stop condition:** a correlation or shared-effect assumption materially affects the result but has no defensible basis. Report the conditional alternatives rather than selecting the smaller uncertainty.


## Exact reference records

- [Repeatability conditions](../records/repeatability-conditions.md)
- [Reproducibility conditions](../records/reproducibility-conditions.md)
- [Uncertainty of a repeated-reading mean](../records/type-a-mean.md)
- [Variance of a mean with correlated inputs](../records/correlated-mean.md)
- [A common offset does not average away](../records/shared-offset-average.md)
