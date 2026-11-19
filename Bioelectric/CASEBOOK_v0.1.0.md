# ATLAS FORGE Bioelectric Atlas — 18 constructed investigations (v0.1.0)

These are **synthetic educational calculations**, not measurements of humans, organisms or devices. Every case must include a checkable expected result, a negative condition, units, scope and an evidence status.

## Investigation 01 — Dimensional consistency for bioelectric systems

**Question:** The membrane potential is an electrical potential difference, not a force, current or chemical concentration. All quantities must be dimensioned explicitly. Core constants from the SI defining system are kB=1.380649e−23 J/K, e=1.602176634e−19 C, and NA=6.02214076e23 mol−1. Hence R=kB NA and F=e NA are algebraic combinations of exact SI definitions; practical experiment measurement of temperature, concentration, cell area and currents remains uncertain.

**Governing relation:** `V_T=k_B T/e; F=e N_A; C_mem=C_specific*A; U_C=0.5 C_mem V^2`.

**Finite reproduction:** For area A=0.5 m² and specific capacitance c=0.02 F/m², the model predicts C=0.01 F. For C=2 F and V=3 V, ideal stored energy is 9 J. These synthetic examples verify dimensions only, not an actual cell.

**Negative or falsification condition:** No membrane geometry, injury threshold, live-cell permeability or patient outcome is measured. The numerical tests must never become unqualified equipment specifications or stimulation guidance.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 02 — Ion activities, chemical potential and membrane separation

**Question:** For an ideal dilute solution, an ion electrochemical potential combines concentration and electrical work. The driving force depends on both the logarithm of the activities and the electrical potential. Cells are not ideal salt containers: activity coefficients, binding, fixed charge, osmolarity, transporters and ion gradients may invalidate this simple form.

**Governing relation:** `μ_i = μ_i° + R T ln(a_i) + z_i F φ`.

**Finite reproduction:** If the activity ratio outside/inside is 10 and z=+1, the ideal chemical contribution is R T ln(10). Its voltage equivalent is positive for the chosen Nernst sign convention. Reversing concentrations reverses sign, and doubling valence halves the voltage.

**Negative or falsification condition:** Do not infer equilibrium from one voltage measurement. No direct material characterization, membrane composition, ion pump work or equilibrium measurements are provided.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 03 — Nernst equilibrium voltage with explicit valence and units

**Question:** The Nernst potential of a permeant ion is the voltage at which the electrochemical potential differences balance under the ideal single-ion model. The sign depends on which side is called inside and on the ion charge. It is particularly easy to reverse the chloride result if valence is omitted.

**Governing relation:** `E_ion = (R T / z F) ln(a_out/a_in)`.

**Finite reproduction:** For a positive monovalent species, T=310.15 K, c_in=140 and c_out=5 in identical units, E≈−89 mV. Swapping inside/outside makes +89 mV. For an anion with the same concentration ratio, the sign reverses.

**Negative or falsification condition:** This is not a personal health measurement or a recipe for applying potentials to tissue. No transport pumps, geometry, Nernst-Planck field gradients or clinical thresholds are inferred.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 04 — Goldman–Hodgkin–Katz constant-field voltage and limiting cases

**Question:** When Na+, K+ and Cl− contribute to a membrane voltage, their permeabilities and concentration gradients influence the zero-current potential. A simplified constant-field GHK formula uses monovalent ions, fixed permeability ratios and no explicit active pump current. The chloride concentrations reverse sides because its valence is negative.

**Governing relation:** `V = (R T/F) ln((P_K K_out+P_Na Na_out+P_Cl Cl_in)/(P_K K_in+P_Na Na_in+P_Cl Cl_out))`.

**Finite reproduction:** Set all permeability weights to zero except P_K and verify exact Nernst reduction; repeat for P_Na and P_Cl (with sign reversal). Compare a weight tuple (1,0.1,0.01) with (100,10,1): both must give the same voltage.

**Negative or falsification condition:** A fitted GHK voltage alone does not identify unique permeability values, prove channel abundance or validate any clinical inference. Source-to-equation reviewer acceptance remains absent.

**Source locator:** `GOLDMAN-1943`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 05 — Passive membrane as capacitor and conductance network

**Question:** A lumped passive membrane can be approximated by a capacitor in parallel with an Ohmic leak conductance toward a reversal potential. Kirchhoff current balance gives a first-order differential equation with an exponential analytical solution. This is a building block for understanding time constants and input resistance.

