# ATLAS FORGE — Bioelectric Atlas v0.1.0

**Original, nonclinical offline mathematical reconstruction reference.** This is one node inside the unchanged original canonical ATLAS FORGE federation; it is not a new federation.

# 01. Dimensional consistency for bioelectric systems

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The membrane potential is an electrical potential difference, not a force, current or chemical concentration. All quantities must be dimensioned explicitly. Core constants from the SI defining system are kB=1.380649e−23 J/K, e=1.602176634e−19 C, and NA=6.02214076e23 mol−1. Hence R=kB NA and F=e NA are algebraic combinations of exact SI definitions; practical experiment measurement of temperature, concentration, cell area and currents remains uncertain.

## Governing mathematical model

`V_T=k_B T/e; F=e N_A; C_mem=C_specific*A; U_C=0.5 C_mem V^2`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use K for thermodynamic temperature, mol/m³ (or a declared consistent concentration unit for ratios), C for charge, A for current, F for capacitance, S for conductance and V for voltage. Equations using mV or ms must provide explicit conversion factors. A common reconstruction failure is mixing microfarads per square centimeter with farads per square meter, creating a factor-of-ten-thousand error in area scaling. Biological signals are usually small enough that grounding and interference can dominate observations; none of those physical errors is automatically represented by a software trace. Test formula dimensions before interpreting numerical outputs.

A membrane capacitor is a useful electrical approximation because the lipid bilayer impedes charge transport while its faces support charge separation. This does not mean every biological membrane is a perfect linear, lossless capacitor; voltage-dependent capacitance, membrane geometry, access resistance and electrode artifacts can matter. The Atlas retains the assumptions as part of the scientific result.

## Independently checkable worked case

For area A=0.5 m² and specific capacitance c=0.02 F/m², the model predicts C=0.01 F. For C=2 F and V=3 V, ideal stored energy is 9 J. These synthetic examples verify dimensions only, not an actual cell.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No membrane geometry, injury threshold, live-cell permeability or patient outcome is measured. The numerical tests must never become unqualified equipment specifications or stimulation guidance.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 02. Ion activities, chemical potential and membrane separation

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

For an ideal dilute solution, an ion electrochemical potential combines concentration and electrical work. The driving force depends on both the logarithm of the activities and the electrical potential. Cells are not ideal salt containers: activity coefficients, binding, fixed charge, osmolarity, transporters and ion gradients may invalidate this simple form.

## Governing mathematical model

`μ_i = μ_i° + R T ln(a_i) + z_i F φ`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

State the sign convention for transmembrane voltage as inside potential minus outside potential. Chemical and electrical terms have dimensions of joules per mole. The relative chemical driving term is R T ln(a_out/a_in), with a dimensionless activity ratio. Concentration ratios may approximate activities only with stated assumptions.

In a physical membrane, gradients are maintained by metabolism, selective permeability and transport pumps. Equal electrochemical potential implies no net passive driving force for that ion, not absence of all other ion fluxes or ATP consumption. Distinguish equilibrium from steady state: maintained pumps can produce stable concentrations under continual net transport. This is critical to designing measurements and interpreting apparent resting voltages.

## Independently checkable worked case

If the activity ratio outside/inside is 10 and z=+1, the ideal chemical contribution is R T ln(10). Its voltage equivalent is positive for the chosen Nernst sign convention. Reversing concentrations reverses sign, and doubling valence halves the voltage.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Do not infer equilibrium from one voltage measurement. No direct material characterization, membrane composition, ion pump work or equilibrium measurements are provided.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 03. Nernst equilibrium voltage with explicit valence and units

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The Nernst potential of a permeant ion is the voltage at which the electrochemical potential differences balance under the ideal single-ion model. The sign depends on which side is called inside and on the ion charge. It is particularly easy to reverse the chloride result if valence is omitted.

## Governing mathematical model

