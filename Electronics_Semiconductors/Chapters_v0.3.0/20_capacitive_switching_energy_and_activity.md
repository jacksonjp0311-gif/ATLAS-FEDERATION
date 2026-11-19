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