**Governing relation:** `C dV/dt = -g(V-E) + I; τ=C/g; V(t)=V_inf+(V0-V_inf)exp(-t/τ)`.

**Finite reproduction:** Take C=1 microfarad, g=1 millisiemens and V0=100 mV relative to a zero reversal, I=0. The time constant is 1 ms; after 1 ms the model gives about 36.79 mV. Recalculate by independently solving the linear ODE as a numerical check.

**Negative or falsification condition:** The result is a mathematically defined lumped RC response, not a measured squid axon, a human neuron, or a valid bioelectric stimulation dose.

**Source locator:** `NEURON-CABLE`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 06 — Parallel channel conductances and current conservation

**Question:** The total membrane current is the sum of capacitive, leak and channel currents. When each channel is approximated as Ohmic at one operating point, the conductance-weighted equilibrium follows directly from Kirchhoff’s current law. Current direction conventions must be explicit to avoid sign errors.

**Governing relation:** `0 = Σ_k g_k(E_k-V) + I; V*=(Σg_k E_k+I)/Σg_k`.

**Finite reproduction:** For two channels with g=(2,1) S and E=(−0.1,+0.2) V, equilibrium is zero. Add 0.2 A inward to the g=2 S, E=−0.1 V system and its equilibrium also becomes zero. These numbers are dimension-checking fixtures, not actual biological conductances.

**Negative or falsification condition:** Do not infer tissue health, identity of the active channel, action-potential threshold or safety limits from this linearized example.

**Source locator:** `HODGKIN-HUXLEY-1952`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 07 — A reconstructible sealed-end passive cable discretization

**Question:** Spatial conduction arises because neighboring membrane segments exchange axial current through electrical resistance. A finite compartment chain can approximate one-dimensional cable behavior: each segment has a membrane capacitance, leakage conductance and coupling to adjacent segments. Sealed ends have no external axial neighbor current.

**Governing relation:** `C dV_i/dt = g_a Σ_neighbors(V_j−V_i) − g_l(V_i−E_l)+I_i`.

**Finite reproduction:** For 5 nodes with initial voltages (0,0,1,0,0), leak 0, coupling 1 S and C=1 F per node, a small step redistributes voltage to neighbors while keeping the sum equal to 1. With a two-node sealed chain (1,0), dt=0.1, the next pair is (0.9,0.1).

**Negative or falsification condition:** The discretization does not represent a measured axon conduction speed, refractory myelination or stimulation threshold. It is a mathematical reconstruction of a passive network only.

**Source locator:** `NEURON-CABLE`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 08 — Cable-step stability, conservation and discretization errors

**Question:** A numerical simulation of a physical equation has its own stability conditions. Even if the continuum PDE is passive, choosing a time step beyond the explicit solver’s stability bound can create artificial oscillation or growth. Finite-step numerical evidence must therefore include the method, resolution and error constraints.

**Governing relation:** `Δt ≤ C/(degree_max g_ax+g_leak) (sufficient nonnegative weights)`.

**Finite reproduction:** Initialize five random node voltages; evolve with leak 0, no applied current and an admissible time step. After each step, sum all voltages and verify conservation to floating-point tolerance. Deliberately choose a step larger than the bound and require refusal, not a fictitious oscillatory “spike.”

**Negative or falsification condition:** Stability of a numerical integrator does not prove a biological system stable or a model parameter set experimentally valid.

**Source locator:** `NEURON-CABLE`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 09 — Hodgkin–Huxley voltage-gated sodium and potassium kinetics

**Question:** Hodgkin and Huxley formulated time-dependent sodium, potassium and leak currents for the squid giant axon. Their conductances depend on activation/inactivation variables m, h and n. These probabilities evolve according to voltage-dependent first-order transition rates, and the membrane voltage evolves from ionic and applied currents.

**Governing relation:** `dx/dt=α_x(V)(1−x)−β_x(V)x; I_Na=gNa m³h(V−ENa); I_K=gK n⁴(V−EK)`.

**Finite reproduction:** At −65 mV, the model gate fractions are approximately m=0.05293, h=0.59612 and n=0.31768. Compute gate rates and require all to be nonnegative; compare one exact voltage-held gate update with an independently calculated derivative at a very small Δt.

**Negative or falsification condition:** No inference is permitted about human firing thresholds, individual illness, stimulation current or tissue survival from this parameterization.

**Source locator:** `HODGKIN-HUXLEY-1952`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 10 — Removable singularities in Hodgkin–Huxley rate equations

