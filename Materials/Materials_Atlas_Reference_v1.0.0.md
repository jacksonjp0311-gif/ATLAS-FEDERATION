# Materials Atlas — Scientific Reference Manual v1.0.0
Author: James Paul Jackson research program | Contract: Atlas Common 1.0 | 2026-11-12
**Scope:** An evidence-preserving scientific research reference, not a sample, part, or product certification. Previous chapters are preserved as written; v1 additions are labelled.
**Release boundary:** 32 chapters, 19 investigations, 148 records, 29 source cards, 84 typed relations. Original measurements? None new; archived publisher-source bytes? No; independent scientific review? No; routing? Deferred until all 30 domains.
## Contents
- [01 scope evidence and comparability](chapters/01_scope_evidence_and_comparability.md)
- [02 composition bonding and material identity](chapters/02_composition_bonding_and_material_identity.md)
- [03 lattices cells diffraction and uncertainty](chapters/03_lattices_cells_diffraction_and_uncertainty.md)
- [04 processing microstructure defects](chapters/04_processing_microstructure_defects.md)
- [05 phase equilibria and the lever rule](chapters/05_phase_equilibria_and_the_lever_rule.md)
- [06 thermodynamic models and phase stability](chapters/06_thermodynamic_models_and_phase_stability.md)
- [07 mechanical behavior and standardized testing](chapters/07_mechanical_behavior_and_standardized_testing.md)
- [08 thermal expansion and transport](chapters/08_thermal_expansion_and_transport.md)
- [09 composites mixtures and orientation](chapters/09_composites_mixtures_and_orientation.md)
- [10 degradation fatigue fracture and service](chapters/10_degradation_fatigue_fracture_and_service.md)
- [11 computed versus measured reproducibility and versioning](chapters/11_computed_versus_measured_reproducibility_and_versioning.md)
- [12 decision ledger and cross-domain reuse](chapters/12_decision_ledger_and_cross-domain_reuse.md)
- [13 source data and reproduction](chapters/13_source_data_and_reproduction.md)
- [14 temperature dependent properties](chapters/14_temperature_dependent_properties.md)
- [15 diffusion and kinetics](chapters/15_diffusion_and_kinetics.md)
- [16 tensile properties and conversion](chapters/16_tensile_properties_and_conversion.md)
- [17 crack mechanics and fatigue](chapters/17_crack_mechanics_and_fatigue.md)
- [18 evidence bound decisions](chapters/18_evidence_bound_decisions.md)
- [19 research coverage and backlog](chapters/19_research_coverage_and_backlog.md)
- [20 regular solution phase boundaries](chapters/20_regular_solution_phase_boundaries.md)
- [21 cubic diffraction and uncertainty](chapters/21_cubic_diffraction_and_uncertainty.md)
- [22 hahn1 residual diagnostics](chapters/22_hahn1_residual_diagnostics.md)
- [23 methods status and falsification](chapters/23_methods_status_and_falsification.md)
- [24 nist copper solid thermochemistry](chapters/24_nist_copper_solid_thermochemistry.md)
- [25 corrosion penetration and localized failure](chapters/25_corrosion_penetration_and_localized_failure.md)
- [26 multilayer heat flow and interface conditions](chapters/26_multilayer_heat_flow_and_interface_conditions.md)
- [27 isothermal transformations and non isothermal limits](chapters/27_isothermal_transformations_and_non_isothermal_limits.md)
- [28 creep rates versus life prediction](chapters/28_creep_rates_versus_life_prediction.md)
- [29 weakest link statistics not automatic reliability](chapters/29_weakest_link_statistics_not_automatic_reliability.md)
- [30 evidence quality material certification and abstention](chapters/30_evidence_quality_material_certification_and_abstention.md)
- [31 metrology of materials records and ingestion](chapters/31_metrology_of_materials_records_and_ingestion.md)
- [32 content release boundary and future interoperability](chapters/32_content_release_boundary_and_future_interoperability.md)
## Investigations
- [01 diffraction and identity](investigations/01_diffraction_and_identity.md)
- [02 phase equilibrium and hull](investigations/02_phase_equilibrium_and_hull.md)
- [03 tensile property context](investigations/03_tensile_property_context.md)
- [04 thermal interface and selection](investigations/04_thermal_interface_and_selection.md)
- [05 nist hahn1 copper](investigations/05_nist_hahn1_copper.md)
- [06 diffusion and temperature](investigations/06_diffusion_and_temperature.md)
- [07 fracture fatigue boundaries](investigations/07_fracture_fatigue_boundaries.md)
- [08 materials evidence decision](investigations/08_materials_evidence_decision.md)
- [09 miscibility gap and metastability](investigations/09_miscibility_gap_and_metastability.md)
- [10 indexed cubic peaks and shared uncertainty](investigations/10_indexed_cubic_peaks_and_shared_uncertainty.md)
- [11 nist hahn1 residuals](investigations/11_nist_hahn1_residuals.md)
- [12 copper webbook thermochemistry](investigations/12_copper_webbook_thermochemistry.md)
- [13 corrosion coupon nonuniform attack](investigations/13_corrosion_coupon_nonuniform_attack.md)
- [14 thermal contact stack](investigations/14_thermal_contact_stack.md)
- [15 isothermal avrami and schedule failure](investigations/15_isothermal_avrami_and_schedule_failure.md)
- [16 creep rate beyond the test regime](investigations/16_creep_rate_beyond_the_test_regime.md)
- [17 ordinary weibull vs bulk weakest link](investigations/17_ordinary_weibull_vs_bulk_weakest_link.md)
- [18 copper identity cross source trap](investigations/18_copper_identity_cross_source_trap.md)
- [19 material selection refusal and study plan](investigations/19_material_selection_refusal_and_study_plan.md)

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

The source dataset is transcribed from a public HTML/text representation because a direct original-byte download failed in the current runtime. `materials_atlas/resources/hahn1/capture.json` identifies the upstream URL, the unavailable upstream byte hash, the SHA-256 hash of our own normalized transcription and the exact validation scope. The 236 rows are in source order (not temperature-sorted), because acquisition order may matter when assessing batch effects. Both the file and the parser assert 236 rows; the calculation covers the actual observed range [14.13, 851.61] K.

