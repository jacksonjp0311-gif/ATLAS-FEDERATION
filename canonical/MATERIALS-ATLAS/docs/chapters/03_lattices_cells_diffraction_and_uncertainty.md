# Chapter 03. Lattices, cells, diffraction and uncertainty

*Evidence maturity: bounded assistant-curated reference, not independently reviewed.*

A crystal description gives a periodic lattice and basis. The unit cell is not the same thing as a grain or physical specimen. For a monatomic cubic lattice, ideal theoretical density is `rho = n M / (N_A a^3)` with a in centimeters; it requires an atom count per cell and molar mass, and assumes a perfect site occupancy. Missing atoms, multiple species, thermal expansion or porosity can invalidate direct identification with a bulk density measurement.

For first-order Bragg diffraction, `2 d sin(theta) = lambda`; published diffractograms typically show `2 theta`, not `theta`. With reflection order `n`, replace the right-hand side by `n lambda`. The relationship locates a spacing *given the indexed reflection and wavelength*. It does not tell you the identity or fraction of a phase without indexing, instrumental correction, selection rules, texture and a model of the whole pattern. The IUCr reciprocal-lattice reference explains the equivalent reflection description in reciprocal space.

**Worked logic:** a peak at full angle 44 degrees with wavelength 1.54 angstrom implies d near 2.06 angstrom for the declared first order. Changing the assumed radiation or treating full angle as theta produces different answers. A single peak cannot establish a phase ID.

**Cautions:** systematic zero shifts, specimen displacement, overlapping peaks and strain broadening are not corrected by the simple calculator. Record radiation source, wavelength and uncertainty; separate peak position from fitted lattice parameter and from claimed phase assignment.

## Reference capsules for this chapter

- **Cubic unit-cell density is conditional** (equation): Theoretical rho=n*M/(NA*a^3) for a cubic cell and stated sites. Bulk density also depends on defects, pores and multiple species.
- **Bragg spacing and 2theta** (equation): The first-order relation 2*d*sin(theta)=lambda uses theta, half the full scan angle 2theta. Peak assignment and instrumental corrections are external.
- **Reciprocal-lattice reflections** (concept): Reflection indices and diffraction geometry determine observed peaks; reciprocal-space interpretation and systematic absences matter for indexing.

## Publisher portions used

[IUCR-BRAGG](https://www.iucr.org/what-we-do/education/pamphlets/introduction-calculation-of-structure-factors) · [IUCR-RECIP](https://dictionary.iucr.org/Reciprocal_lattice)

**Source use:** linked public portions and bounded paraphrases; no publisher text/datasets reproduced.
