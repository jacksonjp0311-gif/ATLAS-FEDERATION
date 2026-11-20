# 20. A regular-solution model: miscibility, spinodal, and metastability

**Status:** original bounded derivation based on standard mean-field thermodynamics. No material-specific phase diagram has been measured or inferred. This chapter explains *what follows if* a symmetric, one-phase, constant-interaction model is stipulated. It is not a CALPHAD assessment, a DFT phase-hull calculation, or a polymer-blend parameter fit.

## The physical question and what must be known

Suppose a binary mixture has overall mole fraction of component B equal to x and temperature T. We want to distinguish a stable homogeneous phase, a metastable homogeneous state, and a locally unstable state. A composition alone cannot answer that question: we need a free-energy model, its reference state, the competing phases, and equilibrium assumptions. Here we assume a single symmetric substitutional solution, ideal configurational entropy, and a nonnegative constant molar interaction parameter omega. We exclude composition-dependent interactions, elastic misfit, multiple crystal structures, surfaces, diffusion kinetics and nucleation barriers.

The molar Gibbs free energy of mixing relative to pure-component reference is

`Gmix(x,T) = R*T*[x*ln(x)+(1-x)*ln(1-x)] + omega*x*(1-x)`.

Here `R=8.31446261815324 J mol^-1 K^-1`, `T>0 K`, `omega>=0 J/mol`, and `0<x<1` is dimensionless. This is a model function, not a measured free energy. The entropy term favors mixing; positive omega penalizes unlike neighbors. Its derivatives at fixed T are

`G' = R*T*ln(x/(1-x)) + omega*(1-2*x)`

`G'' = R*T/[x*(1-x)] - 2*omega`.

An implementation must not silently evaluate the logarithms at x=0 or 1. Their limiting values exist for G, but the derivatives are singular there. Our calculator explicitly refuses endpoints.

## Three boundaries are not interchangeable

The *critical temperature* for the stipulated symmetric model is `Tc=omega/(2R)` for omega>0. Above or at Tc the mean-field model has no two-phase miscibility gap. Below Tc the free-energy curve has two equivalent minima at compositions `x_b` and `1-x_b`. In this special symmetric model the common tangent is horizontal; the lower binodal composition solves the **noncentral** root of `G'(x_b)=0`. A naive root solver can return the ever-present stationary point x=0.5 instead of the binodal. The Atlas brackets the lower root strictly below the lower spinodal and refuses numerically unresolvable low-temperature limits.

The *spinodal* is the local curvature boundary `G''=0`, with lower composition

`x_s = (1 - sqrt(1 - 2*R*T/omega))/2`.

The code evaluates this using a cancellation-resistant algebraic form near small `2RT/omega`. For `x_s < x < 1-x_s`, the homogeneous state has negative curvature and is locally unstable in this mean-field thermodynamic model. Between the lower binodal and lower spinodal, or the symmetric upper interval, curvature can be positive but the state is still **metastable** because a two-phase mixture has lower global free energy. A model that labels all positive-curvature states stable confuses local and global criteria.

The *equilibrium two-phase fractions* follow a lever rule: for binodal endpoints a and b, `f_high=(x-a)/(b-a)` and `f_low=1-f_high`. They describe equilibrium composition accounting, not nucleation rates, domain sizes or the speed of phase separation. Our code reports the homogeneous-to-equilibrium free-energy difference to expose metastability, but it does not model microstructure formation.

## How to audit a computed phase boundary

A reproducible check should: declare omega, T and x; verify omega and T units; confirm that the noncentral binodal lies outside the spinodal; evaluate the free-energy curvature at x; confirm mass conservation in the lever fractions; compare homogeneous and phase-separated energies; and retain all model exclusions. For numerical confidence, a separate algorithm can minimize the Gibbs energy directly and compare its minimum with the derivative-root implementation. These checks validate the calculation under the chosen model; they cannot tell us whether the chosen omega represents any real alloy or polymer.

## What can go wrong

If omega depends on T, if additional phases are stable, or if the material is strongly nonideal, this model may be qualitatively misleading. A 0 K DFT convex hull is not the same object as a finite-T Gibbs free-energy common-tangent construction. If the material is not at equilibrium, a spinodal may predict a local thermodynamic tendency without describing observable kinetics. A real study would need composition/temperature calibration, specimen processing, phase-identification evidence, uncertainty and an independently justified free-energy description.

**Sources and scope:** MIT OpenCourseWare 3.012, lecture 19 pp. 11–12 (PDF text and page images checked): https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/9fa239d16926f0de29a87ed6f2e963d0_lec19t.pdf ; IUPAC Gold Book spinodal definition https://goldbook.iupac.org/terms/view/S05869 (search excerpt checked; direct page was blocked). The regular-solution derivation is original educational reasoning, not measured alloy data.
