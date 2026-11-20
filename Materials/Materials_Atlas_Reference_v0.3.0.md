# Materials Atlas depth manual — v0.3.0
**Scientific reference and executable teaching methods; not material qualification.**

This edition retains every earlier chapter and investigation and adds phase miscibility, indexed diffraction uncertainty, and NIST Hahn1 residual diagnostics. The reader must distinguish source observations, calculated model predictions, and synthetic exercises.


---

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


---

# Chapter 02. Composition, bonding, and material identity

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Composition can be written as atomic fractions, mass fractions, mole ratios, elemental counts, or nominal commercial grades. These conventions must not be mixed. The formula AB2 gives a 1:2 atom count, but says nothing on its own about which crystal polymorph, defects, porosity, or heat-treatment state is present. A single chemical formula may have multiple structures and distinct properties.

Bonding families (metallic, ionic, covalent, van der Waals) help organize explanations, not compute a unique mechanical response. Processing changes grain size, precipitate state, point-defect population, texture, interfaces and residual stress without necessarily changing bulk elemental composition. Materials Project explicitly distinguishes relaxed computational structures and magnetic initializations; those conditions are part of the identity of a computational entry.

**Structure hierarchy:** elemental identity and stoichiometry; atomic coordinates and lattice; microstructure and phases; sample and surface state; component geometry; service conditions. Moving between scales requires a declared model. A value for one single crystal can differ from a polycrystal; a dry laboratory polymer test may not represent aged humid service conditions.

**Mandatory input:** name the basis when giving a composition, and preserve the raw nominal or measured field. Do not infer a grade from density or color alone. Chemical identity and safety restrictions are external to this mathematical reference.

## Reference capsules for this chapter

- **Composition is not phase identification** (concept): A stoichiometric formula specifies atom count ratios but need not identify a unique polymorph, microstructure or state. A phase claim requires structure-sensitive evidence.
- **Processing changes material state** (concept): Thermal, mechanical and chemical processing can alter phase distribution, grain size, texture and residual stress without changing nominal composition.
- **Bonding categories are explanatory not sufficient predictors** (concept): Bonding families help organize trends but do not specify elastic, thermal or electrical properties without structure, conditions and model.

## Publisher portions used

