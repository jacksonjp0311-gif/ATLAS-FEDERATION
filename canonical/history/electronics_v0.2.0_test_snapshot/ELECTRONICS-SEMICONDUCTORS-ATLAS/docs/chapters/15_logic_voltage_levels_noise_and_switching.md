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
