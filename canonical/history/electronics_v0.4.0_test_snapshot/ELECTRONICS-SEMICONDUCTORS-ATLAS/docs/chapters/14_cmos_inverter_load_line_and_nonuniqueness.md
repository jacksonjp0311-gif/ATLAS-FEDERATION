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