**Question:** Classic Hodgkin–Huxley activation-rate formulas contain factors of the form x/(1−exp(−x/a)). At x=0 a naive floating-point evaluation gives 0/0, even though the physical mathematical limit exists. Software that inserts an arbitrary epsilon or returns zero can produce a discontinuous gating rate and invalid dynamics.

**Governing relation:** `lim_{x→0} x/(1−exp(−x/a)) = a`.

**Finite reproduction:** At −40 mV, the m activation rate has the finite limit 1/ms; at −55 mV, n activation is 0.1/ms. Perturb either voltage by ±10⁻⁵ mV and verify the rate approaches the same finite limit smoothly, rather than throwing or becoming zero.

**Negative or falsification condition:** A mathematically stable rate calculation does not establish that any particular ion channel behaves according to the squid model.

**Source locator:** `HODGKIN-HUXLEY-1952`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 11 — Time integration of the HH membrane with explicit scope limits

**Question:** The HH system combines one membrane voltage equation and three first-order gating equations. Numerical integration choices matter: very large explicit steps can generate fictitious firing, negative gate fractions or numerical instability. A reproducible implementation must specify its integration method, time units, parameter domain and result trace format.

**Governing relation:** `C_m dV/dt=I_in−I_Na−I_K−I_l; gated x(t+Δt)=x_inf+(x−x_inf)e^{−Δt/τ}`.

**Finite reproduction:** Run 500 steps at 0.01 ms from the classical rest gate equilibrium and require all voltages and gate fractions to remain finite. Repeat with identical inputs and compare complete traces for exact deterministic replay. Deliberately request Δt=0.2 ms and require rejection.

**Negative or falsification condition:** The original source had experimental support for squid giant axon physiology. This Atlas reimplementation itself has no direct biological experiment, temperature-corrected human tissue model or clinical validation.

**Source locator:** `HODGKIN-HUXLEY-1952`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 12 — FitzHugh–Nagumo dimensionless excitability dynamics

**Question:** A reduced two-variable excitable-system model can reproduce qualitative phase-plane behavior while omitting the specific molecular channels of Hodgkin–Huxley. A typical FitzHugh–Nagumo reference contains a fast excitation variable v and a slow recovery variable w. Its variables and time parameters are dimensionless unless a specific validated scaling is supplied.

**Governing relation:** `dv/dt = v−v³/3−w+I; dw/dt=ε(v+a−bw)`.

**Finite reproduction:** Start from (v,w)=(-1,0), a=0.7,b=0.8,epsilon=0.08 and dt=0.01. Compare the RK4 result with two steps of dt=0.005 to better than the documented local tolerance. Change the drive and observe a different trajectory.

**Negative or falsification condition:** This is a generic excitable dynamical reference, not a model of human nervous function, diagnosis, consciousness or therapeutic stimulation.

**Source locator:** `FITZHUGH-1961`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 13 — Electrode–electrolyte interface as a passive dummy-load circuit

**Question:** Recording electrodes may introduce a complex impedance involving solution resistance, interfacial charge transfer, double-layer capacitance and nonideal electrochemistry. A minimal Randles-style network can be treated as solution resistance in series with an interface resistance in parallel with a capacitor. This is a **dummy electrical network** for algebraic checks, not a description of every biological electrode.

**Governing relation:** `Z(ω)=R_s + 1/(1/R_ct + jω C_dl)`.

**Finite reproduction:** Take Rs=100 Ω, Rct=900 Ω, Cdl=1 µF. At DC expect 1000 Ω. As frequency rises, real impedance approaches 100 Ω and phase approaches zero. Verify these limiting cases algebraically and with the standalone code.

**Negative or falsification condition:** Never infer stimulation safety, clinical measurement accuracy, electrode gel compatibility or tissue electrode properties from this synthetic RC network.

**Source locator:** `NEURON-CABLE`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 14 — Sampling, Nyquist limits and ADC error models

**Question:** Bioelectric signals are often sampled with electronic instruments, but the sampling process can distort or misrepresent the underlying analog waveform. An ideal uniform ADC maps a bounded voltage range into discrete integer codes. Quantization error, clipping and aliasing must be documented independently from biological interpretation.

**Governing relation:** `ΔV=(V_max−V_min)/(2^N−1); |quantization error|≤ΔV/2 for unclipped ideal nearest-code samples`.

**Finite reproduction:** Quantize an unclipped 0–1 V sample using 10 bits and require reconstruction error below half an ideal code step. Compare 200 samples of 17 Hz and 117 Hz sines at 100 samples/s and observe nearly identical discrete values.

