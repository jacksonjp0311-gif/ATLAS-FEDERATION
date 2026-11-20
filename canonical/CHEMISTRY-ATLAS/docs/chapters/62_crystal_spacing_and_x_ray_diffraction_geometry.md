# 62. Crystal spacing and X-ray diffraction geometry

**Theme:** Materials characterization · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Crystalline materials are ordered arrangements with periodic atomic structure. X-ray diffraction can produce characteristic angles from constructive interference between crystallographic planes. The Bragg relation is a geometric inference using wavelength and scattering angle; the output is a lattice-plane spacing under the stated assumptions. It does not identify a compound or certify material purity. Real XRD analysis requires instrument calibration, phase indexing, grain size and strain, preferred orientation, and reference patterns. Those inputs are often available in commercial or scientific crystallographic data collections with rights and provenance restrictions.

## Governing relationship and dimensional conventions

`n lambda=2 d sin(theta), theta the Bragg angle (half a reported 2theta instrument angle), not necessarily a direct peak label.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

For coherent elastic scattering from parallel crystallographic planes, the path difference for waves reflected by adjacent planes is 2d sin theta. Constructive interference at integer wavelength multiples yields the Bragg relation. Reversing it yields d=n lambda/(2 sin theta). Because sin theta is monotonic between zero and ninety degrees, a higher Bragg angle at fixed wavelength yields smaller d. Multiple structures can share one spacing, so a single diffraction peak is not uniquely identifying.

## Original worked investigation

At lambda=0.15406 nm and theta=30°, compute d=0.15406 nm for first-order reflection. Then explain why an instrument that reports 2theta=30° requires converting to theta=15° before using the same formula. The resulting spacing differs without any change to the crystal.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

No X-ray exposure, instrument operation, crystallographic phase identification or material safety is performed in this atlas. Source data and measurement uncertainties remain unverified.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/)
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
