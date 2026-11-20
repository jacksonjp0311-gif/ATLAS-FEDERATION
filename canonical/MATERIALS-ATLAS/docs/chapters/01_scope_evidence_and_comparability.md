# Chapter 01. Scope, evidence, and comparability

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A materials question must begin with an *object* and an *operating context*: material identity, composition, phase distribution, processing history, specimen preparation, environment, stress path, time, and measurement method. A question such as “What is the tensile strength of steel?” suppresses alloy, temper, heat treatment, orientation, temperature, specimen size, rate, and whether strength refers to yield or maximum engineering stress. The Atlas refuses to turn a property label into a universal constant.

Data sources are not interchangeable. An **observed experimental result** refers to a specific specimen and instrument at a date, subject to calibration and measurement uncertainty. A **simulation output** follows a model, software build, parameterization and boundary conditions. A **database value** may be processed, averaged, fitted, or post-corrected and can change between database releases. An **editorial explanation** states an inference or principle with an explicit source and scope. No category is automatically elevated by search popularity.

The minimum evidence packet is: named target quantity with units; specimen or model identity; method identifier; method revision; temperature/pressure/humidity where applicable; orientation; preparation history; raw versus processed value; uncertainty model; origin, source locator and rights. A claim without one of these may be useful background but cannot silently be used to approve a component.

**Decision rule.** Compare two entries numerically only if all required context fields are compatible. A graph with scattered points is not an experimental replication. A material datasheet is not proof of the exact performance of every product lot. NIST’s mechanical-testing data-management work emphasizes machine configuration, test history and provenance, while the materials repository warns that contributed records may not be critically reviewed.

**Failure mode:** assigning a predicted crystal modulus to a machined, textured, porous, heat-treated part without orientation or porosity mapping. **Transfer:** use Measurement Atlas to specify uncertainty and traceability, and Causal Atlas to separate effects of composition from processing changes.

## Reference capsules for this chapter

- **Evidence type determines permissible inference** (concept): Measured specimen data, computed model output, metadata indexing and author commentary have different provenance. Store origin, methods and missing conditions before numerical comparison.
- **Property conditions are part of the reported value** (concept): Temperature, loading orientation, rate, processing and sample state qualify a material property. A context-free scalar does not define a trustworthy component specification.
- **Repository visibility is not a reproduction license** (concept): Linked third-party data may carry provider-specific rights. The node stores identifiers and bounded paraphrase rather than mirroring unrestricted amounts of externally authored records.

## Publisher portions used

[NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system) · [NIST-REPO](https://materialsdata.nist.gov/) · [NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
