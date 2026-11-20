# 23. Model status ledger, falsification, and AI-ready evidence closure

Each calculator in this edition has an explicit model and evidence status. A reproducible mathematical calculation is not a calibrated materials property. A phase-boundary calculation with user-selected interaction energy does not prove an alloy phase diagram; indexed powder peaks do not identify a crystal; temperature-binned residuals of a certified fit do not establish model applicability. A response from any model is usable in an engineering decision only with its assumptions and excluded mechanisms attached.

## Reusable verification procedure

1. **Declare the question**: material and specimen, property or microstructure, environment, temperature, composition and unit basis. If these cannot be specified, answer with scope limitations rather than a spurious scalar.
2. **Identify source type**: experimental observation, publisher certified numerical benchmark, derived model, tabulated material property, synthetic test or editorial hypothesis. Never present an observation from a synthetic generator as a published experiment.
3. **Check physics**: conservation laws, units, state variables and whether the chosen model is valid. For phase calculations, check the Gibbs reference state and difference between local instability and global coexistence. For diffraction, confirm 2θ convention and externally known indexing. For the NIST reanalysis, distinguish response type from numerical multiplier.
4. **Verify algorithms**: use a separate numerical algorithm, adversarial inputs and explicit failure handling. A fit is not physically qualified by matching its own training RSS. Do not claim numerical cross-checking is independent human review.
5. **Expose conflicts and abstentions**: contradictory evidence, unknown sample state, absent instrument calibration and unresolved unit scale must appear in the output. Complete source closure is mandatory for a bounded context package.
6. **Preserve versions**: separate research-software version, corpus revision, schema contract, source revision and evidence maturity. Change any one independently. Do not rewrite earlier record revisions or attach a “passed” scientific gate to a model unit test.

## Readiness rule

A declared Materials content v1 would need richer empirical test cases, original data acquisition or verified publisher-byte lineage, phase equilibrium beyond the symmetric regular model, actual diffraction patterns with indexing and instrument treatment, mechanical test curves, degradation evidence, and independent review. This 0.3 edition **does not satisfy those gates**. The fixed user sequence is all thirty domain libraries first, routing and live Bitwork evaluation last, transfer after system-wide integration.

**References:** MIT OCW 3.012 lecture 19; IUCr Bragg’s law and cubic crystal system; NIST StRD Hahn1 benchmark. Source links and inspected portions are recorded separately in `evidence/source_register.json`. No new physical measurements or independent scientific review are claimed.
