# ATLAS FORGE — Electronics & Semiconductors v0.2.0 (original federation, offline manual)



---

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


---

# 12. Minority-carrier diffusion, recombination and discrete conservation

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Minority-carrier diffusion, recombination and discrete conservation. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`D u\x27\x27-u/τ=0; L_D=√(Dτ); F=-D du/dx; F_R-F_L+Σ_i (h u_i/τ)=0`

**Units:** m²/s, s, m, m⁻³, m⁻²s⁻¹. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

For low-level injected excess carrier density u(x), assume spatially uniform D>0, a fixed lifetime τ>0, no field and no generation. Continuity at steady state becomes D u''−u/τ=0 with injection/recombination boundary values u(0)=u_L, u(L)=u_R. The exact analytic solution is u(x)=u_L sinh((L−x)/L_D)/sinh(L/L_D)+u_R sinh(x/L_D)/sinh(L/L_D), L_D=sqrt(Dτ). For L/L_D≫1, compute ratios with scaled exponentials to avoid overflow.

On N equal cells, (2+h²/(Dτ))u_i−u_(i−1)−u_(i+1)=0. The tridiagonal matrix has positive diagonal and nonpositive off-diagonals and admits a positive inverse under the prescribed conditions. Summing its finite-volume continuity rows gives F_R−F_L+Σ h u_i/τ=0 exactly up to floating rounding. The boundary fluxes represent the carrier supply needed to balance bulk recombination.

## Independently executable algorithm

Reconstruct `minority_diffusion_profile` by Thomas elimination; confirm nonnegative interior for nonnegative boundaries and validate the telescoping flux balance independently of the tridiagonal residual. Compare each profile to the hyperbolic analytic solution. Double the grid from N=20 to 40 to 80 and check an approximately fourfold reduction in maximum interior error at fixed physical parameters.

## Worked scientific investigation

Choose D=0.002 m²/s, τ=10⁻⁷ s, L=10⁻⁵ m, u_L=1 normalized density and u_R=0.1. Compare N=20/40/80 discrete solutions against the analytic sinh solution. Report peak errors and net recombination and boundary fluxes with units. Changing τ changes L_D; a fitted lifetime cannot be inferred from an arbitrarily chosen synthetic profile.

## Failure conditions and counterexamples

The fixed-lifetime linear law is not valid for strong injection, nonlinear SRH/Auger/radiative recombination, field-assisted processes or spatially varying materials. Do not relabel exact numerical conservation as experimental calibration.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

# 13. Nodal circuit analysis, conductance matrices and power accounting

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Nodal circuit analysis, conductance matrices and power accounting. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`Σ_j (V_i−V_j)/R_ij=I_i^inj; P_R=Σ_edges (V_a−V_b)^2/R_ab`

**Units:** Ω, S, V, A, W. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

Kirchhoff’s current law at each free node states that current leaving through connected resistors equals externally injected current. Assemble conductance matrix G: G_ii=Σ_j 1/R_ij and G_ij=−Σ_(i,j)1/R_ij. Move fixed-potential neighbors to the right-hand side, retaining their source reaction currents. With positive resistances and at least one fixed potential per connected component, the reduced G is symmetric positive definite. A floating component has a gauge degree of freedom; refuse it instead of silently assigning ground.

The power certificate follows by multiplying each KCL row by V_i and summing. Every edge contributes (V_a−V_b)²/R, so total resistive loss equals the sum of injected-current power and fixed-voltage-source reaction power. This equality checks sign conventions and assembly without asserting a physical resistor’s actual tolerance or temperature behavior.

## Independently executable algorithm

Use `resistor_network` with bounded node count (≤64), positive finite resistances and finite fixed potentials/current injections. Independently assemble dense NumPy G and solve with `numpy.linalg.solve` in the optional oracle. Verify KCL on every free node, source-current sum, Joule positivity and power balance. Deliberately test an isolated component, self-loop, zero resistance and negative resistance.

## Worked scientific investigation

A 3 V source drives a 1 kΩ and 2 kΩ series divider to ground. KCL gives V_mid=3×(2/3)=2 V, I=1 mA, P_R=(1 mA)²×3 kΩ=3 mW. Compute fixed-node source reactions and verify the 3 mW external delivery. For a distributed network, insert parallel edges and independent current injections and compare the result with a second dense assembly.

## Failure conditions and counterexamples

This solver covers linear DC resistors, ideal current injections and fixed voltages. It does not model capacitors, inductors, nonlinear junctions, wires at high frequency or parasitic thermal coupling. Solving KCL does not prove manufacturability.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

# 14. CMOS inverter DC load lines and the indeterminate saturation plateau

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

CMOS inverter DC load lines and the indeterminate saturation plateau. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`I_n(V_in,V_out)=I_p(V_DD−V_in,V_DD−V_out)`

**Units:** V, A, A/V². Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

In a complementary CMOS inverter, the nMOS drain current from the output node to ground equals the pMOS source current from V_DD into the output at static equilibrium. Use the existing ideal long-channel square-law I(V_GS,V_DS) for each device, reversing pMOS voltage polarities. Outside cut-off, both currents are monotone functions of output voltage with opposite sign, so a bracketed root can be found by bisection.

A subtle exception matters: ideal square-law saturation has no dependence on drain voltage if channel-length modulation is zero. If both devices saturate over a finite V_out interval and their saturation currents exactly match, *every output in that interval is a DC solution*. The model must report non-identifiability rather than fabricate one chosen voltage. A second nonidentifiability occurs when both transistors are below threshold. Real device λ, leakage, mismatch and parasitics often resolve the plateau, but those effects are not included in this ideal model.

## Independently executable algorithm

Solve f(V_out)=I_n−I_p using a 0-to-V_DD bracket. Check cutoff and saturation plateau degeneracy before bisection. Test rail endpoints, asymmetric device strengths, reversal monotonicity and exact balanced plateau rejection. Do not derive analog input thresholds or fabricated noise margins solely from the ideal square-law curve.

## Worked scientific investigation

For V_DD=1.2 V, k_n=k_p=10⁻⁴ A/V², V_TN=|V_TP|=0.3 V and V_in=0.6 V, both saturation currents equal 0.5k×0.3². Over the interior output interval [0.3,0.9] V, both currents are constant. Report the continuum of valid DC solutions. Asymmetric k_n and k_p moves the unique switch point, but does not make the model calibrated to a real transistor.

## Failure conditions and counterexamples

Square-law MOSFET assumptions omit short-channel velocity saturation, subthreshold leakage, body effects, channel-length modulation, process variation, thermal changes and contact resistance. Physical noise margins need measured or validated transfer characteristics.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

# 15. Logic voltage thresholds, noise margins and simplified RC switching

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Logic voltage thresholds, noise margins and simplified RC switching. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`NM_L=V_IL−V_OL; NM_H=V_OH−V_IH; t_(50%)=RC ln2`

**Units:** V, Ω, F, s, J. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

A Boolean truth table specifies symbols, not analog validity. Logic families use guaranteed high and low output windows (V_OH,V_OL) and permissible input windows (V_IH,V_IL). Positive low and high noise margins quantify allowable perturbation before a receiving logic gate is no longer guaranteed to interpret a signal correctly. These guaranteed limits must come from actual characterization or explicit technology specifications, not from ideal gate truth tables.

For a lumped constant-output-resistance switch charging a known load capacitance, the first-order ODE C dV/dt=(V_supply−V)/R gives V(t)=V_supply+(V0−V_supply)exp(−t/RC). At 50% of the total step, t_50=RC ln2. A gate-design timing budget must account for a path of gates and interconnect separately. This pedagogical RC approximation cannot predict sub-nanosecond real-device timing without measured parasitics and switching currents.

## Independently executable algorithm

Use `noise_margins_from_characterization` only on previously characterized voltage levels; reject non-ordered thresholds and negative margins. Reuse the earlier exact `rc_step` for a finite lumped circuit and verify its half-time and monotonicity. Test 2-input NAND and NOR truth tables separately from any analog assertions. Trace each V, Ω, F, s input and uncertainty.

## Worked scientific investigation

Suppose an externally specified 1.2 V logic family guarantees V_OL≤0.10 V, V_OH≥1.10 V, V_IL=0.40 V, V_IH=0.80 V. Then NM_L=0.30 V and NM_H=0.30 V. With R=1000 Ω and C=1 nF, t_50≈0.693 μs. This is a constructed specification and RC fixture, not a semiconductor measurement.

## Failure conditions and counterexamples

Noise margins depend on temperature, loading, fabrication variation and actual device transfer curves. RC timing ignores short-circuit dissipation, waveform slew limits, crosstalk, clock jitter and metastability.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

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


---