`E_ion = (R T / z F) ln(a_out/a_in)`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use a dimensionless activity or consistent-concentration ratio, thermodynamic temperature T>0 and nonzero integer valence z. A log10 expression requires multiplying by 2.303; natural logarithms have no such factor. Unit errors can be caught by comparing the thermodynamic voltage scale R T/F with the exact kB T/e value. For multivalent ions, z appears in the denominator.

The mathematical model is deterministic. Its biological applicability is not: the membrane may be permeable to several species, activity coefficients may deviate from unity and a measured potential may have reference-electrode junction offsets. The implementation therefore refuses zero or negative concentrations and invalid valence rather than silently defaulting to a membrane voltage.

## Independently checkable worked case

For a positive monovalent species, T=310.15 K, c_in=140 and c_out=5 in identical units, E≈−89 mV. Swapping inside/outside makes +89 mV. For an anion with the same concentration ratio, the sign reverses.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

This is not a personal health measurement or a recipe for applying potentials to tissue. No transport pumps, geometry, Nernst-Planck field gradients or clinical thresholds are inferred.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 04. Goldman–Hodgkin–Katz constant-field voltage and limiting cases

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

When Na+, K+ and Cl− contribute to a membrane voltage, their permeabilities and concentration gradients influence the zero-current potential. A simplified constant-field GHK formula uses monovalent ions, fixed permeability ratios and no explicit active pump current. The chloride concentrations reverse sides because its valence is negative.

## Governing mathematical model

`V = (R T/F) ln((P_K K_out+P_Na Na_out+P_Cl Cl_in)/(P_K K_in+P_Na Na_in+P_Cl Cl_out))`

**Source orientation:** GOLDMAN-1943 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC2142582/`), DOI 10.1085/jgp.27.1.37. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The numerator and denominator contain products of relative permeability and concentrations in consistent units. The ratio remains dimensionless. Scale every permeability by a positive common factor and the potential must not change. As any one permeability dominates, the result should reduce to that ion’s Nernst voltage. This provides an independent suite of limiting-case checks even when no actual membrane has been measured.

The constant-field model is a specific mechanistic approximation, not a general replacement for tissue electrodiffusion or ion-channel current-voltage measurements. Relative permeability may change with voltage or state; channel interactions and ion selectivity can violate the assumed independence. The numerical implementation records these limits and rejects zero-total permeability and nonphysical concentrations.

## Independently checkable worked case

Set all permeability weights to zero except P_K and verify exact Nernst reduction; repeat for P_Na and P_Cl (with sign reversal). Compare a weight tuple (1,0.1,0.01) with (100,10,1): both must give the same voltage.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

A fitted GHK voltage alone does not identify unique permeability values, prove channel abundance or validate any clinical inference. Source-to-equation reviewer acceptance remains absent.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 05. Passive membrane as capacitor and conductance network

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A lumped passive membrane can be approximated by a capacitor in parallel with an Ohmic leak conductance toward a reversal potential. Kirchhoff current balance gives a first-order differential equation with an exponential analytical solution. This is a building block for understanding time constants and input resistance.

## Governing mathematical model

`C dV/dt = -g(V-E) + I; τ=C/g; V(t)=V_inf+(V0-V_inf)exp(-t/τ)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Specify capacitance in farads, conductance in siemens, voltage in volts, current in amperes and time in seconds. If the injected current is defined positive inward, V_inf=E+I/g for constant forcing and τ=C/g. With several independent parallel channels, the total conductance is the sum and the equilibrium voltage is the conductance-weighted reversal voltage plus I/g_total. A zero-total-conductance system has no finite passive time constant and must not return an invented equilibrium.

This model does not capture excitability, nonlinear gating or spatial conduction. Real cell geometries have membrane and axial access resistance; whole-cell recordings may introduce series resistance and capacitive transients that appear biological if not accounted for. Synthetic parameter sets must be labeled as such.

## Independently checkable worked case

