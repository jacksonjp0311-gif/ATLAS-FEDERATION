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