# 17. From CMOS gates to a full adder and n-bit ripple-carry arithmetic

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

From CMOS gates to a full adder and n-bit ripple-carry arithmetic. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`s=a XOR b XOR c_in; c_out=(a AND b) OR ((a XOR b) AND c_in)`

**Units:** bits, dimensionless Boolean values. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

Boolean arithmetic can be assembled from logic primitives (NAND is functionally complete). A full adder has three binary inputs a, b, carry_in and two outputs sum and carry_out. For all eight input triples the integer identity a+b+c_in=s+2c_out must hold. A ripple-carry adder propagates carry from bit i to bit i+1. Induction on the bit position proves that after processing i bits, accumulated lower output bits and carry encode the lower-i-bit sum exactly. The final result obeys a+b+c_in = sum + 2^width×carry_out.

This constructs an unambiguous *symbolic* arithmetic layer. It does not require transistors to execute the Python reference; its role is to preserve a bridge from transistor-level truth tables to the logical structure of arithmetic hardware. A physical carry chain has finite switching delays, fan-out limits and potential hazards that must be measured separately.

## Independently executable algorithm

Implement `full_adder` from XOR/AND/OR and `ripple_adder_unsigned` from repeated full-adders without Python arithmetic for the result construction. Test all eight full-adder truth cases and exhaust all 3-bit input pairs and carries. Then randomly compare 1–64-bit outputs with Python integer addition, including overflow. Reject out-of-range operands; do not silently reinterpret them as signed two’s-complement values.

## Worked scientific investigation

Use width=4 and add 1101₂ (13) + 0110₂ (6). Bitwise carry produces output 0011₂ (3) and carry_out=1, reconstructing 19 = 3 + 16. Then add the largest 64-bit unsigned word plus 1: the output word is zero and carry_out=1. Neither example demonstrates an actual CMOS chip.

## Failure conditions and counterexamples

This establishes functional Boolean correctness, not a timed latch, register file, clock system, memory, processor ISA or manufactured circuit. Real propagation delay may grow with carry length; a ripple adder is a simple reference, not an optimized architecture.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

# 18. Technological continuity: interfaces from semiconductor equations to computer architecture

**ATLAS FORGE / ORIGINAL canonical federation / Electronics & Semiconductors v0.2.0**

**Evidence:** authored mathematical reconstruction; constructed test fixtures. No field device, fabricated chip or signed independent science review.

## Technical question

Technological continuity: interfaces from semiconductor equations to computer architecture. What must a future engineer know to reproduce the model, detect its failure and connect it to later computing hardware?

## Equations and units

`materials → carriers/fields → device I–V → logic thresholds → gates → combinational arithmetic → registers → ISA → compiler → AI runtime`

**Units:** SI physical units; bits and architectural state. Use the indicated SI conventions and specify the direction of conventional electric current.

## Derivation and underlying reasoning

A reconstructible computing system is a chain of separately testable claims. Materials and dopants require chemical and metrology evidence. Carrier transport requires field equations, constitutive parameters and boundary conditions. Diode/transistor models then require measured I–V curves. Reliable logic needs guaranteed voltage windows, noise margins and timing budgets. Arithmetic needs exhaustive Boolean truth tables and carry correctness. Sequential computation adds metastability-aware storage, oscillators/clocks, reset, instruction semantics, memory mapping and software loading.

Each arrow is an explicit dependency, not an implication. A mathematically correct Python full adder does not provide a fabricated transistor; an accurate I–V fit does not certify a working CPU; a running CPU does not prove an independently validated AI training system. This chapter creates evidence slots for the Manufacturing and Computer Architecture domains without prematurely modifying either domain's canonical collection.

## Independently executable algorithm

Reconstruct the chain in layers: (1) verify exact SI constants and source rights; (2) run stable drift/diffusion checks and boundary conservation; (3) validate nodal KCL and power balance; (4) characterize transistor DC and dynamic thresholds on controlled measurements; (5) exhaust gate truth tables and arithmetic primitives; (6) design finite-state storage and an ISA in Computer Architecture; (7) bootstrap compiler/interpreter; (8) validate a minimal offline AI computation. At every stage preserve inputs, code, failed attempts, raw evidence, rights and reproducible hash receipts.

## Worked scientific investigation

Begin with 2,669 verified predecessor federation records, append this edition's exact revision records, test a single drift–diffusion edge, a 3-node resistor divider, a logic-family margin fixture and a four-bit full adder. For each layer, distinguish numerical exactness, model-form assumption, required laboratory instrument, and next-domain handoff. Failure to obtain a real silicon transfer curve is an open experimental gate, not a reason to erase software proofs.

## Failure conditions and counterexamples

No semiconductor wafers, integrated circuits, fabrication tolerances, clocked processor, silicon lithography or physical AI accelerator are constructed by this text. Manufacturing and Computer Architecture remain separate future Atlas nodes, and Bitwork routing is still prohibited until all content domains are established.

## Source fidelity and rights

Publisher reference card: `MIT-OCW-6012`. This bibliography is orientation, not an authenticated archived original publication. Chapters and code are newly authored. Source-to-equation certification by a qualified reviewer remains absent.

## Required cross-domain links

Mathematics & Physics supports the governing equations and unit analysis; Chemistry and Materials constrain device parameters; Measurement requires traceability; Computation and future Computer Architecture specify logical behavior. The reference models are runnable offline; experimental calibration requires actual instruments.


---

# V0.3.0 additions: physical circuits to timed state and error checks

# Chapter 19: From resistor-capacitor networks to timed node voltages

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Given capacitances to ground, conductive edges and applied current or voltage sources, reconstruct the voltages after a finite time step. This is the circuit analogue of a finite-volume conservation law. A future engineer must distinguish a calculated digital delay from measured voltage transitions.

## Derivation and dimensions
Write Kirchhoff current conservation at each free node as

\[C_i\frac{dV_i}{dt}+\sum_j G_{ij}V_j=I_i,\]

where capacitance is in farads, conductance is in siemens, voltage is in volts, and current is in amperes. Each edge \(g_{ij}\) contributes \(+g_{ij}\) to two diagonal entries and \(-g_{ij}\) to the corresponding off-diagonals. A grounded resistor contributes only to the diagonal. For backward Euler,

\[(C/\Delta t+G)\,V^{n+1}=C V^n/\Delta t+I^{n+1}.\]

A prescribed Dirichlet voltage is removed from the free-node system and transferred to the right-hand side. For positive grounding and capacitance this finite system is positive definite on free nodes. The reference implementation uses bounded pivoted Gaussian elimination, not production sparse factorization.

## Worked investigation
One capacitor \(C=1\ \mu\mathrm F\), shunt \(R=1\ \mathrm{k}\Omega\) (\(G=1\ \mathrm{mS}\)), \(V_0=2\ \mathrm V\), and \(\Delta t=1\ \mathrm{ms}\) gives \(V_1=(2)/(1+\Delta t/(RC))=1\ \mathrm V\). For an edge from a fixed 1 V node through a 1 kΩ resistor to a 1 µF node starting at 0 V, the first step gives 0.5 V.

## Limits and counterexamples
An exact time-continuous exponential is not equal to one backward-Euler step: at \(\Delta t=RC\), \(V_1/V_0=1/2\) versus \(e^{-1}\) analytically. Small discrete KCL residual does not establish small time-discretization error. Ideal fixed voltage sources do not predict source limitations, device parasitics, dielectric leakage or electromagnetic radiation. Large ill-conditioned networks require sparse solvers and measurement-validated elements.

## Reconstruct and verify offline
Run `rc_nodal_backward_euler` and compare every free-node voltage against a separately assembled linear system. Check graph indexing, finite inputs, positive R/C, discrete KCL residuals, step refinement and the effect of controlled voltage sources. Reject malformed graphs instead of silently inventing a reference node.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `rc_nodal_backward_euler`.
- **Equation/invariant:** `C dV/dt+G V=I; (C/dt+G)V_next=C V_old/dt+I`.
- **Units:** Farad, Siemens, Volt, Ampere, seconds.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 20: Energy from charging a digital node

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
How much energy does an ideal switching capacitance draw from a supply, and how can that constrain the power budget for future computer hardware?

## Derivation
For a capacitor \(C\) charged from 0 to \(V\) by an ideal constant supply, the source delivers \(Q V=C V^2\). The capacitor stores \(\tfrac12 CV^2\); the remaining \(\tfrac12 CV^2\) is dissipated in the resistive charging path. Discharging through a resistor dissipates the stored \(\tfrac12 CV^2\). Thus one completed 0→1→0 cycle dissipates \(CV^2\). If the mean **number of 0→1 events per clock** is \(\alpha\),

\[P_{\rm dynamic}=\alpha C V^2 f.\]

