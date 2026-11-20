# Investigation 07 — A stress-intensity number is not a service-life estimate

**Origin:** original constructed calculation. Take a hypothetical tensile stress 200 MPa, crack parameter a=0.001 m and known geometry factor Y=1. A linear-elastic mode-I model gives K_I ≈ 11.21 MPa√m. That result answers only the mathematical question under the stated crack convention; geometry factor selection, residual stress, yield behavior, and defect uncertainty are not verified.

For a separate hypothetical Paris-regime law, choose C=10⁻⁷ [mm/cycle]/[MPa√m]³, exponent 3, and ΔK=10 MPa√m in a stipulated validated 5–20 MPa√m interval. The computed growth rate is 10⁻⁴ mm/cycle. At 30 MPa√m, the calculator **refuses** the request: crossing outside the supplied empirical regime invalidates the simple equation, even though numerical exponentiation is easy.

The two toy models are intentionally **not** combined into one cycle-to-failure or safety claim. Such a claim requires variable crack geometry, actual stress cycles, crack-growth resistance, threshold behavior, large-scale plasticity limits and validation of the Paris law regime. A point rate and a point intensity cannot be equated to a certified fatigue life.

A human investigation should include metallographic inspection, geometry qualification, load spectrum, cyclic stress ratio, temperature, environment, base-metal and welded zones, residual stress, non-destructive inspection limits, standard-specific fracture testing, and reviewed uncertainties. The final AI answer should be framed as a calculation with missing prerequisites, not an engineering sign-off.
