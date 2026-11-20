# 61. SI scaling, metrology, and traceability of semiconductor variables

## Exact defining constants are not exact materials data

The elementary charge \(q=1.602176634\times10^{-19}\,\mathrm{C}\) and Boltzmann constant \(k_B=1.380649\times10^{-23}\,\mathrm{J/K}\) are exact defining constants of the present SI, as stated by the official BIPM SI Brochure, ninth edition, version 4.01 (June 2026). The *temperature measured in a laboratory*, a material's dielectric permittivity, the mobility of a doped sample, and the physical dimension of a lithographic feature are **not** exact merely because their units are SI. Preserve the raw measurement, calibration procedure, instrument uncertainty, source version and dates separately from physical model parameters.

Compute the thermal voltage \(V_T=k_B T/q\) and diffusion \(D=\mu V_T\) only under an explicitly declared nondegenerate Einstein-relation assumption. The dimensionless charge coupling is \(\lambda^2=\epsilon V_T/(qN_\mathrm{ref}L^2)\). Thus doubling \(L\) with other parameters fixed quarters \(\lambda^2\), whereas doubling \(T\) doubles both \(V_T\) and \(\lambda^2\). These scaling identities are software regression checks and dimensional checks, not measurements.

## Reconstruct a numerical experiment

Define measured or hypothetical \(L,\epsilon,N_\mathrm{ref},T,\mu\) with declared SI units. Validate that every parameter is finite and within the reference model's explicit supported domain. Compute \(V_T,\lambda^2,D\) from them; then specify \(u,n,p,C\), contacts and an observation model. The reference program reports only model-normalized values. To convert current, multiply the *particle flux* by \(D_\mathrm{ref}N_\mathrm{ref}/L\), then the species charge sign. Misidentifying an electron particle flux as conventional current reverses the sign and may corrupt device reasoning.

## Source chain and rights provenance

Primary metrology target: Bureau International des Poids et Mesures (BIPM), *The International System of Units*, 9th ed., revision 4.01 (2026), DOI 10.59161/AUEZ1291, official page https://www.bipm.org/en/publications/si-brochure/ and license Creative Commons Attribution 4.0 International. A verified source **URL** and publication-rights statement are not the same as an authenticated original PDF transport-file SHA-256. During this release construction, the original publisher file could not be retrieved for byte-level preservation. Accordingly the source card remains bibliographic and the release does not count an authenticated original copy. External reviewers have not signed the source-to-equation reconciliation. These explicit gaps prevent later users from confusing a local derivative explanation with the primary official document.

## Error propagation

For independent small input uncertainties, first-order relative propagation for \(\lambda^2\) is \((\delta\lambda^2/\lambda^2)^2\approx(\delta\epsilon/\epsilon)^2+(\delta T/T)^2+(\delta N/N)^2+4(\delta L/L)^2\). This independence assumption is often wrong when multiple instrument readings share calibration errors: preserve the covariance and use \(\mathrm{Var}(f)\approx\nabla f^T\Sigma\nabla f\). Nonlinear or bounded uncertainties need interval or Monte Carlo propagation; they are not solved by calling a numerical residual small.