Take C=1 microfarad, g=1 millisiemens and V0=100 mV relative to a zero reversal, I=0. The time constant is 1 ms; after 1 ms the model gives about 36.79 mV. Recalculate by independently solving the linear ODE as a numerical check.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The result is a mathematically defined lumped RC response, not a measured squid axon, a human neuron, or a valid bioelectric stimulation dose.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 06. Parallel channel conductances and current conservation

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The total membrane current is the sum of capacitive, leak and channel currents. When each channel is approximated as Ohmic at one operating point, the conductance-weighted equilibrium follows directly from Kirchhoff’s current law. Current direction conventions must be explicit to avoid sign errors.

## Governing mathematical model

`0 = Σ_k g_k(E_k-V) + I; V*=(Σg_k E_k+I)/Σg_k`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For fixed conductances, the conductance sum is nonnegative and strictly positive for a finite equilibrium. If all conductances are zero, V is not identified by the equilibrium equation. Changes in one channel conductance change both the time constant and steady voltage. In living tissue, voltage-gated channels make g depend on voltage and time, so a single fixed conductance equilibrium may be invalid.

A model can pass numerical tests while using unrealistic dimensions or ignoring gradients maintained by ATP-driven pumps. To avoid false confidence, require a list of which currents were modeled, whether the state is dynamic, the selected time reference, and the error bounds for input current and conductance parameters. Keep the original ion model and the numerical solver as distinct reproducibility claims.

## Independently checkable worked case

For two channels with g=(2,1) S and E=(−0.1,+0.2) V, equilibrium is zero. Add 0.2 A inward to the g=2 S, E=−0.1 V system and its equilibrium also becomes zero. These numbers are dimension-checking fixtures, not actual biological conductances.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Do not infer tissue health, identity of the active channel, action-potential threshold or safety limits from this linearized example.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 07. A reconstructible sealed-end passive cable discretization

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Spatial conduction arises because neighboring membrane segments exchange axial current through electrical resistance. A finite compartment chain can approximate one-dimensional cable behavior: each segment has a membrane capacitance, leakage conductance and coupling to adjacent segments. Sealed ends have no external axial neighbor current.

## Governing mathematical model

`C dV_i/dt = g_a Σ_neighbors(V_j−V_i) − g_l(V_i−E_l)+I_i`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The graph Laplacian sum is negative semidefinite, so in a passive leakless chain with no injected current the capacitance-weighted total charge relative to a reference remains constant. A spatially uniform potential yields no axial current. If all segment capacitances are equal, finite differences reduce to a simple neighbor average. This reference uses equal node lump parameters and only adjacent coupling; it is not calibrated to measured diameter, myelin, branching or extracellular volume conductor geometry.

The numerical method is explicit Euler. For nodes with maximum degree d, a sufficient nonnegative-coefficient stability/positivity condition is Δt ≤ C/(d g_a+g_l). The algorithm refuses larger steps rather than silently generating oscillatory or negative-weight artifacts. A real cable equation in distributed units requires geometric conversion from ohms per length and membrane capacitance per area.

## Independently checkable worked case

For 5 nodes with initial voltages (0,0,1,0,0), leak 0, coupling 1 S and C=1 F per node, a small step redistributes voltage to neighbors while keeping the sum equal to 1. With a two-node sealed chain (1,0), dt=0.1, the next pair is (0.9,0.1).

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The discretization does not represent a measured axon conduction speed, refractory myelination or stimulation threshold. It is a mathematical reconstruction of a passive network only.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 08. Cable-step stability, conservation and discretization errors

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A numerical simulation of a physical equation has its own stability conditions. Even if the continuum PDE is passive, choosing a time step beyond the explicit solver’s stability bound can create artificial oscillation or growth. Finite-step numerical evidence must therefore include the method, resolution and error constraints.

## Governing mathematical model

