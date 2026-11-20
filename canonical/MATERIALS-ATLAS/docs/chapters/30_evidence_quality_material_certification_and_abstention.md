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