This definition of \(\alpha\) is explicit; calling it a fraction of all toggles without the corresponding factor of two would be inconsistent.

## Worked investigation
A 2 pF load charged to 1.5 V one hundred times in one thousand cycles at 1 GHz consumes \(100\,(2\times10^{-12})(1.5)^2=4.5\times10^{-10}\) J from the ideal supply over those cycles, or 0.45 mW average supply power. The capacitor stores 2.25 pJ after each charge, which is released on a subsequent full discharge.

## Counterexamples and failure bounds
Short-circuit overlap current, leakage, glitch transitions, supply droop, dynamic body effect, thermal noise, transistor size and routing capacitance are absent. This equation cannot demonstrate a real chip's consumption or a safe operating point. A numerical energy estimate without measured \(C\), \(V\) and activity is only a scenario.

## Reconstruction exercise
Create charge-event traces and separately count rising edges. Reproduce source energy, stored capacitor energy and average power using different clock frequencies; test zero-voltage and zero-event limits. Record the difference between a rise count and total transition count.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `charge_supply_energy`.
- **Equation/invariant:** `E_supply=N_rise C V^2; P=alpha C V^2 f`.
- **Units:** Farad, Volt, Joule, Watt, Hz.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 21: Reconstruct Boolean arithmetic from a single universal gate

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Can integer addition be reconstructed from a single universal Boolean primitive without assuming a preexisting CPU? The NAND operation \(N(a,b)=\neg(a\land b)\) is functionally complete; the reference uses only NAND at its combinational core.

## Derivation
Define \(u=N(a,b)\), \(v=N(a,u)\), and \(w=N(b,u)\). Then \(a\oplus b=N(v,w)\). A one-bit full adder computes \(x=a\oplus b\), \(s=x\oplus c_{in}\), and carry \(c_{out}=ab+c_{in}x\). Written purely with NAND, \(c_{out}=N(N(a,b),N(x,c_{in}))\). The invariant is

\[a+b+c_{in}=s+2c_{out}.\]

For width \(w\), iterate from least significant to most significant bit. The final carry corresponds to overflow from an unsigned \(w\)-bit result; signed two's-complement overflow requires separate logic.

## Worked investigation
Adding 15 and 1 in width four yields (sum,carry)=(0,1), representing the full unsigned value 16. For input (a,b,c)=(1,1,1), sum=1 and carry=1 because 3=1+2. Exhausting 2^(2w+1) input combinations for small widths is stronger than checking a few convenient examples.

## Counterexamples
Boolean equality does not guarantee voltage noise margins, propagation delay, switching power, fan-out drive, hazard freedom or semiconductor manufacturability. Ideal NAND logic cannot substitute for timed circuit verification. Inputs must be exact bits, not noisy analog voltages silently rounded to Boolean states.

## Reconstruction exercise
Derive the four-NAND XOR on paper; test all 8 full-adder rows, then ripple-carry for all small-width operand pairs. Compare to integer addition, explicitly testing carry and overflow. Document the gate-level netlist separately from physical layout.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `nand_full_adder, nand_ripple_add`.
- **Equation/invariant:** `x=a XOR b (four NAND); s=x XOR cin; cout=ab+cin*x`.
- **Units:** dimensionless bits; time and voltage are not modeled.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 22: State storage is not equivalent to combinational logic

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
A combinational circuit produces a function of current inputs. A sequential circuit also depends on prior state. To bridge from a full adder to a computer we need register semantics, clock edges, data stability and a representation of observations that cannot be asserted reliably.

## Model
An edge-triggered D register samples its input at a clock edge \(t_e\), assuming the input is stable for a setup interval \([t_e-t_{setup},t_e]\) and a hold interval \([t_e,t_e+t_{hold}]\). The mathematical reference accepts reported transition times. If any transition falls in this inclusive vulnerable interval, it outputs `None` (UNKNOWN) and does **not** sample a manufactured bit. An unviolated later capture may restore a known state.

## Worked investigation
For \(t_{setup}=0.2\) s, \(t_{hold}=0.1\) s, a clock edge at 1.0 s and input transition at 0.9 s violate setup; the reference returns unknown. With the next edge at 2.0 s and last input change at 1.4 s, the next sample is accepted. These large times are chosen for educational arithmetic, not transistor timing specifications.

## What UNKNOWN does and does not mean
UNKNOWN encodes insufficient guaranteed timing information. It is neither a statement that a real flip-flop always resolves incorrectly nor a probability distribution over metastable states. Real metastability may persist for variable durations and requires analog characterization, synchronizers and MTBF analysis. Digital simulation must not claim those physical guarantees.

## Reconstruction exercise
Record a clock and input-transition timeline, calculate each vulnerable interval, apply a trace, and distinguish known/unknown states. Repeat at exact interval boundaries and reject nonmonotonic edge/transition times. Chain a register to the abstract register bank in Chapter 25 but keep hardware specifications separate.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `EdgeRegister.capture`.
- **Equation/invariant:** `if transition in [edge-setup,edge+hold], state=UNKNOWN`.
- **Units:** seconds; abstract bits/UNKNOWN.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 23: Timing inequalities for a synchronous circuit

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Boolean correctness is insufficient to establish whether a circuit can run at a given clock frequency. Reliable synchronous design requires both longest-path setup and shortest-path hold timing constraints.

## Derivation and sign convention
Let positive capture skew \(s\) mean the capture clock arrives later than the launch clock. For a register-to-register path,

\[T+s\ge t_{CQ,max}+t_{PD,logic}+t_{setup},\]

\[t_{CQ,min}+t_{CD,logic}\ge t_{hold}+s.\]

Here \(t_{PD}\) is the latest propagation delay and \(t_{CD}\) the earliest contamination delay. The setup margin equals \(T+s-t_{CQ,max}-t_{PD}-t_{setup}\); the hold margin equals \(t_{CQ,min}+t_{CD}-t_{hold}-s\). Both must be nonnegative within uncertainty budgets.

## Worked investigation
For period 10 units, \(t_{CQ,min}=1\), \(t_{CQ,max}=2\), \(t_{CD}=2\), \(t_{PD}=3\), setup=1, hold=2, skew=0: setup margin=4, hold margin=1. A +2 capture skew improves setup margin to 6 but changes hold margin to -1: the path fails hold, despite the longer time available to setup.

## Failure modes and scope
Slowing the clock can repair setup but cannot repair a hold violation; modifying minimum path delay or skew is required. The example ignores supply/temperature/process variation, jitter, clock-tree uncertainty, clock-domain crossings, asynchronously asserted reset, real layout extraction and analog metastability. Source reference: MIT 6.004 computation structures official course materials, navigational citation only.

## Reconstruction exercise
Compute both margins for every path, seek the tightest setup and hold constraints, and test positive/negative skew. Explicitly refuse inconsistent delay bounds (earliest greater than latest). Do not infer a safe maximum frequency from a single illustrative path.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `register_path_timing`.
- **Equation/invariant:** `T+skew >= tCQmax+tPD+tsetup; tCQmin+tCD >= thold+skew`.
- **Units:** seconds; GHz=1/seconds.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 24: Preserving data integrity with a small error-correcting code

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
Stored or transmitted bits may flip. A minimal reconstructible error-correcting demonstration is the extended Hamming (8,4) single-error-correct/double-error-detect (SECDED) code. Its guarantees depend on a bounded error model.

## Construction
Place four data bits in 1-based codeword positions 3,5,6,7. Compute even parity at positions 1,2,4, each covering the positions whose binary indices share that parity bit. Set global position 8 to make total eight-bit parity even. To decode, compute the three-bit syndrome \(s\) over positions 1..7 and overall parity \(p\).

- \(s=0,p=0\): accept as clean.
- \(s\ne0,p=1\): one error at position \(s\), flip it and accept as corrected.
- \(s=0,p=1\): error in global parity bit 8, correct it.
- \(s\ne0,p=0\): a two-bit error is detected and data is **not** returned.

The code has minimum distance four. All one-bit errors are correctable, all two-bit errors detectable; higher-weight errors are not guaranteed to be detected or correctly interpreted.

## Worked investigation
For each of 16 data nibbles, the archive reference tests its clean codeword, all eight one-bit flips and all 28 two-bit flips. That is 16 × (1+8+28)=592 finite cases, with uncorrectable doubles returning no payload.

