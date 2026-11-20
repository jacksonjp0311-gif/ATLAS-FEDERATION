# Chapter 20: Inspection guard bands and conditional false acceptance

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`P(accept | actual x)=Φ((USL−g−x)/σ)−Φ((LSL+g−x)/σ)`

## Scientific derivation and engineering reasoning

A tolerance limit is a condition on the actual measurand; a measuring instrument returns an uncertain observation. If accepting every reading inside [LSL,USL] creates unacceptable risks near the boundaries, a decision rule may require readings in a narrower interval [LSL+g,USL−g]. Under a synthetic zero-bias Gaussian instrument-error model with known σ, a specific true part value x has a calculable probability of producing an accepted reading.

That conditional probability is **not** P(true conforming | observed reading), which would require a prior distribution of true part values and a calibrated likelihood. Confusing the two is a serious inferential error. The user must provide an explicit decision rule, expanded or standard uncertainty convention, and treatment of asymmetry, drift and calibration bias.

Constructed case: true x=0, specification ±1, sigma=1, g=0 gives acceptance probability 0.682689492. Increasing guard band lowers that conditional probability. For a truly nonconforming item x=1.5 and sigma=.2, compute a finite false-accept chance even though the nominal part lies outside specification; the result is illustrative and not a manufacturing acceptance certificate.

Actual decision rules require measured uncertainties, a reference instrument, calibration, process distribution, product risk requirements and a documented rejection/indeterminate category.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.normal_inspection_acceptance_risk`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

This probability presumes Gaussian unbiased errors and a specified actual value; no observed error distribution is supplied.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
