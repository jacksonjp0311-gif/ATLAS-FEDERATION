# Mathematics & Physics v0.2 — six finite constructed investigations

## Chapter 39 — Householder QR and stable least-squares reconstruction
**Reference:** `qr_least_squares(matrix, rhs)`

A=[[1,1],[1,2],[1,3],[1,4]], b=[3,5,7,9]. The fitted parameters are [1,2] with residual norm approximately 0.

**Failure boundary:** Full-column-rank only: rank loss, underdetermined inputs and extreme scaling are rejected. Residual does not establish parameter identifiability under noise.

**Evidence:** finite deterministic calculation; no experimental physical observation.

## Chapter 40 — Singular values, rank and identifiability boundaries
**Reference:** `svd2_diagnostics(matrix, rank_rtol)`

A=diag(5,2) has singular values (5,2) and condition 2.5. A=[[1,1],[1,1]] has values (2,0), rank one.

**Failure boundary:** Implements only analytic 2×2 singular-value diagnostics; it is NOT a general SVD or pseudoinverse. Small singular values may lose accuracy in determinant cancellation.

**Evidence:** finite deterministic calculation; no experimental physical observation.

## Chapter 41 — Radix-two FFT, spectral sampling and aliasing tests
**Reference:** `fft_radix2(samples, inverse)`

For N=4 and x=[0,1,0,0], forward spectrum [1,−i,−1,i] and inverse restores the impulse.

**Failure boundary:** Only power-of-two N≤4096 and finite scalar samples. Sampling cannot distinguish frequencies separated by integer multiples of sample rate.

**Evidence:** finite deterministic calculation; no experimental physical observation.

## Chapter 42 — Adaptive nonlinear ODE integration and local error estimation
**Reference:** `nonlinear_rk4_adaptive(rhs, t0, y0, t1)`

For y′=y(1−y), y(0)=0.1, the exact solution y(2)=1/[1+9e⁻²]≈0.450853; compare to adaptive RK4.

**Failure boundary:** Step-doubling local tolerance is not a proof of global error or stiff-system stability. Refuses invalid initial/time domains and step-budget exhaustion.

**Evidence:** finite deterministic calculation; no experimental physical observation.

## Chapter 43 — Heat equation, diffusion stability and bounded temperature fields
**Reference:** `heat1d_dirichlet(initial, alpha, dx, dt, steps)`

T(x,0)=sin(πx/L), T(0,t)=T(L,t)=0. Exact reference is T(x,t)=sin(πx/L)exp[−α(π/L)²t].

**Failure boundary:** One-dimensional constant-diffusivity linear conduction with fixed-zero Dirichlet boundaries only; refuses Fourier number >1/2. Not a calibrated materials-property or heat-transfer prediction.

**Evidence:** finite deterministic calculation; no experimental physical observation.

## Chapter 44 — Wave equation, leapfrog propagation and electromagnetic scope
**Reference:** `wave1d_dirichlet(displacement, c, dx, dt, steps)`

For u(x,0)=sin(πx/L), u_t(x,0)=0, fixed ends: u(x,t)=sin(πx/L)cos(cπt/L).

**Failure boundary:** Scalar 1D wave with fixed-zero ends and zero initial velocity; not a Maxwell field solver, transmission-line impedance model, or radiation prediction.

**Evidence:** finite deterministic calculation; no experimental physical observation.

