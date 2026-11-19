# MATERIALS ATLAS · Reference Manual 0.1.0

**James Paul Jackson research program · 12 November 2026 · Bounded educational/research content**

This manual documents scientific principles and limitations. Its computations use authored synthetic data. It does not authenticate any experiment, certify a material, or reproduce an external dataset.

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