`Δt ≤ C/(degree_max g_ax+g_leak) (sufficient nonnegative weights)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For a leak-free sealed chain, sum of C(V_i−V_ref) remains constant under exact arithmetic because every axial edge current appears once with a positive and once with a negative sign. This invariance provides a strong finite numerical test independent of a particular waveform. With leak, the sum decays toward the reversal; with injected currents, the total changes according to the supplied net current.

A convergence study must compare results at decreasing Δt and increasing spatial resolution, while retaining actual geometry and boundary conditions. The simple implemented model keeps the number of nodes finite and does not infer any real tissue size. It rejects input-current lists of the wrong length, negative conductances, nonfinite voltages and time steps beyond its declared bound.

## Independently checkable worked case

Initialize five random node voltages; evolve with leak 0, no applied current and an admissible time step. After each step, sum all voltages and verify conservation to floating-point tolerance. Deliberately choose a step larger than the bound and require refusal, not a fictitious oscillatory “spike.”

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Stability of a numerical integrator does not prove a biological system stable or a model parameter set experimentally valid.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 09. Hodgkin–Huxley voltage-gated sodium and potassium kinetics

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Hodgkin and Huxley formulated time-dependent sodium, potassium and leak currents for the squid giant axon. Their conductances depend on activation/inactivation variables m, h and n. These probabilities evolve according to voltage-dependent first-order transition rates, and the membrane voltage evolves from ionic and applied currents.

## Governing mathematical model

`dx/dt=α_x(V)(1−x)−β_x(V)x; I_Na=gNa m³h(V−ENa); I_K=gK n⁴(V−EK)`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The classical parameterization is in mV, ms, µA/cm², mS/cm² and µF/cm², commonly associated with an experimental temperature around 6.3 °C. Code must not mix those units with the SI-only passive reference without a conversion layer. The voltage reference is modern inside-negative rest around −65 mV; the historical article uses differing original conventions, so maintain a clearly documented translation. For each gate, x_inf=α/(α+β) and τ=1/(α+β). If voltage is held constant during a step, the gate has an exact exponential update that remains within [0,1].

The nominal coefficients (gNa=120, gK=36, gL=0.3 in mS/cm²; ENa=50, EK=−77, EL=−54.387 mV) are an illustrative historical model fit. They are not human cell constants and should not be used to design a medical intervention. A separate solver must respect numerical stability and source-form assumptions.

## Independently checkable worked case

At −65 mV, the model gate fractions are approximately m=0.05293, h=0.59612 and n=0.31768. Compute gate rates and require all to be nonnegative; compare one exact voltage-held gate update with an independently calculated derivative at a very small Δt.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No inference is permitted about human firing thresholds, individual illness, stimulation current or tissue survival from this parameterization.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 10. Removable singularities in Hodgkin–Huxley rate equations

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Classic Hodgkin–Huxley activation-rate formulas contain factors of the form x/(1−exp(−x/a)). At x=0 a naive floating-point evaluation gives 0/0, even though the physical mathematical limit exists. Software that inserts an arbitrary epsilon or returns zero can produce a discontinuous gating rate and invalid dynamics.

## Governing mathematical model

`lim_{x→0} x/(1−exp(−x/a)) = a`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use expm1 where possible to compute exp(x)−1 accurately for small arguments, and a series expansion around the removable singularity. For gate m this occurs near −40 mV, and for gate n near −55 mV under the conventional rest-normalized voltage representation. A strictly positive temperature is required for any thermodynamic extension, and the rate model should reject unreasonable voltage extrapolations instead of producing infinities.

Calculate convergence by evaluating values on either side of the singularity and checking smooth approach to the analytical limit. Preserve independent identity tests, not just two hardcoded voltage values. Numerical methods must not be mistaken for independently verified biophysics; the target historical equation still depends on experimental context and translation of voltage reference conventions.

## Independently checkable worked case

At −40 mV, the m activation rate has the finite limit 1/ms; at −55 mV, n activation is 0.1/ms. Perturb either voltage by ±10⁻⁵ mV and verify the rate approaches the same finite limit smoothly, rather than throwing or becoming zero.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

A mathematically stable rate calculation does not establish that any particular ion channel behaves according to the squid model.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 11. Time integration of the HH membrane with explicit scope limits

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The HH system combines one membrane voltage equation and three first-order gating equations. Numerical integration choices matter: very large explicit steps can generate fictitious firing, negative gate fractions or numerical instability. A reproducible implementation must specify its integration method, time units, parameter domain and result trace format.

## Governing mathematical model

`C_m dV/dt=I_in−I_Na−I_K−I_l; gated x(t+Δt)=x_inf+(x−x_inf)e^{−Δt/τ}`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

The reference integrates V with bounded explicit Euler and gates by their exact voltage-held exponential solution. This is a numerical splitting scheme, not an analytically exact solution of the coupled nonlinear HH system. The implementation requires Δt≤0.025 ms, finite bounded synthetic injected current, a defined initial state and a finite step budget. A comparison to a smaller step or a separate numerical integrator can reveal discretization error.

The model's current values are declared in µA/cm² and capacitance in µF/cm², so mV/ms emerges correctly. Gating fractions remain in [0,1] if the rates and step are valid. The initial historical −65 mV rest state has only a small residual drift under the rounded leak parameters; this is not a failure of the arithmetic. Outputs are labeled simulated squid membrane traces rather than measurement or medical advice.

## Independently checkable worked case

Run 500 steps at 0.01 ms from the classical rest gate equilibrium and require all voltages and gate fractions to remain finite. Repeat with identical inputs and compare complete traces for exact deterministic replay. Deliberately request Δt=0.2 ms and require rejection.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The original source had experimental support for squid giant axon physiology. This Atlas reimplementation itself has no direct biological experiment, temperature-corrected human tissue model or clinical validation.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 12. FitzHugh–Nagumo dimensionless excitability dynamics

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A reduced two-variable excitable-system model can reproduce qualitative phase-plane behavior while omitting the specific molecular channels of Hodgkin–Huxley. A typical FitzHugh–Nagumo reference contains a fast excitation variable v and a slow recovery variable w. Its variables and time parameters are dimensionless unless a specific validated scaling is supplied.

## Governing mathematical model

`dv/dt = v−v³/3−w+I; dw/dt=ε(v+a−bw)`

**Source orientation:** FITZHUGH-1961 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1366333/`), DOI 10.1016/S0006-3495(61)86902-6. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Unlike membrane voltage in volts, FHN v is a dimensionless state coordinate. Converting an FHN trajectory directly to a measured neuronal action potential is invalid without an experimentally calibrated transformation. The model is integrated with classical fourth-order Runge–Kutta using a small bounded step. The result is a reproducible nonlinear dynamical system that can demonstrate excitability and oscillator intuition without guessing channel conductances.