[MP-CALC](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 03. Lattices, cells, diffraction and uncertainty

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A crystal description gives a periodic lattice and basis. The unit cell is not the same thing as a grain or physical specimen. For a monatomic cubic lattice, ideal theoretical density is `rho = n M / (N_A a^3)` with a in centimeters; it requires an atom count per cell and molar mass, and assumes a perfect site occupancy. Missing atoms, multiple species, thermal expansion or porosity can invalidate direct identification with a bulk density measurement.

For first-order Bragg diffraction, `2 d sin(theta) = lambda`; published diffractograms typically show `2 theta`, not `theta`. With reflection order `n`, replace the right-hand side by `n lambda`. The relationship locates a spacing *given the indexed reflection and wavelength*. It does not tell you the identity or fraction of a phase without indexing, instrumental correction, selection rules, texture and a model of the whole pattern. The IUCr reciprocal-lattice reference explains the equivalent reflection description in reciprocal space.

**Worked logic:** a peak at full angle 44 degrees with wavelength 1.54 angstrom implies d near 2.06 angstrom for the declared first order. Changing the assumed radiation or treating full angle as theta produces different answers. A single peak cannot establish a phase ID.

**Cautions:** systematic zero shifts, specimen displacement, overlapping peaks and strain broadening are not corrected by the simple calculator. Record radiation source, wavelength and uncertainty; separate peak position from fitted lattice parameter and from claimed phase assignment.

## Reference capsules for this chapter

- **Cubic unit-cell density is conditional** (equation): Theoretical rho=n*M/(NA*a^3) for a cubic cell and stated sites. Bulk density also depends on defects, pores and multiple species.
- **Bragg spacing and 2theta** (equation): The first-order relation 2*d*sin(theta)=lambda uses theta, half the full scan angle 2theta. Peak assignment and instrumental corrections are external.
- **Reciprocal-lattice reflections** (concept): Reflection indices and diffraction geometry determine observed peaks; reciprocal-space interpretation and systematic absences matter for indexing.

## Publisher portions used

[IUCR-BRAGG](https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors) · [IUCR-RECIP](https://dictionary.iucr.org/Reciprocal_lattice)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 04. Processing, microstructure, defects

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Properties are not functions of chemistry alone. Casting, cold working, solution treatment, aging, sintering, additive processing and joining may alter phase fractions, grain size, dislocation density, residual stress or porosity. A valid property record needs the processing state. When comparing lots, distinguish processing mechanism, inspection variation and measurement variation instead of immediately concluding the alloy changed.

Defect families include vacancies, interstitials, dislocations, grain boundaries, pores and cracks. Each can influence different transport, strength and fracture behaviors. The statement “more defects cause stronger material” is not universal: some defects impede dislocations, others initiate fatigue cracks or lower load-bearing area. The relevant defect type, distribution and loading must be declared.

Microstructural measurements are *sampling procedures*. A surface section might not represent the interior. Grain-size, porosity and inclusion estimates depend on image threshold, section orientation and field-selection strategy. Preserve segmentation settings and sampling method; do not present a micrograph as an entire-volume census.

**Failure mode:** two nominally identical printed metal parts show different fatigue performance due to texture/porosity or post-processing. The Atlas can explain candidate mechanisms but cannot determine causation without designed comparisons, fractography and appropriately sampled characterization.

## Reference capsules for this chapter

- **Grain is not a unit cell** (concept): The microstructural grain is a physical region of approximate crystal orientation; a lattice cell is a mathematical periodic repeat. Sampling methods determine observed grain statistics.
- **Defect families have distinct consequences** (concept): Vacancies, dislocations, inclusions, pores and microcracks can influence transport, strength or failure differently. More defects do not universally mean stronger or weaker material.

## Publisher portions used

[NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management) · [NIST-RES](https://www.nist.gov/mgi/materials-data-resources)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 05. Phase equilibria and the lever rule

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A phase diagram represents equilibrium constraints under specified pressure, temperature and composition. Solvus, liquidus and solidus boundaries are not interchangeable. An equilibrium phase diagram does not guarantee a rapidly cooled or diffusion-limited sample has reached the predicted state. Metastability, nucleation barriers, microsegregation and finite rate introduce kinetics that this first edition does not solve.

Within a binary two-phase tie line with compositions `C_alpha` and `C_beta`, an overall composition `C0` has `f_beta=(C0-C_alpha)/(C_beta-C_alpha)` and `f_alpha=1-f_beta`. Every composition must use the *same mass- or mole-fraction basis* and tie line at the same temperature and pressure. This arithmetic is a conservation statement conditional on only the two specified phases. A third phase or incompatible bases invalidates it.

NIST’s solidification lever-rule material explicitly assumes complete diffusion in the equilibrium stepping model. It is therefore not an automatic prediction of as-cast microstructure. If measured phase fractions disagree, first inspect thermal history and tie-line source before claiming that conservation failed.

**Counterexample:** the overall composition lies outside the chosen tie endpoints, making one computed fraction negative. The calculator rejects this rather than hiding the extrapolation. Near-identical endpoints imply an unstable denominator and large sensitivity to composition uncertainty; do not rely on the fractions alone for acceptance.

## Reference capsules for this chapter

- **Equilibrium diagrams do not ensure equilibrium specimens** (concept): A phase diagram requires specified conditions and equilibrium assumptions. Thermal history and kinetics can keep actual phases away from equilibrium predictions.
- **Binary two-phase lever rule** (equation): Given two endpoints on one tie line and a composition between them, the beta fraction is (C0-Ca)/(Cb-Ca). Compositional bases must match.
- **Out-of-range tie lines must be rejected** (method): Negative phase fractions indicate incompatible inputs or extrapolation, not a physical negative amount of material. Missing phases and nonequilibrium render the model inapplicable.

## Publisher portions used

[NIST-LEVER](https://www.ctcms.nist.gov/~kattner/solidifc/lever.html) · [MP-PD](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 06. Thermodynamic models and phase stability

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A formation energy per atom subtracts compatible elemental reference energies from the total phase energy and divides by atom count. On a common energy scale, the lower convex envelope of candidate energies across composition yields a **relative 0 K stability ranking** for the *supplied competing phase set*. `E_above_hull` measures energy above that envelope. It does not determine kinetic accessibility, equilibrium at room temperature, chemical compatibility under humidity, or manufacturing cost.

The Materials Project’s formation-energy and hull documentation is explicit about zero-temperature electronic energies and about functional mixing. In particular, calculated entries from GGA, GGA+U and r2SCAN can require corrections before being placed in the same hull. The same composition’s computed energy can shift with model version, correction and database release. An uncorrected mixed-functional list is not a valid apples-to-apples competitor set.

**Toy hull:** if a binary end member has energy 0, a phase at x=0.5 has energy -0.40 eV/atom, and a candidate at x=0.3 is -0.18 eV/atom, the reference hull interpolation is -0.24; the candidate is 0.06 eV/atom above that *supplied* hull. A more favorable phase omitted from the database could lower the hull and change the result.

At finite temperature and pressure the relevant Gibbs free energy includes entropy and PV contributions. A zero-temperature electronic energy is not measured Gibbs free energy. Do not compare to a published calorimetric enthalpy without a thermodynamic conversion model, uncertainty and source harmonization. **The tool cannot claim synthesizeability.**

## Reference capsules for this chapter

- **Reference-consistent formation energy** (equation): E_f=(E_phase-sum(n_i*mu_i))/sum(n_i) in per-atom electronic-energy units, provided all references and corrections share a compatible basis.
- **Lower convex envelope of supplied phases** (method): A binary 0 K hull computes the lowest convex mixture of provided energies at composition x. Missing competing phases and corrected energy scales limit its use.
- **0 K DFT stability is not room-temperature Gibbs stability** (concept): Computed electronic energies usually omit temperature-dependent entropy and kinetic effects. Do not report 0 K energy-above-hull as a room-temperature measured equilibrium result.
- **Functional mixing requires correction consistency** (method): GGA, GGA+U and r2SCAN total energies cannot be blindly combined. The Materials Project documents compatibility and correction pipelines.
- **Database release can alter computed properties** (concept): Materials Project correction schemes and thermodynamic entries evolve. Preserve database version, calculation identifiers and correction model.

## Publisher portions used

[MP-PD](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds) · [MP-CALC](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details) · [MP-ENERGY](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability) · [MP-GLOSSARY](https://github.com/materialsproject/public-docs/blob/main/glossary-of-terms.md) · [MP-RELEASE](https://docs.materialsproject.org/changes/database-versions)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 07. Mechanical behavior and standardized testing

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Uniaxial engineering stress is force divided by initial cross-sectional area; engineering strain is extension divided by initial gauge length. One reported stress/strain pair is not enough to estimate elastic modulus, offset yield, ultimate tensile strength, fracture strain or toughness. The interpretation of yield depends on the chosen definition, strain instrumentation, rate and the observed curve.

ASTM E8/E8M’s public scope covers metallic tensile testing and stresses that machined specimens from selected regions do not necessarily represent entire components in service. The Atlas links to the publisher description but does not distribute the restricted standard or claim compliance with its complete procedure.

Separate *elastic* stiffness, *plastic* resistance, *fracture* toughness, *hardness*, *creep* response and *fatigue* life. A high hardness value is not automatically a measured strength, and an ultimate tensile stress is not a design allowable under cyclic loading. Test specimens must preserve geometry, strain rate, orientation, environment and surface treatment.

**Cross-Atlas link:** Measurement Atlas owns instrument calibration and uncertainty, while Manufacturing Atlas will own process capability and equipment diagnosis. This Materials node owns physical interpretation and applicability of the property claim; Causal Atlas owns designed comparisons when processing is changed.

## Reference capsules for this chapter

- **Engineering stress and strain from tensile geometry** (equation): Engineering sigma=F/A0 and epsilon=ΔL/L0. A single point does not establish modulus, yield, toughness or ultimate tensile strength.
- **Test coupon need not represent full component** (concept): A coupon taken from selected material may not capture local geometry, residual stress, processing gradient or in-service environment.
- **Elastic stiffness and failure strength differ** (concept): Elastic modulus is a slope within a model and strain regime; yield and ultimate strengths refer to different deformation or failure thresholds.

## Publisher portions used

[ASTM-E8](https://store.astm.org/standards/e8_e8m) · [NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 08. Thermal expansion and transport

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Thermal expansion is directional for many crystals and composites. A scalar approximation `delta_L/L = alpha delta_T` requires a defined interval and, for larger ranges, a justified temperature dependence. Two freely expanding materials with coefficients alpha_a and alpha_b differ in free thermal strain by `(alpha_a-alpha_b)delta_T`. That mismatch is not itself an interface stress: constraint, modulus, geometry and bonding determine stress.

Thermal conductivity, thermal diffusivity and heat capacity are distinct quantities. A tabulated conductivity cannot be converted to diffusivity without density and heat capacity on a compatible basis and at the same state. Electrical resistivity and conductivity are reciprocals only when units, temperature and the intended constitutive model are consistent; anisotropic behavior requires tensors.

NIST’s dimensional-metrology FAQ shows why gauge-material selection depends on expansion, thermal diffusivity, dimensional stability, wear and environmental conditions. A room-temperature expansion coefficient is not universally valid at cryogenic or elevated temperatures.

**Counterexample:** two mating components with mismatched thermal expansion can have significant free strain difference after heating but no predictable stress without an interface mechanics model. The new calculator reports strain only and refuses to invent stress or failure risk.

## Reference capsules for this chapter

- **Free thermal mismatch is not stress** (equation): A scalar free-strain mismatch equals (alpha_a-alpha_b) ΔT if expansion coefficients are constant. Actual stress requires constraint and mechanics.
- **Diffusivity, conductivity and heat capacity differ** (concept): Thermal diffusivity requires conductivity, heat capacity and density under consistent conditions. None is interchangeable without the model and units.
- **Transport can be anisotropic** (concept): Anisotropic crystals and textured parts require directional or tensor property data. Do not collapse a direction into an invariant scalar without rationale.

## Publisher portions used

[NIST-GAGE](https://emtoolbox.nist.gov/faq/faq.asp) · [NIST-RES](https://www.nist.gov/mgi/materials-data-resources)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 09. Composites, mixtures, and orientation

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A two-phase idealized axial elastic modulus can be represented by the iso-strain arithmetic mixture `E_V=v E_a+(1-v) E_b`, while an iso-stress harmonic model gives `E_R=1/(v/E_a+(1-v)/E_b)`. These provide transparent *idealized comparison models*, not certified bounds for every microstructure, nonlinear polymer or porous composite. The fiber alignment, interface, load direction and constituent anisotropy are decisive.

Volume fraction must not be silently substituted with mass fraction. Density is needed to convert the two. Units of constituent moduli must be compatible. A large difference between idealized parallel/series predictions warns that detailed microstructural information is important; it is not direct experimental error.

For polycrystals, crystallographic texture and residual stress influence directional behavior. Report the property as a scalar only if isotropy was measured or defensibly modeled. Composite failure can depend on interfaces, delamination, local buckling and damage accumulation, none of which is solved by the two-scalar mixture illustration.

**Application:** when selecting a lightweight stiff panel, keep specific stiffness, temperature, moisture aging, dimensional constraints, processing yield and testing standards separate; do not choose a winner based solely on one predicted modulus.

## Reference capsules for this chapter

- **Idealized iso-strain stiffness model** (equation): The arithmetic stiffness mixture vEa+(1-v)Eb assumes a common strain and idealized constituents, not a certified composite stiffness.
- **Idealized iso-stress stiffness model** (equation): The harmonic scalar mixture 1/(v/Ea+(1-v)/Eb) assumes common stress and idealized linear constituents.
- **Mass fraction and volume fraction are different** (concept): A mixture model using volume fractions cannot accept mass fractions without constituent density conversion.

## Publisher portions used

[NIST-RES](https://www.nist.gov/mgi/materials-data-resources) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 10. Degradation, fatigue, fracture and service

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

Corrosion, oxidation, wear, creep, fatigue and fracture evolve in time and frequently interact. Their governing exposures differ: electrochemical environment, stress cycling, time at temperature, contact pressure, surface state and defect distribution. No single “material strength” number summarizes all service-failure modes.

Fatigue observations require stress-ratio, amplitude, number of cycles, waveform, environment and censoring/runout handling. An S–N plot from one geometry may not transfer to a notched part. Fracture-toughness estimates depend on geometry, constraint and crack measurement; this reference does not implement licensed test standards.

A sample that survives 10,000 cycles is not proof of indefinite life. A failure during service does not identify a unique material root cause: part geometry, assembly preload, environment and process controls may be co-causes. NIST’s testing provenance guidance supports preserving machine changes, material history and test configuration together.

**Evidence gate:** if the intended application concerns pressure vessels, aircraft or medical devices, the Atlas must abstain from design certification and request applicable codes, independently reviewed properties and qualified engineering decisions. This starter library is educational and research-facing.

## Reference capsules for this chapter

- **Fatigue results depend on load history** (concept): Cycles, stress amplitude, stress ratio, environment, geometry, surface and censoring affect interpretation. A tensile coupon strength cannot establish fatigue life.
- **Fracture conditions differ from monotonic tension** (concept): Cracks, geometry, constraint and loading rate control fracture testing; ultimate strength is not a general fracture toughness surrogate.
- **A failed part does not identify a unique cause** (method): Combine fracture observations with manufacturing, assembly and service evidence; use a causal design to distinguish alternative explanations.

## Publisher portions used

[ASTM-E8](https://store.astm.org/standards/e8_e8m) · [NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 11. Computed versus measured, reproducibility and versioning

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A calculation can reproduce an equation yet not validate the physics that generated its input. Store the software release, pseudopotential/basis model, functional, U parameters, convergence controls, k-point strategy, structure file, correction scheme, units and computational energy normalization. For experiments, store instrument identity, standard/edition, calibration, reference specimen, raw curve, analysis script, environmental conditions and uncertainty model.

Database revision changes can alter computed results without changing the nominal material identifier. Avoid treating a value obtained in one Materials Project release as equivalent to another without checking the correction and thermodynamic reference. The publication itself explains that compatibility across mixed functionals requires correction schemes.

The NIST materials repository notes that contributed information may not be critically reviewed. Availability and indexing are not source validation. The Atlas records original source URLs but does not mirror third-party datasets without verified rights. If raw files are absent, record that limitation explicitly. Favor stable persistent identifiers where available.

**Data comparison guard:** before computing a numerical difference, check property, method, units, temperature, direction, sample condition and origin. Contradictory values may be condition-specific rather than truly contradictory. The comparison utility uses equality of a fixed metadata list and still does not calculate significance without a covariance and coverage model.

## Reference capsules for this chapter

- **Computed entries need a reproducible pipeline** (method): Record functional, code release, structure, magnetic initialization, convergence, reference energies, and corrections.
- **Measurements need sample and machine histories** (method): Record raw curve, sample processing, geometry, machine configuration, calibration, environment and data reduction code.
- **Metadata equality precedes property subtraction** (method): Compare only quantities with compatible property, units, method, state, temperature and orientation; even then statistical inference requires joint uncertainty.
- **Data availability is not quality certification** (concept): A public repository entry is not necessarily critically reviewed; provider rights and provenance must be checked separately.

## Publisher portions used

[MP-CALC](https://docs.materialsproject.org/methodology/materials-methodology/calculation-details) · [MP-ENERGY](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability) · [MP-RELEASE](https://docs.materialsproject.org/changes/database-versions) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system) · [NIST-REPO](https://materialsdata.nist.gov/)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 12. Decision ledger and cross-domain reuse

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A materials selection decision needs a target environment, design constraints, hazard context, availability, cost assumptions, validated property distribution and alternative candidates. A bounded Atlas reference can support this reasoning but cannot replace qualification testing. Define a decision before retrieving attractive data: What failure mode matters? Which property controls it? Which state and test are representative? What would change the result?

Treat knowledge as a versioned network of *claims with support and limits*, not a flat database of numbers. Phase stability depends on reference energies and assumed conditions; diffraction spacing depends on wavelength and reflection indexing; tensile stress depends on specimen geometry. The context compiler must keep those dependencies intact and refuse unsupported answers when qualifiers are missing.

Our repeated workflow is **discover → inspect → represent → reproduce → compare → qualify → reuse → revise**. The first Materials release includes no independently obtained original laboratory data, no actual phase identification, and no new external simulation. Its casebook deliberately separates invented inputs from published principles; counts of records or passing tests are not completeness metrics.

**Future scope:** CALPHAD and finite-temperature phase-field kinetics; quantitative diffusion and transformation; EBSD/XRD refinement; tensor mechanics and fracture; corrosion tests; microstructural images with rights; real benchmark datasets and uncertainties. These remain explicitly open rather than silently implied by twelve chapter titles.

## Reference capsules for this chapter

- **Selection requires service constraints** (method): Define environment, loads, aging, safety class, test standards, failure modes, cost and target before using tabulated material values.
- **Measurement and causal interfaces remain distinct** (concept): Materials owns conditional physical claims, Measurement owns calibration and uncertainty, Causal owns intervention effects, Manufacturing will own equipment-specific diagnosis.
- **Unknowns should travel with material claims** (method): When processing history, test basis or physical conditions are missing, context consumers must preserve uncertainty and abstain from certification.

## Publisher portions used

[NIST-NCAL](https://www.nist.gov/programs-projects/ncal-data-management) · [NIST-MDCS](https://www.nist.gov/programs-projects/materials-data-curation-system) · [MP-GLOSSARY](https://github.com/materialsproject/public-docs/blob/main/glossary-of-terms.md)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.


---

# Chapter 13 — An experimental dataset is not its fitted equation

**Question:** What does it mean to reproduce a material-property analysis when the original experiment cannot be repeated?

This chapter adds a concrete distinction between (1) a physical specimen measurement, (2) a published observation table, (3) a numerical reconstruction of a published analysis, and (4) use of a model for a new specimen. These are different evidence levels and cannot be upgraded by increasing the number of software tests. The Materials Atlas uses NIST's 236-point Hahn1 copper thermal expansion example to show this distinction. The original NIST study is credited to Thomas Hahn (1979) and the Handbook and StRD pages describe one study, not independent measurement campaigns.

## Reproduction boundary

Our source report identifies the predictor as temperature in kelvin and the response as a coefficient of thermal expansion. NIST's displayed table does **not** assign a clear physical unit or scale to the response. The Atlas therefore stores the original numeric response with `response_scale_unresolved` and refuses to calculate a physical length change from it. In particular, the values 16–21 must not be silently relabeled `10^-6 K^-1`, even if that interpretation seems chemically plausible. Property semantics must come from a checked source, not inference.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## What remains before material qualification

Obtain verified original source bytes or independent publisher confirmation of the values, documentary response units, instrument/method metadata, uncertainty, specimen purity, grain history, and independent scientific review. NIST notes a lower-quality quadratic/quadratic rational model can produce structured residuals even when plotted data look close; model fit is not model adequacy. A new copper lot may behave differently from this experiment, and an equation calibrated only in the published range must not be extrapolated.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.


---

# Chapter 14 — Thermal properties vary with state, temperature and direction

An engineering property record requires material specification, composition, processing state, orientation, temperature, testing method, and provenance before it can support a design comparison. A single tabulated coefficient at 295 K does not establish that coefficient over 20–800 K. The NIST Neutron Research reference table provides illustrative values for selected materials **at 295 K**, including aluminum and copper density, expansion and thermal conductivity; it does not document a particular specimen in the user's possession.

## Three thermal questions that must not be conflated

1. **Coefficient at one state:** instantaneous scalar coefficient `alpha(T) = d[ln L(T)] / dT`, when this definition is appropriate. Isotropy and direction have to be stated.
2. **Free dimension change along a path:** `ln(L(T1)/L(T0)) = integral_T0^T1 alpha(T) dT`, if the material follows a reversible path represented by the same function. `materials_atlas.advanced.linear_thermal_strain_path` uses trapezoidal quadrature over strictly increasing supplied temperatures. Its input MUST be in reciprocal kelvin; it will not infer units.
3. **Interfacial stress and failure:** free mismatch `Delta epsilon = (alpha_A - alpha_B) Delta T` is not stress. Constraint, spatial temperature gradients, plasticity, creep, adhesive state, transient heat transfer and geometry govern the resulting stresses. No joint safety decision follows from a scalar mismatch alone.

Temperature-dependent α curves can be affected by phase transformation, heat-treatment history, crystallographic direction and environmental factors. In crystalline anisotropic materials α is a tensor; using an average can be poor for an oriented single crystal. In polymers, glasses and composites, time and relaxation history often matter. Reversible small-strain integration also fails if heating triggers irreversible changes.

## Model demonstration, not measured property

With a synthetic coefficient grid of `[18,20,22]×10^-6 K^-1` at `[300,350,400] K`, trapezoidal integration returns log length change 0.002 and the length ratio `exp(0.002)`, approximately 1.002002. A shortcut multiplying α(300 K) by 100 K returns 0.0018, a different estimate even within the same constructed model. Neither result validates that any actual alloy has those coefficients.

**Re-use rule:** A measured curve, a handbook table and a DFT-computed property cannot be put into one comparison without declaring their different reference states and uncertainty. The optional NIST table is a contextual reference; the Hahn1 response scale remains unresolved. Related shared nodes: Measurement Atlas for uncertainty and Control Atlas (queued) for temperature-control effects.

**Source:** NIST NCNR Reference Tables, `https://www.nist.gov/ncnr/neutron-instruments/sample-environment/sample-mounting/reference-tables`.


---

# Chapter 15 — Diffusion as a mechanism-specific, temperature-dependent process

Diffusion coefficients are not universal constants for an element. A source record must identify diffusing species, host crystal phase, direction, specimen microstructure, concentration regime and temperature. Bulk self-diffusion, grain-boundary diffusion, surface diffusion and interdiffusion can be different processes with different activation energy and prefactors.

## Arrhenius model

For a supplied regime, `D(T) = D0 exp[-Q/(R T)]`, with D0 in m²/s, Q in J/mol, R in J/(mol·K) and T in K. Holding D0 and Q fixed, a higher T implies higher D for Q positive. Arrhenius behavior can fail across phase changes, trap saturation, changing defect mechanisms, mixed pathways or non-ideal concentration dependence. Do not extrapolate one high-temperature experimental segment to all service temperatures.

The `arrhenius_diffusivity` utility checks positive D0/T and nonnegative Q and returns D at a temperature for which **the caller must independently establish the parameter regime**. It neither fits parameters nor measures diffusion. For a stipulated one-dimensional homogeneous Gaussian random walk, the root-mean-square displacement is `sqrt(2 D t)`; this is a displacement scale, not an exact penetration front. Boundary conditions and chemical reaction can invalidate the simplifying model.

## Distinguish activation from proof of mechanism

An Arrhenius line fitted through only two temperature values does not uniquely identify the mechanism. If the intercept and slope are measured, repeatability, uncertainties in both axes, temperature calibration and sample state affect interpretation. An apparent activation energy may mix different kinetic paths. A diffusion-length result also does not tell whether interface bonding, corrosion or material failure occurred.

Our teaching calculation uses `D0=1e-5 m²/s`, `Q=100000 J/mol`, `T=850 K` as expressly synthetic parameters; no matching real alloy is asserted. A separate 3600-second demonstration with specified `D=1e-12 m²/s` returns a one-dimensional RMS displacement near 85 micrometers. The two examples are intentionally not combined into a material-specific claim.

## Evidence packet for a future real study

Require species/host/phase, concentration profile and method, temperature time series, specimen history, surface condition, grain size and orientation, calibration records, raw measurements, fit residuals, analysis code, confidence intervals, source locator and a warning for any model extrapolation. Link to Materials and Measurement records for shared uncertainty definitions.

**Source:** NIST materials data resources, which distinguishes experimental and computational diffusion repositories, `https://www.nist.gov/mgi/materials-data-resources`, and NIST reported kinetics study summaries describing Arrhenius behavior on their own narrow experimental ranges.


---

# Chapter 16 — One stress–strain point does not describe a material's tensile response

Tensile reporting is a chain of measurements and definitions, not one number. The force measurement needs calibration, initial cross-sectional area needs measured dimensions, displacement/strain requires gauge length and a validated extensometer, and a complete result depends on the test procedure, specimen orientation, temperature and strain rate. ASTM E8/E8M-25 identifies yield behavior, tensile strength, elongation and reduction of area as reportable outcomes and warns that machined specimens may not represent an entire finished product. This Atlas does not reproduce or claim conformance with the paywalled standard.

Engineering stress is `F/A0`, while engineering strain is `Delta L/L0`. The `engineering_tensile_point` method provides these arithmetic quantities for one supplied point, without identifying modulus, yield, ultimate tensile strength or failure. A complete stress–strain curve requires a sufficiently resolved trace from which properties can be calculated by a predeclared procedure. `E` is a slope in a justified elastic region; it is not a fit to arbitrary high-strain points. A 0.2% offset yield crossing requires an appropriately established elastic line and sampling across the intersection.

Under *uniform deformation and approximately constant volume before necking*, one often uses `sigma_true = sigma_engineering (1 + e)` and `epsilon_true = ln(1 + e)`. Our calculator explicitly requires the caller to affirm that restriction. Once local necking begins, the local true stress depends on the actual local cross-sectional area and more complex correction; blindly continuing the conversion is unjustified. This is a transformation of definitions and assumptions, not new material data.

## Example

For synthetic engineering stress 400 MPa and engineering strain 0.05 in a declared pre-necking state, the calculator yields 420 MPa true stress and `ln(1.05)` ≈ 0.048790 true strain. It does not infer yield, strength of another specimen, or ductility. If the uniform-deformation premise is omitted or false, it refuses the conversion rather than returning a plausible but ungrounded number.

A useful AI context packet includes original force–displacement, corrected specimen dimensions, strain instrumentation, measurement rates, calibration/uncertainty, specimen direction, fracture location and repeatability across specimens. Any available curve needs acceptance by the person responsible for the actual standard's requirements; calculator tests do not qualify a product.

**Source:** ASTM International E8/E8M-25, publicly accessible scope and limitations, `https://store.astm.org/standards/e8_e8m`.


---

# Chapter 17 — Fracture intensity, crack growth, and why a rate is not lifetime

Linear-elastic mode-I stress intensity can be represented as `K_I = Y sigma sqrt(pi a)` where Y is a dimensionless factor for a **particular** geometry and crack-length convention, `sigma` is a nominal tensile stress and `a` is the crack parameter used by Y. `materials_atlas.advanced.fracture_mode_i` returns MPa·sqrt(m) from MPa and m. It explicitly does not infer the geometry factor from a component photo, identify an actual crack length, or guarantee a small-scale-yielding region.

Fracture toughness `K_IC` is not interchangeable with any measured `K` number. Valid plane-strain toughness determinations require standard-specific sample dimensions, crack preparation and test conditions. A toy inequality `K_I >= K_IC` is insufficient to declare component failure: plasticity, geometry correction, defects, loading rate, mixed mode, temperature, residual stress and uncertainty matter. Likewise, threshold comparisons below `K_IC` do not prove indefinite safety.

In an empirically identified intermediate fatigue regime the Paris relation may be written `da/dN = C (Delta K)^m`. The coefficient C's units **depend on m and the chosen length units**; the exponent and coefficient must be fitted to matching material, environment, load ratio and regime. The implemented `paris_fatigue_rate` calculates a rate only when ΔK is inside the supplied valid interval. It refuses values outside that domain. No integration across unknown geometry, changing load histories, thresholds or rapid-fracture regime occurs.

## Failure-mode example

With synthetic `sigma=200 MPa`, `a=1 mm`, and supplied `Y=1`, K_I ≈11.21 MPa·sqrt(m). It is a bounded stress-intensity calculation, not crack growth or failure probability. A second synthetic law with `C=10^-7` (mm/cycle)/(MPa·sqrt(m))³, `m=3`, ΔK=10 yields `10^-4 mm/cycle` but only within the declared 5..20 MPa·sqrt(m) range. Calculating an end-of-life cycle count from that single rate without propagation of changing ΔK would be scientifically misleading.

## What a real damage investigation needs

Quantified crack geometry/orientation, nondestructive inspection uncertainty, local stress range and residual stress, actual fatigue loading and R ratio, environment/corrosion, fracture-surface evidence, metallurgical processing and heat treatment, validated material toughness and crack-growth data, component-specific design procedures, and independent approval. Absence of these inputs should lead to a refusal or a request for measurements rather than a fabricated safety margin.

**Source boundary:** These are standard analytical definitions and authored examples. The restricted contents of fracture and fatigue standards are not reproduced. The present edition has no measured crack-growth dataset or experimentally reviewed component model.


---

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


---

# Chapter 19 — What remains unverified and how to proceed without inventing results

Materials Atlas is growing through depth and reproducibility, not through a claim to have captured all human materials science. This release adds one authentic published observation transcription and corresponding numerical check plus bounded models for transport and mechanical stress. It does NOT resolve experimental phase diagrams, CALPHAD model uncertainty, broad computational data licensing, real tensile curve segmentation, verified crack-growth histories, anisotropic elasticity, corrosion under service conditions, standardized certification or a cross-source benchmarking system.

## Next scientific families

**Microstructure and transformations:** condition-specific particle-size distributions, diffraction peak indexing, texture and grain boundary statistics; quantitative evidence of how processing changes structure. Models must specify microscopy resolution and acquisition bias.

**Phase equilibria and kinetics:** real ternary alloy datasets with verified source terms, measured transition temperatures, corrected phase-property labels and finite-temperature Gibbs-model limitations. A lever-rule calculator is not CALPHAD and a 0 K hull is not a liquidus.

**Mechanical and fatigue:** rights-cleared full tensile curves, specimen geometry and rate records, uncertainty analysis, model selection, fracture surface/cycle loading data; fail loudly on unknown necking state, out-of-range stress intensity or missing experimental approval.

**Electrical and magnetic:** conductivity versus microstructure and temperature, magnetization and hysteresis, semiconductor carrier physics with measured versus computed uncertainties and anisotropy. These remain reference gaps rather than promised implementations.

**Corrosion, polymers, ceramics, biomaterials:** composition/process mapping, immersion/oxidation methods, aging pathways, toxicity and regulatory claims; biological safety cannot be inferred from this knowledge tool.

## Reproduction priorities

Acquire a verified NIST upstream Hahn1 byte snapshot through a permitted download channel, check units with the original publication, compare fits and residual diagnostics with publisher plots, and obtain real thermophysical tables with explicit conditions, uncertainty, and reuse rights. Preserve the checked current transcription and never replace it silently. A second-source copy of identical original measurements does not become an independent experiment.

## Release stages

Materials 0.2 is a **content-development milestone**, not independently reviewed Materials 1.0. A substantive v1 reference will require an agreed, bounded scientific scope with deeper case coverage and explicit open gaps. Platform testing and live Bitwork routing remain deferred until the user has finished building all 30 libraries. The current node and shared runtime contain no real routing evaluation.


---

# 20. A regular-solution model: miscibility, spinodal, and metastability

**Status:** original bounded derivation based on standard mean-field thermodynamics. No material-specific phase diagram has been measured or inferred. This chapter explains *what follows if* a symmetric, one-phase, constant-interaction model is stipulated. It is not a CALPHAD assessment, a DFT phase-hull calculation, or a polymer-blend parameter fit.

## The physical question and what must be known

Suppose a binary mixture has overall mole fraction of component B equal to x and temperature T. We want to distinguish a stable homogeneous phase, a metastable homogeneous state, and a locally unstable state. A composition alone cannot answer that question: we need a free-energy model, its reference state, the competing phases, and equilibrium assumptions. Here we assume a single symmetric substitutional solution, ideal configurational entropy, and a nonnegative constant molar interaction parameter omega. We exclude composition-dependent interactions, elastic misfit, multiple crystal structures, surfaces, diffusion kinetics and nucleation barriers.

The molar Gibbs free energy of mixing relative to pure-component reference is

`Gmix(x,T) = R*T*[x*ln(x)+(1-x)*ln(1-x)] + omega*x*(1-x)`.

Here `R=8.31446261815324 J mol^-1 K^-1`, `T>0 K`, `omega>=0 J/mol`, and `0<x<1` is dimensionless. This is a model function, not a measured free energy. The entropy term favors mixing; positive omega penalizes unlike neighbors. Its derivatives at fixed T are

`G' = R*T*ln(x/(1-x)) + omega*(1-2*x)`

`G'' = R*T/[x*(1-x)] - 2*omega`.

An implementation must not silently evaluate the logarithms at x=0 or 1. Their limiting values exist for G, but the derivatives are singular there. Our calculator explicitly refuses endpoints.

## Three boundaries are not interchangeable

The *critical temperature* for the stipulated symmetric model is `Tc=omega/(2R)` for omega>0. Above or at Tc the mean-field model has no two-phase miscibility gap. Below Tc the free-energy curve has two equivalent minima at compositions `x_b` and `1-x_b`. In this special symmetric model the common tangent is horizontal; the lower binodal composition solves the **noncentral** root of `G'(x_b)=0`. A naive root solver can return the ever-present stationary point x=0.5 instead of the binodal. The Atlas brackets the lower root strictly below the lower spinodal and refuses numerically unresolvable low-temperature limits.

The *spinodal* is the local curvature boundary `G''=0`, with lower composition

`x_s = (1 - sqrt(1 - 2*R*T/omega))/2`.

The code evaluates this using a cancellation-resistant algebraic form near small `2RT/omega`. For `x_s < x < 1-x_s`, the homogeneous state has negative curvature and is locally unstable in this mean-field thermodynamic model. Between the lower binodal and lower spinodal, or the symmetric upper interval, curvature can be positive but the state is still **metastable** because a two-phase mixture has lower global free energy. A model that labels all positive-curvature states stable confuses local and global criteria.

The *equilibrium two-phase fractions* follow a lever rule: for binodal endpoints a and b, `f_high=(x-a)/(b-a)` and `f_low=1-f_high`. They describe equilibrium composition accounting, not nucleation rates, domain sizes or the speed of phase separation. Our code reports the homogeneous-to-equilibrium free-energy difference to expose metastability, but it does not model microstructure formation.

## How to audit a computed phase boundary

A reproducible check should: declare omega, T and x; verify omega and T units; confirm that the noncentral binodal lies outside the spinodal; evaluate the free-energy curvature at x; confirm mass conservation in the lever fractions; compare homogeneous and phase-separated energies; and retain all model exclusions. For numerical confidence, a separate algorithm can minimize the Gibbs energy directly and compare its minimum with the derivative-root implementation. These checks validate the calculation under the chosen model; they cannot tell us whether the chosen omega represents any real alloy or polymer.

## What can go wrong

If omega depends on T, if additional phases are stable, or if the material is strongly nonideal, this model may be qualitatively misleading. A 0 K DFT convex hull is not the same object as a finite-T Gibbs free-energy common-tangent construction. If the material is not at equilibrium, a spinodal may predict a local thermodynamic tendency without describing observable kinetics. A real study would need composition/temperature calibration, specimen processing, phase-identification evidence, uncertainty and an independently justified free-energy description.

**Sources and scope:** NIST *SANS Toolbox*, indexed section on binodal/spinodal lines (polymer-blend context, not a direct source for alloy parameters): https://www.nist.gov/system/files/documents/2023/04/14/the_sans_toolbox.pdf ; NIST lever-rule explanation: https://www.ctcms.nist.gov/~kattner/solidifc/lever.html . The particular constant-omega symmetric equations and examples here are original pedagogical derivations; the PDF has not been reviewed in full.


---

# 21. Indexed cubic diffraction: recovering a lattice parameter without overclaiming

**Status:** bounded first-order diffraction arithmetic from supplied peak assignments. It does not identify an unknown crystal, perform Rietveld refinement, validate instrument calibration, or certify a sample.

## The measurable and the inferred quantities

A powder diffraction instrument reports intensity against a scattering angle, often denoted **2theta**. The Bragg angle theta is half that value. For first-order Bragg scattering, `lambda=2*d*sin(theta)`. For a cubic lattice whose reflection has already been indexed as (h,k,l), `d=a/sqrt(h²+k²+l²)`, so

`a=lambda*sqrt(h²+k²+l²)/(2*sin(theta))`.

The wavelength lambda and resulting lattice parameter a must use the same length unit. The Atlas accepts angstroms, degrees for 2theta, and integer h,k,l; it converts the half-angle to radians internally. It requires nonzero hkl and `0<2theta<180°`. The first-order convention does not by itself establish whether the assigned reflection is allowed by the lattice's space group.

The IUCr explains why the 1D powder pattern compresses 3D reciprocal-space information and why peak overlap and indexing ambiguity matter. An apparent set of lattice parameters from a few assigned peaks is not proof of material identity. Distinct phases can overlap; texture, microstrain, sample displacement and instrument aberrations can shift or reshape peaks. A serious phase identification needs independent structure-factor and pattern evidence.

## Multiple peaks and independent angular errors

If several independent indexed peaks produce estimates `a_i` with first-order angle standard uncertainties `u_i`, the inverse-variance estimate is `a_bar = sum(a_i/u_i²)/sum(1/u_i²)`, with angle-only standard uncertainty `1/sqrt(sum(1/u_i²))`. For one peak, the absolute first-order sensitivity to the **full** scan angle 2theta expressed in degrees is

`|da/d(2theta_deg)| = |a*cot(theta)*pi/360|`.

The factor `pi/360` includes both the degree-to-radian conversion and the halving of 2theta. Omitting either doubles or otherwise distorts the uncertainty. Our code rejects missing or zero uncertainty and repeated equivalent cubic reflection families because those inputs would need a covariance model rather than independent weights.

## A common uncertainty is not another independent observation

Every peak in one scan typically uses the same nominal wavelength. Its uncertainty is a shared component, not independent per peak. Under small-error linear propagation, `u_a,lambda = |a_bar/lambda| * u_lambda`. The combined standard uncertainty in this restricted model is `sqrt(u_a,angle² + u_a,lambda²)` when the two components are independent. Adding more peaks may reduce the random-angle contribution; it does **not** divide the common wavelength contribution by the square root of the peak count. The same logic applies to many shared calibration effects, although this implementation does not model instrument zero offset or peak-to-peak angular covariance.

The program reports `chi²=sum(((a_i-a_bar)/u_i)²)` and degrees of freedom `n-1`. A large chi-square may signal underestimated errors, bad indexing, noncubic symmetry, or unmodeled systematic effects. It is a diagnostic; the software does not silently scale the uncertainties to force a good fit. A small chi-square is not proof that the specimen is phase-pure.

## Practical study template

Record specimen identifier, composition, processing history, scan date, radiation/wavelength and its uncertainty, temperature, peak extraction method, independently justified hkl indexing, each 2theta and uncertainty, instrument correction method, excluded peaks and reasons, covariance assumptions, fitted a and diagnostics, and all remaining uncertainty contributors. A publication-quality crystallographic refinement requires substantially more than this teaching calculator.

**Sources and scope:** IUCr *International Tables*, powder diffraction errors and aberrations: https://onlinelibrary.wiley.com/iucr/itc/Cb/ch5o2v0001/sec5o2o1o2/ ; IUCr lattice-parameter measurement introduction: https://onlinelibrary.wiley.com/iucr/itc/Cb/ch5o3v0001/sec5o3o1/ . Only selected public portions were inspected; no restricted tables or source PDF were mirrored.


---

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


---
# Worked investigations


---

# Investigation 01 — Can a single XRD peak identify a material?

**Evidence type:** Original constructed teaching scenario. No real diffractogram was obtained. Reference: [IUCr Bragg education](https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors) and [IUCr reciprocal lattice](https://dictionary.iucr.org/Reciprocal_lattice).

## Research question
A fabricated sample's nominal supplier label says “alloy A.” A technician records a prominent diffraction peak at full scattering angle `2θ=44°`, using a declared monochromatic wavelength of `1.54 Å`. What conclusion is allowed from this single measurement summary?

## Reproduction
The first-order Bragg relation gives `d = lambda/(2 sin(theta))`, where `theta=22°`, not 44°. The standalone `materials_atlas.methods.bragg_spacing` calculator reproduces approximately `2.055 Å`. This is a **conditional interplanar-spacing calculation**. The diffraction experiment, indexing, line shape and calibration are not reproduced.

## What fails
The tempting inference is that one line uniquely identifies the alloy and its phase fraction. That does not follow. Many crystals can share similar interplanar spacings; different allowed reflections may overlap. Peak intensity depends on crystallographic structure factors, preferred orientation and instrumental conditions. A broad peak could include microstrain, size effects or instrumental broadening. The reported number may also shift due to radiation mixture, zero offset and specimen displacement.

An indexed hkl plane or a reference pattern must be independently justified. The algorithm does not infer symmetry, site occupancy, composition, grain size or a sample phase fraction. Nor does it determine a real material's source or processing history.

## Better evidence package
Preserve the original raw scan; scan geometry, source and wavelength, optics and instrumental corrections; sample orientation/preparation; complete peak fitting and uncertainty; and any complementary chemical or microscopy evidence. A phase-identification claim should point to an explicit accepted procedure and competing candidate patterns. Use the Measurement Atlas for angle calibration uncertainty and source-traceable reference settings.

**Outcome:** supported — a conditional `d` calculation. Not supported — “the sample is alloy A.” For a new investigation the assistant should abstain from phase identification and list the additional evidence needed.


---

# Investigation 02 — Two different concepts of “stable”

**Evidence type:** Original fictitious binary-system model. External references: [NIST lever-rule assumptions](https://www.ctcms.nist.gov/~kattner/solidifc/lever.html) and [Materials Project phase diagram method](https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds).

## Part A: an equilibrium tie line
Suppose, at a specified but otherwise fictional equilibrium temperature and pressure, an alloy has `C0=0.40` fraction of component B, and two coexisting phases are `C_alpha=0.20` and `C_beta=0.70` on the same mass-fraction basis. Conservation gives `f_beta=(0.40-0.20)/(0.70-0.20)=0.40` and `f_alpha=0.60`. These fractions are conditional on the existence of this *two-phase equilibrium state*. The result is not a cooling curve or an experimentally measured micrograph.

If a second source provides mole fractions instead of mass fractions, the calculator is not authorized to combine them directly. If a third phase is present or rapid cooling prevents complete diffusion, the lever rule does not predict the actual as-manufactured phases.

## Part B: a computational reference hull
A separate artificial model defines electronic energies for A at xB=0 as `0 eV/atom`, AB at xB=0.5 as `−0.40 eV/atom`, and B at xB=1 as `0 eV/atom`. A hypothetical candidate at xB=0.3 is `−0.18 eV/atom`. The binary lower hull at that composition is `−0.24 eV/atom`, making its distance above the supplied hull `+0.06 eV/atom`.

This is **not** the same calculation as the finite-temperature lever rule: the hull is a relative ranking on the specified 0 K electronic-energy scale among supplied candidates. It does not tell us a furnace's equilibrium phase fraction, a material's actual Gibbs free energy at service temperature, or a sample's cooling kinetics.

## Structural counterexample
If an omitted new phase at the same composition is found with electronic energy `−0.30 eV/atom`, the previous hull is incomplete and the relative stability calculation must be recomputed. The old `+0.06` result was correct for its *input set* but not necessarily for the completed system. A candidate below a supplied hull is flagged as evidence the reference list needs expansion; it is not an impossible negative physical energy.

## Evidence and decision
A valid computational phase claim must declare model/functional, corrections and database version, structure IDs, competing-phase coverage, energy normalization and temperature. Materials Project documents corrections for mixed exchange-correlation schemes; the initial numbers in this investigation are fabricated and not its database entries. The method must not be used to certify synthesis feasibility or real equilibrium without more evidence.


---

# Investigation 03 — Why two reported strengths may not conflict

**Evidence type:** Original hypothetical mechanical-testing comparison. The quantities and specimens are invented. Reference: [ASTM E8/E8M publisher scope](https://store.astm.org/standards/e8_e8m) and [NIST mechanical data provenance](https://www.nist.gov/programs-projects/ncal-data-management).

## Initial observation
A technician reports that “batch A is stronger than batch B” because two labels read 250 and 220 MPa. Before treating these as competing estimates of the same property, the analyst needs to learn whether the values are yield strengths, ultimate tensile strengths, applied engineering stresses, or design allowable limits. The temperature, strain rate, direction, specimen location, heat treatment and method edition can differ.

The Atlas can calculate engineering stress for a fabricated point: `5000 N / 20 mm² = 250 MPa`. Paused there, the result is only **one point**. An invented extension `0.5 mm` over `50 mm` initial gauge length gives `epsilon=0.01`, but none of these inputs establishes the elastic modulus or a 0.2% offset yield. Those quantities need curves, procedures and equipment records.

## Comparison gate
If two fully typed records differ in method or origin, `compare_properties` refuses to subtract their values. A simulated modulus from a perfectly periodic ideal crystal is not automatically an experimental tensile result from an annealed polycrystal. If the methods and all selected context fields match, arithmetic subtraction is allowed, but the interface does **not** claim statistical significance: shared calibration errors and within-lot variation are not modeled.

A conservative investigator must preserve both original results, record the discrepancy's possible context explanation, and either obtain compatible tests or scope the conclusion to the exact conditions actually observed.

## Application to process changes
If a plant changed material supplier and heat treatment simultaneously, even a real observed property difference does not uniquely identify which factor caused it. The Causal Atlas is needed for experiments and confounding; Manufacturing Atlas will later capture operating conditions and equipment. The Materials Atlas supplies the physical interpretation and conditions without assuming causal identification.

**Outcome:** computed stress and strain from invented inputs; no qualified material ranking, no laboratory replication and no standard compliance.


---

# Investigation 04 — Thermal mismatch versus actual interface risk

**Evidence type:** Author-constructed thermal example. Reference: [NIST Engineering Metrology Toolbox FAQ](https://emtoolbox.nist.gov/faq/faq.asp).

Two illustrative materials have scalar thermal-expansion coefficients `23e−6 /K` and `12e−6 /K`, assumed constant over a `+60 K` change. The free strain difference is `(23−12)e−6 × 60 = 660 microstrain`. This algebra does not provide an interface stress or an engineering failure criterion. Actual constraint, bond, geometry and temperature-dependent properties are missing.

A robot housing may need thermal cycling life, oxidation protection, mechanical fatigue resistance, dimensional tolerance and assembly fit in addition to stiffness. A table of room-temperature moduli will not settle the design. The correct comparison ledger includes property origin, tested range, thermal history and load path, plus what qualification test must be run before deployment.

A materials selection answer from this first Atlas edition should therefore read: “The assumed pair has a modeled free thermal mismatch of 660 microstrain; component-level reliability cannot be determined from these inputs.” The latter statement is as essential as the numerical result.


---

# Investigation 05 — Reanalyzing NIST Hahn1 copper thermal-expansion observations

**Data origin:** NIST reported experimental data; reproduced analysis with a local, checked text transcription. **No new physical measurements.**

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## Step-by-step protocol

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## Numerical outcome

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

## Interpretation

The agreement supports transcription/model consistency. It does not establish material identity, uncertainty, data rights to relicense NIST's publications, or an ability to predict expansion for another copper lot. These records must not be represented as instrument calibration or engineering material qualification. The NIST handbook shows that a visually plausible quadratic-over-quadratic rational curve can still leave patterned residuals; diagnostics and an adequate measurement model matter.

**Publisher links:** [Hahn1 data](https://itl.nist.gov/div898/handbook/datasets/HAHN1.DAT), [Handbook background](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd641.htm), [StRD certified values](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/v-hahn1.shtml), [certification method](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/c-hahn1.shtml), [quadratic-model diagnostic](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd644.htm).


---

# Investigation 06 — Why a diffusion parameter is not a universal lifetime model

**Origin:** original constructed model, not an experiment. The question: If a metal is heated, how far can a species move within a prescribed time?

Choose a hypothetical activated diffusion process with D0=10⁻⁵ m²/s and Q=100 kJ/mol. Calculate D at 850 K by the Arrhenius relation. This is a stipulated activation energy, not an observed copper result. Substituting D in a one-dimensional RMS displacement formula requires a separate premise: that transport is constant-D Fickian and not reaction-, boundary-, or microstructure-limited.

A second illustrative case directly supplies D=10⁻¹² m²/s for one hour and computes `sqrt(2*D*3600)` ≈ 84.85 micrometers. This result must not be mistaken for a concentration penetration depth, a corrosion front or an interface failure prediction. Diffusion length generally depends on the chosen concentration threshold and boundary conditions.

**Failures to document:** unknown sample phase; unexamined grain boundaries or dislocations; temperature outside activation-regime fit; surface oxidation and moving interfaces; activation energy from the wrong transport species; repeated heating/cooling and irreversible changes; units confused as eV versus J/mol. The calculator requires J/mol and absolute kelvin.

A useful research package would retain diffusion profiles, specimen preparation, temperature calibration, concentration measurement and uncertainty, fitted and alternate transport models, residuals, material identity, and a source/version statement. The current Atlas contains only the bounded method and synthetic numbers.

**Background:** [NIST materials data resources](https://www.nist.gov/mgi/materials-data-resources).


---

# Investigation 07 — A stress-intensity number is not a service-life estimate

**Origin:** original constructed calculation. Take a hypothetical tensile stress 200 MPa, crack parameter a=0.001 m and known geometry factor Y=1. A linear-elastic mode-I model gives K_I ≈ 11.21 MPa√m. That result answers only the mathematical question under the stated crack convention; geometry factor selection, residual stress, yield behavior, and defect uncertainty are not verified.

For a separate hypothetical Paris-regime law, choose C=10⁻⁷ [mm/cycle]/[MPa√m]³, exponent 3, and ΔK=10 MPa√m in a stipulated validated 5–20 MPa√m interval. The computed growth rate is 10⁻⁴ mm/cycle. At 30 MPa√m, the calculator **refuses** the request: crossing outside the supplied empirical regime invalidates the simple equation, even though numerical exponentiation is easy.

The two toy models are intentionally **not** combined into one cycle-to-failure or safety claim. Such a claim requires variable crack geometry, actual stress cycles, crack-growth resistance, threshold behavior, large-scale plasticity limits and validation of the Paris law regime. A point rate and a point intensity cannot be equated to a certified fatigue life.

A human investigation should include metallographic inspection, geometry qualification, load spectrum, cyclic stress ratio, temperature, environment, base-metal and welded zones, residual stress, non-destructive inspection limits, standard-specific fracture testing, and reviewed uncertainties. The final AI answer should be framed as a calculation with missing prerequisites, not an engineering sign-off.


---

# Investigation 08 — Why the apparently strongest material may be an invalid comparison

**Origin:** authored decision protocol. Imagine a data sheet reporting a predicted 0 K elastic response for one ideal crystal while another reports a measured tensile modulus of a heat-treated commercial component. A simple sorting algorithm treats the two values as competing properties. Materials Atlas refuses that comparison because their evidence origin, direction, processing and temperature do not match.

Reformulate the query with (a) specified operating conditions, (b) specimen shape and orientation, (c) production process, (d) failure mode, (e) required standards, and (f) acceptable uncertainty. Request comparable measurements or validated modeling on an aligned basis. If a material record lacks the test method or source qualification, the correct action is abstention or a bounded research lead, not a fabricated maximum-service-load number.

This same discipline applies to NIST's published 295 K thermal reference table, the Hahn1 copper data whose response scale remains unresolved, and Materials Project 0 K phase stability. These are different data products; an integrated reference may link them, but should not merge them into one unqualified material-property field.

Deliverable template: source pointer, exact material identity, origin type, numerical value/unit, physical conditions, method and uncertainty, source release, missing inputs, alternative mechanisms, and conditional next measurement. Full routing and model evaluation are intentionally deferred until all thirty domains have content editions.


---

# Investigation 09 — A model with two different phase boundaries

**Question:** Can a homogeneous mixture have positive free-energy curvature and still be thermodynamically disfavored? **Origin:** original synthetic regular-solution model; no specimen, composition measurement or physical phase diagram.

Stipulate `omega=20,000 J/mol` and `R=8.31446261815324 J/(mol K)`. The model critical temperature is `Tc=omega/(2R)`, approximately 1,202.72 K. Choose `T=0.8*Tc`, or approximately 962.17 K, and evaluate `Gmix=RT[x ln x+(1-x)ln(1-x)]+omega*x(1-x)`. The binodal endpoints are the noncentral roots of the derivative, while the spinodal endpoints satisfy zero curvature. The calculator returns both rather than conflating them.

At overall `x=0.5`, the homogeneous curvature is negative, so this stipulated mean-field state is locally unstable. At a composition halfway between the lower binodal and spinodal, curvature is positive but a two-phase mixture has lower global free energy. That is the **metastable** region. The computed phase fractions sum to one and conserve x. At temperatures above Tc, the same model reports a single-phase region.

**Reproduce:** `python -m materials_atlas expanded-cases` and inspect `binodal_wider_than_spinodal`, `central_composition_unstable`, `metastable_not_stable`, and `above_critical_single_phase`. `python tools/phase_diffraction_oracle.py` compares the Atlas derivative-root result against SciPy direct minimization over 90 seeded models.

**What this does not show:** a real alloy's coexistence curve, the speed of phase separation, spinodal decomposition morphology, or any real critical temperature. A single regular-solution omega cannot substitute for experimental phase diagrams or thermodynamic assessments. NIST's discussion of binodal/spinodal in polymer blends supports the conceptual distinction, not this model's numeric parameter choice.


---

# Investigation 10 — Why four peaks do not erase a shared calibration uncertainty

**Question:** If we add more indexed diffraction peaks, which parts of the lattice-parameter uncertainty should shrink? **Origin:** original synthetic peak positions, not a copper powder measurement.

Stipulate a cubic lattice `a=3.61 angstrom`, radiation wavelength `lambda=1.5406 angstrom`, a shared wavelength standard uncertainty `u_lambda=0.0001 angstrom`, and independent `u(2theta)=0.015 degree` for each of four externally assigned reflections (111), (200), (220), and (311). Construct ideal peak angles by inverting the Bragg equation, then calculate each `a_i` and its first-order angular uncertainty. The inverse-variance weighted mean recovers 3.61 angstrom to floating-point precision because the inputs were generated from that exact model.

The combined uncertainty has **two** parts: random angle uncertainty, which may decrease with additional independent peaks, and the wavelength contribution `a_bar*u_lambda/lambda`, which is common to every peak. Treating the latter as independent and dividing it by `sqrt(n)` would understate uncertainty. The implementation retains these two components separately and reports the chi-square residual diagnostic. Because the ideal peak positions are noise-free, their chi-square is nearly zero; this is not an actual fit quality claim.

**Reproduce:** `python -m materials_atlas expanded-cases`, then `python tools/phase_diffraction_oracle.py` for 240 seeded diffraction examples checked against a separate vectorized NumPy calculation. The tool rejects missing standard uncertainties, duplicate cubic reflection families and noninteger indices. It does not automatically index an unknown pattern.

**Study requirements for real data:** a justified phase and hkl assignment, instrument/wavelength calibration, angle zero-offset and specimen displacement corrections, possible peak overlap and texture, covariance, specimen processing and measurement temperature. IUCr's powder diffraction treatment supplies the physical Bragg and cubic metric relations; the synthetic dataset supplies no material-identification evidence.


---

# Investigation 11 — A numerically certified fit can still need diagnostic review

**Question:** Does reproducing a published fit prove it is a physically reliable predictor? **Origin:** computational reanalysis of 236 source-reported NIST Hahn1 copper observations transcribed in the previous Materials release.

[SRD140_PUBLIC_WITHHELD] Unavailable in this public derivative: NIST SRD140 input, certified values and source-dependent results are withheld because redistribution permission is unresolved. Original methods and publisher references are retained where separable; historical acceptance does not apply.

This increment adds descriptive residual bins ordered by temperature, not by time. For eight bins, each contains a nearly equal number of observations; each reports its temperature range, mean residual and RMSE. We also report a temperature-neighbor residual correlation but explicitly **do not** label it temporal autocorrelation or evidence of instrument drift. A residual pattern can be a reason to investigate model inadequacy, not proof of a particular physical mechanism.

**Reproduce:** `python -m materials_atlas hahn-diagnostics` and `python tools/phase_diffraction_oracle.py`. The first uses the existing published-data capture; the second recomputes bin statistics using NumPy as a separate implementation. Both keep original upstream-byte acquisition and response-scale verification open.

**Further evidence needed:** original NIST data-file bytes, independent source audit, a justified response unit multiplier, test specimen identity, uncertainty budget and a predeclared external validation set. This is a useful benchmark for software correctness, not a new materials-science discovery.


---

# Publisher-source register (scoped review, 2026-11-12)

**No source PDFs or third-party datasets are mirrored.** Inspected portions are limited to the descriptions below. Linking does not imply independent validation.

## MP-PD: Phase diagrams and 0 K thermodynamics

- Publisher: Materials Project
- Link: https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/phase-diagrams-pds
- Reviewed portion: Formation energy per atom, convex hull construction, 0 K versus Gibbs assumptions; selected public HTML only.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## MP-CALC: Calculation details

- Publisher: Materials Project
- Link: https://docs.materialsproject.org/methodology/materials-methodology/calculation-details
- Reviewed portion: Calculation method, DFT VASP, spin and structure treatment, 0 K/0 atm modelling; public documentation.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## MP-ENERGY: Energy corrections and functional mixing

- Publisher: Materials Project
- Link: https://docs.materialsproject.org/methodology/materials-methodology/thermodynamic-stability/thermodynamic-stability
- Reviewed portion: GGA/GGA+U and r2SCAN mixing, energy corrections; selected public HTML.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## MP-GLOSSARY: Glossary of calculated material properties

- Publisher: Materials Project
- Link: https://github.com/materialsproject/public-docs/blob/main/glossary-of-terms.md
- Reviewed portion: Definitions of formation energy, hull, and conditional 0 K calculated values; public source file view.
- Type: web-source-file
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## MP-RELEASE: Database versions and release changes

- Publisher: Materials Project
- Link: https://docs.materialsproject.org/changes/database-versions
- Reviewed portion: Database changes and correction-related property revisions; selected release documentation.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## IUCR-BRAGG: Structure factors and Bragg equation

- Publisher: International Union of Crystallography
- Link: https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors
- Reviewed portion: Bragg derivation 2 d sin(theta)=n lambda; public educational webpage.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## IUCR-RECIP: Reciprocal lattice dictionary entry

- Publisher: International Union of Crystallography
- Link: https://dictionary.iucr.org/Reciprocal_lattice
- Reviewed portion: Reciprocal-lattice and reflection relations; public dictionary entry.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-LEVER: Lever rule and solidification calculation

- Publisher: National Institute of Standards and Technology
- Link: https://www.ctcms.nist.gov/~kattner/solidifc/lever.html
- Reviewed portion: Equilibrium tie-line and full-diffusion lever-rule assumptions; public explanation.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## ASTM-E8: E8/E8M-25 tension testing metallic materials

- Publisher: ASTM International
- Link: https://store.astm.org/standards/e8_e8m
- Reviewed portion: Public significance/scope excerpt; specimen representativeness limitations; no full standard access.
- Type: publisher-description
- Rights: no copyrighted standard text bundled
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-NCAL: Mechanical testing data management

- Publisher: National Institute of Standards and Technology
- Link: https://www.nist.gov/programs-projects/ncal-data-management
- Reviewed portion: Provenance, materials/specimen details, machines and configuration history; public NIST page.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-MDCS: Materials Data Curation System

- Publisher: National Institute of Standards and Technology
- Link: https://www.nist.gov/programs-projects/materials-data-curation-system
- Reviewed portion: Materials metadata templating, data interconnection and federation; public overview.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-REPO: Materials Data Repository

- Publisher: National Institute of Standards and Technology
- Link: https://materialsdata.nist.gov/
- Reviewed portion: Repository provider rights/review caveats and user-supplied data; public home.
- Type: landing-page
- Rights: Provider controls terms; no dataset mirrored
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-RES: Materials data resources

- Publisher: National Institute of Standards and Technology
- Link: https://www.nist.gov/mgi/materials-data-resources
- Reviewed portion: Separates thermophysical experimental alloy data, computational/experimental diffusion, repository and registries.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.

## NIST-GAGE: Engineering metrology toolbox FAQ

- Publisher: National Institute of Standards and Technology
- Link: https://emtoolbox.nist.gov/faq/faq.asp
- Reviewed portion: Material selection for gauge artifacts: thermal expansion, diffusivity, stability and wear.
- Type: web-page
- Rights: link-only; wording paraphrased
- Archive: none; no original bytes, dataset nor screenshot.



## Materials v0.2 publisher source cards and capture

- **NIST-HAHN1-DATA** — [NIST e-Handbook, Thermal Expansion of Copper §4.6.4.1](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd641.htm), 236 source-reported observations, Thomas Hahn study, text and data links checked 2026-11-12. Data are captured as a **local checked transcription** in `materials_atlas/resources/hahn1/`, without original upstream bytes and without independent laboratory repetition. No unverified unit assignment.
- **NIST-HAHN1-CERT** — [NIST Statistical Reference Datasets certified Hahn1 values](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/v-hahn1.shtml), seven rational coefficients, RSS, RSD and 229 degrees of freedom; public HTML reviewed 2026-11-12. Distinguish numerical certification from a new experiment.
- **NIST-HAHN1-DIAGNOSTIC** — [NIST Handbook §4.6.4.4](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd644.htm), residual pattern of quadratic/quadratic rational fit; selected HTML reviewed, not a full paper scan.
- **NIST-295K-TABLE** — [NIST NCNR reference table](https://www.nist.gov/ncnr/neutron-instruments/sample-environment/sample-mounting/reference-tables), physical properties of selected metals at 295 K. Not a specimen-qualification dataset.
- **NIST-MATERIAL-DATA** — [NIST Materials Data Resources](https://www.nist.gov/mgi/materials-data-resources), curated experimental/computed data resources; overview only, not a copied dataset.
- **ASTM-E8-25** — [ASTM E8/E8M-25 public scope](https://store.astm.org/standards/e8_e8m), room-temperature tensile testing, specimen and representativeness limitations. Only public publisher scope checked; copyrighted standard not accessed or mirrored.

**Source scope:** web pages and publisher figures/tables described above, not internal unpublished methods. Numeric formulas beyond source statements are identified as original teaching derivations; scientific evidence classification does not change without independent review.

- **AFGROW-PARIS** — [AFGROW DTD Handbook §5.1.2](https://www.afgrow.net/applications/DTDHandbook/Sections/page5_1_2.aspx), inspected public HTML on 2026-11-12. Paris intermediate-regime power law, fitted constants and explicit caution about extrapolation. Only bounded paraphrase; not a certified materials dataset.


## Materials v0.3 scoped source additions

- **IUCR-POWDER-ERRORS** — [IUCr International Tables, powder diffraction errors and aberrations](https://onlinelibrary.wiley.com/iucr/itc/Cb/ch5o2v0001/sec5o2o1o2/). Selected public publisher excerpt checked 2026-11-12: Bragg law, cubic d-spacing, instrumental error context. No full chapter mirrored; not an instrument-specific uncertainty budget.
- **IUCR-LATTICE-ACCURACY** — [IUCr International Tables, lattice-parameter measurements](https://onlinelibrary.wiley.com/iucr/itc/Cb/ch5o3v0001/sec5o3o1/). Selected public section 5.3.1.1 checked 2026-11-12: Bragg relation, refraction correction, absolute/relative lattice parameters. Not a complete powder refinement method.
- **NIST-SANS-BINODAL** — [NIST SANS Toolbox PDF](https://www.nist.gov/system/files/documents/2023/04/14/the_sans_toolbox.pdf). Indexed excerpt on binodal and spinodal boundaries and tangent/curvature conditions, checked 2026-11-12. Full PDF pages not independently reviewed; source concerns polymer blends, and the Atlas's constant-omega symmetric model is a separately authored pedagogical simplification. No source bytes mirrored.

**Rights and maturity:** links and original bounded paraphrases only; no new measured data, full copyrighted source reproductions or independent scientific review. The new calculations are conditional on user-supplied or synthetic parameters.

# Materials Atlas 0.3 — scientific coverage and unresolved scope

**This is a content-depth checkpoint, not final Materials scientific v1 certification.** A chapter, calculator or numeric match does not establish specimen behavior.

| Scientific family | Reference content | Verified execution / evidence | Remains open |
|---|---|---|---|
| Source and unit provenance | Hahn1 dataset, capture manifest, NIST certified fit replay; no response unit invention | 236 checked transcribed observations; RSS/RSD at NIST certified coefficients | Original upstream transport bytes, response scale and full specimen uncertainty |
| Material identity and crystallography | Lattice, Bragg, structure, microstructure chapters | Ideal teaching calculations, no sample data | Actual XRD indexing, texture and symmetry solution |
| Phase equilibria / thermodynamics | Lever rule, formation energy and binary hull | Finite supplied-phase toy cases | Verified experimental tie lines, CALPHAD, finite-T stability and real DFT updates |
| Diffusion kinetics | Arrhenius and RMS models, mechanism limits | Author-supplied numeric inputs, range guards | Rights-cleared measured profiles, fit and activation confidence intervals, reaction boundaries |
| Mechanical response | Stress–strain definition, pre-necking conversion and ASTM public scope | Validated arithmetic and explicit refusal for missing uniformity | Actual full tensile curves, yield/UTS inference, standard conformance and uncertainty |
| Fracture and fatigue | K_I and in-regime Paris rate, no lifetime inference | Dimensional units and out-of-regime refusal | Real toughness tests, S-N and crack-growth datasets, environmental and geometry validity |
| Thermal response | Temperature-varying α integral and mismatch caveat | Synthetic grid integration checks | Direction-resolved real α(T), uncertainty and thermal stress model |
| Data cross-check / selection | Source-type and state-condition comparison | Exact shared-contract context closure | Independent scientific review, heterogeneous-data benchmark, materials qualification |
| AI routing and desktop installation | Deferred by owner until all 30 domains built | None claimed | Pin actual Bitwork, same-budget held-out retrieval, real consuming models and Windows tests |

**Materials content_ready = false.** Control is queued, not started. **All domains first, routing last, desktop transfer last.**


### v0.3 depth additions and remaining limitations

| Topic | Now covered | Still unverified |
|---|---|---|
| Regular-solution phase equilibrium | Mean-field Gibbs model, critical temperature, binodal, spinodal, metastability and equilibrium lever fractions; SciPy cross-check | Real assessed phase diagrams, composition/temperature uncertainty, kinetics, interfacial energy, elastic effects, CALPHAD data |
| Indexed cubic diffraction | First-order Bragg inversion, supplied hkl, random angle and shared wavelength standard uncertainty, chi-square diagnostic | Actual indexed instrument data, phase identification, wavelength calibration, systematic angle corrections, full covariance/refinement |
| Hahn1 residual diagnostics | Temperature-ordered residual bins, in-sample RSS check and explicit source-data limits | Original publisher transport bytes, response unit scale, independent specimen test and external prediction validation |

**Scientific-content status remains in progress.** The next meaningful increment should add a rights-cleared measured mechanical/phase/diffraction dataset with complete source conditions or deepen an outstanding engineering property family; do not substitute another synthetic example for that evidence gap.

# Materials Atlas review templates

## Experimental property record
Material ID / batch / nominal vs verified composition / processing state / sample location / geometry / method + revision / measured property and units / raw file and local hash / temperature and atmosphere / orientation / replicate count / calibration and uncertainty / instrument changes / rights / reviewer / use limitations.

## Computed property record
Structure ID / phase and composition / input file hash / software and version / functional and correction scheme / pseudopotential / k point settings / convergence / energy normalization / magnetic state / structural relaxation / competing phases included / calculated property and units / data release / known accuracy limitations / source and rights.

## Candidate comparison
Operating conditions / failure mode / property definition and direction / comparable condition table / required reliability / manufacturability / cost assumptions / missing values / screening result / uncertainty and qualification plan / refusal reasons.

## Evidence-change log
Original record ID and revision / new source or raw data / contradictory values and condition differences / author and checker / review status / downstream contexts affected / supersession link / versioned release change.


## v0.3 phase-model audit worksheet

- Specimen or model identity: ____ ; real measurement or stipulated model: ____
- Composition basis (mole/mass fraction), temperature K, omega J/mol, and source: ____
- Reference free energy and available competing phases: ____
- Binodal/spinodal calculation and numerical precision: ____
- Global versus local stability assessment: ____
- Kinetic/interfacial/elastic effects omitted: ____
- Reproduction command and input hash: ____
- Decision boundary: what cannot be claimed? ____

## v0.3 indexed diffraction worksheet

- Specimen identity, processing, temperature, phase hypothesis: ____
- Radiation/wavelength and shared standard uncertainty: ____
- Instrument zero-offset, displacement and calibration: ____
- For each peak: hkl, 2theta, angle uncertainty, extraction method: ____
- Correlated versus independent error components: ____
- Mean a, standard uncertainty components, chi-square, rejected peaks: ____
- Independent phase/indexing justification and unresolved alternatives: ____

## v0.3 published-data residual worksheet

- Source URL, original byte availability and local transcription hash: ____
- Response units, temperature units, model equation and parameter provenance: ____
- In-sample RSS, number of observations, bins and descriptive statistics: ____
- What sorting order was used and what it does *not* establish: ____
- Out-of-sample evidence and physical measurement uncertainty: ____

# Materials Atlas authored review prompts (not held-out model evaluation)

These 20 checks are visible development aids. They were not independently authored or administered to an AI model.

1. When is a measured property comparable across two lots? Specify mandatory context fields.
2. What cannot be concluded from a Materials Project 0 K energy above hull?
3. Why is the model/functional and correction scheme part of a computed energy record?
4. Demonstrate a mass-versus-mole-fraction failure in a two-phase lever rule.
5. Why does a unit-cell theoretical density differ from real bulk density?
6. What is the difference between θ and 2θ in a powder diffraction report?
7. What additional measurements can distinguish competing phases with overlapping peaks?
8. Why is a crystal unit cell not a grain?
9. Give two processing changes that can affect properties without changing bulk chemistry.
10. What must be known before calculating a yield strength from a force/extension trace?
11. Why is ultimate tensile strength not a fatigue-life guarantee?
12. Explain why a single stress–strain point does not determine modulus.
13. What assumption is made in the Voigt scalar mixture equation?
14. Why cannot mass fraction replace volume fraction in a modulus mixture?
15. When does thermal free-strain mismatch fail to determine interface stress?
16. What changes in the result if a missing competing phase is added to a computed binary hull?
17. Why may two data entries with equal units and names still be incomparable?
18. What rights and uncertainty metadata must accompany a reused repository value?
19. What should the Atlas say when a component qualification question lacks test standards?
20. Which questions should be passed to Measurement, Causal and Manufacturing rather than answered solely from Materials?

**Review intent:** Check evidence closure, assumptions, abstention and failure modes, not memorization of toy numbers.


## v0.2.0 new evidence-focused questions (authored, not held-out evaluation)

1. What evidence would establish the physical units of the NIST Hahn1 response?
2. What does agreement between certified RSS and a locally copied data table support, and not support?
3. Why is a least-squares solution initialized near the certified optimum not evidence of unique global convergence?
4. Under which physical assumptions can an α(T) curve predict an unconstrained specimen's length ratio?
5. Why can't a coefficient tabulated at 295 K justify a 600 K design assumption without more information?
6. How would you distinguish bulk diffusion from grain-boundary transport in measured concentration profiles?
7. Which uncertainties enter the conversion from force–extension data to reported yield strength?
8. Why does uniform deformation have to be established before converting engineering to true stress?
9. What measured information is required before stress intensity can be compared to validated fracture toughness?
10. Why does a Paris rate at one ΔK not establish cycles to failure?
11. What conditions would trigger refusing a materials ranking even when all candidate numbers are finite?
12. Which deployment and routing checks remain deferred until all thirty content libraries exist?


## v0.3 additional scientific review questions (authored, not held-out)

1. In a symmetric regular solution, why can a locally positive Gibbs curvature coexist with a globally lower two-phase free energy?
2. What is the mathematical difference between a binodal and a spinodal, and why is the x=0.5 stationary point a dangerous root-solver trap?
3. What conditions must hold before a lever-rule fraction can be interpreted as an observed phase fraction?
4. Why does a 0 K DFT convex hull not substitute for a finite-temperature regular-solution phase diagram?
5. Why does a diffraction instrument's reported 2theta need to be halved before using Bragg's law?
6. What external evidence is needed before assigned hkl values become a defensible phase identification?
7. Derive the first-order sensitivity of cubic a to 2theta in degrees and explain the pi/360 factor.
8. Why does wavelength uncertainty not shrink when more peaks from the same calibration are included?
9. What can an anomalous reduced chi-square indicate, and what does it *not* prove?
10. Why is residual adjacency after temperature sorting not a temporal autocorrelation?
11. Which source bytes and response units are unresolved for Hahn1, and what inference do they block?
12. Explain why numerical certification of a published regression does not certify a material property.
