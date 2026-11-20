# Electronics v0.2 — eight constructed investigations

## Investigation 11: Constant-field drift–diffusion and exponential-fitted charge flux

Let n_L=n_R=10^19 m⁻³, μ=0.07 m²/(V·s), E=500 V/m, h=10⁻⁶ m, T=300 K. Because the concentration gradient vanishes, J=qμnE≈560.7618219 A/m². Evaluate the fitted flux and verify relative agreement within double precision. Then perturb n_R, hold all other assumptions, and compare the fitted flux to an 80-digit exact boundary solution.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** Continuum drift–diffusion fails under ballistic transport, strong degeneracy, velocity saturation, hot carriers, sharply varying contacts or low statistics. A numerically stable edge flux is not a measurement or independently calibrated silicon transport prediction.

## Investigation 12: Minority-carrier diffusion, recombination and discrete conservation

Choose D=0.002 m²/s, τ=10⁻⁷ s, L=10⁻⁵ m, u_L=1 normalized density and u_R=0.1. Compare N=20/40/80 discrete solutions against the analytic sinh solution. Report peak errors and net recombination and boundary fluxes with units. Changing τ changes L_D; a fitted lifetime cannot be inferred from an arbitrarily chosen synthetic profile.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** The fixed-lifetime linear law is not valid for strong injection, nonlinear SRH/Auger/radiative recombination, field-assisted processes or spatially varying materials. Do not relabel exact numerical conservation as experimental calibration.

## Investigation 13: Nodal circuit analysis, conductance matrices and power accounting

A 3 V source drives a 1 kΩ and 2 kΩ series divider to ground. KCL gives V_mid=3×(2/3)=2 V, I=1 mA, P_R=(1 mA)²×3 kΩ=3 mW. Compute fixed-node source reactions and verify the 3 mW external delivery. For a distributed network, insert parallel edges and independent current injections and compare the result with a second dense assembly.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** This solver covers linear DC resistors, ideal current injections and fixed voltages. It does not model capacitors, inductors, nonlinear junctions, wires at high frequency or parasitic thermal coupling. Solving KCL does not prove manufacturability.

## Investigation 14: CMOS inverter DC load lines and the indeterminate saturation plateau

For V_DD=1.2 V, k_n=k_p=10⁻⁴ A/V², V_TN=|V_TP|=0.3 V and V_in=0.6 V, both saturation currents equal 0.5k×0.3². Over the interior output interval [0.3,0.9] V, both currents are constant. Report the continuum of valid DC solutions. Asymmetric k_n and k_p moves the unique switch point, but does not make the model calibrated to a real transistor.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** Square-law MOSFET assumptions omit short-channel velocity saturation, subthreshold leakage, body effects, channel-length modulation, process variation, thermal changes and contact resistance. Physical noise margins need measured or validated transfer characteristics.

## Investigation 15: Logic voltage thresholds, noise margins and simplified RC switching

Suppose an externally specified 1.2 V logic family guarantees V_OL≤0.10 V, V_OH≥1.10 V, V_IL=0.40 V, V_IH=0.80 V. Then NM_L=0.30 V and NM_H=0.30 V. With R=1000 Ω and C=1 nF, t_50≈0.693 μs. This is a constructed specification and RC fixture, not a semiconductor measurement.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** Noise margins depend on temperature, loading, fabrication variation and actual device transfer curves. RC timing ignores short-circuit dissipation, waveform slew limits, crosstalk, clock jitter and metastability.

## Investigation 16: Electrical metrology, sensitivity derivatives and covariance propagation

Choose I_s=10⁻¹² A, V=0.2 V, T=300 K, n=1, σ_V=1 mV, σ_T=0.2 K and Cov=0. Compare the analytic current and sensitivity with centered finite differences. Repeat with maximal legal positive/negative covariance to display range of predicted first-order uncertainty. These inputs are constructed, not recorded instruments.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** First-order linearization is unreliable for large voltage/temperature errors; the ideal diode law ignores series resistance, reverse breakdown and thermally varying I_s. A full metrology report requires traceable calibrations, raw samples, repeat measurements and an independently reviewed uncertainty model.

## Investigation 17: From CMOS gates to a full adder and n-bit ripple-carry arithmetic

Use width=4 and add 1101₂ (13) + 0110₂ (6). Bitwise carry produces output 0011₂ (3) and carry_out=1, reconstructing 19 = 3 + 16. Then add the largest 64-bit unsigned word plus 1: the output word is zero and carry_out=1. Neither example demonstrates an actual CMOS chip.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** This establishes functional Boolean correctness, not a timed latch, register file, clock system, memory, processor ISA or manufactured circuit. Real propagation delay may grow with carry length; a ripple adder is a simple reference, not an optimized architecture.

