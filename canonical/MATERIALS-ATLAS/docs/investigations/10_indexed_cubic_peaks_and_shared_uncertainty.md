# Investigation 10 — Why four peaks do not erase a shared calibration uncertainty

**Question:** If we add more indexed diffraction peaks, which parts of the lattice-parameter uncertainty should shrink? **Origin:** original synthetic peak positions, not a copper powder measurement.

Stipulate a cubic lattice `a=3.61 angstrom`, radiation wavelength `lambda=1.5406 angstrom`, a shared wavelength standard uncertainty `u_lambda=0.0001 angstrom`, and independent `u(2theta)=0.015 degree` for each of four externally assigned reflections (111), (200), (220), and (311). Construct ideal peak angles by inverting the Bragg equation, then calculate each `a_i` and its first-order angular uncertainty. The inverse-variance weighted mean recovers 3.61 angstrom to floating-point precision because the inputs were generated from that exact model.

The combined uncertainty has **two** parts: random angle uncertainty, which may decrease with additional independent peaks, and the wavelength contribution `a_bar*u_lambda/lambda`, which is common to every peak. Treating the latter as independent and dividing it by `sqrt(n)` would understate uncertainty. The implementation retains these two components separately and reports the chi-square residual diagnostic. Because the ideal peak positions are noise-free, their chi-square is nearly zero; this is not an actual fit quality claim.

**Reproduce:** `python -m materials_atlas expanded-cases`, then `python tools/phase_diffraction_oracle.py` for 240 seeded diffraction examples checked against a separate vectorized NumPy calculation. The tool rejects missing standard uncertainties, duplicate cubic reflection families and noninteger indices. It does not automatically index an unknown pattern.

**Study requirements for real data:** a justified phase and hkl assignment, instrument/wavelength calibration, angle zero-offset and specimen displacement corrections, possible peak overlap and texture, covariance, specimen processing and measurement temperature. IUCr's powder diffraction treatment supplies the physical Bragg and cubic metric relations; the synthetic dataset supplies no material-identification evidence.