## Limitation and reconstruction
Coding-theoretic checks are not measured memory-error rates, radiation-hardening qualification or proof of long-term archival survival. Rebuild the parity-check matrix independently and compare syndrome behavior; document exactly which error patterns remain unprotected. Add checksums, redundancy, error logs and archival refresh outside this local coding model.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `hamming84_encode,hamming84_decode`.
- **Equation/invariant:** `minimum Hamming distance 4; SECDED syndrome and overall parity`.
- **Units:** dimensionless binary codewords.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 25: A minimal register bank with explicit unknown-state propagation

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Question and reconstruction objective
A future computer needs addressable, updateable state. A minimal word-addressable register-bank transition model separates hardware-independent semantics from physical memory-cell implementation.

## State transition
Let \(M\) be an array of words, \(a\) a valid address, \(d\) the input word and \(w\in\{0,1\}\) the write enable. At the active abstract edge,

\[M'_{i}=\begin{cases}d,&i=a\land w=1,\\M_i,&\text{otherwise}.\end{cases}\]

Reading the addressed location returns \(M'_a\) in this **write-first abstract convention**. Other architectures may choose read-first or no-change semantics; those choices must be explicit before constructing an ISA or memory system.

## Worked investigation
Given three byte registers [0,1,2], write 254 into location 1: next state [0,254,2] and readback 254. A timing-unsafe or otherwise indeterminate input is represented by UNKNOWN (`None`), propagating through the bank instead of quietly being converted to zero.

## Failure modes
An abstract register bank does not describe memory bitcell circuits, transistor access, clock networks, retention time, radiation upsets, physical read/write delays, endurance or temperature sensitivity. Address and data checks must reject invalid values, rather than wrap or truncate silently.

## Reconstruction exercise
Test each address for write and no-write behavior, deliberate UNKNOWN propagation, address out-of-range, and finite capacity. Extend with an ISA-level load/store operation in the separate future Computer Architecture Atlas, while retaining this node as the electronic-state prerequisite.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `register_bank_step`.
- **Equation/invariant:** `M'[a]=data if write_enabled else M[a]`.
- **Units:** byte values 0..255, address dimensionless.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# Chapter 26: Evidence-driven handoff to computer architecture

**ATLAS FORGE / original canonical 13-node federation — Electronics & Semiconductors v0.3.0**

**Evidence status:** original educational/engineering synthesis and finite constructed software tests. No publisher-original file authentication, independent scientific review, wafer process, device calibration, or functioning CPU is claimed.

## Objective
Place the preceding electronics knowledge into a specific reconstruction dependency chain. A binary full adder is not a CPU; a register is not a reliable clocked system; a digital simulator is not semiconductor fabrication evidence.

## Interface ledger
1. **Material and geometry prerequisites:** carrier concentration, mobility, doping profiles, dielectric permittivity, transistor geometry and process uncertainty come from Chemistry, Materials and future Manufacturing.
2. **Electrical primitives:** measured transistor I–V, capacitance, leakage, switching delays, voltage windows, power supply/load requirements and thermal behavior must be established experimentally before hardware signoff.
3. **Logical primitives:** NAND truth tables, XOR, adders, decoder/multiplexer and finite state semantics can be verified exhaustively on bounded designs.
4. **Sequential primitives:** setup/hold, propagation/contamination delays, clock skew, unknown states and synchronizer requirements must be specified; timing signoff requires measured or characterized values.
5. **Information integrity:** explicit data formats, error detection, error-correction limits, reset, watchdog behavior, and machine-checkable test vectors.
6. **Architecture handoff:** a separately versioned Computer Architecture Atlas defines datapaths, control states, an instruction set, memory maps, boot sequence, interrupt/error handling and a minimal test program.
7. **AI continuation:** only after an executable computer, compiler/runtime and reproducible model/inference are available should the federation assert an end-to-end AI reconstruction demonstration.

## Minimal bounded proof obligation
Demonstrate gate-level XOR and NAND-only full adder, four-bit ripple addition with correct carry, abstract state storage, and a timing-path audit. The v0.3 reference gives these numerical/test-vector components without claiming their fabrication. A prospective laboratory campaign should compare characterized voltage transfers, delays and power/temperature traces to reference models, preserving raw data and uncertainty budgets.

## Scientific evidence boundary
ATLAS FORGE's new chapter is original synthesis with verifiable finite software tests and bibliographic pointers, not a rights-cleared archive of MIT publications or independent hardware expert certification. Keep the original 30-domain queue unchanged, complete content libraries first, Bitwork routing afterward, integrated validation and desktop transfer last.

## Reference implementation and source accountability
- **Executable kernel:** `electronics_atlas/v03_models.py` — `reconstruction dependency matrix`.
- **Equation/invariant:** `physical→logic→registers→architecture→compiler→AI runtime`.
- **Units:** SI units and binary abstractions.
- **Historical dependency:** Chapters 1–18 of the same Electronics node and Mathematics/Physics reference; unchanged historical release snapshots preserved.
- **Bibliography:** MIT OpenCourseWare 6.004 computation structures, course index and timing notes, *navigational reference only*. No complete authenticated publisher PDF or license clearance for republishing course material is represented.
- **Evidence:** local v0.3 tests; independently assembled finite NumPy/integer oracle. Calibration and expert review remain separately outstanding.


---

# v0.4.0 — New original reconstructions (chapters 27–34)

# Chapter 27: Digital voltage thresholds and guaranteed noise windows

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Foundations and derivation
Binary digits are abstractions of analog voltage intervals, not fixed voltages. For a receiving gate, values no greater than VIL(max) represent low, and values no less than VIH(min) represent high. Voltages strictly between those two limits have no guaranteed binary interpretation. The driving gate's worst low output is VOL(max), and its worst high output is VOH(min).

For a high signal to be guaranteed valid after bounded noise of magnitude N, its lower bound VOH(min) − N must remain at least VIH(min); therefore N ≤ VOH(min) − VIH(min). For low signals, VOL(max) + N ≤ VIL(max), giving N ≤ VIL(max) − VOL(max). Take the minimum to obtain a symmetric conservative noise budget. The implementation rejects inconsistent ranges; it does not coerce an unknown input to 0.

## Worked investigation
Suppose VDD=3.3 V, VOL≤0.4 V, VIL≤1.0 V, VIH≥2.1 V, VOH≥2.9 V. The two static margins are 0.6 and 0.8 V. A measured input at 1.5 V lies between thresholds and must yield UNKNOWN, not a fabricated bit. A margin of 0 V is logically possible but admits no positive bounded noise.

## Failure analysis and reconstruction
There is no universal CMOS threshold; thresholds depend on process, supply, temperature and loading. Neither these intervals nor a static margin establish dynamic noise immunity, hysteresis, interconnect crosstalk, supply droop or immunity to radiation events. To reconstruct them physically, characterize low/high transfer limits over voltage, temperature and input transition rate; retain instruments, uncertainty and repeat traces. A source card without original publisher bytes is not measured evidence.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `digital_noise_margins, input_logic_level`.
- **Governing relation:** `NML = VIL(max) - VOL(max), NMH = VOH(min) - VIH(min)`.
- **Units:** volts.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 28: Combinational timing from acyclic gate networks

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Reconstructible directed acyclic graph
A combinational circuit is represented as a directed graph whose leaf pins have arrival intervals and whose gates have bounded contamination/minimum and propagation/maximum delays. Each node is evaluated after all its predecessors. Reject disconnected pins, duplicate drivers, negative bounds and directed cycles. The independent oracle enumerates all input–output paths on small acyclic graphs, instead of repeating the topological dynamic-programming algorithm.

The min/max recurrence gives a **conservative envelope** of possible arrival times, not a functional sensitization proof: Boolean conditions may prevent some structural paths from switching. It also omits interconnect parasitics, transition-dependent timing, glitch energy, correlated process corners, and reconvergent path complexity.

## Worked investigation
Two primary inputs have arrivals A=[0,1] ns and B=[0,2] ns. Gate G1(A) delay [1,1] ns, G2(B) delay [2,4] ns, G3(G1,G2) delay [1,2] ns. The output earliest is 2 ns (A→G1→G3), and latest is 8 ns (B→G2→G3). The reported longest structural path is B–G2–G3. A negative delay or a feedback loop is not made magically schedulable by the reference implementation.

## Build and measurement handoff
A physical timing library would supply characterized delays indexed by voltage, input slew, output load and process corner. Future Manufacturing must preserve layer stacks and parasitics, while Computer Architecture must connect the path to register-to-register timing. This chapter does not claim to contain a transistor-extracted design or signoff-grade static timing analysis.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `logic_dag_arrival`.
- **Governing relation:** `t_earliest(out)=min_i t_earliest(in_i)+d_min; t_latest(out)=max_i t_latest(in_i)+d_max`.
- **Units:** seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 29: Setup, hold, clock skew, and timing closure

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Edge convention and proof obligations
Consider one launch register clocked at time 0 and one capture register clocked at time Δ (positive capture-minus-launch skew). The next capture edge is T+Δ. The latest data reaches the destination at t_cq,max + t_comb,max. Safe setup requires latest arrival ≤ T+Δ−t_setup−u_setup. The earliest data arrives at t_cq,min+t_comb,min; safe hold requires earliest arrival ≥ Δ+t_hold+u_hold. The equations above are these inequalities rearranged as slacks. Positive capture skew eases setup but makes hold harder.

The model refuses inconsistent minimum/maximum bounds and exposes both slacks separately. A circuit cannot be judged safe using only maximum delay. Negative slack is a violation of the declared assumptions, not a number to round up.

## Worked investigation
Take T=10 ns, t_cq[min,max]=[1,2] ns, combinational[min,max]=[2,4] ns, setup=1 ns, hold=0.5 ns, and zero skew/uncertainty. Setup slack=3 ns and hold slack=2.5 ns. With positive 2 ns capture skew, setup slack becomes 5 ns but hold slack drops to 0.5 ns. Now add enough skew/uncertainty to make hold negative; accepting the setup margin alone would be unsafe.

## Limits
This is single-clock, one-cycle static timing, not a multi-clock signoff engine. Actual gate delay tables, clock tree jitter, launch/capture correlations, input-output constraints, metastability and silicon process/thermal corners are not supplied. Measurement across chips and corners would be needed before asserting any maximum clock rate.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `synchronous_setup_hold`.
- **Governing relation:** `S_setup=T+skew−t_setup−u_setup−t_cq,max−t_comb,max; S_hold=t_cq,min+t_comb,min−skew−t_hold−u_hold`.
- **Units:** seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 30: Metastability, synchronization, and empirical failure envelopes

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Why deterministic digital proofs stop at clock-domain boundaries
A clocked storage element can enter an analog metastable region if an input changes near its aperture. No finite digital-time bound guarantees resolution for every possible event. The correct engineering approach is to reduce risk through synchronizer stages and protocol design, not to declare the event impossible.

An illustrative empirical tail model uses two **measured device parameters** T0 (seconds) and τ (seconds): the event rate is approximately f_clk f_data T0 exp(−T_res/τ), so MTBF is its reciprocal. Work in logarithms to avoid overflow at large resolution times. This equation assumes a stationary input-toggle process, appropriate synchronizer topology, suitable environmental calibration and a regime where a fitted exponential model is justified. It is not universally predictive.

## Worked investigation
For a *hypothetical* example with f_clk=10 MHz, f_data=1 MHz, T0=1 ns, and τ=30 ps, increasing available resolution from 1 ns to 2 ns raises log10(MTBF) by ΔT/(τ ln10)≈14.48 orders of magnitude under this formula. These parameters are invented demonstration inputs, not characterized semiconductor data; the result must not be interpreted as a silicon reliability guarantee.

## Reconstruction protocol
Record the flip-flop family, process/corner, clock tree, supply, temperature, output load and metastability characterization method before claiming an empirical MTBF. For multi-bit buses, independently synchronizing each bit is insufficient to guarantee coherent atomic capture. Use a handshake, Gray-coded pointer with proper constraints, or asynchronous FIFO under specified assumptions. The reference calculation deliberately requires explicit T0 and τ rather than defaulting to misleading constants.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `synchronizer_mtbf_log10`.
- **Governing relation:** `MTBF≈exp(T_res/τ)/(f_clk f_data T0); log10(MTBF)=T_res/(τ ln10)−log10(f_clk f_data T0)`.
- **Units:** hertz and seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 31: Reconstructing a word ALU from gate-level addition

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Binary operations and two's-complement representation
A word-level ALU is built from Boolean gates, adders and controlled multiplexing. For w-bit nonnegative operands a,b, let mask=2^w−1. A NAND-built ripple-carry adder computes ADD modulo 2^w and reports the final unsigned carry. SUB uses a+(mask XOR b)+1. For subtraction the final carry equal to 1 means **no unsigned borrow**; conflating carry and borrow would corrupt later arithmetic.

Signed two's-complement overflow is not the same as unsigned carry. For ADD, overflow is true when the operand sign bits agree and the result sign differs. For SUB, overflow is true when operand signs disagree and result sign differs from a. Zero and negative flags are derived from the result; other operations explicitly define carry rather than implicitly preserving an undocumented flag.

## Worked investigation
In 4 bits: 7+1 produces result 8 (binary 1000), no unsigned carry, but signed overflow=1 because +8 exceeds the signed range [−8,7]. In contrast 15+1 produces result 0 and carry=1 without signed overflow. For 8−1, result=7 and signed overflow=1 because −8−1 is below representable range.

## Reconstruction boundary
The model accepts widths 1–16, validates exact integers and refuses unsupported operations. It is *combinational semantics*, not a clocked ISA, datapath schedule, gate-count synthesis, physical layout, memory bus, or silicon CPU. A later Computer Architecture node must define control sequencing, instruction decoding and observable machine state. Exhaustive 4-bit and random 8-bit oracles detect implementation mistakes without proving a physically fabricated ALU.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `primitive_alu (uses nand_ripple_add from v0.3)`.
- **Governing relation:** `sum=(a+b+cin) mod 2^w; carry_out=floor((a+b+cin)/2^w); SUB=a+not(b)+1`.
- **Units:** binary words and flags.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 32: Addressable memory: collisions, unknowns, and reliability boundaries

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Explicit memory transition semantics
Physical storage arrays require refresh or retention assumptions, word lines, bit lines, sense amplifiers and peripheral circuits. The abstract memory kernel exposes only one bounded edge-to-edge update for a finite list of words. Valid addresses and word widths are checked rather than silently wrapped. An UNKNOWN stored word remains unknown.

A simultaneous read and write of the same address has **no universal semantic convention**. Read-first returns the old word, write-first returns the new word, and undefined returns UNKNOWN. A future computer architecture must declare which convention its instructions and memory bus require. The model does not assert any read/write transition time, endurance or bitcell stability.

## Worked investigation
Start with words [1,2,3], address 1, and write value 9. The post-cycle words are [1,9,3]. For read-first the response is 2; for write-first it is 9; for undefined it is UNKNOWN. Each is a different *declared* contract, and pretending one is universal would make a reconstructed machine nondeterministic across implementations.

## Reliability and verification
Pair this transition model with the v0.3 SECDED code for a bounded detection/correction exercise, including explicit double-error detection. That does not prevent all multi-bit faults, address corruption, errors within the decoder, soft-error bursts, or data corruption during writes. A full memory requires measured bitcell retention, read disturb, static noise margin, access delay, sense-amplifier error rates, ECC overhead and temperature drift.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `bounded_memory_cycle; previous SECDED encode/decode`.
- **Governing relation:** `M_next[a]=data if write=1 else M[a]; read-collision must declare read-first/write-first/undefined`.
- **Units:** words and addresses, dimensionless.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

# Chapter 33: Four-phase handshake and asynchronous interface correctness

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Asynchronous data transfer contracts
Two independent clocks cannot be assumed aligned. A four-phase return-to-zero request/acknowledge protocol is one way to define a causal exchange: requester asserts request while data is stable, receiver eventually asserts acknowledge, requester deasserts request, receiver deasserts acknowledge. Four logical phases are [00,10,11,01,00]. Explicit stateful validation rejects illegal orderings, rather than treating unordered transitions as a successful transaction.

The logical protocol **does not implement a physical synchronizer**. Its assumptions include appropriately synchronized control signals, data stability until acknowledged, monotonic return-to-zero behavior, no unbounded transport faults, and an explicit timeout/retry/error policy. The state machine cannot guarantee bounded metastability resolution, arbitration progress or data coherency across asynchronous buses by itself.

## Worked investigation
Starting in IDLE at 00, the request transitions 10 (REQUESTED), then 11 (ACKNOWLEDGED), then 01 (RETURNING), then 00 (IDLE). Attempting 00→11 skips the request stage and is rejected. Deasserting acknowledge before the requester drops request likewise violates the specified order.

## Reconstruction handoff
A measured implementation would instrument request/ack arrival times, metastable or missing transitions, control crossing constraints, data setup and failure injection, and would preserve timing/uncertainty logs. Later Computer Architecture must define the bus and memory ordering; later Manufacturing must supply a characterized standard-cell or discrete hardware implementation.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `four_phase_handshake_step`.
- **Governing relation:** `(req,ack) state sequence: 00→10→11→01→00`.
- **Units:** binary logic state.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.


---

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


---

# Scoped v1 release candidate — Original reconstruction chapters 35–52

The following 18 chapters extend the original 34; chapters remain separately readable and indexed. Claim scope is finite scientific software and authored mathematical reconstruction; not wafer fabrication, real hardware validation or expert-reviewed scientific conclusions.

# Chapter 35 — SI electrical constants, units and measurement traceability

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The chain from electrons to a computer begins with *measured* electric charge, time, temperature, length and geometry. Do not substitute unitless constants or assume that a textbook material parameter is a reference standard. In the SI, the elementary charge q is exactly 1.602176634×10⁻¹⁹ C and Boltzmann's constant is exactly 1.380649×10⁻²³ J K⁻¹ by definition. Vacuum permittivity is not a defined exact constant; use the cited CODATA edition and record uncertainty when needed.

Thermal voltage is V_T=k_B T/q. Checking dimensions: (J/K)(K)/(C)=J/C=V. At T=300 K the reference implementation yields approximately 25.852 mV. Conversion of dopant density must be explicit: 1 cm⁻³ = 10⁶ m⁻³. Resistivity is Ω·m, sheet resistance is Ω per square, mobility is m²/(V·s), Hall carrier density is m⁻³ and oxide capacitance per area is F/m².

An audit chain should name the instrument, its measurement quantity, calibration certificate, uncertainty, traceability, date, temperature, fixtures, and sampling method. In this edition no physical instrument results or accredited calibrations have been received. All numerical values used in examples are constructed inputs.

**Worked investigation:** calculate V_T at 250, 300 and 350 K, then show that an ideal diode current's voltage sensitivity varies with 1/V_T. Retain the input temperatures and q/k_B constants in a machine-readable receipt. Reject T≤0 K as physically outside the model. Source references: BIPM SI Brochure and NIST semiconductor metrology pages, bibliographic links only.

## Implementable contract and falsification

- **Reference equation:** `V_T = k_B T/q`.
- **Dimensional quantities:** V, K, J, C; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `thermal_voltage`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `BIPM-SI` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 36 — Carrier statistics, neutrality and coupled charge

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A semiconductor model must distinguish mobile electron concentration n from mobile hole concentration p, ionized donors N_D⁺, ionized acceptors N_A⁻, and trapped or fixed charge. For nondegenerate thermal equilibrium, the mass-action approximation is np≈n_i². The local space-charge density under the elementary drift–diffusion model is ρ=q(p−n+N_D⁺−N_A⁻)+ρ_fixed. These are not interchangeable with net dopant inventory: a compensated wafer can have large N_D and N_A but small net carrier density.

Electric potential couples into carrier statistics through electrochemical potentials. To avoid sign errors, explicitly write φ as electrostatic potential in volts, E=−∂φ/∂x, and the electron-charge sign as −q; use current J_n and J_p with their own sign conventions. Mathematically the coupled problem involves Poisson and two continuity equations; the Mathematics & Physics node already preserves a bounded 1D reference. Reuse it as an exact revisioned dependency instead of silently reimplementing a conflicting equation.

Boundary cases are as important as typical examples: n,p>0, total charge balance, contact and insulator boundary conditions, and uniqueness of the solutions are not guaranteed merely by a small nonlinear residual. A measured I–V curve needs additional mobility, recombination, trap, interface, and geometry calibration.

**Worked investigation:** choose n=10²¹ m⁻³, p=10¹⁹ m⁻³, N_D⁺=10²¹ m⁻³, N_A⁻=10¹⁹ m⁻³. The bracketed net ρ/q is zero; then perturb one term to demonstrate that charge neutrality is not hard-coded.

## Implementable contract and falsification

- **Reference equation:** `rho = q(p − n + N_D⁺ − N_A⁻) + rho_fixed`.
- **Dimensional quantities:** C/m³, m⁻³; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `coupled_math_dependency`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 37 — Junction I–V, diode stable numerics and missing parasitics

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The ideal Shockley law I=I_s(exp(V/(n V_T))−1) follows from low-level injection, quasi-neutral regions and diffusion transport under a limited p–n junction model. It is not an avalanche-breakdown equation, a series-resistance model, a high-injection model, or a thermal device model. Logarithmic current plots can hide the difference between measured leakage and an assumed saturation current.

Use `expm1(x)` for the difference exp(x)−1 when |x| is small. Direct subtraction loses relative precision near zero bias. In reverse bias many thermal voltages below zero, the ideal current approaches −I_s, but real reverse leakage and breakdown are absent. At large forward voltages, the ideal exponential overflows or predicts unphysical currents; the reference implementation reports its bounded range rather than returning an invented value.

A measured I–V acquisition plan records T, current compliance, fixture contact resistance, forward and reverse sweep direction, dwell time, self-heating, and repeatability. Only after measuring these can one estimate ideality factor from d ln I/dV, and only in an empirically justified bias interval.

**Worked investigation:** compute I at 0, ±0.1 and +0.3 V at T=300 K, with a declared synthetic I_s and n. Show exactly zero current at V=0 and the −I_s asymptote in the ideal model. Independently calculate with high precision and mark that as numerical, not laboratory evidence.

## Implementable contract and falsification

- **Reference equation:** `I = I_s expm1(V/(n V_T))`.
- **Dimensional quantities:** A, V, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `ideal_diode_current`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 38 — MOS oxide capacitance and material thickness

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A metal–insulator–semiconductor stack first requires geometrical capacitance. A uniform planar oxide of thickness t_ox, electrode area A and relative permittivity ε_r has C_ox=ε₀ ε_r A/t_ox. Its per-area capacitance is C_ox/A=ε₀ ε_r/t_ox. Derivation: E≈V/t in the ideal uniform slab; D=εE; Q=DA; C=dQ/dV=εA/t. The derivation assumes no fringing, no dielectric dispersion, no breakdown, and uniform dimensions.

A real MOS capacitance–voltage curve differs from the oxide-only expression because space-charge, interface-state, depletion, accumulation and inversion capacitances can contribute in series or frequency-dependent ways. Forcing a measured C–V curve to equal this simple equation would erase critical semiconductor information.

Manufacturing reconstruction requires dielectric composition and thickness metrology; ellipsometry, capacitance measurement, reference geometry and contact calibration must be separately documented. A single tabulated ε_r value does not certify a process.

**Worked investigation:** double the oxide thickness at constant area and composition. The model predicts a capacitance ratio of 1/2. Multiply area by four and verify a fourfold capacitance change. Reject t_ox=0 and ε_r≤0. The implementation is explicitly parallel-plate only.

## Implementable contract and falsification

- **Reference equation:** `C_ox = epsilon_0 epsilon_r A/t_ox`.
- **Dimensional quantities:** F, F/m², m; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `mos_oxide_capacitance`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 39 — MOS substrate body effect, threshold definition and signs

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

For a long-channel NMOS with a p-type body under the standard depletion approximation, reverse source–body bias increases the magnitude of depletion charge. One compact threshold expression is V_T(V_SB)=V_T0+γ(√(2φ_F+V_SB)−√(2φ_F)), with φ_F taken as a positive potential magnitude and V_SB≥0. Gamma carries units √V. The square-root term can be derived by combining Poisson charge in the depleted bulk with the oxide gate-charge relation.

This relation is not universal for short-channel transistors, forward-bias bulk junctions, nonuniform doping, floating body or strong interface-charge effects. Always state the sign convention: V_SB=V_source−V_body. Permitting negative V_SB in a model documented only for reverse bias can silently invalidate the derivation.

Threshold voltage itself depends on an operational extraction definition, not a single primitive constant. Device characterization should record how threshold was extracted from current–voltage curves, temperature, drain bias and body bias.

**Worked investigation:** for synthetic V_T0=0.6 V, γ=0.3√V, φ_F=0.3 V, V_SB increasing 0→2 V, demonstrate monotone threshold increase. Check that V_SB=0 reproduces V_T0. Mark measured γ and φ_F as unavailable.

## Implementable contract and falsification

- **Reference equation:** `V_T(V_SB)=V_T0+gamma(sqrt(2phi_F+V_SB)-sqrt(2phi_F))`.
- **Dimensional quantities:** V, sqrt(V); all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `mos_body_effect_threshold`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 40 — Long-channel MOSFET current regions and transconductance

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Start from the ideal charge-sheet gradual-channel approximation with channel inversion charge proportional to V_GS−V_T−V(x). Under a constant mobility, uniform width-to-length ratio and negligible velocity saturation, integrate the charge drift term along the channel to get I_D=k[(V_GS−V_T)V_DS−V_DS²/2] for 0≤V_DS<V_GS−V_T. At pinch-off, the ideal saturated result is k(V_GS−V_T)²/2. The factor k normally contains μ_n C_ox(W/L) and its value must be identified experimentally or from a qualified process model.

For V_GS≤V_T, a deliberately ideal *cutoff* branch returns zero; this is not how measured subthreshold leakage behaves. Optional channel-length modulation multiplies by (1+λ V_DS), an empirical convenience, not evidence that short-channel electrostatics is modeled. The transconductance g_m=∂I_D/∂V_GS is k V_DS in the triode region and k(V_GS−V_T) in the ideal saturated region (both scaled by the declared λ factor).

**Worked investigation:** evaluate an NMOS at V_GS=1 V, V_T=0.5 V, V_DS=0.25 V, k=1 mA/V²; compare the 93.75 μA linear-region result to 125 μA in ideal saturation. Check continuity at V_DS=0.5 V. Explicitly reject negative V_DS in the forward-only model.

## Implementable contract and falsification

- **Reference equation:** `I_D,linear=k[(V_GS−V_T)V_DS−V_DS²/2]`.
- **Dimensional quantities:** A, V, S; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `long_channel_nmos`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 41 — Short-channel, subthreshold and device model limits

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Practical transistors exhibit weak inversion, drain-induced barrier lowering, velocity saturation, mobility degradation, gate tunneling, junction leakage and parasitic resistance/capacitance. Many effects make an ideal square-law current versus gate voltage incorrect over the full operating range. A simple subthreshold mnemonic is I_D∝exp[(V_GS−V_T)/(n_s V_T)] with a measured subthreshold slope factor n_s, but the prefactor and boundary conditions are device specific. This memo deliberately does not blend that form into the ideal MOS model without calibrated parameters.

The device should be characterized by families of I_D–V_GS and I_D–V_DS sweeps at several controlled temperatures, drain voltages and body biases; observations must distinguish threshold extraction, leakage floor, current compliance, self-heating and time-dependent bias effects. Cross-corner validity requires model error metrics at process/voltage/temperature corners, not one appealing fit.

A reconstruction package must preserve both the model and evidence of its failures. The present finite references demonstrate long-channel mathematics, not transistor fidelity at nanometer feature sizes.

**Worked investigation:** construct two hypothetical I–V traces with the same textbook threshold but different leakage and slope parameters. Show that a single threshold number cannot identify leakage behavior. Record the identifiability gap as a review blocker rather than tuning arbitrary constants.

## Implementable contract and falsification

- **Reference equation:** `S_sub = (ln(10)) n_s V_T  [V/decade]`.
- **Dimensional quantities:** V, A, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `none`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 42 — Diffusion equation and bounded dopant redistribution

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Under Fick diffusion with constant D, the concentration obeys ∂C/∂t=D∂²C/∂x². For an idealized surface sheet dose Q distributed into the nonnegative half-space with reflecting boundary and no loss, the Gaussian solution is C(x,t)=Q exp[−x²/(4Dt)]/√(πDt). Its integral over x∈[0,∞) is Q, showing dose conservation. The finite-depth integral is Q erf[x/(2√Dt)].

This is *not* a furnace diffusion recipe. Real implants, oxide interfaces, vacancies, activation, clustering, electric-field effects and temperature-dependent diffusivity invalidate the constant-D, delta-initial-dose model. Restoring actual semiconductor processing requires distinct measurement, safety and contamination-control methods; the Atlas preserves the equation and its falsifiable assumptions, not an unverified physical process.

**Worked investigation:** Q=10¹⁶ m⁻², D=10⁻¹⁴ m²/s, t=10 s. Verify that the integrated dose approaches Q at large depth and that the surface concentration declines with √t. Compare erf-integral against a high-precision oracle; report absolute and relative numerical errors. Reject t≤0 and D≤0.

## Implementable contract and falsification

- **Reference equation:** `C(x,t)=Q exp(-x²/(4Dt))/sqrt(pi D t)`.
- **Dimensional quantities:** m⁻³, m²/s, m⁻²; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `half_space_gaussian_dopant`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6012` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 43 — Four-point probe, sheet resistance and Hall metrology

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Electrical metrology starts with geometry and identifiability. For a homogeneous, isotropic, infinite thin conducting sheet and four equally spaced collinear probes, R_sheet=(π/ln 2)(V/I). Finite boundaries, inhomogeneous thickness, contact geometry, sample anisotropy, temperature drift and thermoelectric offsets require correction. The coefficient is not a universal value for arbitrary probe placements.

In a simple one-carrier Hall bar, |n|=|IB/(q t V_H)| from R_H=V_H t/(IB) and |R_H|=1/(q|n|). Carrier-type sign requires a carefully documented voltage, magnetic field and current orientation; the reference function returns magnitude only. Multi-carrier systems, Hall factors and contact nonidealities can substantially alter inference.

A real acquisition should reverse both current and magnetic field to suppress offsets, measure thickness and instrument uncertainties, and preserve raw traces and calibration certificates.

**Worked investigation:** synthesize V and I for R_sheet=50 Ω/□; recover the sheet resistance. Then synthesize a Hall voltage for n=10²² m⁻³ and verify recovery without claiming actual wafer doping was measured. Reject B=0 and V_H=0 as non-identifiable in this model.

## Implementable contract and falsification

- **Reference equation:** `R_sheet=(pi/ln2)(V/I); n=|I B/(q t V_H)|`.
- **Dimensional quantities:** Ohms/square, m⁻³; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `four_point_sheet_resistance;hall_carrier_density`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `NIST-HALL` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 44 — Capacitance–voltage and current–voltage parameter extraction

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The same measured C–V or I–V dataset can support more than one physical explanation. MOS accumulation capacitance estimates oxide capacitance only within a regime where semiconductor depletion and frequency response do not dominate. An apparent density from slope of 1/C² versus bias relies on the assumed depletion model, junction geometry and material permittivity. A measured transistor transfer curve requires a threshold *extraction procedure* and declared current criterion.

A reproducible electronic-characterization dataset must include raw units, voltage polarity, source-meter compliance, sweep direction and speed, temperature, geometry, instrument accuracy, open/short compensation, time series and uncertainty budget. Save raw samples separately from fitted parameters. For each fitted model record the residuals, parameter covariance, outliers, alternate fits and what data would falsify the interpretation.

A numerical output matching a few points is neither calibration nor identifiability. The Atlas should reject requests to infer an unmeasured oxide thickness or donor profile with no suitable geometry and control data.

**Worked investigation:** compute a synthetic oxide capacitance from area, thickness and ε_r. Repeat with 10% area uncertainty and show that an inferred thickness inherits systematic uncertainty. Report the missing real calibration and full-equation review as HOLD.

## Implementable contract and falsification

- **Reference equation:** `C/A = epsilon_0 epsilon_r/t_ox`.
- **Dimensional quantities:** F, m, V; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `mos_oxide_capacitance`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `NIST-DIELECTRIC` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 45 — Lithographic pattern transfer and overlay error budgets

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Patterned semiconductor devices depend on more than masks: substrate flatness, optical wavelength, numerical aperture, illumination, resist chemistry, focus, etch bias, registration and defect contamination all affect printed critical dimensions. The conventional optical resolution heuristic CD≈k₁ λ/NA is only a scaling relationship; it is not a process-qualified printability equation and should not be extrapolated beyond the applicable system.

An explicit manufacturing reconstruction graph records mask production, lithographic imaging, resist development, etch, alignment verification and final structural metrology. Static tolerance stacking can give a conservative worst-case bound by summing declared independent *bounds*; it cannot establish statistical yield, line-edge roughness or correlated errors.

**Worked investigation:** a hypothetical 40 nm nominal feature has bounded error contributions of 1 nm mask, 2 nm alignment and 3 nm etch bias, producing a 6 nm worst-case additive bound. This is a mathematical budget, not a verified achievable semiconductor process. Compare that bound with an externally established permitted tolerance, and reject negative tolerance inputs.

## Implementable contract and falsification

- **Reference equation:** `CD approx k1 lambda/NA; err_max <= err_mask+err_overlay+err_etch`.
- **Dimensional quantities:** nm, dimensionless; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `line_edge_overlay_budget`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `IBM-SEMICONDUCTOR` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 46 — Oxidation, deposition, etch, doping and process order

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

Chip fabrication is a dependency-controlled sequence of transformations of the wafer, not one material recipe. A minimal account distinguishes starting substrate inspection, surface preparation, electrical isolation, dielectric growth/deposition, lithographic patterning, selective material removal, dopant introduction and activation, conductor formation, interconnect and passivation, probe, packaging and final testing. Each operation changes geometry, stress, composition, electrical behavior or defect population; the order matters because later thermal and chemical steps can modify earlier layers.

For each transformation preserve inputs, outputs, material identity, measurement checkpoints, safety controls, process-window assumptions and evidence grade. A step should not be called successfully reproduced merely because its name exists in a flowchart. Require instrument logs and physical inspection, plus independent validation of wafer purity, overlay, film thickness, sheet resistance, line continuity, and yield.

The reference edition provides a process dependency graph and failure taxonomy, not detailed high-purity cleanroom instructions, chemical specifications or a proven fabrication route.

**Worked investigation:** trace a gate dielectric from target electrical capacitance backward to material permittivity, area, thickness, oxide formation, uniformity measurement, leakage test and circuit-level switching consequences. Flag every handoff where no physical measurement dataset exists.

## Implementable contract and falsification

- **Reference equation:** `gate_C = epsilon A/t; process steps preserve ordering dependencies`.
- **Dimensional quantities:** F, m, s, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `none`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `IBM-SEMICONDUCTOR` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 47 — Thermal conduction, self-heating and power budgeting

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

An electronic circuit stores and dissipates energy. Charging a capacitor C from a supply V stores E_C=½CV²; in a resistive charge cycle the supply delivers CV² and dissipates the remaining half in the path, under the ideal charge model. Activity factor α, clock frequency f and total switched capacitance lead to the common dynamic-power approximation P_dynamic≈α C V² f. Leakage and short-circuit power must be accounted for separately.

The simplest lumped thermal response is C_th dT/dt=P−(T−T_ambient)/R_th. For constant power P, T(t)=T_ambient+PR_th+[T(0)−T_ambient−PR_th]exp[−t/(R_th C_th)]. It does not model hot spots, nonlinear thermal conductivity, multiple packages or electromagnetic coupling.

A temperature limit cannot be established from this model without independent package/interface characterization, steady-state cooling configuration and measured device temperature. Refuse unsupported claims of safe operating conditions.

**Worked investigation:** T_amb=300 K, T(0)=300 K, P=2 W, R_th=10 K/W, C_th=0.1 J/K; the model approaches 320 K with a 1 s time constant. Verify initial and long-time bounds.

## Implementable contract and falsification

- **Reference equation:** `T(t)=T_amb+P R_th+(T0−T_amb−P R_th)exp(−t/(R_th C_th))`.
- **Dimensional quantities:** K, J/K, K/W, W; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `thermal_rc`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 48 — SRAM cell state, noise margins and read disturbance

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The classic six-transistor SRAM bitcell contains two cross-coupled inverters and two access devices. Its binary abstraction has two stable logical states under suitable bias conditions, but actual stability depends on the analog inverter transfer curves, supply voltage, mismatch, noise, bitline precharge and read/write conditions. The static noise margin is not simply the digital VIH−VIL gap; the butterfly-curve construction or an equivalent qualified analog extraction is required.

Write ability and read stability compete through device ratios; an idealized bit array cannot demonstrate either property. A digital register test can verify logical read/write semantics, but cannot certify analog bitcell retention or minimum voltage. The Atlas's prior digital memory models deliberately return unknown when concurrent access policy is unspecified.

**Worked investigation:** compare an ideal bitcell under zero analog noise with an explicitly unknown transfer characteristic. Demonstrate that a Boolean state table alone cannot estimate physical SRAM yield. Build an acquisition table for butterfly curves, write margin, Vdd corners, temperature, mismatch samples and soft-error logging; leave all empirical fields empty pending real measurements.

## Implementable contract and falsification

- **Reference equation:** `static noise margin must derive from analog transfer curves`.
- **Dimensional quantities:** V, s, bit error probability; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `prior_memory_models`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 49 — DRAM charge decay, sense thresholds and refresh policy

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A DRAM bit stores charge on a small capacitor. A simple mathematical leakage model is Q(t)=Q₀ exp(−t/τ). With minimum readable charge Q_min, the ideal refresh deadline is t_ref=τ ln(Q₀/Q_min), assuming Q₀>Q_min and known τ. This formula does not bound the actual worst-case retention time over process, voltage, temperature, disturbance, and distribution tails; real DRAM requires statistical characterization.

A destructive-read or charge-sharing model must additionally include the sense amplifier, bitline capacitance, access-device resistance, wordline timing, refresh serialization and error detection. A memory timing calculation without these dependencies cannot be promoted to a functioning DRAM design.

**Worked investigation:** for synthetic Q₀=10 fC, Q_min=2 fC and τ=1 ms, compute t_ref≈1.609 ms. Check that a query before 95% of the ideal deadline returns retained and after 105% returns not retained. Mark both outcomes as ideal mathematical prediction, not qualified retention.

## Implementable contract and falsification

- **Reference equation:** `Q(t)=Q0 exp(−t/tau); t_ref=tau ln(Q0/Q_min)`.
- **Dimensional quantities:** C, s; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `dram_retention`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 50 — Defect statistics, yield and reliability boundaries

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A deliberately simple defect-limited yield model assumes spatially independent random catastrophic defects of areal density D and chip area A. The zero-defect probability is P(N=0)=exp(−DA). This is a Poisson survival probability, not a validated wafer-yield forecast. Spatial clustering, circuit redundancy, process gradients, repair, systematic lithographic defects, defect size distribution, wafer edge effects and inspection sensitivity violate its assumptions.

A reconstruction process should separate measured defect maps, inspection classification, actual electrical test failures, and modeled yield. Parameter estimation requires defining sampling area, false-negative rate and defect detection thresholds. Radiation soft errors, wearout, dielectric breakdown and electromigration are distinct reliability pathways and cannot be reduced to the same instantaneous defect density.

**Worked investigation:** for D=0.2 defects/cm² and A=3 cm², obtain exp(−0.6)≈0.5488 as a toy clean-die probability. Report how the result changes if D doubles, while refusing to infer a fabrication yield from the toy equation.

## Implementable contract and falsification

- **Reference equation:** `P(clean die)=exp(−D_defects A_chip)`.
- **Dimensional quantities:** cm⁻², cm², probability; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `poisson_defect_free_yield`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `NIST-SEMICONDUCTOR` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 51 — Interconnect, ESD, packaging and operational qualification

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A working device also needs electrically connected contacts, controlled parasitics, thermal pathways, mechanical integrity, environmental protection and test interfaces. Wire resistance is R=ρL/A only under the stated uniform-conductor approximation; interconnect capacitance and inductance couple switching speed to geometry and neighboring nets. Packaging adds thermal resistance and mechanical stress, often dominating field reliability.

ESD susceptibility and latch-up are not captured by Boolean simulation. Qualification requires defined stress conditions, protective circuitry, safety procedures and standards appropriate to the device. This Atlas deliberately does not infer standards compliance from abstract simulation. In the handoff, maintain a risk and evidence register for contact resistance, bond continuity, package thermal tests, humidity, operating temperature, radiation and endurance.

**Worked investigation:** model a hypothetical interconnect as a declared R–C delay and compare it to an abstract setup slack. Show that reducing metal width can increase resistance while reducing some capacitance terms; actual corner models are unavailable. A design may be logically valid but physically fail timing due to interconnect parasitics.

## Implementable contract and falsification

- **Reference equation:** `R_wire=rho L/A; P_dynamic~alpha C V² f`.
- **Dimensional quantities:** ohm, m, F, K; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `prior_timing_models`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.


---

# Chapter 52 — From transistors to a reconstructible stored-program machine

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

The technological-continuity chain should end at an independently testable demonstration, not a claim of a fabricated processor. A software reference can connect word-level arithmetic, registers, state transitions and memory semantics: a finite 8-bit accumulator machine supports loading an immediate value, addition modulo 256, XOR, storing/loading from a 16-byte memory, conditional branches and explicit halting.

The instruction stream encodes each instruction as two bytes. A *step* is an ideal abstract state transition; it does not represent clock gates, transistor layout, power delivery, ROM fabrication, silicon validation, interrupts or a compiler toolchain. Program counter validity, alignment, bounded execution and unsupported opcodes are part of the contract. Arithmetic wraps modulo 256 by definition, while more extensive system architecture belongs in the next Computer Architecture node.

**Worked investigation:** execute LDI 5; ADD 7; STORE 0; XOR 3; HALT. The machine stores 12 in RAM[0] and halts with accumulator 15. Independently exhaust all 256×256 operand pairs with a separate integer arithmetic oracle, and test invalid opcodes and loop limits. This is evidence of finite software semantics; implementing the same state machine in CMOS remains an unfinished physical challenge.

The next milestone is to preserve a full computer-architecture stack—ISA specification, gates-to-register RTL semantics, deterministic boot ROM, assembler, instruction decoding, memory buses, interrupts and transparent end-to-end programs—while retaining all semiconductor parameter calibration gaps. Do not move Bitwork routing forward until all planned domain content libraries are addressed.

## Implementable contract and falsification

- **Reference equation:** `state_next=decode(opcode,operand,state); acc_add=(a+b) mod 256`.
- **Dimensional quantities:** bits, bytes, cycles; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `EightBitAccumulator`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.


---