**Negative or falsification condition:** Sampling examples are simulated and not equipment calibration or human-body electrophysiology measurements. Mains-connected or body-connected measurement circuit construction is out of scope.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 15 — Noise, calibration uncertainty and reproducible signal traces

**Question:** Measurement uncertainty has multiple sources: calibration reference, amplifier drift, thermal noise, digitizer resolution, model inadequacy and environmental interference. A numerical trace can be perfectly reproducible while a real instrument is not. An evidence record must therefore distinguish a random seed and generated noise samples from raw, calibrated laboratory observations.

**Governing relation:** `u_c=√Σu_i² for independent (uncorrelated) standard uncertainties`.

**Finite reproduction:** Combine independent uncertainties 3 and 4 in the same physical units; u_c=5. Generate two artificial noise traces using the same seed and standard deviation and verify identical SHA-256. Change seed and verify digest difference. Label the trace synthetic.

**Negative or falsification condition:** Numerical seed repeatability is not experimental repeatability. This edition does not provide verified biomedical instrumentation, medical diagnostic sensitivity or measured noise covariance.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 16 — Electrogenic pumps, metabolic work and non-equilibrium ion gradients

**Question:** Biological membranes maintain ion gradients through selective permeability and active transport. An instantaneous equilibrium potential is only one part of this system. Maintaining a gradient against dissipation requires energy input and mechanisms such as ATP-consuming pumps; a complete model must conserve matter and charge at the system boundary.

**Governing relation:** `dN_i/dt=J_pump,i−J_leak,i; C_m dV/dt=Σ_i I_i + I_external (specified signs)`.

**Finite reproduction:** Use the capacitor formula Q=C(V−V_ref) and a passive cable of five segments with sealed ends and zero leak. Under internal axial current redistribution, the sum of charge stays constant, showing the mathematical accounting needed before adding active flux terms.

**Negative or falsification condition:** No active pump kinetic parameters, biological viability, wound healing mechanism, or human physiology prediction is certified. This chapter is a dependency map, not a clinical procedure.

**Source locator:** `HODGKIN-HUXLEY-1952`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 17 — Offline engineering bench workflow with non-biological electrical dummies

**Question:** A disaster-recovery scientific library should lead from equations to a demonstrable physical test while avoiding unsafe leaps from simulation to live tissue. The first appropriate hardware check for Bioelectric Atlas is an isolated, battery-powered **non-biological dummy** made from known passive electronic components, not an electrode attached to a person or animal.

**Governing relation:** `Measured Z_dummy(ω) compared with Z_model(ω), with calibrated uncertainty and isolation safeguards`.

**Finite reproduction:** Create a synthetic model of Rs=100 Ω and Rct=900 Ω with parallel Cdl=1 µF. Independently compute the DC and high-frequency limiting impedance. Save a blank measurement worksheet for actual future instrument values. Mark every physical test requirement HOLD until authentic raw measurements and calibration exist.

**Negative or falsification condition:** Do not connect experimental equipment to humans, animals, implanted electronics, energized utility wiring, or life-support apparatus. The program does not contain a certified medical electrical safety design.

**Source locator:** `NAGUMO-1962`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

## Investigation 18 — Scientific evidence gates, source rights and nonclinical acceptance

**Question:** The purpose of a scientific continuity library is to preserve testable knowledge, including its uncertainties, model boundaries, source history and negative findings. A correctly hashed Python output does not prove that its equations apply to a living organism. A source card pointing at a peer-reviewed article does not mean the publication’s original file has been independently authenticated or that its full text can be freely redistributed.

**Governing relation:** `software verified ∧ original-source authentication missing ∧ physical evidence missing ⇒ independent science acceptance HOLD`.

**Finite reproduction:** Re-run the independently coded Nernst, cable, HH, FHN and ADC checks on a freshly reconstructed archive. Confirm that real tissue and peer review remain flagged HOLD. Attempt to pass a metadata field claiming an authenticated study without original bytes: the evidence gate must withhold scientific promotion.

**Negative or falsification condition:** The node is an executable educational reference, not a clinical guideline, neurostimulation device, biomedical research ethics approval, or complete history of electrophysiology.

**Source locator:** `BIPM-SI-2026`. It is a bibliographic reference; no original publisher document bytes were authenticated in this release. The official source does not validate the synthetic parameter choices.

**Classification:** mathematical model reference. Physical measurement: NOT PERFORMED. Medical relevance or clinical safety: NOT ESTABLISHED. Independent peer-review of this Atlas reconstruction: NOT ESTABLISHED.

