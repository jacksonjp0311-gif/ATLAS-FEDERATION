# Chapter 18 — Materials decisions need qualified evidence, not one winning number

A property must be typed before ranking candidates. Matching units are not enough. `temperature`, `orientation`, `process condition`, `measurement method`, `specimen form`, `uncertainty`, and `evidence origin` can change the meaning of a value even when the field name is identical. Materials Atlas already refuses to compare two records if the provenance origin differs (`computed` versus `measured`), even if both report an elastic modulus in gigapascals.

The principal failure is **condition collapse**: a model picks whichever source reports the highest nominal strength, lowest computed formation energy, or most favorable handbook conductivity and silently discards limitations. These are not interchangeable ranking objectives. A correct evidence-bearing question names an application and a target condition; then the Atlas should present the supported comparison and explicitly mark unavailable data.

## The standard decision packet

1. **Question/decision:** component, service load, temperature cycle, environmental exposure, design constraints and acceptable uncertainties.
2. **Candidate identity:** grade, composition tolerance, heat treatment, forming process, porosity, grain orientation and supplier lot.
3. **Property cards:** test method, measured or predicted origin, temperature, units, direction, uncertainty type and source release.
4. **Transformations:** exact formula and declared assumptions; results of an arithmetic calculator are not new measurements.
5. **Missing information:** ability to distinguish absence of data, failed source retrieval, known disagreement, negative evidence and model inapplicability.
6. **Recommendation boundary:** a conditional shortlist is not certification. Safety or regulatory use requires the applicable tests and approvals.

For AI re-use, source references must be exact and stable; short context budgets cannot strip units, temperature ranges or source discrepancies. The Forge record schema provides such reference relationships. The routing system will be built only **after all domain libraries**, and no current test is counted as a Bitwork routing or downstream model-quality benchmark.

## Cross-domain division of labor

Measurement Atlas owns uncertainty, calibration and report conventions. Causal Atlas owns whether a process change caused a shift in properties. Materials Atlas owns the specimen and structure–property model. Control Atlas (queued) will own stabilization of process conditions. Manufacturing Atlas (queued) will own defects and equipment evidence. These links identify shared concerns; they do not assert those future nodes are built.

**Principle:** Material performance is not a scalar lookup. It is a conditional statement about an identified system at a specified state, supported by a chain of observations and models.
