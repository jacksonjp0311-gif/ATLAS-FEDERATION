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