An independent solver should evaluate the derivative separately and compare a one-step RK4 result to two half-steps. Any numerical check must record a, b, epsilon, drive, initial state and integration step. Out-of-range values or nonfinite dynamics should halt rather than be interpreted as extreme biology.

## Independently checkable worked case

Start from (v,w)=(-1,0), a=0.7,b=0.8,epsilon=0.08 and dt=0.01. Compare the RK4 result with two steps of dt=0.005 to better than the documented local tolerance. Change the drive and observe a different trajectory.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

This is a generic excitable dynamical reference, not a model of human nervous function, diagnosis, consciousness or therapeutic stimulation.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 13. Electrode–electrolyte interface as a passive dummy-load circuit

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Recording electrodes may introduce a complex impedance involving solution resistance, interfacial charge transfer, double-layer capacitance and nonideal electrochemistry. A minimal Randles-style network can be treated as solution resistance in series with an interface resistance in parallel with a capacitor. This is a **dummy electrical network** for algebraic checks, not a description of every biological electrode.

## Governing mathematical model

`Z(ω)=R_s + 1/(1/R_ct + jω C_dl)`

**Source orientation:** NEURON-CABLE (`https://www.neuronsimulator.org/en/latest/nmodl/transpiler/contents/cable_equations.html`), DOI not applicable to documentation. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Use ohms, farads and hertz with ω=2πf. At zero frequency the capacitive branch is open, so Z=Rs+Rct. As frequency becomes large, the ideal capacitor shorts the parallel charge-transfer resistance and Z approaches Rs. The imaginary impedance of the ideal RC element is nonpositive under the chosen sign convention. This gives a reproducible analytic limiting behavior for independent verification.

