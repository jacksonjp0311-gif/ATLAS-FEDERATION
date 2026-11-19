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
