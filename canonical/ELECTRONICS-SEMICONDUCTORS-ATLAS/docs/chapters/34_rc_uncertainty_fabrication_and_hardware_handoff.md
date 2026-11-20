# Chapter 34: From numerical electronics to measured gates and a computer

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Material-to-circuit bridge
The continuity chain is chemistry → material and process characterization → device electrical response → logic voltage transfer → timing → registers and memory → architecture and runtime. A numerical simulator cannot validate this chain if its material parameters and circuit abstractions have never been calibrated. Resistivity, doping gradients, dielectric permittivity, thermal coefficients, contact resistance and parasitic capacitances are upstream prerequisites.

A small measurable example is a first-order RC step response. For a rising RC charging response V(t)=VDD(1−exp(−t/(RC))), the midpoint occurs at t50=RC ln2. To propagate small measured uncertainties, differentiate: ∂t/∂R=C ln2 and ∂t/∂C=R ln2. First-order covariance propagation then yields the variance shown above. A positive correlation increases uncertainty if both sensitivities have the same sign. The model requires a valid positive-semidefinite covariance bound and labels this as a local linearization, not device metrology.

## Worked investigation
Let R=1000 Ω, C=1 nF, σ_R=10 Ω, σ_C=0.01 nF, covariance zero. Nominal t50≈0.6931 μs. First-order one-standard-deviation uncertainty is ≈9.80 ns. That only quantifies parameter uncertainty under the assumed RC model; an actual transistor switching path may have slew dependence, Miller charge, interconnect and short-circuit conduction.

## Minimum reconstructible experiment ledger
Record device/material identity and provenance; instrument model/firmware/calibration and raw transport files; temperature/supply; circuit and probe loading; test fixture; test points and repeated timing traces; voltage transfer under input sweeps; setup/hold and metastability observations; uncertainty components and covariance; contact/device dimensions; expected-versus-observed mismatch and negative results; external reviewer findings. Do not imply completion before a human or laboratory performs these measurements.

## Federation roadmap
The original 30-domain list is frozen. Electronics remains within the original 13-node federation, with Manufacturing and Computer Architecture planned as future nodes. The source-linked knowledge schema remains unchanged and Bitwork routing is deferred until content-domain completion. The scoped v1 *software* gate and broader independent scientific/physical gates must be reported separately.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `rc_midpoint_delay_uncertainty`.
- **Governing relation:** `t50=ln(2)RC; Var(t50)≈(ln2 C)^2 Var(R)+(ln2 R)^2 Var(C)+2(ln2)^2 RC Cov(R,C)`.
- **Units:** ohms, farads, seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