Actual electrodes exhibit polarization, constant-phase elements, electrode half-cell offsets, DC drift, biochemical interactions, nonlinearity and safety constraints. An RC model with invented numbers cannot predict current density or safe contact with skin. The reference uses a non-biological dummy load exclusively and should never be wired to a person, animal or implant as a medical or experimental device.

## Independently checkable worked case

Take Rs=100 Ω, Rct=900 Ω, Cdl=1 µF. At DC expect 1000 Ω. As frequency rises, real impedance approaches 100 Ω and phase approaches zero. Verify these limiting cases algebraically and with the standalone code.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Never infer stimulation safety, clinical measurement accuracy, electrode gel compatibility or tissue electrode properties from this synthetic RC network.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 14. Sampling, Nyquist limits and ADC error models

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Bioelectric signals are often sampled with electronic instruments, but the sampling process can distort or misrepresent the underlying analog waveform. An ideal uniform ADC maps a bounded voltage range into discrete integer codes. Quantization error, clipping and aliasing must be documented independently from biological interpretation.

## Governing mathematical model

`ΔV=(V_max−V_min)/(2^N−1); |quantization error|≤ΔV/2 for unclipped ideal nearest-code samples`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For an N-bit ideal code range [0,2^N−1], the encoder maps the analog input to the nearest code and reports any out-of-range clipping. A data report should preserve sample rate, voltage units, offset, transfer function, ADC resolution, reference accuracy and calibration. A realistic front end also needs anti-alias filtering, noise, input impedance, isolated supplies and electrical safety, none of which is implemented by a numerical quantizer.

Aliasing occurs because sample sequences depend on frequency modulo the sample rate. The synthetic sinusoid at 17 Hz sampled at 100 Hz is indistinguishable from a 117 Hz sinusoid at those sample instants. This does not mean the underlying analog signals are identical. A high sample rate alone does not guarantee measurement quality if anti-alias filtering or reference voltage is incorrect.

## Independently checkable worked case

Quantize an unclipped 0–1 V sample using 10 bits and require reconstruction error below half an ideal code step. Compare 200 samples of 17 Hz and 117 Hz sines at 100 samples/s and observe nearly identical discrete values.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Sampling examples are simulated and not equipment calibration or human-body electrophysiology measurements. Mains-connected or body-connected measurement circuit construction is out of scope.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 15. Noise, calibration uncertainty and reproducible signal traces

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Measurement uncertainty has multiple sources: calibration reference, amplifier drift, thermal noise, digitizer resolution, model inadequacy and environmental interference. A numerical trace can be perfectly reproducible while a real instrument is not. An evidence record must therefore distinguish a random seed and generated noise samples from raw, calibrated laboratory observations.

## Governing mathematical model

`u_c=√Σu_i² for independent (uncorrelated) standard uncertainties`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

Root-sum-square combination is valid for independent standard uncertainties or when covariance terms are legitimately zero. With correlated measurements, add the covariance terms; a simple RSS function must not pretend to handle correlation. Synthetic Gaussian noise with a fixed seed supports test replays but does not establish a real biological noise spectrum, PSD, Johnson noise temperature, amplifier 1/f behavior or electrode artifact distribution.

A robust measurement dossier would include instrument model and serial, calibration status, measurement chain, temperature, source impedance, bandwidth, gain, ADC reference, sample-rate uncertainties, and raw unprocessed samples. The Atlas provides a checklist, not the evidence. Calibration receipts from qualified laboratories are necessary for external engineering acceptance.

## Independently checkable worked case

