# Chapter 17 — Fracture intensity, crack growth, and why a rate is not lifetime

Linear-elastic mode-I stress intensity can be represented as `K_I = Y sigma sqrt(pi a)` where Y is a dimensionless factor for a **particular** geometry and crack-length convention, `sigma` is a nominal tensile stress and `a` is the crack parameter used by Y. `materials_atlas.advanced.fracture_mode_i` returns MPa·sqrt(m) from MPa and m. It explicitly does not infer the geometry factor from a component photo, identify an actual crack length, or guarantee a small-scale-yielding region.

Fracture toughness `K_IC` is not interchangeable with any measured `K` number. Valid plane-strain toughness determinations require standard-specific sample dimensions, crack preparation and test conditions. A toy inequality `K_I >= K_IC` is insufficient to declare component failure: plasticity, geometry correction, defects, loading rate, mixed mode, temperature, residual stress and uncertainty matter. Likewise, threshold comparisons below `K_IC` do not prove indefinite safety.

In an empirically identified intermediate fatigue regime the Paris relation may be written `da/dN = C (Delta K)^m`. The coefficient C's units **depend on m and the chosen length units**; the exponent and coefficient must be fitted to matching material, environment, load ratio and regime. The implemented `paris_fatigue_rate` calculates a rate only when ΔK is inside the supplied valid interval. It refuses values outside that domain. No integration across unknown geometry, changing load histories, thresholds or rapid-fracture regime occurs.

## Failure-mode example

With synthetic `sigma=200 MPa`, `a=1 mm`, and supplied `Y=1`, K_I ≈11.21 MPa·sqrt(m). It is a bounded stress-intensity calculation, not crack growth or failure probability. A second synthetic law with `C=10^-7` (mm/cycle)/(MPa·sqrt(m))³, `m=3`, ΔK=10 yields `10^-4 mm/cycle` but only within the declared 5..20 MPa·sqrt(m) range. Calculating an end-of-life cycle count from that single rate without propagation of changing ΔK would be scientifically misleading.

## What a real damage investigation needs

Quantified crack geometry/orientation, nondestructive inspection uncertainty, local stress range and residual stress, actual fatigue loading and R ratio, environment/corrosion, fracture-surface evidence, metallurgical processing and heat treatment, validated material toughness and crack-growth data, component-specific design procedures, and independent approval. Absence of these inputs should lead to a refusal or a request for measurements rather than a fabricated safety margin.

**Source boundary:** These are standard analytical definitions and authored examples. The restricted contents of fracture and fatigue standards are not reproduced. The present edition has no measured crack-growth dataset or experimentally reviewed component model.
