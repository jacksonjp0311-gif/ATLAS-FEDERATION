# 11. Constant-field drift–diffusion and exponential-fitted charge flux

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Constant-field drift–diffusion and exponential-fitted charge flux. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`J_n=-(q D_n/h)[B(-P)n_L-B(P)n_R], P=-E h/V_T, B(z)=z/(e^z-1), D_n=μ_n V_T`

**Units:** V/m, m²/(V·s), m⁻³, A/m². Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

For an electron population, the particle drift velocity is v_n = −μ_n E while the particle flux is F_n = v_n n − D_n dn/dx. The conventional electron *charge current* is J_n = −q F_n, so positive electric field induces positive conventional current. With constant v_n and D_n on a cell, solve the linear first-order differential equation exactly: n(x)=F_n/v_n+(n_L−F_n/v_n) exp(v_n x/D_n). Enforcing n(h)=n_R eliminates F_n and yields the Bernoulli formula above. It is exact for the stated piecewise-constant coefficients, not an exact solution of a device with varying mobility or field.

The Einstein relation D=μ V_T is an explicit nondegenerate-isothermal equilibrium approximation. For E=0 the flux reduces to the central diffusion gradient; for n_L=n_R it reduces to charge drift qμnE. For equilibrium F=0, n_R/n_L=exp(P). A direct exp(P) formulation loses significance near P=0 and overflows for large positive P; use expm1 and asymptotic branches.

## Independently executable algorithm

Use `bernoulli_stable` and `sg_electron_current` from `electronics_atlas/v02_models.py`. Assert units and finite positive mobility, temperature and length, nonnegative carrier densities, and explicit sign conventions. Check the exact reversal transformation (left↔right, E→−E, J→−J), zero-field limit, equilibrium limit and the high-precision reference. The algorithm is a single edge-flux computation; it is not the full coupled drift–diffusion solver.

## Worked scientific investigation

Let n_L=n_R=10^19 m⁻³, μ=0.07 m²/(V·s), E=500 V/m, h=10⁻⁶ m, T=300 K. Because the concentration gradient vanishes, J=qμnE≈560.7618219 A/m². Evaluate the fitted flux and verify relative agreement within double precision. Then perturb n_R, hold all other assumptions, and compare the fitted flux to an 80-digit exact boundary solution.

## Failure conditions and counterexamples

Continuum drift–diffusion fails under ballistic transport, strong degeneracy, velocity saturation, hot carriers, sharply varying contacts or low statistics. A numerically stable edge flux is not a measurement or independently calibrated silicon transport prediction.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.
