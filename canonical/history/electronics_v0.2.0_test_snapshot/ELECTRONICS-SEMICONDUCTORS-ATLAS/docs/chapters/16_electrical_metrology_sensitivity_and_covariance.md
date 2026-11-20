# 16. Electrical metrology, sensitivity derivatives and covariance propagation

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Electrical metrology, sensitivity derivatives and covariance propagation. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`σ_I²≈(∂I/∂V)²σ_V²+(∂I/∂T)²σ_T²+2(∂I/∂V)(∂I/∂T)Cov(V,T)`

**Units:** V, K, A, A/V, A/K, A². Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

Suppose the ideal diode law is I=I_s[exp(qV/(n k_B T))−1] and treat I_s as constant solely for a local derivative audit. With x=qV/(n k_B T), ∂I/∂V=I_s exp(x)/(n V_T) and ∂I/∂T=−I_s exp(x)x/T. A first-order Taylor expansion in correlated V and T measurement errors yields the covariance expression. A valid covariance matrix requires |Cov(V,T)|≤σ_Vσ_T; otherwise the supplied uncertainty budget is inconsistent.

This propagation concerns a *chosen mathematical model*. In real semiconductors I_s often changes strongly with temperature through intrinsic concentration, recombination and transport; holding it constant can give a dramatically misleading temperature sensitivity. Keep model discrepancy, measurement uncertainty and numerical discretization error as distinct categories; do not use a small covariance estimate to certify the model.

## Independently executable algorithm

Call `diode_current_local_uncertainty` with positive ideality, absolute SI temperature, and explicit voltage/temperature uncertainties. Independently finite-difference the voltage and temperature derivatives with multiple step sizes, check correlation bounds, and refuse overflow. Record raw measurement IDs, instrument calibration, acquisition date, temperature range and parameter-covariance sources before using the result physically.

## Worked scientific investigation

Choose I_s=10⁻¹² A, V=0.2 V, T=300 K, n=1, σ_V=1 mV, σ_T=0.2 K and Cov=0. Compare the analytic current and sensitivity with centered finite differences. Repeat with maximal legal positive/negative covariance to display range of predicted first-order uncertainty. These inputs are constructed, not recorded instruments.

## Failure conditions and counterexamples

First-order linearization is unreliable for large voltage/temperature errors; the ideal diode law ignores series resistance, reverse breakdown and thermally varying I_s. A full metrology report requires traceable calibrations, raw samples, repeat measurements and an independently reviewed uncertainty model.

## Source fidelity and rights

Publisher reference card: `NIST-SP330`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.