## Investigation 18: Technological continuity: interfaces from semiconductor equations to computer architecture

Begin with 2,669 verified predecessor federation records, append this edition's exact revision records, test a single drift–diffusion edge, a 3-node resistor divider, a logic-family margin fixture and a four-bit full adder. For each layer, distinguish numerical exactness, model-form assumption, required laboratory instrument, and next-domain handoff. Failure to obtain a real silicon transfer curve is an open experimental gate, not a reason to erase software proofs.

**Oracle:** see `evidence/independent_oracle_v02.py`.

**Boundary:** No semiconductor wafers, integrated circuits, fabrication tolerances, clocked processor, silicon lithography or physical AI accelerator are constructed by this text. Manufacturing and Computer Architecture remain separate future Atlas nodes, and Bitwork routing is still prohibited until all content domains are established.


## New v0.3.0 constructed verification investigations

### Investigation 19 — From resistor-capacitor networks to timed node voltages

Reconstruct `rc_nodal_backward_euler` from `C dV/dt+G V=I; (C/dt+G)V_next=C V_old/dt+I`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 20 — Energy from charging a digital node

Reconstruct `charge_supply_energy` from `E_supply=N_rise C V^2; P=alpha C V^2 f`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 21 — Reconstruct Boolean arithmetic from a single universal gate

Reconstruct `nand_full_adder, nand_ripple_add` from `x=a XOR b (four NAND); s=x XOR cin; cout=ab+cin*x`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 22 — State storage is not equivalent to combinational logic

Reconstruct `EdgeRegister.capture` from `if transition in [edge-setup,edge+hold], state=UNKNOWN`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 23 — Timing inequalities for a synchronous circuit

Reconstruct `register_path_timing` from `T+skew >= tCQmax+tPD+tsetup; tCQmin+tCD >= thold+skew`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 24 — Preserving data integrity with a small error-correcting code

Reconstruct `hamming84_encode,hamming84_decode` from `minimum Hamming distance 4; SECDED syndrome and overall parity`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 25 — A minimal register bank with explicit unknown-state propagation

Reconstruct `register_bank_step` from `M'[a]=data if write_enabled else M[a]`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.

### Investigation 26 — Evidence-driven handoff to computer architecture

Reconstruct `reconstruction dependency matrix` from `physical→logic→registers→architecture→compiler→AI runtime`; run `test_v03_models.py`, record exact input domain, expected numerical or Boolean invariant, one negative input, and discrepancy with any continuous-time or physical model. No laboratory measurement is implied.



# Eight v0.4.0 constructed investigations

## Case 27: Voltage window

Input: 3.3 V supply and VOL=.4, VIL=1.0, VIH=2.1, VOH=2.9 V.

Expected/check: NML=.6 V; NMH=.8 V; input 1.5 V=unknown.

Scope: finite constructed reference, not a measured electronic system.

## Case 28: Critical DAG path

Input: A=[0,1] ns; B=[0,2] ns; gate delays [1,1], [2,4], [1,2] ns.

Expected/check: Earliest=2 ns, latest=8 ns; path B→high→out.

Scope: finite constructed reference, not a measured electronic system.

## Case 29: Skew tradeoff

Input: T=10 ns; clkQ=[1,2] ns, comb=[2,4] ns, setup=1 ns, hold=.5 ns.

Expected/check: No skew: setup 3 ns, hold 2.5 ns. +2 ns skew: setup 5 ns, hold .5 ns.

Scope: finite constructed reference, not a measured electronic system.

## Case 30: Metastability envelope

Input: fclk=10 MHz, fdata=1 MHz, T0=1 ns, tau=30 ps.

Expected/check: A +1 ns of resolution raises log10(MTBF) by ~14.48; synthetic parameters only.

Scope: finite constructed reference, not a measured electronic system.

## Case 31: Signed and unsigned arithmetic

Input: 4-bit 7+1 and 15+1.

Expected/check: 7+1=8 with signed overflow; 15+1=0 with unsigned carry.

Scope: finite constructed reference, not a measured electronic system.

## Case 32: Memory collision

Input: words [1,2,3], address1, write9.

Expected/check: Next words [1,9,3]; read-first 2; write-first 9; undefined unknown.

Scope: finite constructed reference, not a measured electronic system.

## Case 33: Four-phase transfer

Input: 00→10→11→01→00.

Expected/check: Valid cycle; 00→11 illegal.

Scope: finite constructed reference, not a measured electronic system.

## Case 34: RC uncertainty

Input: R=1 kΩ, C=1 nF, sigmaR=10 Ω, sigmaC=.01 nF.

Expected/check: t50≈0.693 μs; sigma≈9.8 ns, first-order approximation.

Scope: finite constructed reference, not a measured electronic system.
