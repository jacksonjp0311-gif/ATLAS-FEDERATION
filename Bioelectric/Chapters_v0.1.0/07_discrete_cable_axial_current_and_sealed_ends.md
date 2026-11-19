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
