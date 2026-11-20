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