The benchmark computes the squared residuals at **NIST's published coefficients** for the cubic-over-cubic rational model. It reproduces the certified sum of squares (1.5324382854) and residual SD (0.081803852243), both to less than 5×10^-9 in their native reported scales. That verifies numerical consistency of the transcription and model evaluation. It does not mean this runtime has directly reproduced the original measurement, discovered the true physical law, or obtained the full precision source-file bits. `tools/hahn1_oracle.py` optionally refits by two SciPy algorithms, explicitly initialized near the certified optimum; that check is not an independently designed blind benchmark.

## What remains before material qualification

Obtain verified original source bytes or independent publisher confirmation of the values, documentary response units, instrument/method metadata, uncertainty, specimen purity, grain history, and independent scientific review. NIST notes a lower-quality quadratic/quadratic rational model can produce structured residuals even when plotted data look close; model fit is not model adequacy. A new copper lot may behave differently from this experiment, and an equation calibrated only in the published range must not be extrapolated.

**Source locators:** NIST Handbook §4.6.4.1 (data); §4.6.4.4 (quadratic model diagnostics); NIST StRD Hahn1 certified values and certification method. The original documents are linked rather than mirrored.


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

**Sources and scope:** MIT OpenCourseWare 3.012, lecture 19 pp. 11–12 (PDF text and page images checked): https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/9fa239d16926f0de29a87ed6f2e963d0_lec19t.pdf ; IUPAC Gold Book spinodal definition https://goldbook.iupac.org/terms/view/S05869 (search excerpt checked; direct page was blocked). The regular-solution derivation is original educational reasoning, not measured alloy data.


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

**Sources and scope:** IUCr Dictionary, *Bragg’s law*, https://dictionary.iucr.org/Bragg%27s_law ; IUCr *International Tables for Crystallography* Vol. C §1.2.6 cubic crystal system, https://it.iucr.org/Cb/ch1o2v0001/sec1o2o6/ ; IUCr educational pamphlet §4.1 cubic structures, https://www.iucr.org/what-we-do/education/pamphlets/study-of-metals-and-alloys-x-ray-powder-diffraction-methods . These specific public sections were inspected; no restricted tables were mirrored.


---

# 22. Hahn1 copper: what a certified numerical fit does and does not establish

**Status:** descriptive reanalysis of the existing NIST Hahn1 local checked transcription. No new physical measurement or original upstream transport-byte acquisition is claimed.

## Separate the three evidence layers

**Layer 1 — source-reported observations.** NIST publishes 236 temperature/response pairs for the Hahn1 copper thermal-expansion benchmark. The Atlas stores the numeric values in original published order as a checked transcription. The predictor temperature is in kelvin; the numerical response scale remains unresolved in our inspected material. A local SHA-256 identifies our transcription, not the original upstream bytes.

**Layer 2 — numerical regression certification.** NIST publishes certified parameters and residual statistics for a seven-parameter rational function. Re-evaluating those parameters on the 236 observations reproduces the residual sum of squares approximately `1.53243828536062`, compared with the certified `1.5324382854`. This is a valuable software/numerical check; it does not determine a physical coefficient uncertainty or the trustworthiness of the material model.

**Layer 3 — physical validity and prediction.** To use the fit to predict expansion in a real specimen, we would need to establish response units, reference specimen and processing conditions, the model's physical applicability, measurement uncertainty, calibration, and temperature range. The Atlas does not infer any of these from the fact that a residual sum of squares matches.

## Why bin the residuals?

The v0.3 calculator sorts the 236 observations by temperature and partitions them into a declared number of equal-count groups (2–20). It reports each bin's temperature span, count, mean residual and root-mean-square residual, along with the overall residual mean and RSS. Binning can expose a temperature-dependent bias that a single RSS conceals, but it depends on the chosen number of bins and can hide patterns. It is a descriptive visualization in numeric form, not a hypothesis test or independent holdout evaluation.

The tool also reports a correlation between adjacent residuals **after temperature sorting**. This is *not* a time-series autocorrelation because sorted temperature order does not represent acquisition time. The distinction is critical: calling a temperature-neighbor statistic evidence of instrument drift would overstate what the available metadata support.

## Limits and useful follow-up

We do not claim a new fitted parameter set, an independent temperature sweep, an error model for the physical experiment, or a validated extrapolation. The publisher data are an in-sample benchmark. A defensible next study would obtain the original upstream data bytes and source metadata, resolve response units, predeclare an out-of-sample or independent-specimen comparison, and quantify uncertainty from measurement and model inadequacy. This domain can provide an analysis checklist and computational reference while marking those steps open.

**Sources:** NIST e-Handbook copper Hahn1 example: https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd641.htm ; NIST StRD certified values: https://www.itl.nist.gov/div898/strd/nls/data/LINKS/v-hahn1.shtml ; NIST model diagnostics: https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd644.htm . The cited pages are publisher material; the Atlas calculation is original reanalysis.


---

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


---

# 24. Copper thermochemistry from a bounded publisher fit

**Source type:** NIST Chemistry WebBook SRD 69, copper condensed-phase Shomate coefficients (Chase 1998 compilation; data reviewed June 1977). **Inspection:** publisher HTML and selected display rows, 2026-11-12. **Status:** computational reproduction of a *compiled, fitted representation*; not a new calorimetry experiment. [Publisher record](https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS).

## Define the material and the quantity

The fitted solid-phase entry is for elemental copper, Cu (CAS 7440-50-8), not a named alloy or a particular lot. The independent variable is thermodynamic temperature **T in kelvin**. Its published fit applies to **298–1358 K**. The response quantities are molar heat capacity at constant pressure, Cp in J/(mol K); molar enthalpy relative to 298.15 K, H−H(298.15) in kJ/mol; and molar entropy S in J/(mol K). These are *thermodynamic compilation quantities*, not Hahn1's experimental thermal-expansion response and not generic engineering material constants.

## The numerical contract

Set t=T/1000 and evaluate the Shomate family with the publisher's selected solid coefficients:

- Cp=A+B t+C t²+D t³+E/t²
- H−H(298.15)=A t+(B/2)t²+(C/3)t³+(D/4)t⁴−E/t+F−H
- S=A ln(t)+B t+(C/2)t²+(D/3)t³−E/(2t²)+G

Here `(A,B,C,D,E,F,G,H)=(17.72891,28.09870,−31.25289,13.97243,0.068611,−6.056591,47.89592,0)`. These eight numerical facts and six selected checks are included only as needed to reproduce the calculation; the source table and third-party compilation are not mirrored. The source identifies a data-compilation copyright, so this package links to the authoritative page, provides attribution and does not imply that publication rights have been conveyed. The coefficient precision shown by NIST is finite; it does not establish a coefficient covariance or combined material uncertainty budget.