Combine independent uncertainties 3 and 4 in the same physical units; u_c=5. Generate two artificial noise traces using the same seed and standard deviation and verify identical SHA-256. Change seed and verify digest difference. Label the trace synthetic.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Numerical seed repeatability is not experimental repeatability. This edition does not provide verified biomedical instrumentation, medical diagnostic sensitivity or measured noise covariance.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 16. Electrogenic pumps, metabolic work and non-equilibrium ion gradients

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

Biological membranes maintain ion gradients through selective permeability and active transport. An instantaneous equilibrium potential is only one part of this system. Maintaining a gradient against dissipation requires energy input and mechanisms such as ATP-consuming pumps; a complete model must conserve matter and charge at the system boundary.

## Governing mathematical model

`dN_i/dt=J_pump,i−J_leak,i; C_m dV/dt=Σ_i I_i + I_external (specified signs)`

**Source orientation:** HODGKIN-HUXLEY-1952 (`https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/`), DOI 10.1113/jphysiol.1952.sp004764. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

A physically adequate model would track ionic inventories on both sides, membrane geometry, osmotic effects, channel state, buffering, binding and metabolic energy. The present Bioelectric Atlas does not implement a validated multi-species electrodiffusion solver or a pump ATP cycle; it records those as independent scientific requirements and future computational nodes. Treat the source of free energy and charge continuity as prerequisites before interpreting a steady membrane potential.

When quantities are written per area, concentration and flux must be converted to total amounts using surface area and compartment volume. Charge neutrality can hold approximately in bulk electrolytes while thin interfacial double layers carry electrical charge. The capacitor picture is thus a useful abstraction but cannot replace a full electrochemical model. The checkable software components here cover ideal potentials and passive charge; biological pump rates remain unmeasured.

## Independently checkable worked case

Use the capacitor formula Q=C(V−V_ref) and a passive cable of five segments with sealed ends and zero leak. Under internal axial current redistribution, the sum of charge stays constant, showing the mathematical accounting needed before adding active flux terms.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

No active pump kinetic parameters, biological viability, wound healing mechanism, or human physiology prediction is certified. This chapter is a dependency map, not a clinical procedure.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 17. Offline engineering bench workflow with non-biological electrical dummies

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

A disaster-recovery scientific library should lead from equations to a demonstrable physical test while avoiding unsafe leaps from simulation to live tissue. The first appropriate hardware check for Bioelectric Atlas is an isolated, battery-powered **non-biological dummy** made from known passive electronic components, not an electrode attached to a person or animal.

## Governing mathematical model

`Measured Z_dummy(ω) compared with Z_model(ω), with calibrated uncertainty and isolation safeguards`

**Source orientation:** NAGUMO-1962 (`https://ieeexplore.ieee.org/abstract/document/4066548`), DOI 10.1109/JRPROC.1962.288235. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

A high-level engineering test plan would select a known commercial resistor/capacitor dummy device, independently check its ratings and tolerance, obtain reliable reference instrumentation, define a narrow nonclinical measurement objective and capture a raw measurement with an independent observer. No direct body connection, mains circuit, implant, wound, contact stimulation or unspecified high-voltage prototype is part of the scope. When physical infrastructure is absent, the safe fallback is to preserve the mathematics and the test protocol rather than fabricating measurements.

The existing Manufacturing Atlas supplies traceability, work instructions, quality control and acceptance predicates. The Electronics Atlas supplies device laws and timing. The Measurement Atlas supplies uncertainty and calibration. The present bioelectric numerical circuit can generate an expected spectrum for comparison but cannot certify a bench’s safety or calibration by itself. A 3D printer can produce a protective non-load-bearing fixture if its material and dimensions are tested; it does not produce calibrated electrodes, biosensors, ICs or safe electrical isolation automatically.

## Independently checkable worked case

Create a synthetic model of Rs=100 Ω and Rct=900 Ω with parallel Cdl=1 µF. Independently compute the DC and high-frequency limiting impedance. Save a blank measurement worksheet for actual future instrument values. Mark every physical test requirement HOLD until authentic raw measurements and calibration exist.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

