# 57. Photon energy and semiconductor band-gap physics

**Theme:** Photonics and electronics · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

Semiconductors form the physical substrate of modern digital computing, data storage, imaging and many AI accelerators. Optical absorption and emission depend on electronic band structure and photons. The basic quantum relation E=h nu=hc/lambda connects a wavelength to photon energy. A photon whose energy exceeds a material band gap has sufficient energy for certain electronic transitions, but optical selection rules, phonons, excitons, defects and surfaces determine whether absorption actually occurs. Band gaps are temperature- and material-dependent; they are not universal constants that can be inserted without source data.

## Governing relationship and dimensional conventions

`E_gamma=hc/lambda; E_gamma[eV]=hc/(lambda q_e). Compare E_gamma to an assumed Eg[eV] while retaining optical transition restrictions.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

The photon relation follows from Planck's quantization and the vacuum relation nu=c/lambda. Converting joules to electronvolts uses elementary charge in coulombs, whose SI numerical value is exact. The comparison is only an energetic test; it does not identify a material or establish a quantum efficiency. A future chip designer needs semiconductor material data, lattice defects and carrier properties before drawing engineering conclusions from band-gap arithmetic.

## Original worked investigation

At an invented 500 nm vacuum wavelength, calculate photon energy in joules and electronvolts. Compare to a stipulated Eg=2 eV and note that the result gives an energetic possibility, not measured photoconductivity. Repeat at 1000 nm and explain why the energetic comparison changes.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

Does not implement detailed absorption spectra, temperature broadening, junction behavior or photoresponse. No source-defined device performance or usable semiconductor process inferred.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/)
- [NIST/CODATA 2022 recommended constants, 2025 paper](https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
