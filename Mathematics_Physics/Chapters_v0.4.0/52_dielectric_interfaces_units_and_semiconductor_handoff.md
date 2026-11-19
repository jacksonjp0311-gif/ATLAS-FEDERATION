# Chapter 52 — Dielectric interfaces, SI metrology and the semiconductor handoff

**Edition:** Mathematics & Physics v0.4.0. **Status:** a reconstructible linear-electrostatics reference and an explicit map of *missing* semiconductor knowledge.

## Physical meaning before computation

The electrostatic model takes ε(x,y) as **already known**. It does not infer ε from measurements and it does not predict how charge carriers redistribute in silicon. For a linear scalar dielectric, ε=εr ε0. The NIST 2022 CODATA recommendation for vacuum permittivity is approximately `ε0 = 8.8541878188 × 10^−12 F/m` with a nonzero published standard uncertainty; it is *not* an exact fixed SI constant. Material relative permittivity εr varies with composition, frequency, temperature, fields and measurement protocol. A numerical grid value is not a calibration certificate.

The fundamental equations preserved in this node are

\[
\mathbf E=-\nabla V,\qquad \mathbf D=\epsilon\mathbf E,
\qquad \nabla\cdot\mathbf D=\rho.
\]

For an interface without free surface charge, the **normal displacement** is continuous; electric field need not be continuous when ε differs. A dielectric interface with a prescribed free sheet charge or polarization discontinuity requires additional jump conditions not covered by assigning a piecewise ε grid alone.

## Why harmonic face averaging is a useful first approximation

In one dimension consider two adjacent half-cells of width h/2 with ε1, ε2. At steady state, the same displacement passes through both segments. Their voltage drops add:

\[
\Delta V=-(D/\epsilon_1)(h/2)-(D/\epsilon_2)(h/2)
=-D\,h/\epsilon_{\rm face}.
\]

Solving gives `εface=2ε1ε2/(ε1+ε2)`, the harmonic average used in the v0.4 reference. This preserves shared-face flux cancellation. It assumes an axis-aligned interface and an isotropic, linear medium; on curved or oblique interfaces the modeling error needs a separate investigation. For a prescribed interface sheet charge, this simple average without a jump/source term is insufficient.

## Worked exercise: two dielectrics and fixed perimeter voltage

Take a unit rectangle with prescribed `V=x` along all boundary edges and set ε=1×10⁻¹¹ F/m for x<0.5 and 6×10⁻¹¹ F/m for x≥0.5. Let ρ=0. Construct a 13×11 interior grid with `poisson2d_problem`, solve with `solve_poisson2d_cg`, and check the integrated residual `Φboundary−Qinterior`. The computed potential is generally **not exactly V=x** throughout: the change in ε redistributes gradient so normal displacement can be continuous across internal faces. This is a synthetic dielectric-interface test, not an actual materials experiment.

A stronger future investigation should construct an analytic two-layer one-dimensional-in-x solution with piecewise slopes satisfying `ε1 E1=ε2 E2` at an aligned interface, compare exact face charge, and examine error when the interface does not align with the computational grid. This v0.4 reference does not claim those convergence properties yet.

## Reconstructible semiconductor bridge: what is still missing

Even a perfect electrostatic Poisson solver alone cannot reconstruct a transistor. The next Electronics & Semiconductors Atlas requires (at minimum):

- Semiconductor crystal structure and measured band structure; intrinsic carrier concentration and statistical mechanics with temperature.
- Doping, ionized impurity populations, Poisson-carrier coupling, electron and hole continuity equations, mobility/diffusion and recombination mechanisms.
- Contacts, electrochemical potential, Schottky/ohmic interfaces, gate oxide geometry, breakdown and interface traps; circuit-level boundary conditions.
- Material and process metrology, lithography, thin-film deposition, doping/anneal, manufacturing tolerances and test instruments.
- Mesh convergence, uncertainty propagation, calibration against actual measured devices and peer-reviewed source transport/rights verification.

Treat the v0.4 solver as a **numerical prerequisite**, not a semiconductor model or validated tool for device design. The original thirty-domain priority queue remains immutable. Complete domain libraries before any Bitwork routing or integrated desktop transfer.

## Evidence ledger and source provenance

- NIST CODATA permittivity entry: https://physics.nist.gov/cgi-bin/cuu/Value?ep0 (publisher value and uncertainty only; no authenticated publisher file bytes archived).
- NIST CODATA research overview: https://www.nist.gov/publications/codata-recommended-values-fundamental-physical-constants-2022 .
- OpenStax University Physics Vol. 2, Gauss law: https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law (orientation only; original publisher file not mirrored).

All original formulas and explanations in this chapter are AI-assisted synthesis prepared for ATLAS FORGE. The model has **zero field experiments, zero independently authenticated primary-source publisher transport files, and no external scientific peer review**.
