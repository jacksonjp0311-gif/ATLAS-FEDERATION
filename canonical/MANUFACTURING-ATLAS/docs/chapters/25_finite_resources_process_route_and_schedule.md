# Chapter 25: A feasible process plan is not an optimal factory schedule

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`start_i >= max(end_dependencies,resource_free_time); end_i=start_i+duration_i`

## Scientific derivation and engineering reasoning

A real production route is a dependency graph with both precedence and finite resource constraints. A simple topological critical path determines a lower bound on completion time but can underestimate makespan when two operations compete for the same spindle, metrology station or operator. Resource-constrained scheduling must assign start and end times without violating prerequisites or machine occupancy.

The reference uses deterministic list scheduling on a DAG with each resource treated as unary. The recurrence starts each task no earlier than both its latest predecessor completion and its assigned resource's previous availability. It explicitly reports that the result is feasible, **not provably optimal**. It ignores changeover costs, worker constraints, maintenance, urgent jobs, yield, rework, batch setups and machine breakdowns.

Constructed example: a cutting task A=3 minutes and B=4 minutes share one station. Their combined occupied time is at least 7 minutes regardless of precedence. With a separate inspection task C depending on A, C may overlap B only if it uses a different resource. Deterministic schedules must be checked independently against resource occupancy and precedence, not trusted because a list of operations exists.

A future planner should include measured process time distributions, scrap probabilities, safety and energy constraints before scheduling an actual factory.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.resource_bounded_schedule`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Schedule outputs are not shop-floor safety authorization or throughput forecasts.

Bibliography card: `NIST-STAT-CAPABILITY`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