Do not connect experimental equipment to humans, animals, implanted electronics, energized utility wiring, or life-support apparatus. The program does not contain a certified medical electrical safety design.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.


---

# 18. Scientific evidence gates, source rights and nonclinical acceptance

**ATLAS FORGE — Bioelectric Atlas 0.1.0; ORIGINAL CANONICAL FEDERATION node #16.**

**Evidence tier:** original educational mathematical synthesis and bounded synthetic computer tests. No original publisher technical file has been authenticated by this edition; no physical cell, human subject, medical device or independent scientific review has been performed. See local `SCIENTIFIC_AND_SAFETY_LIMITS.md`.

## Reconstruction question and physical definitions

The purpose of a scientific continuity library is to preserve testable knowledge, including its uncertainties, model boundaries, source history and negative findings. A correctly hashed Python output does not prove that its equations apply to a living organism. A source card pointing at a peer-reviewed article does not mean the publication’s original file has been independently authenticated or that its full text can be freely redistributed.

## Governing mathematical model

`software verified ∧ original-source authentication missing ∧ physical evidence missing ⇒ independent science acceptance HOLD`

**Source orientation:** BIPM-SI-2026 (`https://www.bipm.org/en/publications/si-brochure`), DOI 10.59161/AUEZ1291. This bibliographic link is not a locally authenticated original publisher document; no third-party full text was copied.

## Derivation and procedure

For every computational claim, store the exact input parameters, canonical code version, mathematical assumptions, time/space discretization, independent test results and failing counterexamples. For external source claims, record publisher URL, DOI, page/equation locator, edition, full original byte SHA and license permission once those are independently checked. For actual biological claims, require protocols approved by qualified experts, experimental safeguards, instrumentation calibration and raw data with uncertainty.

The first release includes original mathematical reference models, a scientific manual and an independent numerical oracle. It does not import a publisher’s copyrighted figures or articles, perform an electrode experiment, collect clinical data or certify a model for medical decision-making. The original 30-domain queue is preserved exactly and Bioelectric priority #9 is added as a new node in the same federation. The next original unregistered domain after existing Manufacturing #10 is Software Design Patterns #11, not an invented alternative roadmap.

## Independently checkable worked case

Re-run the independently coded Nernst, cable, HH, FHN and ADC checks on a freshly reconstructed archive. Confirm that real tissue and peer review remain flagged HOLD. Attempt to pass a metadata field claiming an authenticated study without original bytes: the evidence gate must withhold scientific promotion.

Record the exact parameter units, validated input range, equation edition, expected finite output, and at least one deliberately invalid input. Compare with the independent numerical oracle under a fresh process, preserving the failure record and SHA-256 of the exact local code/trace bytes. For physical work, establish equipment calibration, raw measurements and qualified review separately.

## Counterexamples, safety and acceptance boundary

The node is an executable educational reference, not a clinical guideline, neurostimulation device, biomedical research ethics approval, or complete history of electrophysiology.

The Bioelectric Atlas cannot produce safe medical stimulation settings and is not licensed or verified for use on people, animals, implants or life-support systems. Analogies between excitable media and electronics are useful for learning, not equivalence of clinical or physical properties. A physical experiment or safety-critical implementation requires qualified independent professionals and an approved protocol.

## Cross-federation dependencies and source rights

Prior original nodes: Measurement (calibration/uncertainty); Chemistry (electrolytes); Mathematics & Physics (ODE/PDE, dimensional analysis); Materials (dielectrics); Electronics & Semiconductors (RC, diode and ADC principles); Manufacturing (evidence quality and fixtures); Energy (charge and energy accounting); Computer Architecture (offline source-to-program tools). The source cards preserve navigational provenance only; original publishers retain their own rights. This chapter adds a new exact-revision record without altering the preceding fifteen nodes or original 30-domain queue.
