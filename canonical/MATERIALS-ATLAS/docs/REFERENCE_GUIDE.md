# Materials Atlas v1.0.0 — Reading guide
**Composition → Processing → Structure → Properties → Performance → Evidence.**
Use the scoped chapter and case, then check its cited source card and limitations before reusing any quantitative conclusion.

## Chapters 1–23: preserved reference foundations
Includes identity, lattice/diffraction, phase stability, mechanical and thermal properties, source reproducibility, diffusion, fracture/fatigue, regular-solution modeling, indexed cubic diffraction and NIST Hahn1 residuals.
- [scope evidence and comparability](chapters/01_scope_evidence_and_comparability.md)
- [composition bonding and material identity](chapters/02_composition_bonding_and_material_identity.md)
- [lattices cells diffraction and uncertainty](chapters/03_lattices_cells_diffraction_and_uncertainty.md)
- [processing microstructure defects](chapters/04_processing_microstructure_defects.md)
- [phase equilibria and the lever rule](chapters/05_phase_equilibria_and_the_lever_rule.md)
- [thermodynamic models and phase stability](chapters/06_thermodynamic_models_and_phase_stability.md)
- [mechanical behavior and standardized testing](chapters/07_mechanical_behavior_and_standardized_testing.md)
- [thermal expansion and transport](chapters/08_thermal_expansion_and_transport.md)
- [composites mixtures and orientation](chapters/09_composites_mixtures_and_orientation.md)
- [degradation fatigue fracture and service](chapters/10_degradation_fatigue_fracture_and_service.md)
- [computed versus measured reproducibility and versioning](chapters/11_computed_versus_measured_reproducibility_and_versioning.md)
- [decision ledger and cross-domain reuse](chapters/12_decision_ledger_and_cross-domain_reuse.md)
- [source data and reproduction](chapters/13_source_data_and_reproduction.md)
- [temperature dependent properties](chapters/14_temperature_dependent_properties.md)
- [diffusion and kinetics](chapters/15_diffusion_and_kinetics.md)
- [tensile properties and conversion](chapters/16_tensile_properties_and_conversion.md)
- [crack mechanics and fatigue](chapters/17_crack_mechanics_and_fatigue.md)
- [evidence bound decisions](chapters/18_evidence_bound_decisions.md)
- [research coverage and backlog](chapters/19_research_coverage_and_backlog.md)
- [regular solution phase boundaries](chapters/20_regular_solution_phase_boundaries.md)
- [cubic diffraction and uncertainty](chapters/21_cubic_diffraction_and_uncertainty.md)
- [hahn1 residual diagnostics](chapters/22_hahn1_residual_diagnostics.md)
- [methods status and falsification](chapters/23_methods_status_and_falsification.md)

## Chapters 24–32: scoped v1 content completion
- [nist copper solid thermochemistry](chapters/24_nist_copper_solid_thermochemistry.md)
- [corrosion penetration and localized failure](chapters/25_corrosion_penetration_and_localized_failure.md)
- [multilayer heat flow and interface conditions](chapters/26_multilayer_heat_flow_and_interface_conditions.md)
- [isothermal transformations and non isothermal limits](chapters/27_isothermal_transformations_and_non_isothermal_limits.md)
- [creep rates versus life prediction](chapters/28_creep_rates_versus_life_prediction.md)
- [weakest link statistics not automatic reliability](chapters/29_weakest_link_statistics_not_automatic_reliability.md)
- [evidence quality material certification and abstention](chapters/30_evidence_quality_material_certification_and_abstention.md)
- [metrology of materials records and ingestion](chapters/31_metrology_of_materials_records_and_ingestion.md)
- [content release boundary and future interoperability](chapters/32_content_release_boundary_and_future_interoperability.md)

## Nineteen investigations and reproducible calculators
- [diffraction and identity](investigations/01_diffraction_and_identity.md)
- [phase equilibrium and hull](investigations/02_phase_equilibrium_and_hull.md)
- [tensile property context](investigations/03_tensile_property_context.md)
- [thermal interface and selection](investigations/04_thermal_interface_and_selection.md)
- [nist hahn1 copper](investigations/05_nist_hahn1_copper.md)
- [diffusion and temperature](investigations/06_diffusion_and_temperature.md)
- [fracture fatigue boundaries](investigations/07_fracture_fatigue_boundaries.md)
- [materials evidence decision](investigations/08_materials_evidence_decision.md)
- [miscibility gap and metastability](investigations/09_miscibility_gap_and_metastability.md)
- [indexed cubic peaks and shared uncertainty](investigations/10_indexed_cubic_peaks_and_shared_uncertainty.md)
- [nist hahn1 residuals](investigations/11_nist_hahn1_residuals.md)
- [copper webbook thermochemistry](investigations/12_copper_webbook_thermochemistry.md)
- [corrosion coupon nonuniform attack](investigations/13_corrosion_coupon_nonuniform_attack.md)
- [thermal contact stack](investigations/14_thermal_contact_stack.md)
- [isothermal avrami and schedule failure](investigations/15_isothermal_avrami_and_schedule_failure.md)
- [creep rate beyond the test regime](investigations/16_creep_rate_beyond_the_test_regime.md)
- [ordinary weibull vs bulk weakest link](investigations/17_ordinary_weibull_vs_bulk_weakest_link.md)
- [copper identity cross source trap](investigations/18_copper_identity_cross_source_trap.md)
- [material selection refusal and study plan](investigations/19_material_selection_refusal_and_study_plan.md)

## Run explicit methods
```sh
python -m materials_atlas casebook
python -m materials_atlas advanced-cases
python -m materials_atlas published-hahn1
python -m materials_atlas expanded-cases
python -m materials_atlas v1-cases
```
The v1 casebook has 8 new cases, 18 selected published-display numerical targets and synthetic model examples. Retrieved text never executes methods. An independent numerical algorithm checker is `python tools/v1_numerical_oracle.py` (optional SciPy/NumPy); no extra runtime dependencies are required.

## Acceptance
[Scientific coverage and gaps](COVERAGE_MATRIX.md) · [Source register](SOURCE_REGISTER.md) · [Review questions](REVIEW_QUESTIONS.md) · [Templates](TEMPLATES.md) · [Release audit](VALIDATION_v1.0.0.md).
Content v1.0.0 means scoped reference content complete, *not* independent scientific, measurement, safety or deployment acceptance.
