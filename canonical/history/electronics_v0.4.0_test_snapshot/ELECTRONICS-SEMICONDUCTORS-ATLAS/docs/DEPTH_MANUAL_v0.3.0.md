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