At 400 K, the recomputation gives Cp≈25.29098 J/(mol K), Hrel≈2.53404 kJ/mol and S≈40.4740 J/(mol K). The publisher displays 25.29, 2.53 and 40.47 respectively. At 900 K, the recomputation gives Cp≈27.97351 J/(mol K), Hrel≈15.90054 kJ/mol and S≈62.01235 J/(mol K), consistent with the publisher's two-decimal display. The maximum discrepancy across six selected row triples is about 0.00488 in the quantity's printed units. This is an **author-chosen numerical check**, not independent scrutiny of the source compilation.

## A useful independent identity

For thermodynamic consistency within the fit, `dH/dT=Cp`, after the kJ-to-J conversion, and `dS/dT=Cp/T`. The v1 numerical oracle integrates Cp independently and differentiates the compiled expressions. It tests the mathematical implementation, not the empirical validity of the coefficients. Example: `H(900 K)−H(400 K)` is approximately **13.3665058843 kJ/mol** from the published fit. This is not a latent-heat measurement.

## Refusal and source boundaries

The calculator rejects a temperature outside 298–1358 K rather than extrapolating. It does not transition to the liquid coefficients at the solidus, infer alloy heat capacity from elemental copper, or treat this enthalpy series as thermal expansion. Report the phase, domain, units, reference state, source version, and coefficient-display precision with each result. A fit that matches rounded NIST rows can still be inappropriate for a real component with impurity, cold work, temperature gradients, or unknown service conditions.

**Cross-links:** Chapter 14 (temperature-dependent properties), Chapter 22 (fit residuals), Chapter 29 (decision ledger). `python -m materials_atlas v1-cases` reproduces the explicit published-row checks.


---

# 25. Mass-loss corrosion rates are not maximum damage depths

