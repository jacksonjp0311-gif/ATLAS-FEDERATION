# Manufacturing Atlas — 14 deterministic constructed investigations

Run `python -m manufacturing_atlas`; its JSON outputs are recomputed by the standard-library reference models.

The cases intentionally use finite synthetic inputs without machine-specific parameters. They address nominal clearance, interval stack, thermal length, machining estimates, structural compliance, lead screw reachability, process-capability HOLD, inspection guardbands, linear calibration, DAG planning, ideal casting scale, additive height, discrete roughness, and first-order thermal dynamics.

No case is an industrial acceptance test or physical experiment.


# Manufacturing v0.2.0 — Twelve new constructed investigations

## Investigation 19: Why covariance must be positive semidefinite

Reimplement `covariance_budget_psd` using the stated equation `u_y² = aᵀ Σ a, and Σ must be symmetric PSD` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 20: Inspection guard bands and conditional false acceptance

Reimplement `normal_inspection_acceptance_risk` using the stated equation `P(accept | actual x)=Φ((USL−g−x)/σ)−Φ((LSL+g−x)/σ)` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 21: Process stability is a prerequisite to capability

Reimplement `stable_process_capability` using the stated equation `Cp=(USL−LSL)/(6s), Cpk=min(USL−μ,μ−LSL)/(3s)` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 22: Finite-sample yield is not guaranteed reliability

Reimplement `wilson_yield_interval` using the stated equation `p_hat=k/n; Wilson 95% lower bound < 1 even when k=n` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 23: An unbroken metrology chain needs real evidence

Reimplement `traceability_chain_audit` using the stated equation `measurand → instrument → lab reference → SI realization, each with uncertainty` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 24: Datum frames connect drawings to measured coordinates

Reimplement `datum_rigid_transform_xy` using the stated equation `[X,Y]ᵀ = t + s R(θ)[x,y]ᵀ` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 25: A feasible process plan is not an optimal factory schedule

Reimplement `resource_bounded_schedule` using the stated equation `start_i >= max(end_dependencies,resource_free_time); end_i=start_i+duration_i` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 26: Mass and energy constraints are reconstruction invariants

Reimplement `manufacturing_atlas.models.cutting_estimate; resource_bounded_schedule` using the stated equation `m_in=m_part+m_scrap+m_recoverable+Δinventory; P=energy/time` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 27: Evidence-carrying process plans refuse unsupported completion

Reimplement `manufacturing_evidence_gate` using the stated equation `ready_i = inputs_present ∧ required_evidence_present ∧ all_dependencies_ready` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 28: Manufacturing prerequisites for silicon gates and integrated circuits

Reimplement `manufacturing_evidence_gate; electronics-atlas method prerequisites` using the stated equation `materials→geometry→fabrication→metrology→device IV/CV→cell delay→logic` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 29: Repairs must regenerate qualification evidence

Reimplement `manufacturing_evidence_gate; covariance_budget_psd` using the stated equation `postrepair acceptance = spec ∧ traceable_measurement ∧ evidence_of_changed_components` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

## Investigation 30: An auditable chain from physical parts to computing

Reimplement `manufacturing_evidence_gate; electronics_atlas.v1_scoped_models.EightBitAccumulator` using the stated equation `reconstructible claim = science_reference ∧ manufacturing_evidence ∧ hardware_measurement ∧ verified_computation` and an independent oracle. Test a passing synthetic case, a deliberately invalid case and a missing-measurement HOLD. Record assumptions and units. These are constructed software investigations, not manufactured samples.

