# 40. Storage fire safety and thermochemical limits

**Area:** Storage · **Edition:** Energy Atlas v0.2.0 · **Evidence type:** author-original explanatory research, source pages inspected only in described scope. **No real equipment operated.**

## Definitions, problem and physical system boundary

Electrochemical storage contains energy in materials that may react during failure. Thermal runaway, venting, flammable gases, propagation between cells and inadequate fault isolation are separate hazard pathways. Safe system design requires independent evidence for cell chemistry, pack architecture, state of charge, thermal environment, ventilation, fire detection, spacing, response plans, and local regulation. Calculated voltage, capacity or round-trip efficiency does not verify any of these. The 2026 NFPA 855 standard contains installation and emergency-response requirements; its content remains copyrighted and was not copied into this library. EPA public guidance describes battery incidents and safety standards, but neither document constitutes certification of an unspecified design.

## Equation, symbols and dimensional units

`Energy available for release is not a fire-risk probability. E_chemical ≈ V_nominal*Ah (Wh) under a crude electrical nameplate model, not a heat-release-rate or explosion calculation.`

The variable names and input units are part of the model; for power/energy calculations W and Wh must not be exchanged. A correct mathematical result is conditional on the stated boundary, not the presence of actual calibrated data.

## Derivation, physical assumptions and proof of accounting

An electrical energy label reports nominal electrical work under an operating convention. During abuse or failure, heat can also arise from exothermic chemical pathways, so equating electrical nameplate energy to maximum fire heat release is unjustified. Accurate hazard assessment requires measured calorimetry, gas composition, cell and pack standards, and independent validation. A simplified charge/discharge model must never infer thermal-runaway thresholds or fire-suppression actions.

## Hand reconstruction and independent calculation

Read a hypothetical pack label of 48 V and 100 Ah and compute 4.8 kWh nominal electrical capacity. Record that the calculation does not say the pack is safe, whether it has protection, how it would behave under a short circuit, or its energy under failure. Build a source card listing manufacturer documents and applicable qualified tests needed before any physical evaluation.

The numbered values are **authored example inputs**, not measured site or equipment performance. Reproduce them with the pure-Python library where a named method exists, then inspect the counterexample.

## Counterexample, unresolved evidence and limits

Lithium battery faults can escalate rapidly. The package contains no DIY battery-building, short-circuit, cell venting or suppression instructions. Energy accounting does not establish electrical or fire safety.

## Life safety and operational boundary

Real battery installation and emergency response require current codes, certified hardware and local competent authorities; no remote model supplies permission or safety certification.

## Source navigation and preservation debt

- **U.S. EPA, Battery Energy Storage Systems Safety and Incident Response:** https://www.epa.gov/electronics-batteries-management/battery-energy-storage-systems-main-considerations-safe — Battery fire response, community planning, relevant standards; no site engineering standard reproduced
- **NFPA 855, Stationary Energy Storage Installation Standard, 2026 edition:** https://www.nfpa.org/product/nfpa-855-standard/p0855code?l=134 — Product description and 2026 edition overview only; standard is copyrighted and full clauses were not acquired
- **DOE Energy Storage Strategy and Roadmap:** https://www.energy.gov/oe/energy-storage-strategy-and-roadmap — Energy storage technology and deployment; cross-technology requirements

These are scoped citations and original explanations, **not** authenticated original publisher files or a construction authorization. The missing source bytes are recorded in the source-acquisition register.
