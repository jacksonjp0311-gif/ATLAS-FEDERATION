# Chapter 16 — One stress–strain point does not describe a material's tensile response

Tensile reporting is a chain of measurements and definitions, not one number. The force measurement needs calibration, initial cross-sectional area needs measured dimensions, displacement/strain requires gauge length and a validated extensometer, and a complete result depends on the test procedure, specimen orientation, temperature and strain rate. ASTM E8/E8M-25 identifies yield behavior, tensile strength, elongation and reduction of area as reportable outcomes and warns that machined specimens may not represent an entire finished product. This Atlas does not reproduce or claim conformance with the paywalled standard.

Engineering stress is `F/A0`, while engineering strain is `Delta L/L0`. The `engineering_tensile_point` method provides these arithmetic quantities for one supplied point, without identifying modulus, yield, ultimate tensile strength or failure. A complete stress–strain curve requires a sufficiently resolved trace from which properties can be calculated by a predeclared procedure. `E` is a slope in a justified elastic region; it is not a fit to arbitrary high-strain points. A 0.2% offset yield crossing requires an appropriately established elastic line and sampling across the intersection.

Under *uniform deformation and approximately constant volume before necking*, one often uses `sigma_true = sigma_engineering (1 + e)` and `epsilon_true = ln(1 + e)`. Our calculator explicitly requires the caller to affirm that restriction. Once local necking begins, the local true stress depends on the actual local cross-sectional area and more complex correction; blindly continuing the conversion is unjustified. This is a transformation of definitions and assumptions, not new material data.

## Example

For synthetic engineering stress 400 MPa and engineering strain 0.05 in a declared pre-necking state, the calculator yields 420 MPa true stress and `ln(1.05)` ≈ 0.048790 true strain. It does not infer yield, strength of another specimen, or ductility. If the uniform-deformation premise is omitted or false, it refuses the conversion rather than returning a plausible but ungrounded number.

A useful AI context packet includes original force–displacement, corrected specimen dimensions, strain instrumentation, measurement rates, calibration/uncertainty, specimen direction, fracture location and repeatability across specimens. Any available curve needs acceptance by the person responsible for the actual standard's requirements; calculator tests do not qualify a product.

**Source:** ASTM International E8/E8M-25, publicly accessible scope and limitations, `https://store.astm.org/standards/e8_e8m`.
