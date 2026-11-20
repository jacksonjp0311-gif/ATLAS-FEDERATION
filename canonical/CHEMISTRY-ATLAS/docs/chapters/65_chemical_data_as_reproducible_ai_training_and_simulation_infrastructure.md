# 65. Chemical data as reproducible AI training and simulation infrastructure

**Theme:** Scientific data infrastructure · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

An AI system can use chemistry knowledge only if its records retain units, provenance, physical state, uncertainty, rights and distinct train/test partitions. A chemical database may contain thermochemistry, spectra, structures, materials simulations and reaction kinetics from different experiments. Conflating measured and calculated properties creates false validation. The NIST Chemistry WebBook documents compiled experimental quantities under identifiable sources, while computational materials repositories often provide theory-dependent predicted structures. A source URL alone does not archive raw source bytes; a checksum on a model-generated table does not authenticate its publisher.

## Governing relationship and dimensional conventions

`Knowledge record = (identity, property, numerical value, unit, T, p, phase, method, uncertainty, source edition, original-byte SHA, rights, dataset split, transformations, review status).`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

A reproducible ingestion protocol first records the authentic original transport file when legally permitted, preserving the source's exact hash. Derived tables are separate artifacts with explicit parsing and normalization code. Rejected or unknown observations remain unknown, not false. Training/test splits must account for polymorphs, duplicated experiments, source overlap and leakage across equivalent materials records. Physical tests and independent human reviews are distinct evidence layers, never inferred from a successful model execution.

## Original worked investigation

Create a fully invented materials property row with formula X2Y3, temperature 300 K, solid phase, energy gap 1.5 eV and source status “synthetic.” Record the lack of a publisher original and uncertainty. Query the record and inspect whether a consumer can distinguish it from experimental silicon data. Do not train a real materials model or imply the synthetic number is authentic.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

The reference intentionally contains no authenticated NIST spectra or Materials Project datasets and no statistically valid held-out chemistry predictor. Author-supplied training data cannot substantiate a discovery.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [NIST Chemistry WebBook — database thermochemistry user guide](https://webbook.nist.gov/chemistry/guide/)
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api)
- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
