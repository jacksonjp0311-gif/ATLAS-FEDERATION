# 57. Coupled Poisson and electron–hole continuity

**Reconstruction aim.** From mathematical definitions and basic constants, obtain a finite-volume system that a researcher can execute on a disconnected Python installation. This chapter is a modeling derivation; no particular crystal, wafer, fabrication process, measured device or independent scientific review is certified.

## State variables and dimensional equations

Take a one-dimensional isothermal semiconductor in a region \(X\in[0,L]\), electric potential \(V\) in volts, electron and hole number concentrations \(n,p\) in \(\mathrm{m}^{-3}\), ionized net dopant density \(C=N_D^+-N_A^-\) in \(\mathrm{m}^{-3}\), permittivity \(\epsilon\) in F/m, elementary charge \(q>0\) in C, and the thermal voltage \(V_T=k_BT/q\). Define electric field \(E=-\partial_X V\) and charge density \(\rho=q(p-n+C)\). Gauss’s electrostatic law gives

\[-\frac{d}{dX}\left(\epsilon\frac{dV}{dX}\right)=q(p-n+C).\]

For nondegenerate carriers obeying Einstein diffusion \(D=\mu V_T\), model number fluxes to the right as

\[F_n=-D_n\frac{dn}{dX}+\mu_n n\frac{dV}{dX},\qquad
F_p=-D_p\frac{dp}{dX}-\mu_p p\frac{dV}{dX}.\]

*Number flux* is particles per \(\mathrm{m}^2\) per second, not conventional electric current. Conventional currents are \(J_n=-qF_n\) and \(J_p=qF_p\). For a stationary model without generation or recombination, \(\partial_X F_n=\partial_X F_p=0\). These signs matter. A sign error can yield a plausible potential but incorrect current direction.

## Scale before solving

Set \(x=X/L\), \(u=V/V_T\), and scale \(n,p,C\) by an explicitly declared \(N_\mathrm{ref}>0\). Then

\[-\lambda^2 u''=p-n+C,\qquad
\lambda^2=\frac{\epsilon V_T}{qN_\mathrm{ref} L^2}.\]

In a homogeneous material with fixed \(\epsilon>0\), normalize each diffusion coefficient by a reference \(D_\mathrm{ref}\). For a species with dimensionless \(D\), its dimensionless flux is \(F=-D\,\partial_x n\pm Dn\,\partial_x u\). The physical number-flux scale is \(D_\mathrm{ref}N_\mathrm{ref}/L\). The physical current-density scale is \(q D_\mathrm{ref}N_\mathrm{ref}/L\). This rescaling prevents numerical loss caused by directly combining \(10^{-19}\) C and \(10^{21}\) \(\mathrm{m}^{-3}\) in an unscaled residual.

## Finite-volume balance and conservation

On nodes \(x_i=ih\), \(h=1/(m+1)\), impose two Dirichlet contacts for each of \(u,n,p\). For \(i=1,\ldots,m\), use

\[\frac{\lambda^2}{h^2}(2u_i-u_{i-1}-u_{i+1})=p_i-n_i+C_i,\]

\[F_{n,i+1/2}-F_{n,i-1/2}=0,\quad F_{p,i+1/2}-F_{p,i-1/2}=0.\]

Summing Poisson’s equation over interior cells cancels every interior field contribution, leaving only the boundary field slopes. Likewise, the flux balance telescopes and each species’ interior flux is constant. **Preserving these identities is mandatory**, separate from achieving a small local nonlinear residual.

## Boundary and model-form limits

The executable reference accepts strictly positive, *prescribed* electron/hole contact concentrations and potential endpoints. This makes the algebra definite but is not a validated ohmic, Schottky or recombination-velocity boundary model. It excludes nonzero generation/recombination, carrier traps, transient switching, quantum transport, heating, heterojunctions, anisotropic permittivity and measured mobility. Not all prescribed contacts are thermodynamically self-consistent; those are intentional stress cases, not devices ready to manufacture.

## Reconstruct and test

Run `python -m unittest discover -s tests -p 'test_v1_models.py' -q` in this atlas root, then `python tools/independent_oracle_v1.py` when SciPy/NumPy are available. Inspect `math_physics_atlas/v1_models.py`; its solver must raise an explicit non-convergence error rather than emit a converged flag for a failed iteration. Check independently both charge–flux boundary balance and the two particle conservation residuals. For an apparent device prediction, demand measured \(\epsilon\), doping profiles, mobility versus carrier density/field/temperature, calibrated contacts, error bounds and actual device observations before increasing the evidence status.
