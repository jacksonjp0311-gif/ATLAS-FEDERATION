# Investigation 09 — A model with two different phase boundaries

**Question:** Can a homogeneous mixture have positive free-energy curvature and still be thermodynamically disfavored? **Origin:** original synthetic regular-solution model; no specimen, composition measurement or physical phase diagram.

Stipulate `omega=20,000 J/mol` and `R=8.31446261815324 J/(mol K)`. The model critical temperature is `Tc=omega/(2R)`, approximately 1,202.72 K. Choose `T=0.8*Tc`, or approximately 962.17 K, and evaluate `Gmix=RT[x ln x+(1-x)ln(1-x)]+omega*x(1-x)`. The binodal endpoints are the noncentral roots of the derivative, while the spinodal endpoints satisfy zero curvature. The calculator returns both rather than conflating them.

At overall `x=0.5`, the homogeneous curvature is negative, so this stipulated mean-field state is locally unstable. At a composition halfway between the lower binodal and spinodal, curvature is positive but a two-phase mixture has lower global free energy. That is the **metastable** region. The computed phase fractions sum to one and conserve x. At temperatures above Tc, the same model reports a single-phase region.

**Reproduce:** `python -m materials_atlas expanded-cases` and inspect `binodal_wider_than_spinodal`, `central_composition_unstable`, `metastable_not_stable`, and `above_critical_single_phase`. `python tools/phase_diffraction_oracle.py` compares the Atlas derivative-root result against SciPy direct minimization over 90 seeded models.

**What this does not show:** a real alloy's coexistence curve, the speed of phase separation, spinodal decomposition morphology, or any real critical temperature. A single regular-solution omega cannot substitute for experimental phase diagrams or thermodynamic assessments. NIST's discussion of binodal/spinodal in polymer blends supports the conceptual distinction, not this model's numeric parameter choice.
