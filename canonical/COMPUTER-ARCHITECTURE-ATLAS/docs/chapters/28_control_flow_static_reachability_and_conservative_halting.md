# 28. Static control-flow graphs, unreachable code and conservative halting analysis

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

An executable ROM can have control-flow errors despite valid instruction encodings. A static control-flow graph places nodes at even PC positions, with edges for ordinary fall-through, conditional taken/not taken branches and unconditional jumps; HALT has no successor. A fall-through beyond the ROM is a possible program counter trap, not a successful termination. Dynamic inputs to JZ and JNZ depend on runtime register values.

## Technical derivation and invariants

Let Reach be the least fixed point from PC=0 over all graph successors. A conservative structural guarantee that *all graph paths terminate at HALT* holds if the reachable subgraph is acyclic, has no fall-off traps, and every reachable sink is HALT. If a cycle exists, the correct result is `not structurally guaranteed`; one cannot infer that a particular program loops forever, because branch feasibility is not analyzed. This is a syntactic, not dynamic termination proof.

## Executable method and reproduction requirements

`control_flow_analysis` decodes every ROM instruction using original ISA rules and builds a bounded finite graph. It reports reachable and unreachable byte PCs, structurally cyclic nodes, reachable HALTs, fall-off traps and the bounded structural property. Test jumps over dead code, loops that run and terminate in finite samples, loops with unknown termination, and programs missing HALT.

## Constructed investigation

Consider `LDI R0,3; L: ADDI R0,255; JNZ R0,L; HALT`. Runtime countdown halts, yet the static graph includes a cycle. The analyzer rightly refuses a universal acyclic guarantee. Conversely `JMP DONE; LDI R0,99; DONE: HALT` has unreachable code at PC=2 and a structural halt proof.

## Counterexamples, scientific limits and missing evidence

General program termination is undecidable for unbounded computation and input; AT8 ROM/RAM are finite but the analyzer conservatively ignores state and inputs to avoid falsely claiming universal safety. Missing port data, simulated hardware defects and metastability are outside the graph proof.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.