**Sources:** NIST-hosted *Corrosion of Copper and Steel Alloys in the Presence of Acetobacter sp.* (Sowards and Mansfield, July 2013), notably its section labelled corrosion-rate measurements; a bounded ASTM G31 formula is displayed. [Publisher-hosted presentation](https://www.nist.gov/system/files/documents/mml/acmd/2013-07-22-Corrosion-of-Copper-and-Steel-Alloys-Sowards.pdf). The publisher PDF's extracted text was checked; a requested screenshot failed because the retrieval cache missed. We therefore do **not** claim a visually authenticated full-PDF review or a licensed reproduction of the ASTM standard.

## Define the measurement

An immersion coupon's corrected **mass loss W**, exposed **surface area A**, duration **t**, and measured **density ρ** can determine an average *equivalent uniform penetration*. For W in grams, A in cm², ρ in g/cm³ and t in hours:

`average penetration rate (mm/y) = 87600 W/(A ρ t)`.

The coefficient follows directly from `W/(Aρ)` cm thickness, times 10 mm/cm and 8760 hours per 365-day year. The NIST-hosted presentation prints 8.76×10⁴ for mm/y under the same units. Neither the exact standard nor all cleaning and specimen requirements are included in this Atlas. The qualified investigator must consult the applicable current standard and report the testing conditions.

## Worked result

A hypothetical coupon loses **0.10 g** after **240 h**, with **100 cm²** exposure area and **7.8 g/cm³** density. The arithmetic gives **0.0467948718 mm/y equivalent uniform penetration**. Doubling the corrected loss while holding the same area, time and density doubles this calculated average. These are **synthetic inputs**, not data from the NIST experiment and not a corrosion rate for all carbon steels.

## Where the simple estimate fails

A coupon can have substantial localized attack while its total mass loss is low. If the specimen has pits, under-deposit corrosion, crevice corrosion, galvanic coupling, biofilms, selective corrosion, or oxide retention, an average equivalent penetration can seriously understate the maximum local depth. Coupon cleaning may also remove substrate or leave corrosion products, so the corrected mass loss needs a laboratory procedure and uncertainty budget. Uniform area may change, time dependence need not be linear, and the application environment can differ substantially from the bath chemistry. Zero resolved mass loss does not establish zero corrosion or absence of pits.

**Minimum provenance:** source material grade and composition; processing/heat treatment; exposed area and masking; exact duration; solution composition/pH, dissolved oxygen and temperature; cleaning method and blank correction; instrument mass calibration, detection limit, density basis; macroscopic and microscopic damage inspection; replicate distribution; uncertainty and traceability; sample selection. Without this, output remains a geometry calculation on supplied numbers.

**Refuse the inference** “the wall has N years remaining” from coupon mass-loss arithmetic. Predicting life requires actual local wall-thickness records, local attack morphology, damage propagation, safety factors and engineering standards. The interface returns `not_inferred` fields for these targets.


---

# 26. Heat flow, interfaces, and thermal design boundaries

## The governing model

For a steady one-dimensional plane wall with isotropic scalar conductivity `k` and no internal generation, Fourier's law gives `Q = k A ΔT/L`. Written as a thermal circuit, one layer contributes `R=L/(kA)` with units K/W. Thermal resistances in *series* add. For a declared contact resistance Rc (K/W), `Q=ΔT/(Σ L_i/(k_i A)+Σ Rc)`.

This is an **engineering model**; it is not a measured conductivity or a heat-transfer experiment. It assumes that the layer cross-section and pathway are known, material conductivities are approximately constant in the temperature range, lateral leakage is negligible, and the specified contact resistances represent interface effects. Real components may have radiation, convection, phase change, porosity, anisotropy and transient heating; absent terms are not zero merely because the input omits them.

## Worked synthetic stack

Declare area `0.1 m²`, a `1 mm` copper-like conductive layer assigned `200 W/(m K)`, a `5 mm` insulating layer assigned `1 W/(m K)`, a contact resistance `0.3 K/W`, and applied temperature difference `50 K`. The model gives `R1=0.00005 K/W`, `R2=0.05 K/W`, total `0.35005 K/W`, and approximately **142.836738 W** of heat rate. Without the declared contact resistance, the predicted rate is about **999.001 W**. This large difference illustrates why surface finish, pressure, contact material and assembly conditions matter. The numbers are hypothetical, not tested values for a commercial thermal interface material.

## Measurement and model error

A conductivity value from a materials database is often measured at a stated temperature and microstructural condition. It may not represent a laminate, foam, coated part, grain-aligned crystal or specimen under compression. If conductivity varies with temperature, the exact 1D stationary law requires integrating `k(T)` and imposing the correct thermal boundary conditions; substituting a single catalogue value can bias the result. Contact conductance can change over cycles or with mounting pressure, and a thermal interface does not automatically have a transferable scalar k. Never infer contact resistance from a polymer bulk conductivity without actual interface measurement.

## Uncertainty and decisions

Treat geometry, material composition, conductivity fit, interface resistance, heat source, environmental boundary and sensor positioning as different error contributors. Changing a design from one material to another requires recalculation with representative property distributions and conditions, not merely comparing single conductivity numbers. The new calculator reports the declared per-layer and total resistances and refuses nonpositive conductivities or missing layers. **It does not predict actual interface temperatures, thermal stress, equipment uptime, or a pass/fail decision.**

**Related material:** Chapter 08 on thermal transport, Chapter 14 on temperature-dependent properties, and Measurement Atlas on uncertainty budgets and calibration.


---

# 27. Transformation kinetics: isothermal laws and temperature-history traps

## What the model says

A standard phenomenological form for an isothermal transformed fraction is `X(t)=1−exp[−(k t)^n]`, often associated with Johnson–Mehl–Avrami–Kolmogorov-type kinetics under selected nucleation and growth assumptions. `k` has units s⁻¹, `n` is dimensionless, time is seconds, and `X` is between zero and one. The form is *not* a universal law of microstructural evolution. Different process routes, nucleation mechanisms, impingement, spatial distributions and incubation effects can produce different kinetics.

For target fraction `0<X<1`, invert to `t=[−ln(1−X)]^(1/n)/k`. The calculator requires a strictly interior desired fraction; an exact fraction one occurs asymptotically in the ideal model and must not be reported as a finite termination time. A nonpositive kinetic rate or exponent is invalid.

## Constructed example

For assumed `k=0.001 s⁻¹` and `n=2`, half transformation occurs at approximately **832.55 seconds**. Applying the forward equation to this time returns 0.5 within floating-point rounding. The chosen parameters are not from a real alloy and cannot be used to specify a furnace recipe. The example is an algebraic verification, not evidence for a physical half-transformation time.

## What must be learned experimentally

A reproducible kinetic claim needs the starting phase fractions, sample composition and history, quench and aging protocol, actual specimen thermal profile, measurement method (DSC, dilatometry, microscopy, diffraction, etc.), segmentation calibration, uncertainty and replicate data. Fit parameters must be estimated with a documented temperature and composition range. Multiple mechanisms can fit a short transformation curve; a high R² is not enough to establish the kinetic model. Nucleation barriers, diffusion constraints and competing reactions may change throughout the process.

## Critical failure: using an isothermal model for a cooling curve

A continuous-cooling transformation is a **history-dependent** problem. A measured TTT curve is not automatically a CCT curve, and simply adding separate isothermal fractions is generally unjustified. If the thermal path changes, a validated state-evolution model or direct nonisothermal evidence is required. This Atlas does not implement Scheil additivity, latent-heat-coupled process simulation or microstructure prediction. The model returns fractions only under the specifically declared fixed-temperature parameterization.

**Connections:** Chapter 04 (processing and defects), Chapter 15 (diffusion and kinetics), Chapter 20 (phase equilibria), and Control Atlas (eventual temperature-program models, not yet built). The v1 content deliberately separates an executable arithmetic function from actual heat-treatment qualification.


---

# 28. Creep: a steady strain-rate formula is not a rupture forecast

## Response and physical regime

At elevated homologous temperatures or otherwise creep-sensitive conditions, stress and time can produce inelastic deformation. Materials may exhibit primary, approximately steady secondary, and tertiary creep with damage accumulation; the regime boundaries depend on composition, grain size, stress, temperature, environment, and service history. A simplified *Norton–Arrhenius* steady-state strain-rate relation is `εdot=A σ^n exp(−Q/(RT))`.

`εdot` is s⁻¹, σ is entered in MPa, n is dimensionless, Q is J/mol, R=8.31446261815324 J/(mol K), T is kelvin, and **A must carry units s⁻¹ MPa⁻ⁿ**. The parameter set is not universal; it must be fitted to relevant creep measurements, ideally with uncertainty, stress/temperature coverage, and documented sample state. Substituting a tensile strength or a creep rate for an unrelated alloy violates the model's material identity.

## Sensitivity example

For constructed values `A=10⁻⁸ s⁻¹ MPa⁻³`, `n=3`, `Q=200,000 J/mol`, `T=900 K`, σ=50 MPa, the model gives approximately **3.086×10⁻¹⁵ s⁻¹**. Doubling stress to 100 MPa at constant temperature changes the rate by `2^3=8`; this identity follows from the *stipulated model*, not empirical validation. The strain accumulated over a selected duration under the constant-rate assumption is `ε≈εdot t`. It does not include elastic strain, primary creep, tertiary acceleration or microstructural damage.

## Why extrapolation is dangerous

A calibrated rate over hours at a particular stress and temperature does not establish safe lifetime for years at another temperature. A mechanism map may change from dislocation climb to diffusional creep, or microstructural aging may invalidate constant A, n, Q. Grain-boundary cavitation, oxidation, load multiaxiality, welds and stresses from thermal cycling can make rupture behavior very different from strain-rate behavior. The Atlas refuses to output creep rupture or component safe-life estimates from the rate alone.

## Essential reporting

Report the source of A/n/Q, regression model, applied stress basis and stress evolution, precise T/K history, sample composition/heat treatment, specimen geometry, stress and strain measurement system, calibration, confidence bands, replication, and whether the requested quantity lies inside the measured regime. The v1 implementation checks positive finite temperature and stress, dimensional convention for the pre-factor, and numerical overflow/underflow. It returns a conditional rate and a steady-regime increment with explicit exclusions.

**Connections:** mechanical properties (Chapter 07), fracture and fatigue (Chapter 17), degradation (Chapter 10), and time-sensitive equipment modeling (Control Atlas, queued).


---

# 29. Weibull strength fits versus a physical weakest-link model

## Separate a distribution from its mechanism

The ordinary two-parameter Weibull distribution is a flexible probability law for a random variable. Fitting it to a collection of measured strengths does not automatically justify the *weakest-link fracture theory* needed to scale from a test coupon to a larger component. An explicit methodological discussion appears in *Statistics of ceramic strength: Use ordinary Weibull distribution function or Weibull statistical fracture theory?*, *Ceramics International* 46 (2020), DOI 10.1016/j.ceramint.2020.05.024. [Accessible publisher abstract](https://www.sciencedirect.com/science/article/pii/S0272884220313092).

## Conditional volume scaling

If the model assumes independent, identically distributed elemental volumes and spatially uniform stress, a simplified conditional volume survival law is `S(σ,V)=exp[−(V/V0)(σ/σ0)^m]`. Here `σ` and `σ0` are in the same stress units (the calculator uses MPa), V and V0 are in the same volume units (mm³), and m is dimensionless. The model assumes an actual **bulk flaw population** appropriate for volume scaling. Surface flaws, stress gradients, nonuniform microstructures and shape differences require other formulations. The model is not established by fitting an ordinary Weibull CDF alone.

## What the simulator demonstrates

Given assumed σ=120 MPa, σ0=200 MPa, m=5, V=V0=1000 mm³, conditional survival is approximately **0.9252**. Doubling the volume under the *declared independent bulk-flaw model* yields survival approximately **0.8560**, equal to the original survival squared. These numbers are constructed parameter illustrations, not reliability estimates for a real ceramic. The software requires an explicit `physical_weakest_link_assumed=True` argument to prevent accidental application of volume scaling to arbitrary empirical strength distributions.

## Why an estimate is not a qualification

Estimating shape and scale requires representative specimens, failure censoring policy, fracture origin characterization, machining and surface finish, residual stress and a defensible statistical sampling model. Test fixture, loading mode, environment, stressed area/volume, temperature, time-dependent slow crack growth and manufacturing defects all matter. Use appropriate design and fracture standards and independent review for certification or safety-critical sizing. The program does not estimate Weibull parameters from sample strengths, does not implement design allowables, and makes no component reliability guarantee.

The safest default for an unknown flaw model is to **refuse transfer across volumes**. When the physical weakest-link hypothesis is unsubstantiated, report the empirical fitted distribution and its specimen domain separately. A numerical probability output should carry its experimental basis, uncertainties, failure definition and source limitations intact.

**Connections:** Chapter 17 crack mechanics, Chapter 10 degradation and service, and Measurement Atlas for reliability/uncertainty interpretation.


---

# 30. The materials qualification evidence chain

A materials model should be a **traceable evidence object**, not a context-free scalar. Consider the statement: “this steel's tensile strength is 650 MPa.” Without composition, specification, condition (annealed, quenched, cold worked), processing and thickness, test temperature, strain rate, orientation, specimen geometry, test-standard revision, heat/lot identity, uncertainty, and the basis of the quoted statistic, it is not safely transferable to another component.

## Build the chain

1. Identify the physical material and product form, lot, and history. Source documents include certificates, specimen logs, process travellers and instrument records.
2. Specify the target quantity and operating conditions. A room-temperature proof stress is not high-temperature creep strength and a 0 K DFT hull energy is not a measured phase boundary.
3. Select the test or computational protocol and record its domain. Retain instrument traceability, data processing steps, calibrations, sample conditioning and exclusions.
4. Record the actual observations separately from calculations, model output, secondary compilations and assumptions. A graph or source title does not authenticate a sample.
5. Reproduce calculations with units and uncertainty; compare primary displays without retuning thresholds merely to obtain agreement.
6. Delineate conflicting evidence, model dependence, finite data, and relevance to the target lot. Keep incompatible claims side by side.
7. Produce an outcome that can be **verified, limited or refused**. If the goal is a regulated specification, design allowable or failure prognosis, defer to qualified testing and governing standards.

## Six failure patterns

**Unidentified state:** “Copper” may refer to an element, commercial alloy, cold-worked part or thin film. **Unit drift:** a strain, linear expansion coefficient and enthalpy response can all be attached to a copper record yet are not interchangeable. **Temperature extrapolation:** material stiffness, conductivity and creep can change nonlinearly outside measured conditions. **Model aliasing:** a 0 K convex hull and room-temperature phase diagram have different thermodynamic potentials. **Averages hide local damage:** a mass-loss rate cannot rule out pitting. **Model success confounded with evidence validity:** an analytic formula or held-in data-fit can be right under assumptions that a real specimen violates.

## Cross-domain handoff

Measurement Atlas owns calibration/uncertainty interpretations, Causal Atlas owns intervention vs association, Materials Atlas owns material identity, microstructure, phase and properties. Forge must supply the exact record, sources and limitations as one inclusion unit; it must not compress a refusal into a confident materials selection. Control and Manufacturing Atlases will later handle system feedback and process failures. All domains are built before routing integration by explicit owner instruction.

## Content-v1 scope

The current release supplies a bounded research and instructional reference, primary-source pointers, more than one reproduced publisher numerical source, and executable conditional calculations with original failure cases. It does **not** claim complete standards coverage, independent lab certification, absence of unknown materials phenomena, qualified physical modelling, independent expert review, or AI answer-performance improvement. Those are separately named integration and validation gates, not mislabeled failures of ordinary software tests.


---

# 31. Ingest materials data without losing the physical meaning

## One dataset, many identities

A materials database often stores a property alongside a chemical formula and a scalar numerical value. That is not sufficient to determine whether two numbers refer to the same physical quantity. A robust record must distinguish *element vs compound vs mixture vs device*, exact composition, crystal structure/phase fractions, orientation, processing history, sample condition, environment and temperature, measurement mode and frequency, units, uncertainty, source license and provenance. When a property is computational, it additionally needs model class, functional or force field, code/library version, correction scheme, convergence settings and structural relaxation protocol.

## Provenance requirements

At minimum include: stable source ID and access URL; inspected portion; source record time and scientific publication/version; data licensing; acquisition type (author-measured, publisher table, transcription, calculation, simulation); local content hash where bytes are stored; original transport-byte hash if authenticated (otherwise `null`); transformation script and code version; row counts, parsing policy and validation outputs; missing values and selection mechanism; statistical aggregation level; and explanatory limitations. A hash authenticates a **representation's bytes**, not the authority or physical correctness of their contents.

## The copper example

Hahn1 and NIST WebBook copper data should not be merged into a single “copper curve.” Hahn1 is a nonlinear least-squares benchmark using published observations of a thermal expansion-related response; its response scaling was not authenticated in this package. NIST WebBook provides a compiled solid-copper thermodynamic fit for Cp, relative H and S, with explicitly defined temperature range and units. A naive database join on the string “copper” would erase the difference between measured response, fitted thermodynamic representation, uncertainty and physical sample. A correct join uses typed quantities and retains both evidence sources and their differences.

## Import and validation workflow

A well-formed importer must reject unknown material states, record raw and normalized units separately, verify conversion dimension, and keep the original source text/number when rights permit. For tables, validate row counts and ordering, normal ranges, missingness, scale factors and numeric parsing, and use read-only immutable snapshots. Multiple source pages can be different displays of the same underlying experiment; do not count them as independent replications. A benchmark dataset designed to verify a numerical solver can be useful for algorithms without proving physical materials performance.

## Versioning and rollback

The common contract includes record ID, revision, source closure, evidence maturity, original ID, rights and typed relationships. In this release all previous Materials record revisions are required to survive byte-identically in the new node. Added records and links get new revisions. No previous source is silently reinterpreted as newly verified. A curated model can be updated in a future release without rewriting old experiments. The source register records what was actually inspected, including access failures and partial views.

**Quality test:** can a consumer distinguish “published rounded table matches the local Shomate calculation” from “a real manufactured copper heat sink meets its service requirement”? If not, the record packaging has lost scientific meaning even when its JSON schema passes.


---

# 32. Materials Atlas v1 content acceptance and the full collection

## Version numbers must indicate the class of milestone

The `1.0.0` label here denotes a **scoped scientific reference content edition**: a stable, installable materials knowledge node covering the declared foundations and method families, with source-attributed explanations, reproducible publisher calculations, explicit synthetic examples, and bounded scientific tools. It does not mean a complete encyclopedia of materials science, certified materials property database, engineering approval or independent reproducibility of physical experiments.

## v1 content scope

The current reference teaches material identity and provenance; crystallography/diffraction; processing and microstructure; thermodynamic stability and idealized phase diagrams; mechanical data interpretation; thermal expansion and conduction; diffusion and phase transformations; fatigue and fracture; coupon corrosion loss; creep; weakest-link fracture statistics; thermochemical compilation reproduction; materials evidence ledgers and method-selection refusal. Authentic reproducible **numerical** work consists of NIST Hahn1 transcribed observation analysis and the selected NIST copper Shomate compiled-fit checks. A numerical match does not imply an independent experiment or a genuine specimen qualification.

The program includes additive equations only when scope is explicit. Do not confuse a synthetic interaction parameter with a CALPHAD assessed value, use a stress-intensity factor outside appropriate mode/geometry, predict rupture from a creep rate, treat an ordinary Weibull fit as a physically valid volume-scaling law, or apply the NIST elemental-copper solid fit to arbitrary copper products. Each computation returns limits, not merely a number.

## Still outside the content scope

**Real specimen datasets and certified properties:** acquisition with original transport hashes where permissible; provenance including grades, specimen conditions, standards and raw uncertainty. **Advanced material theories:** multicomponent CALPHAD assessed parameters, DFT benchmark workflows, phonons and electron transport, nonlinearity in composites, corrosion electrochemistry, kinetic Monte Carlo and uncertainty-aware microstructure simulation. **Scientific approval:** domain-expert review of release-critical derivations and source locators, and design/qualification testing. **Deployment:** real Windows host, live Bitwork route and AI answer-quality evaluation across the complete 30-domain collection.

These outstanding items are transparent backlog rather than a claim of zero uncertainty. Source records may be compiled, transcribed or abbreviated; no source URL or file hash by itself confirms the underlying material. The next content domain can begin while these cross-cutting gates remain deferred, as the owner explicitly directed.

## Handoff contract

The collection retains the original Signal, Cymatics, Measurement and Causal snapshots, and the shared retrieval contract. The new Materials node is a separate package and corpus. Routing itself is unchanged. Only after **all thirty** planned domain references exist will the program implement and evaluate Bitwork-powered routing, then test the integrated system and transfer the collection to the user's computer. No copy to GitHub, desktop or global skills is implied by saving this release in the Library.

**Release veto:** if a new record loses the original source and scope, a published rounded target fails without an explicit discrepancy, a numerical function silently extrapolates, a prior record revision changes, a required schema fails, or the extracted archive does not reproduce its tests, the content package must remain a candidate rather than a final 1.0 release.


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

The published seven-parameter rational function evaluated on the local checked transcription reproduces NIST's certified RSS (about 1.5324382854). That verifies a specific numerical calculation at supplied parameters. It does not independently verify the source acquisition, model adequacy, coefficient units, sample processing or measurement uncertainty.

This increment adds descriptive residual bins ordered by temperature, not by time. For eight bins, each contains a nearly equal number of observations; each reports its temperature range, mean residual and RMSE. We also report a temperature-neighbor residual correlation but explicitly **do not** label it temporal autocorrelation or evidence of instrument drift. A residual pattern can be a reason to investigate model inadequacy, not proof of a particular physical mechanism.

**Reproduce:** `python -m materials_atlas hahn-diagnostics` and `python tools/phase_diffraction_oracle.py`. The first uses the existing published-data capture; the second recomputes bin statistics using NumPy as a separate implementation. Both keep original upstream-byte acquisition and response-scale verification open.

**Further evidence needed:** original NIST data-file bytes, independent source audit, a justified response unit multiplier, test specimen identity, uncertainty budget and a predeclared external validation set. This is a useful benchmark for software correctness, not a new materials-science discovery.


---

# Investigation 12 — NIST copper thermochemistry reproduction

**Question.** Can the Materials Atlas reproduce a second published numerical representation, separate from Hahn1's regression observations, while keeping its domain explicit?

**Authoritative source.** NIST WebBook, SRD69, copper, solid-phase Shomate representation 298–1358 K, Chase 1998. The source reports a compiled fitted representation, not direct observations from this Atlas. The coefficients and six two-decimal display rows are recorded only as needed to reproduce selected checks, with attribution; the full copyright-marked compilation is not mirrored. [Primary link](https://webbook.nist.gov/cgi/inchi?ID=C7440508&Table=on&Type=JANAFS).

**Reproduction method.** Use t=T/1000 in the published Cp, H relative to 298.15 K, S formulas; verify heat capacity in J/(mol K), enthalpy in kJ/mol and entropy in J/(mol K). Evaluate 300, 400, 500, 700, 900 and 1300 K. Each row has three independent displayed quantities, giving 18 narrow numerical comparisons. The maximum observed absolute difference from the two-decimal displays is approximately **0.00487735** in each field's respective unit, inside a predeclared tolerance of 0.00501. This is a rounding/display comparison; **not** 18 independent experimental measurements.

**Independent functional identity.** For an interior temperature T, numerically differentiate H(T) against T and check Cp, with 1000 J/kJ scaling. Alternatively integrate Cp(T)/1000 from 400 to 900 K using a separate quadrature algorithm and compare the answer **13.3665058843 kJ/mol** to H(900)−H(400). A successful identity validates the formula implementation in this domain, not the underlying source assessment.

**Counterexample.** Asking for Cp at 1500 K must fail: that temperature is beyond the published **solid phase** fit even though the same NIST page provides separate **liquid** data. Do not silently switch phases; the transition enthalpy cannot be inferred by continuing a single solid fit. Similarly, a named copper alloy, composite or specimen does not inherit elemental-copper coefficients without measurement/model justification.

**Provenance.** No original HTTP transport bytes were authenticated. Checked date 2026-11-12. Numerical facts were read from the publisher HTML; this package stores a local normalized computation record, not a complete NIST source snapshot. NIST's displayed coefficient rounding precludes a separately justified coefficient uncertainty. The previous Hahn1 response-unit ambiguity remains untouched.

**Outcome.** Successful narrow computational reproduction; no material property qualification, laboratory replication, or permission to extrapolate.


---

# Investigation 13 — Correct mass loss does not establish maximum corrosion damage

**Stated observations:** none. The input is a constructed laboratory coupon scenario, not a published experiment or field sample. A hypothetical specimen starts and ends with a corrected mass loss of 0.1 g, has 100 cm² exposed area, is immersed for 240 h, and has an assumed density of 7.8 g/cm³.

**Model.** Equivalent average uniform penetration `87600 W/(Aρt)` gives **0.0467948718 mm/year**. This equals geometric conversion of the hypothetical loss into a mean thickness. A second hypothetical coupon losing 0.2 g under identical conditions returns exactly twice the average rate. The software unit tests check proportionality and reject negative loss and zero area/duration/density.

**Failure mode.** Suppose almost all attack is concentrated at one small crevice. The same overall mass loss could be compatible with a deep local pit or a shallow uniform film because the mass integral does not uniquely specify its spatial distribution. The output must therefore never be relabeled as the maximum pit depth, minimum remaining wall thickness, or safe-life estimate. A specimen with zero resolved mass loss also does not prove absence of galvanic or localized damage.

**What would be needed.** Full solution and specimen preparation records, cleaning/blank corrections, initial and final calibrated masses, cross-sectional damage mapping, pit-depth distribution, exposed-area map, replicate specimens, microstructural information, and actual service environment. A governing corrosion standard may require licensed access and qualified execution.

**Source inspection boundary.** The formula and 8.76×10⁴ mm/y factor occur in a NIST-hosted presentation attributed to Sowards and Mansfield, referencing ASTM G31. The text was retrieved, but web PDF screenshot verification failed due to cache access. This release records that limitation; it does not claim a fully inspected current ASTM practice. [NIST source link](https://www.nist.gov/system/files/documents/mml/acmd/2013-07-22-Corrosion-of-Copper-and-Steel-Alloys-Sowards.pdf).

**Outcome:** a verifiable arithmetic teaching case coupled to a required refusal on localized failure or remaining service life.


---

# Investigation 14 — The interface dominates a two-layer heat path

A hypothetical device has two layers conducting in one dimension over 0.1 m². Layer 1 is 1 mm thick with assigned conductivity 200 W/(m K); layer 2 is 5 mm thick with assigned conductivity 1 W/(m K). The applied temperature difference is 50 K, and a declared contact resistance is 0.3 K/W.

The resistances are `0.001/(200×0.1)=0.00005 K/W` and `0.005/(1×0.1)=0.05 K/W`. Total resistance is **0.35005 K/W**, giving **142.8367376 W** by the steady 1D model. Without the contact resistance, the same geometric formula would give about 999 W: a warning against treating catalogue bulk conductivity as interface conductance.

These are chosen numbers, not an actual thermal-interface test. Neither thickness nor conductivity is known to represent a specific product. Heat flow can change with thermomechanical contact, temperature-dependent conductivities, convection, radiation and side leakage. The calculator cannot infer a device safe temperature or prevent a burn, fire or equipment failure. It can highlight which missing measurement is likely important.

A real investigation would record sample thickness under actual compression, thermal-contact conductance at assembly pressure, temperature profile, contact area, environmental boundary temperatures, sensor position and calibration, dissipated power, transient history and repeated mounting. Anisotropy or a three-dimensional heat field may require a different model entirely.

The calculation rejects zero thermal conductivity, negative thickness, or missing layers and returns model assumptions with the numeric result. The result can inform a test plan but does not certify a component.


---

# Investigation 15 — Isothermal fraction inversion versus a real heat-treatment schedule

Consider a purely invented isothermal transformation with rate parameter `k=0.001 s⁻¹` and exponent `n=2`. Applying `X=1−exp[−(kt)^n]`, solving for X=0.5 gives **832.554611 s**. Substituting this time in the forward equation reproduces the fraction. This is exact algebra under a stipulated model, not a measured steel or polymer kinetic response.

Now imagine an operator changes temperature during the hold. The formerly fitted k is not guaranteed to apply: nucleation, growth, diffusivity, activation energy and phase pathways may differ at each temperature. The same final elapsed time does not guarantee the same final fraction. Applying the old isothermal formula to a nonisothermal cycle is an *unverified extrapolation*, not a small computational error.

To make a real heat-treatment decision, obtain a time-temperature history, representative microstructure, composition, nucleation constraints, phase fraction measurement method and quality, actual process kinetics, confidence bounds and possibly TTT/CCT measurements. A process controller's set-point log is not necessarily the specimen thermal record.

The Atlas calculator returns a conditional fraction only. It refuses exact fraction 1 when solving for finite time because this ideal law approaches 1 asymptotically. This protects evidence boundaries rather than inventing a finish time. Real heat-treatment qualification must use calibrated kinetics and relevant standards.


---

# Investigation 16 — A factor-of-eight creep-rate change is not eightfold risk

Take hypothetical Norton–Arrhenius parameters A=1e−8 s⁻¹ MPa⁻³, n=3, Q=200 kJ/mol, T=900 K. For 50 MPa the modeled steady creep strain rate is about **3.0863×10⁻¹⁵ s⁻¹**. Doubling stress to 100 MPa multiplies the model rate by eight because n=3. The numerical factor is entailed by an assumed power law, not proof that any metal follows it in service.

**Invalid conclusion:** “therefore the part will fail eight times faster.” Rupture-time, tertiary acceleration, necking, grain-boundary damage, oxidation and stress redistribution are not in this model. Even cumulative constant-rate strain `ε≈εdot t` is not a creep failure criterion. Environmental and load histories can dominate a real application.

A sound report would identify actual material heat, processing, sample size and geometry, creep-test curves, strain gauge calibration, stress and temperature control, duration, fitted parameter covariance, mechanism validity and extrapolation bounds. Without that evidence, a time-to-failure output is intentionally unavailable. The calculator accepts the parameter units explicitly and refuses nonpositive temperature and numerical underflow rather than declaring a truly zero creep rate.

**Outcome:** a bounded kinetics teaching tool and a clear line between calculation and prognostics. Control Atlas (queued) will later address changing stress/temperature over time, but cannot create missing material test evidence.


---

# Investigation 17 — Can coupon strength be scaled to twice the volume?

A fitted Weibull curve for failure stress is not automatically a physical weakest-link fracture law. The publisher abstract of a 2020 *Ceramics International* review explicitly distinguishes the ordinary empirical distribution from Weibull fracture theory. [Abstract and DOI](https://www.sciencedirect.com/science/article/pii/S0272884220313092). No full article was mirrored or claimed inspected.

**Constructed conditional model.** Assume physically independent identical bulk flaw populations over elemental volume, uniform tension, and survival `S=exp[−(V/V0)(σ/σ0)^m]`. For σ=120 MPa, σ0=200 MPa, m=5, V=V0=1000 mm³, survival is **0.925186445**. At twice the volume with the same stated law, survival is **0.855969957**, the square of the first result. This illustrates how a physical failure mechanism could imply size dependence.

**Critical alternative.** If observed failure originates from surface machining flaws, the number and severity of critical flaws may scale with stressed surface area, not bulk volume. Residual stress, flaw orientation or spatial stress gradients also break the simplified bulk-volume form. Two samples of equal material chemistry could have different strength distributions due to finishing or geometry. The calculator therefore refuses any volume scaling until a caller explicitly asserts the bulk weakest-link hypothesis. Assertion is **not verification**.

A real component-strength prediction requires measured specimen failure statistics, failure-origin fractography, correct loading geometry, sampling uncertainty, environmental sensitivity and appropriate design standards. The Atlas does not infer characteristic strength from a tensile curve or provide a certified failure probability.

**Outcome:** computed conditional probabilities only, not reliability qualification. The default abstention prevents a misleading transfer from empirical statistics to structural reliability.


---

# Investigation 18 — Two records named copper are not interchangeable

**Input A:** NIST StRD Hahn1, a numerical benchmark that reports 236 experimental observations and certified nonlinear least-squares parameters. It is used here to check the implementation of regression and residual calculations. The local capture is a checked transcription; the response numerical scale is unresolved.

**Input B:** NIST Chemistry WebBook copper solid-phase Shomate compilation, which reports Cp, relative H and S across 298–1358 K, using a published thermodynamic fit. It is not the same test and does not measure the Hahn1 regression response.

A naive keyword router could select both because they mention copper and temperature, then blend them into a synthetic material constant. The Atlas forbids such an inference: the two evidence types, response dimensions, data provenance and material-state qualifications differ. They are separately source-linked records and are meant to be retrieved with their qualifiers and exclusion criteria.

**Demonstration:** request a change in molar enthalpy of pure solid copper from 400 to 900 K. The WebBook fit yields approximately 13.3665 kJ/mol. Hahn1 cannot answer that request because its benchmark response is not molar enthalpy and its numeric scale is not authenticated. Conversely, requesting the residual pattern of the Hahn1 regression should not invoke WebBook heat-capacity coefficients.

**Required records:** type of measurement/compilation, physical quantity and units, phase, composition, temperature range, source inspected section, source-release hash (if original bytes exist), local capture hash, calculation implementation, and flags for incomplete source authentication. A correct shared navigation system must carry this information intact after all 30 domains are built. This checkpoint does not implement or test Bitwork routing.


---

# Investigation 19 — A material recommendation requires a study, not just property rankings

A manufacturing engineer asks whether to switch to an alternative alloy for a hot corrosive component. The available material entries show nominal thermal conductivity, published room-temperature tensile strength, a synthetic corrosion rate, and an uncalibrated steady-creep formula. No heat/lot certification, temperature-resolved creep measurements, service chemistry, geometry, loading spectrum, local damage inspection, or design-code requirements are provided.

**What can be calculated:** a heat-flow ranking under supplied one-dimensional assumptions, an equivalent mass-loss corrosion rate from corrected coupon values, and a conditional strain-rate from chosen creep parameters. **What cannot be established:** which alloy is safer, if the part meets service life, or whether corrosion is localized. A DFT formation-energy hull cannot supply this missing evidence either.

**Study design:** (1) define the failure modes and load/temperature history; (2) identify exact candidate alloys, product form, condition and lot; (3) measure or source suitably comparable temperature-dependent properties; (4) evaluate corrosion under representative medium and flow with local morphology; (5) review welds and manufacturing effects; (6) model coupled thermal, mechanical and chemical conditions with sensitivity analyses; (7) compare against applicable qualification requirements; (8) run independent engineering review and specimen tests where warranted.

**Decision record:** `insufficient_evidence_for_material_substitution`. Missing entries remain blank, and neither source ratings nor test counts are substitutes for traceability. This refusal is a useful scientific output: it identifies the observations and assumptions required to turn a plausible model into a defensible engineering conclusion.


---

## Source and release policy
All third-party publishers retain their rights; included text is original synthesis with attribution and selected factual numbers. Use linked primary sources for controlling standards. Uninspected source portions are not called reviewed. The NIST-hosted corrosion PDF screenshot was requested but unavailable; this is not presented as a complete PDF review.
A computation that matches a published display is a numerical reproduction, not a repeat of the publisher’s laboratory experiment. Measurements and compiled thermodynamic fits carry different evidence classes. The other four nodes are unchanged; routing/Bitwork and desktop transfer remain deferred until all 30 domain libraries are built.
