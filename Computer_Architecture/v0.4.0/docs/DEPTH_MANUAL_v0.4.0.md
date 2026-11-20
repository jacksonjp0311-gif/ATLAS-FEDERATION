# ATLAS FORGE — Computer Architecture & Digital Hardware / v0.3.0 Original Federation

**A single original 15-node research infrastructure.** 48 complete chapters, 42 constructed software cases; no physical computer fabrication, original publisher file authentication, or external scientific review.

## Predecessor: unchanged v0.2 source chapters 01–36

# ATLAS FORGE — COMPUTER ARCHITECTURE & DIGITAL HARDWARE

## A reconstructible computer, not a fabricated one

Original 24-chapter scientific/engineering reference, part of the one original ATLAS FORGE federation. It defines a finite ISA, assembler, logic gates, microcycle machine, independent evidence and a manufacturing challenge. Every physical verification gate remains open pending actual measurements.

# 01. Architecture, microarchitecture, and reconstruction contracts

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Architecture, microarchitecture, and reconstruction contracts. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A computer architecture is a contract for externally observable computation. An instruction-set architecture (ISA) specifies the bits in instructions, the machine-visible state, how instructions transform that state, how memory and devices are addressed, and when execution faults. A microarchitecture implements that contract with datapaths, control, storage and timing. Distinguishing these layers is essential: an architecturally correct emulator does not establish that a physical processor was fabricated, and a fabricated logic circuit does not automatically implement the promised ISA. The AT8 reference intentionally has one small immutable ROM, four 8-bit general-purpose registers, 256 8-bit RAM cells, four abstract ports and a 2-byte fixed instruction format. All memory and register values are reset to zero. The reference model defines exact deterministic state transitions. A second four-phase implementation interprets the same binary words using an alternative control decomposition. A third independent reference validates the instruction results. These are three useful *software* evidence streams but not three independent silicon implementations.

A complete reconstruction chain proceeds from electrical gates through register cells, interconnect and timing into a CPU datapath, then firmware/assembler, memory interfaces, boot, and an executing program. AT8 implements only the digital semantic middle layer in Python. Its material, timing, transistor and packaging dependencies are typed cross-links to the existing Electronics and Manufacturing nodes, whose physical evidence gaps remain open.

## Executable contract and invariants

**Governing statement:** `S_(t+1)=ISA_step(S_t, instruction_at_PC); implementation != architectural specification`.

**Implementation:** `computer_atlas.spec.SpecMachine and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** bits, bytes, finite state. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Compare the same ROM on both machines, checking PC, all four registers, 256 RAM bytes, flags, output tape and input cursor after every committed instruction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An ISA can be mathematically coherent while a circuit fails setup/hold, overheats, or never passes a wafer test; do not promote executable Python into a fabricated hardware claim.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 02. Binary words, two’s complement, carry, and signed overflow

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Binary words, two’s complement, carry, and signed overflow. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

For an n-bit unsigned word, the mathematical state space is the ring of residues modulo 2^n. A stored 8-bit value ranges from 0 to 255, with arithmetic wraparound. Signed two’s complement reinterprets bit 7 as weight −128 and retains the same stored 8 bits. Signed and unsigned meanings differ; there is no separate physical storage representation. For 8-bit ADDI, form integer t=a+b, store t mod 256, carry=1 iff t>255. Signed overflow holds if the two operands have equal sign and the result has a different sign. Zero and negative flags follow from the result. For CMP, compute a−b modulo 256, use carry=1 to mean no unsigned borrow (a>=b), and calculate signed subtraction overflow from differing input sign bits. CMP updates flags but not a register. In AT8, conditional branches test the selected register, *not* the flags; failing to state this would make the instruction-set specification ambiguous.

A reconstruction needs a table of arithmetic cases, not only a formula. Test 255+1→0 with carry, 127+1→128 with signed overflow, 0−1→255 without unsigned carry, and equal operands yielding zero. The numerical oracle exhaustively covers all 65,536 8-bit operand pairs for the NAND adder, including carry and signed overflow.

## Executable contract and invariants

**Governing statement:** `ADD8(a,b)= (a+b) mod 256; C=[a+b>=256]; V=signs_equal(a,b) AND signs_differ(a,result)`.

**Implementation:** `computer_atlas.gates.alu8 and computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** 8-bit words, Boolean flags. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For 127 + 1, result is 128, carry 0, signed overflow 1; for 255 + 1, result is zero, carry 1, signed overflow 0.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

A zero flag, negative flag, unsigned carry and signed overflow are distinct properties. Omitting any of them loses information needed for software and verification.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 03. NAND gates, XOR, full adders, and compositional arithmetic

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

NAND gates, XOR, full adders, and compositional arithmetic. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

NAND is functionally complete: NOT(a)=NAND(a,a), AND(a,b)=NOT(NAND(a,b)), and OR(a,b)=NAND(NOT(a),NOT(b)). Four NAND operations implement XOR with an intermediate t=NAND(a,b). An elementary full adder computes s=a XOR b XOR cin and carry=ab+cin(a XOR b). Applying this bit by bit produces the ripple-carry adder. This decomposition provides a bridge from single-gate Boolean truth tables to machine-level ADDI semantics without assuming an existing software arithmetic instruction. The gate library is independently executable with pure Python bitwise arithmetic. Its finite results can be exhaustively checked against integer addition, but these checks do not establish logic-family voltage levels, fanout limits, propagation delay, gate count after synthesis or a semiconductor layout.

Long carry chains have increasing worst-case delay and expose why a combinational proof is not a timing proof. In physical hardware, the register-to-register path must include input setup time, cell delays, interconnect parasitics, clock uncertainty and receiving hold constraints. The preserved Electronics node contains reference timing equations; manufacturing evidence must supply characterized cell data.

## Executable contract and invariants

**Governing statement:** `s=a XOR b XOR cin; cout=(a AND b) OR (cin AND (a XOR b))`.

**Implementation:** `computer_atlas.gates.nand, full_adder, ripple_add`.

**Relevant dimensions:** bits, logic delay unspecified. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Enumerate all eight full-adder input triples and all 16×16 operand pairs for a 4-bit ripple adder; verify s+2cout=a+b+cin.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Truth-table correctness does not imply a physical clock frequency, hazard freedom, or transistor-level correctness.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 04. Four-register file, reset state, and instruction atomicity

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Four-register file, reset state, and instruction atomicity. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A small register file is addressable storage feeding a combinational datapath. AT8 has four architecturally visible registers R0..R3, each exactly 8 bits. On reset all registers and RAM bytes are zero, flags are Z=1,N=C=V=0, PC=0 and I/O tapes begin at their initial positions. An instruction reads its operands from the prior committed state and updates a staged next state. A STORE writes the old source register to RAM only when the instruction commits; MOV reads the specified source register even if its destination is the same register. This is a digital state-transition contract and intentionally not a physical 6T SRAM, flip-flop or clocked netlist.

Instruction atomicity is useful when a fault occurs. If an IN operation has no input on the requested port, the model raises an input-exhaustion trap without partially changing the destination register, flags, I/O cursor or RAM. The microcycle model also defers register and memory changes until COMMIT. This demonstrates rollback semantics in software; whether a physical design can guarantee the same observation in the presence of power failure or asynchronous signals requires separate study.

## Executable contract and invariants

**Governing statement:** `architectural_state_after = commit(architectural_state_before, decoded_operation)`.

**Implementation:** `computer_atlas.spec.SpecMachine.snapshot; computer_atlas.microcoded.MicrocodedMachine.tick`.

**Relevant dimensions:** bits, bytes, abstract instruction cycles. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Reset R0..R3, verify all zeros, execute LDI R0,77; STORE R0,200; LOAD R2,200; check RAM[200]=77 and R2=77.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Do not compare a partially executed microstage with an architectural instruction boundary; only COMMIT is an externally visible instruction state.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 05. ALU functions and the register-to-register datapath

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

ALU functions and the register-to-register datapath. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

The arithmetic logic unit (ALU) takes finite byte operands and a selected operation. AT8 supports addition with immediate, XOR, AND, OR and subtraction-like comparison; it also exposes LDI, LOAD and MOV as data movement. Datapath control must select source registers, immediate operand, function, destination register and flag updates. A physically implemented datapath would connect multiplexers, an ALU, register file, memory and program counter. The software reference deliberately describes these choices without pretending the machine has a verified silicon area or switching power.

Flags form part of the instruction-visible state, and each instruction specifies whether they change. Arithmetic or byte-producing operations update zero and negative, with carry and overflow set only where they have defined arithmetic meaning. STORE, branches, OUT and HALT preserve the existing flags. CMP affects flags but leaves the input register unchanged. This explicitness prevents a programmer from relying on accidental host-language behavior. The separate microcoded implementation computes the ADDI arithmetic using NAND-based gate functions, while the atomic specification uses native integer arithmetic; agreement across many cases is stronger than testing the same code twice.

## Executable contract and invariants

**Governing statement:** `ALUout = f(register_byte, immediate_byte); flags_next=flag_function(ALUout, operands)`.

**Implementation:** `computer_atlas.gates.alu8; computer_atlas.spec.SpecMachine; computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** 8-bit words, 4 Boolean flags. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Execute LDI R0,127 then ADDI R0,1; verify R0=128, N=1, V=1 and C=0. Compare microcoded and atomic snapshots.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

ALU throughput, power and gate count depend on physical implementation; no PPA (power, performance, area) claim is certified here.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 06. AT8 encoding: fixed 2-byte instructions and strict decoder

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

AT8 encoding: fixed 2-byte instructions and strict decoder. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

An instruction encoding is a byte-level contract, independent of how a processor might fetch the instruction. AT8 encodes every operation as exactly two bytes. The first byte uses its upper four bits for one of 16 operation codes and the lower nibble for a register index when the operation accepts a register. Only low-nibble values 0..3 are valid register indices, leaving other encodings reserved. NOP, JMP and HALT require the low nibble to be zero. The second byte is an unsigned 8-bit immediate, absolute branch target, memory address, source register for MOV, or port index depending on opcode. NOP and HALT require the second byte to be zero; MOV and I/O operands are bounded to indices 0..3. Branches require 2-byte-aligned absolute byte addresses.

Reserved encodings are rejected, not interpreted as future extensions or wrapped into legal values. The decoder should refuse any byte sequence of odd length, more than 256 program bytes or an invalid branch destination. These constraints establish a small, auditable image format. However, valid syntax and a present HALT instruction do not prove termination: a program may jump forever before reaching HALT. The assembler and runtime both enforce appropriate bounds.

## Executable contract and invariants

**Governing statement:** `word0 = (opcode << 4) OR reg4; word1 = unsigned_operand8; PC_next = PC+2 unless branch`.

**Implementation:** `computer_atlas.isa.encode, decode, validate_rom`.

**Relevant dimensions:** bytes, bit fields, PC byte addresses. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For LDI R0,5, the exact bytes are 0x10 0x05. For HALT they are 0xF0 0x00. The illegal byte sequence 0xF0 0x01 must fail validation.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An encoding table alone does not supply a PCB, boot ROM programmer, bus electrical standard or instruction-timing design.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 07. An auditable two-pass assembler with labels and diagnostics

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

An auditable two-pass assembler with labels and diagnostics. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Assembly language is a human-friendly notation for machine code. The AT8 assembler first scans labels and assigns addresses at two bytes per instruction, then resolves operand symbols and encodes bytes. This separation avoids accidental dependency on declaration order and permits forward branch references. Labels have a restricted ASCII identifier grammar and are case-insensitive. Numeric operands may be decimal, hexadecimal (0x) or binary (0b), but they must be unsigned bytes; negative numbers and floats are not silently truncated. A branch to a non-existent label, odd target address, duplicate label, reserved opcode, invalid register or ROM image exceeding 256 bytes is rejected with an explicit error.

The disassembler produces canonical numeric-target assembly. Assembling its result must reproduce the original bytes exactly for every valid image. That round-trip is an information-preservation invariant: it proves the tooling does not discard reserved fields or alter the binary representation. It does not prove the original program terminates or that its output is correct. Reconstructible computer systems should keep original assembly sources, exact binary hashes and semantic regression vectors together.

## Executable contract and invariants

**Governing statement:** `assemble(disassemble(valid_ROM)) == valid_ROM`.

**Implementation:** `computer_atlas.isa.assemble and computer_atlas.isa.disassemble`.

**Relevant dimensions:** UTF-8 assembly, ROM bytes. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble START: LDI R0,3; LOOP: OUT R0,0; ADDI R0,255; JNZ R0,LOOP; HALT. The loop target is byte address 2 and its output is 3,2,1.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

An assembler is not a optimizing compiler, linker or operating-system bootloader. AT8 supports neither object files nor relocatable binaries beyond its two-pass fixed-image labels.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 08. Program ROM, data RAM, and the memory address map

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Program ROM, data RAM, and the memory address map. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

AT8 uses separate immutable program ROM and mutable data RAM. ROM is 2..256 bytes with fixed two-byte instruction alignment; RAM has 256 independent byte locations addressed 0..255. This is a deliberately simple Harvard-style division, though real embedded systems may map memory-mapped devices into an address space, execute from RAM, implement caches, or unify instruction/data storage. In AT8, STORE cannot modify ROM: it writes only RAM. The PC is a byte address into ROM, not a RAM index and not an instruction count. Branch destinations are absolute even byte addresses.

Memory read/write contracts need a collision policy when physical ports can read and write the same location at once. AT8's sequential single-instruction model avoids simultaneous asynchronous accesses at the architectural level, but the preserved Electronics node independently records read-first/write-first/undefined physical memory semantics. The software machine guarantees logical LOAD/STORE behavior only, not SRAM retention time, bitline delay, refresh, ECC strength or physical memory manufacture.

## Executable contract and invariants

**Governing statement:** `ROM read: instruction=ROM[PC:PC+2]; RAM store: RAM[address]=register; PC byte aligned`.

**Implementation:** `computer_atlas.spec.SpecMachine, computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** ROM/RAM bytes, PC addresses. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Execute STORE R1,200 followed by LOAD R2,200 and verify R2 has the stored byte; verify that ROM bytes and the program checksum do not change.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

ROM/RAM separation alone does not prevent malicious programs from producing harmful behavior or all control-flow errors; the software is an educational bounded model.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 09. Fetch, decode, execute, commit: a finite control unit

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Fetch, decode, execute, commit: a finite control unit. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

An instruction-level architecture describes what an instruction does but not which internal operations happen first. The AT8 microcycle machine decomposes each instruction into four symbolic phases: FETCH loads the two ROM bytes into a latch; DECODE interprets opcode/register fields; EXECUTE forms pending register, flag, memory and branch effects; COMMIT makes those effects architecturally visible together. The reference treats every phase as one software tick and every instruction as four ticks, without claiming a physical clock frequency. An actual control state machine would need gate-level timing, reset synchronization, clock distribution, setup/hold margins and careful fault behavior.

The atomic reference executes one instruction in a single logical step and is intentionally different code. For every committed instruction, the microcycle machine's registers, RAM, PC, flags, input cursor and output tape must match the atomic machine. Before COMMIT, the architectural snapshot is unchanged. When the input tape is exhausted at EXECUTE, the partial microcycle state may remain internally latched but the externally visible architecture is unchanged. These are model-level atomicity properties, not claims of hardware transactional rollback.

## Executable contract and invariants

**Governing statement:** `microstate sequence FETCH -> DECODE -> EXECUTE -> COMMIT -> FETCH`.

**Implementation:** `computer_atlas.microcoded.MicrocodedMachine.tick and step_instruction`.

**Relevant dimensions:** symbolic phases, instruction steps. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

The LDI R0,5 instruction takes four microsteps. Assert R0 remains zero during FETCH/DECODE/EXECUTE and becomes five after COMMIT. Compare all outputs with the atomic reference.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Four symbolic software microticks do not imply four real CPU cycles, and no electrical timing is measured by this model.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 10. Program counter, conditional branches, and bounded termination

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Program counter, conditional branches, and bounded termination. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A stored-program machine's computation is determined not only by its arithmetic but also by its sequence of instruction addresses. The AT8 PC begins at zero and normally increases by two. JMP substitutes an absolute aligned ROM address. JNZ and JZ test one specified register for nonzero or zero respectively; they do *not* examine the ALU zero flag, even if a preceding CMP set that flag. This is a deliberate architectural choice that must be stated to avoid a misleading program interpretation. The assembler rejects out-of-range targets and unaligned addresses; the runtime separately checks that a fetched PC is valid.

Program termination is not decidable for arbitrary unbounded general-purpose programs, but this tiny model can always enforce a finite step budget. `run(max_steps)` either halts at HALT or returns an explicit bounded-budget status. It never silently declares an infinite loop successful. A looping program such as JMP 0 is syntactically valid and will repeatedly execute until the chosen bound is reached. A program that falls off the end without HALT raises a program-counter trap. This separation between ROM syntax, execution safety, and eventual termination is important for offline reconstruction and agent-driven experimentation.

## Executable contract and invariants

**Governing statement:** `PC_next = branch_condition ? target : PC+2; bounded run stops at max_steps`.

**Implementation:** `computer_atlas.spec.SpecMachine.step; computer_atlas.isa.assemble`.

**Relevant dimensions:** byte addresses, step counts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

The countdown code initializes R0=3, emits R0, decrements by ADDI 255, and JNZs to the output instruction until R0=0. Expected output: (0,3),(0,2),(0,1).

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Loop-bound completion is a resource limit, not a mathematical proof that the program would eventually halt.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 11. Input/output ports as deterministic recorded event tapes

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Input/output ports as deterministic recorded event tapes. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

External input is a major source of nondeterminism and unreproducible experiments. Rather than invoking devices or network services, AT8 represents each of its four input ports by an explicitly supplied sequence of byte values. An IN instruction reads the next available value on the selected port, then advances an input cursor *only when the instruction commits*. If no value is available it raises an input-exhaustion trap without modifying architectural state. OUT appends a pair (port,byte) to an output event tape and does not communicate with actual hardware. The output tape can be included in a signed-by-hash software test receipt, along with the ROM and input tapes.

This gives a reproducible software interface suitable for scientific verification: the same ROM and input sequences produce the same output and final state under the specified model. It does not establish electrical bus behavior, input synchronizers, output drivers, memory-mapped device timing, interrupt hazards or cybersecurity properties. Real device communication must be designed and characterized separately. The manufacturing evidence gate retains all physical I/O validation as outstanding.

## Executable contract and invariants

**Governing statement:** `IN: R[r]=tape[port][cursor]; cursor++ on COMMIT; OUT: tape_out.append((port,R[r]))`.

**Implementation:** `computer_atlas.spec.SpecMachine and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** byte ports, event order. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Supply input port 1=[7], execute IN R1,1; ADDI R1,2; STORE R1,4; LOAD R3,4; OUT R3,2; HALT, and verify one byte (2,9) is output.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

If the input tape is exhausted, do not return a default zero or consume an input event before a failed instruction commits.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 12. Traps, illegal opcodes, and failure atomicity

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Traps, illegal opcodes, and failure atomicity. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A reconstructible architecture must define what happens when execution cannot continue according to its contract. AT8 distinguishes malformed ROM encodings (DecodeError), assembly source errors (AssemblyError), and runtime traps (AT8Trap). Examples include reserved register encodings, nonzero reserved HALT operands, unaligned or out-of-ROM branches, invalid PC fetch and a missing required input. An illegal instruction is rejected before execution or trapped without silently skipping bytes. A fall-through beyond the last ROM word is an error, not an implicit HALT.

Failure atomicity prevents a partially completed instruction from corrupting the architectural state. The atomic and microcycle models stage register, memory, flags and I/O effects until their final commit. A trap in the input phase must leave all those externally visible properties unchanged, even if internal microstage counters or pending latches have been touched. This behavior is a software model property. A physical processor requires trap vectors, privileged state, precise exceptions, reset circuitry and interrupts; AT8 does not claim those mechanisms.

## Executable contract and invariants

**Governing statement:** `on trap: S_after = S_before (architectural effects); event=structured trap(code,PC)`.

**Implementation:** `computer_atlas.spec.AT8Trap and computer_atlas.microcoded.MicrocodedMachine`.

**Relevant dimensions:** machine state, error classes. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

For ROM IN R0,0; HALT with an empty input tape, snapshot state before the instruction, attempt execution, then assert the trap code is input_exhausted and the architectural snapshot is byte-identical.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Not all real hardware failures are architecturally precise; power loss, analog metastability and memory corruption are outside this digital contract.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 13. Reset vector, boot ROM, and immutable firmware checksums

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Reset vector, boot ROM, and immutable firmware checksums. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A computer's first useful operation depends on a reset path and a program image. AT8 uses a fixed reset vector PC=0 and explicitly initialized registers, RAM, flags, input cursors and output tape. Its ROM is an immutable byte string of even length, validated before execution. This allows an exact SHA-256 ROM identity to travel with a reference execution trace. A hash proves the recorded bytes match a particular receipt; it does not establish that the content is scientifically correct, safe, originally authored by a claimed person or lawfully redistributable.

Physical firmware storage introduces further dependencies: boot ROM fabrication or programmable nonvolatile memory, power-on reset timing, input pin stabilization, clock start, voltage supervision, byte ordering, memory interfaces and recovery if the image is corrupted. AT8 does not include secure boot or signatures. A production design would require a chain of trust and authenticated firmware update mechanism, but none is silently attributed to the present model. The offline ATLAS FORGE archive preserves both source assembly and exact ROM bytes so they can be independently regenerated.

## Executable contract and invariants

**Governing statement:** `boot_pc=0; reset_regs=(0,0,0,0); program_SHA256=SHA256(ROM_bytes)`.

**Implementation:** `computer_atlas.isa.validate_rom; computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** ROM bytes, SHA-256 digest. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble a six-instruction program, record the byte string and SHA-256, run it on two independent implementations, then compare ROM and execution-trace digests after fresh extraction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Checksums are not digital signatures, attestation, or evidence of a working hardware root of trust.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 14. Offline programming pipeline from assembly to ROM and execution trace

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Offline programming pipeline from assembly to ROM and execution trace. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

The minimum self-hosting pathway for a stored-program machine requires a way to describe a program, encode it unambiguously, load its binary representation, and observe its execution. AT8 provides a two-pass assembler, canonical disassembler, ROM validator, atomic executor and microcycle executor. The tools depend only on Python's standard library and do not access a model or network. An optional independent oracle uses its own execution logic to compare results and record exact per-program checks. This is a *software toolchain* and should not be called a compiler, runtime environment or fully self-hosted system.

Reproducibility requires preserving source text, assembler version, ROM bytes, input event tapes, execution budget, output tape, final state, and hashes of the program and trace. The byte layout, label rules and branch semantics must be versioned. The offline wheel must include the actual schema/registry resources so a model can discover the same exact source records after installation. Test the installed wheel from outside its build checkout to ensure the implementation does not silently depend on local files.

## Executable contract and invariants

**Governing statement:** `assembly -> two_pass_assemble -> ROM -> validate -> execute -> deterministic trace`.

**Implementation:** `computer_atlas.isa.assemble/disassemble; computer_atlas.spec.SpecMachine; evidence/independent_oracle.py`.

**Relevant dimensions:** UTF-8 text, bytes, execution events. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Compile the arithmetic/memory program and run it on an isolated installation. Expected RAM[0]=12 and output on port 0 equals 15; compare with a third interpreter.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

The host Python interpreter is a dependency of this software validation. The Atlas has not yet bootstrapped that interpreter on reconstructibly fabricated hardware.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 15. Differential testing: atomic model, microcycles, and third oracle

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Differential testing: atomic model, microcycles, and third oracle. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A system can pass its own unit tests and still contain shared mistakes if the tests reuse the same algorithm. AT8 therefore includes two separately structured DUT implementations and an independent byte interpreter in its evidence suite. The architectural model uses direct arithmetic for ADDI and CMP; the microcycle model uses a NAND-only 8-bit ALU; the third oracle decodes bytes independently and uses native arithmetic. The oracle performs exhaustive gate addition and signed-overflow comparisons for all 65,536 operand pairs, random full-program comparisons, assembler/disassembler round trips, explicit branch fixtures and negative input cases.

Independence is a spectrum, not a binary property. The three implementations share the publicly documented ISA and the same runtime Python environment; a specification error could be repeated in all of them. For scientific acceptance we would need external expert review, hardware-vs-software conformance tests, physically characterized RAM and control timing, and external replication with truly independent tooling. Source-history preservation and independent software oracle agreement establish a strong bounded engineering baseline, not independent scientific certification.

## Executable contract and invariants

**Governing statement:** `forall test_program: state_Spec == state_Micro == state_Independent_reference`.

**Implementation:** `evidence/independent_oracle.py; tests/test_microcoded.py`.

**Relevant dimensions:** finite test cases, SHA-256 receipts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Generate 700 deterministic random programs, execute all three references, compare full state and output, and repeat with different ROM seeds. Exhaust the 8-bit adder input space separately.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

A finite test suite cannot prove universal correctness of arbitrary future instruction extensions, real silicon faults or all program paths.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-6004`, official pointer: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c13/c13s1/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 16. Clock timing from digital control to physical register requirements

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Clock timing from digital control to physical register requirements. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Symbolic FETCH/DECODE/EXECUTE/COMMIT stages are not physical clock cycles. A real synchronous implementation requires a critical-path analysis linking register clock-to-Q delay, combinational logic propagation, setup time, clock skew and uncertainty. The corresponding hold constraint uses contamination/minimum delays and may fail even at a low clock frequency. The Electronics node already contains independently testable one-clock timing inequalities and explicit unknown-state behavior on setup/hold aperture violations. This Computer Architecture node uses those as exact-revision dependencies rather than claiming a Python microstep has an electrical duration.

A physical implementation would need a cell library calibrated over process, supply and temperature, extracted interconnect parasitics, clock tree and reset behavior, asynchronous I/O synchronization, realistic memory delays, and power/thermal budgeting. A clock-frequency claim without those inputs is unsupported. For reconstruction, map each AT8 micro-operation onto a register/ALU/memory control graph, identify its longest and shortest sensitized timing paths, and require measured bounds before signing off. A valid software trace can coexist with a physically unstable circuit.

## Executable contract and invariants

**Governing statement:** `T+skew >= t_cq_max+t_pd+t_setup+uncertainty; t_cq_min+t_cd >= t_hold+skew+uncertainty`.

**Implementation:** `Electronics v0.4 timing context + AT8 microstate DAG (no measured clock)`.

**Relevant dimensions:** seconds, hertz, voltage, temperature. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Use the Electronics timing reference with hypothetical values, then mark the clock-speed field of the AT8 evidence record as unverified. Do not invent a frequency from its four microstates.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

No clock-tree design, metastability characterization, SPICE model, standard-cell synthesis or STA signoff is included here.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-65900-2026`, official pointer: https://csg.csail.mit.edu/6.5900/lecnotes.html. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 17. Memory reliability: parity, SECDED, retention and fault detection

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Memory reliability: parity, SECDED, retention and fault detection. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Digital memory semantics are not physical memory reliability. The inherited Electronics node models a finite Hamming SECDED code, abstract SRAM/DRAM behavior, retention limits and read/write collision conventions. AT8's 256 RAM bytes are perfectly retained in the Python model, and ROM is immutable; this is a simplifying assumption, not a demonstrated memory cell design. A real memory would have finite read access times, energy costs, soft-error rates, partial writes, timing constraints and fault propagation. Error-correcting codes can detect or correct a stated subset of corruptions but do not guarantee correctness against arbitrary burst faults, controller failures or malicious modifications.

For reconstruction, define the memory word/byte layout, read and write ordering, reset behavior, sample ECC codewords and an independent oracle, then introduce fault injection. Test that a bit flip is detected or corrected where guaranteed, and that two-bit errors are rejected by the SECDED model. At the architecture level, choose whether ECC correction is transparent to software or triggers a visible trap; AT8 v0.1 does not encode a physical ECC controller. The manufacturing evidence gate requires actual retention and ECC measurements before claiming working memory.

## Executable contract and invariants

**Governing statement:** `RAM_next[a] = STORE ? R[r] : RAM_old[a]; ECC_correctable_errors <= defined bound`.

**Implementation:** `Electronics v0.3 Hamming SECDED and computer_atlas.spec.SpecMachine`.

**Relevant dimensions:** bits, bytes, BER and time (unmeasured). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Store a byte at RAM address 200 and compare round-trip LOAD. Separately inject single/double errors into a Hamming(8,4) reference code and retain explicit failure records.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Neither software RAM nor an ECC truth table establishes SRAM noise margins, DRAM refresh requirements or radiation reliability in fabricated memory.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 18. Constructing loops, branching programs, and stateful computations

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Constructing loops, branching programs, and stateful computations. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A useful computer must execute algorithms whose behavior depends on prior state, not only one fixed arithmetic expression. AT8 can implement a bounded countdown with a register, arithmetic decrement modulo 256, an OUT event and a JNZ branch to an earlier ROM address. Another program loads a byte from a scripted input port, modifies it, stores it in RAM and emits it on an output port. These examples provide complete traces of state changes. The data values and output sequence are independently reproducible without external services or machine-learning inference.

A stateful execution model must explicitly define program counter updates on branches, arithmetic wraparound, input exhaustion, RAM visibility and final termination. Bounded runtime execution prevents accidental infinite loops from hanging the test harness. Every exception should be reported as a precise failure, rather than hiding errors behind a successful process exit. These properties help future agent systems use the Atlas to verify generated programs. They do not demonstrate memory safety, a typed language, compilers, operating systems or arbitrary real-world peripherals.

## Executable contract and invariants

**Governing statement:** `R0_(k+1)=(R0_k+255) mod 256; JNZ(R0)->loop if R0 != 0`.

**Implementation:** `computer_atlas.programs.COUNTDOWN; computer_atlas.spec.SpecMachine.run`.

**Relevant dimensions:** instruction counts, state variables. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Assemble LDI R0,3; LOOP: OUT R0,0; ADDI R0,255; JNZ R0,LOOP; HALT. Verify output 3,2,1 and termination after 11 instructions.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Loop-step bounds are a resource control and not a proof of termination for all possible programs.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 19. Interrupts, privilege, timers, and memory-mapped I/O: missing architecture

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Interrupts, privilege, timers, and memory-mapped I/O: missing architecture. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

AT8 intentionally has no asynchronous interrupts, privileged mode, exception vector table, virtual memory, timer register or memory-mapped I/O. Its four abstract ports are deterministic event tapes, not physical bus-mapped devices. This limitation matters because a system can execute simple assembly successfully yet fail to coordinate external equipment, recover from hardware faults, protect memory or support an operating system. A more complete architecture would need a documented reset/trap vector, saved PC and cause registers, interrupt arbitration and masks, deterministic memory/IO ordering, privilege separation and device register interfaces. It would also need test vectors for nested interrupts, timing races and invalid memory access.

The present edition explicitly reserves all ISA opcode encodings for its own 16 operations and does not silently assign future privileged functions. Any extended ISA must receive a new version and migration/conformance tests rather than reinterpret old ROM bytes. The future Computer Architecture release can add these mechanisms only after preserving the current contract and verifying interoperability. AT8 v0.1 is a research kernel, not an OS-capable processor.

## Executable contract and invariants

**Governing statement:** `interrupt_pending -> trap_entry(PC, flags, cause) [NOT IMPLEMENTED IN AT8/0.1]`.

**Implementation:** `Future ISA extension contract; no executable interrupt model in v0.1`.

**Relevant dimensions:** bytes, interrupt vectors, time (future). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Test that unsupported opcode spelling such as INT is refused by the assembler rather than accepted with undocumented semantics.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

The absence of privilege/interrupts prevents OS, safety, device driver and real-time guarantees. No secure or industrial controller claims.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 20. Pipelines, dependencies, caches and memory hierarchy: research extensions

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Pipelines, dependencies, caches and memory hierarchy: research extensions. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A four-phase symbolic microsequence is not an instruction pipeline. Real pipelining overlaps the stages of several instructions, introducing hazards: data dependencies between reads and writes, branch/control dependencies, structural competition for hardware resources, and exception-ordering constraints. A pipeline may need forwarding, stalls, flushes, scoreboarding and precise commits. Likewise caches and virtual memory require explicit tags, replacement/eviction rules, dirty-state handling, coherence, translation and consistency semantics. AT8 v0.1 does not implement any of these mechanisms; its instructions commit sequentially in program order, and ROM and RAM access are idealized instantaneous logical operations.

The advantage of preserving a simple sequential architectural reference is that it can later serve as a correctness oracle for a pipelined implementation: every retired instruction must produce the same architectural state as the sequential model under the declared memory/IO semantics. This is differential verification, not an automatic performance model. The ATLAS FORGE roadmap should evolve this work toward a pipeline only after the base ISA is stable and supported by independent tests and circuit timing evidence. A speculative implementation that returns the right output for one program is not enough to prove ordering or precise traps.

## Executable contract and invariants

**Governing statement:** `forall retired instruction k: state_pipeline(k)==state_sequential_AT8(k) [FUTURE REQUIREMENT]`.

**Implementation:** `Future pipeline/register-transfer-level reference, explicitly not implemented`.

**Relevant dimensions:** clock cycles, bytes, access latencies (future). Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Describe a LOAD followed by ADDI using the loaded register and identify a true read-after-write dependency. Sequential AT8 needs no forwarding; a hypothetical pipeline might.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Do not report instruction-per-cycle throughput, cache hit rate or silicon speed without an actual implementation and measured workload.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-65900-2026`, official pointer: https://csg.csail.mit.edu/6.5900/lecnotes.html. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 21. Architectural invariants, refinement obligations, and finite exhaustive testing

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Architectural invariants, refinement obligations, and finite exhaustive testing. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

A rigorous design must have invariants that survive every valid state transition. In AT8, registers and RAM remain bytes, PC is always aligned when an instruction can be fetched, ROM bytes never change, outputs are port-index/byte tuples, and COMMIT is the only architectural visibility boundary. For a valid branch, the target must lie inside ROM; for a normal instruction, PC increments by exactly two. Every illegal or resource-exhausted instruction must trap without partial architectural mutation. These properties are asserted in unit tests and deterministic oracle reports.

This edition does not contain a mechanized theorem prover proof or model-check all 2^(2048) RAM states. The word “formal” here identifies logical contracts and the possibility of future refinement proofs, not completed formal verification. Exhaustive testing of the 8-bit ALU input space and bounded random programs gives useful finite coverage; it is not universal proof for arbitrary ROM contents. A future verifier should model AT8 in a separate theorem prover, establish inductive invariants, and compare any hardware netlist/RTL with the reference on all reachable states under explicit environmental assumptions.

## Executable contract and invariants

**Governing statement:** `invariant: regs, RAM ∈ Byte; PC mod 2=0; ROM_after=ROM_before; commit_effects_only`.

**Implementation:** `computer_atlas.isa.validate_rom; tests/test_spec.py; evidence/independent_oracle.py`.

**Relevant dimensions:** Boolean predicates, finite state counts. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Force invalid ROM operands, empty input tapes and fall-through PC; verify explicit rejections and no earlier committed data loss. Check all 256×256 adder pairs.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

No machine-checked proof certificate or externally reviewed formal equivalence result exists in this release.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 22. Evidence-gated bridge from mathematical CPU to manufactured electronics

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Evidence-gated bridge from mathematical CPU to manufactured electronics. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

ATLAS FORGE now has Manufacturing and Electronics references capable of expressing missing process evidence. The computer architecture's new continuity challenge compiles and executes an AT8 program, then asks the existing Manufacturing Evidence Gate whether the prerequisites for a physical CPU are documented. The software passes; the gate reports missing substrate/mobility measurements, lithographic overlay, oxide characterization, transistor I–V/C–V curves, gate voltage noise margins and timing, memory retention/ECC tests, and a signed independent hardware execution trace. Supplying placeholder metadata may satisfy syntactic process dependencies but cannot authenticate their truth; the manufacturing model expressly refuses to call such metadata independent certification.

This is the most important separation for the technological-continuity mission: a logically correct instruction set is an ingredient, not a physically reconstructed computer. A credible reconstruction would demonstrate a transistor or discrete gate implementation, power and clock, stored ROM and RAM, controlled measurement, repeatable execution of the golden binary, logged output events and independent review. Every stage needs raw measurements and uncertainty. The Atlas should retain missing evidence as first-class data so future systems know precisely what remains to be built.

## Executable contract and invariants

**Governing statement:** `software_verified AND physical_evidence_missing -> physical_reconstruction_status=HOLD`.

**Implementation:** `evidence/continuity_challenge.py; Manufacturing manufacturing_evidence_gate`.

**Relevant dimensions:** source files, measured SI units pending. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Run the original Electronics accumulator and the new AT8 program: both store 12 and compute 15. Then verify all 12 types of physical evidence remain missing across six stages.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Passing both software simulators does not certify a fabricated chip or computer; recorded metadata alone cannot provide independent hardware evidence.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `NAND2TETRIS`, official pointer: https://www.nand2tetris.org/. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 23. Offline preservation: exact revisions, rights, sources, and reproducible builds

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Offline preservation: exact revisions, rights, sources, and reproducible builds. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Scientific and engineering continuity requires preservation at multiple layers. Original authored code, exact record revisions, relationship endpoints, source cards, historical tests, offline artifacts and rebuild scripts must remain available as one coherent graph. A direct incremental release may be much smaller than its predecessor, but its restoration depends on the exact predecessor archive; periodically retained full archives and redundant storage are necessary to avoid brittle dependence on a long delta chain. All target files should be SHA-256 verified and a deterministic full ZIP should be reconstructed byte-for-byte, then extracted into a fresh environment where tests run again.

SHA-256 is a data-integrity mechanism, not evidence of technical validity, licensing, provenance truth or original publisher source authenticity. Bibliographic URLs should remain explicitly unverified until authenticated original bytes with edition, rights and page/equation locations are captured. Independent reviews and measured hardware traces should be separate signed records, not overwritten into existing test receipts. The original 30-domain roadmap must remain unmodified, and this new Computer Architecture node must be labeled an auxiliary enabling domain. ATLAS FORGE's planned Bitwork router remains downstream of scientific content completion.

## Executable contract and invariants

**Governing statement:** `SHA256(restored_full_archive)==SHA256(expected_release_archive) AND immutable_prior_revisions`.

**Implementation:** `ATLAS FORGE common.registry, file manifests, incremental restore and full regression`.

**Relevant dimensions:** bytes, file hashes, revision identifiers. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Restore the exact Manufacturing v0.2.0 archive, apply the new computer patch, verify every file and replay all historical and new tests from a clean extraction.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

Archive integrity does not establish scientific truth, secure supply chains or real hardware reproducibility.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `RISCV-MANUAL`, official pointer: https://github.com/riscv/riscv-isa-manual. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.


---

# 24. From an 8-bit computer contract to compilers, operating systems, and AI

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

From an 8-bit computer contract to compilers, operating systems, and AI. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

The broader technological-continuity mission is to preserve enough layered knowledge that a future human or AI could rebuild and verify a computer starting from materials. AT8 supplies a small, testable ISA and execution reference at the center of that dependency chain. It proves the feasibility of defining and validating a finite stored-program model without assuming cloud services or specialized hardware. But a useful real computer needs considerably more: physical gates, memory fabrication and retention, timing closure, a reliable reset and power chain, observable devices, a complete assembler/linker/compiler, interrupts, privilege, persistent storage, boot firmware, an operating system or runtime, and eventually libraries and AI inference workloads. The original atlas domains for Compiler Design, OS Internals, Distributed Systems and future neural architectures remain separate content priorities in the preserved 30-domain queue.

A sensible roadmap is evidence-driven rather than version-driven: (1) finish finite ISA contract and independent software oracles; (2) translate the datapath/control into a verifiable gate or RTL implementation and compare retired states; (3) characterize and reproduce physical logic/memory; (4) demonstrate a measured hardware program with an independent golden trace; (5) implement assembler/firmware runtime and reliable I/O; (6) use the resulting infrastructure to support scientific computation and AI. Every step has distinct acceptance and failure criteria. The model should not use the phrase 'general intelligence' or 'world-changing discovery' as a substitute for measured reconstruction success.

## Executable contract and invariants

**Governing statement:** `verified_software_model -> physical_gate_evidence -> measured_CPU -> runtime -> scientific_computation`.

**Implementation:** `COMPUTER-ARCHITECTURE-ATLAS docs/SCOPED_V1_GATES.md; Manufacturing/Electronics evidence lattice`.

**Relevant dimensions:** capability dependencies, hardware evidence gaps. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Begin from the verified AT8 three-way execution challenge, list missing physical evidence, and keep independent acceptance on HOLD until measured hardware replicates a golden program.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

No physical computer, independent research replication, general-purpose operating system or AI chip is demonstrated by these initial architecture documents.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-65900-2026`, official pointer: https://csg.csail.mit.edu/6.5900/lecnotes.html. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.



---

# Computer Architecture v0.2.0 — New original chapters 25–36

**One canonical ATLAS FORGE federation.** The preceding 24 chapters are retained verbatim, followed by twelve new bounded, independently testable reconstructions. Physical implementation, publisher original-file acquisition and expert sign-off remain open.

# 25. Preserving byte-exact AT8 semantics and an explicit programming contract

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

AT8-0.1 is two-byte fixed encoding [opcode|register, operand]. The new compiler MUST not reinterpret reserved low bits, register numbers or branch destinations. CPU architectural compatibility is defined by identical externally observable state transitions for every legal instruction, not merely programs that happen to halt. Four general registers are R0..R3, each an unsigned byte; ROM addresses are even and 0..254, and RAM addresses are byte indices 0..255.

## Technical derivation and invariants

For a program P with inputs I, define architectural trace T(P,I) as the sequence of committed (PC, register file, RAM changes, flags, output events) records. An ABI is a convention over this ISA: v0.2 structured programs use R0 as source-visible accumulator and R3, R2, R1 as compiler-reserved loop counters. The compiler must not clobber an active outer loop register. This is not a production calling convention and has no stack, heap or interrupt-safe preservation rules.

## Executable method and reproduction requirements

Keep `computer_atlas.isa.assemble`, `decode`, `SpecMachine` and `MicrocodedMachine` byte-identical to v0.1. The new `v02_bootstrap` compiler emits only those instructions and refuses more than 128 encoded instructions. Negative controls should reject invalid register encodings, unsupported ISA opcodes, odd branch addresses, missing HALT and ambiguous memory semantics.

## Constructed investigation

Compile `SET 5; ADD 7; STORE 4; XOR 3; OUT 0; HALT` (one statement per line). The encoded program executes on the unmodified AT8 and leaves RAM[4]=12, R0=15, and output port 0 emits 15. Re-running with a second execution engine must produce the same architectural state.

## Counterexamples, scientific limits and missing evidence

This contract does not establish a stack ABI, binary executable format, linker, interrupts, privilege modes or hardware pipeline. Its deliberately limited conventions preserve a testable bootstrap, not a general OS ABI.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 26. A bounded structured-language compiler from source to AT8 ROM

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

AT8 already has a label-capable assembler. The next reconstruction tier is a source language that captures intent without asking a human to manage every jump. It has SET, ADD, XOR, AND, OR, LOAD, STORE, IN, OUT, REPEAT/END and terminal HALT. Every statement requires declared byte-sized operands or ports. The parser builds an immutable abstract syntax tree rather than directly emitting bytes while reading text.

## Technical derivation and invariants

Let ⟦S⟧ be the reference source interpreter state transformation and C(S) the compiler output. The desirable finite property is `project(Exec_AT8(C(S),I)) == ⟦S⟧(I)`, where project selects R0, RAM, output stream, consumed input cursors and halting status, excluding compiler-private counter registers. This property is tested, not universally proved for all arbitrary source texts. The source language is purposefully finite, with ROM≤256 bytes and exact integer inputs.

## Executable method and reproduction requirements

`parse_source` rejects malformed blocks, missing terminal HALT, out-of-range ports/bytes, early halt and loop nesting deeper than three. `compile_source` produces assembler instructions and calls the already-preserved AT8 assembler; `evaluate_source` interprets the AST without compiling. A separate test compares final state with both atomic and four-stage execution engines. Each evaluator has a bounded execution budget.

## Constructed investigation

Source: `SET 5; ADD 7; STORE 4; XOR 3; OUT 0; HALT`. The AST reference obtains stored 12, output 15; the AT8 ROM obtained through the compiler must do the same. A compiler that mistakenly maps `SET` to ADDI would fail this test and the exhaustive addition comparisons.

## Counterexamples, scientific limits and missing evidence

This is a small original educational compiler, not a C/LLVM replacement or complete high-level programming language. It lacks variables beyond R0, subroutines, relocation, debugging symbols and standard libraries. Source SHA-256 is identity/provenance, not proof that code is safe or externally authored.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 27. Nested counted loops and compiler-owned register allocation

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A structured counted loop requires the machine to preserve a counter that the body does not overwrite. With only four registers, a conservative allocation reserves R0 for user accumulator and R3, R2, R1 for successively nested loops. An outer loop uses R3 while the inner loop uses R2, preventing counter aliasing. The compiler refuses a fourth nesting level instead of spilling into undocumented memory or silently corrupting state.

## Technical derivation and invariants

For a loop `REPEAT n {B}`, the emitted structure is `LDI Rc,n; L: C(B); ADDI Rc,255; JNZ Rc,L`. Because addition is modulo 256, decrementing 1 by 1 produces zero, and JNZ tests register value, not flags. With 1≤n≤255 and no modification of Rc inside B, the loop body executes exactly n times. Loop expansion consumes three instruction words plus the body, not n explicit source copies, but runtime cost still scales with iteration count.

## Executable method and reproduction requirements

A nested-block parser tracks lexical frames; each END must match one REPEAT, and a block cannot be empty. The independent AST evaluator counts source operations and raises when its budget is exhausted. The AT8 engine has a separate instruction budget. Both must agree about result data, output events, and input consumption; their operation counts need not match.

## Constructed investigation

Run `SET 0; REPEAT 2; REPEAT 3; ADD 2; END; END; HALT`. The result in R0 is 12. Changing the inner repeat to 4 yields 16. With `SET 250; REPEAT 6; ADD 1; END`, R0 wraps to 0, proving byte semantics. A fourth nested loop must be rejected.

## Counterexamples, scientific limits and missing evidence

Counted-loop termination requires the stated compiler-reserved register noninterference and finite input availability. It does not imply termination for arbitrary hand-written AT8 ROM. Nested loops can exceed step budgets; no unknown runtime should be accepted without a bound.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

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


---

# 29. Reproducible source-to-ROM builds, content hashes and provenance

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

Reconstruction requires more than running a program once. The source text, compiler version, ISA specification, exact ROM bytes, input tape and output trace must have stable, separately verifiable identities. An archival manifest can contain SHA-256 of source UTF-8 and ROM bytes, along with a schema version and known source-to-execution mapping. This makes later corruption or accidental code drift detectable, assuming the manifest itself is retained through a trusted route.

## Technical derivation and invariants

A reproducible build statement is `H(C(S)) == H(rom_reference)` for the exact compiler/assembler release, source S, and byte representation. If the input language treats whitespace/comments differently, hashing original text is distinct from hashing a normalized AST; the receipt must state which is used. A SHA-256 collision is not assumed computationally practical, but a content hash alone does not authenticate the publisher or prove program correctness.

## Executable method and reproduction requirements

`compile_receipt` produces source and ROM hashes and source evaluator output, explicitly tagged as constructed software evidence. The full federation packer should independently archive deterministic source, test outcome receipts, SHA-256 file manifests and a direct restoration path. A clean process must re-run compiler, interpreter and machine-model tests without hidden cloud components.

## Constructed investigation

For source `SET 5; ADD 7; HALT`, compare `compile_source` results across fresh processes. The digest must be reproducible; a single literal change from ADD 7 to ADD 8 changes ROM bytes and the recorded hash. A manually edited ROM should fail the expected-manifest digest even when some observed output remains equal.

## Counterexamples, scientific limits and missing evidence

Hash mismatch may be accidental or adversarial; hash equality cannot establish physical execution, editorial correctness, science acceptance or license compliance. The human provenance and original publisher documents remain separate evidence categories.

## Source and dependency ledger

**Primary orientation:** `RISCV-MANUAL` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 30. Byte-wide SECDED (13,8) error control for executable ROM

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A stored eight-bit value can be protected with an extended Hamming code using parity bits at one-based positions 1,2,4,8, data bits at 3,5,6,7,9,10,11,12 and overall even parity at position 13. This gives 13 stored bits per original byte. The codeword is a finite mathematical redundancy scheme, distinct from the underlying physical failure mechanism.

## Technical derivation and invariants

Construct four parity-check bits from the binary positions. On reading, compute syndrome s∈[0,15] and overall parity p. (s,p)=(0,0) means no detected error. Nonzero syndrome with odd overall parity identifies a candidate corrupted location 1..12; zero syndrome and odd parity identifies position 13. Nonzero syndrome and even parity indicates an uncorrectable two-bit pattern; never return a decoded byte then. This guarantees correction of any one flipped bit and detection of every two-bit pattern, but not reliable recovery from arbitrary triple or higher-weight faults.

## Executable method and reproduction requirements

`encode_byte` validates exact 8-bit input and returns 13-bit codeword; `decode_word` marks clean, corrected or detected_double. `protect_rom` adds one such word per byte, and `recover_rom` refuses double-error codewords. An optional independently trusted ROM SHA-256 detects changes that parity alone may miss. Neither ECC nor a raw digest authenticates external origin.

## Constructed investigation

For each of the 256 byte values, verify an untouched codeword, all 13 one-bit flips and all C(13,2)=78 double-bit flips. That is 256×92=23,552 cases before optional ROM-level recovery tests. An independently written parity-matrix encoder should agree with the reference to avoid copying the implementation under test.

## Counterexamples, scientific limits and missing evidence

SECDED cannot certify DRAM/SRAM retention or radiation upset rates. Burst patterns can exceed distance-four guarantees; decoders and metadata may also be faulty. A physically useful memory subsystem requires measured fault distributions, address/data-path protection, scrubbing policy, and well-defined recovery failure behavior.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 31. ROM recovery, failure reporting and verification boundaries

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

An instruction ROM is not equivalent to a mathematical byte sequence if its storage medium can corrupt bits. A reconstruction reference should retain the executable image and a protected codeword representation, then define how to respond when errors are detected. A correct decoder must not silently return a corrupted instruction stream after a double-bit error or after a mismatch against a separately trusted byte hash.

## Technical derivation and invariants

For encoded words c_i, decode each independently; if any word reports detected_double, abort before executing *any* recovered program. After successful decoding, calculate `H(ROM_recovered)` and compare with a pinned expected hash when one exists. A one-bit correction is counted, not concealed. More than two faults within a word may produce undetected or miscorrected patterns, so the checksum adds detection coverage but not absolute security.

## Executable method and reproduction requirements

`recover_rom` checks length and exact 13-bit bounds, counts corrected words, and raises `UncorrectableROMError` for detected two-bit events or hash mismatch. Test one-bit corruption, two-bit corruption, invalid metadata, even-length ROM bounds and independent retention of hash pins. Do not execute a ROM that has failed the gate.

## Constructed investigation

Encode `LDI R0,5; HALT` and flip one encoded parity or data bit. The reference recovers identical ROM bytes and reports exactly one corrected word. Flip two bits in the same word; recovery refuses with an explicit double-error class. Supply the wrong expected SHA-256; recovery refuses even if the ECC decoder sees clean codewords.

## Counterexamples, scientific limits and missing evidence

This handles isolated codeword bit flips, not tampering with the golden hash, provenance identity, unreliable readers, full media failure or hardware fault injection. Real storage protection requires replicated media, calibration, retention tests and external trust roots.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 32. Instruction retirement, staged side effects and differential machine execution

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

Correctness at the ISA boundary is defined by architecturally visible state: PC, registers, RAM, flags, I/O events, consumed input indices and halt/trap status. A microarchitecture may use many hidden control stages but must not expose a half-committed instruction. This creates an important testable separation between the **ISA reference** and an independently implemented four-stage FETCH–DECODE–EXECUTE–COMMIT model.

## Technical derivation and invariants

Let S_n be architectural state after retiring n instructions. For a valid instruction i, `SpecStep(S_n,i)=MicroRetire(S_n,i)` is the key bisimulation-style finite condition. A trapped instruction should not partially commit registers, RAM or input/output state. Non-retired microstage latches are intentionally not part of S_n; they are implementation detail. The two software models can share a specification but must not share the same execution routine.

## Executable method and reproduction requirements

`differential_retirement` advances both models, compares the entire snapshot after each retirement and records deterministic events with state SHA-256. An input exhaustion trap or illegal ROM branch is audited as a stopped computation, not silently turned into HALT. A bounded step budget prevents endless monitoring of loops.

## Constructed investigation

For the arithmetic program `LDI R0,5; ADDI R0,7; STORE R0,0; XORI R0,3; OUT R0,0; HALT`, both models leave RAM[0]=12, R0=15 and output event (port0,15). A broken microcycle implementation that increments the input cursor in DECODE instead of COMMIT would diverge when the input is exhausted.

## Counterexamples, scientific limits and missing evidence

Execution trace hashes establish reproducibility under exact software versions and inputs, not whether a silicon CPU clocked through these phases or whether real signals obey setup/hold. Exact physical timing requires device characterization, clock tree, power and memory-system evidence.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 33. Precise traps, finite watchdog budgets and deterministic I/O tapes

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A reproducible computer requires failure semantics as carefully defined as success semantics. If an input port is exhausted, an instruction is illegal, a branch address is misaligned, or a program counter falls beyond ROM, a model must report a trap with the responsible PC before committing side effects. A watchdog step budget is another explicit stop condition, distinct from HALT.

## Technical derivation and invariants

Define `Snapshot(S)` as architectural state. A failed instruction should satisfy `Snapshot_after_trap = Snapshot_before_instruction`; this preserves precisely observable state so a debugger or recovery process can diagnose without guessing which writes occurred. A loop stopped due to a testing budget is not automatically a program that cannot terminate under another input or budget.

## Executable method and reproduction requirements

The new trace audit includes ROM hash, ordered retired PC and instruction events, aggregate event hash, halted flag and any explicit trap. Input tapes are finite port-indexed byte sequences and output is an ordered list of (port,byte) pairs, independent of host terminal devices. Test bounded loops, insufficient input, replay determinism and invalid metadata.

## Constructed investigation

`IN R0,1; HALT` with an empty port1 tape traps with input_exhausted without incrementing port cursor. `L: JMP L` with step limit=10 returns a bounded unfinished trace instead of an infinite tool call. Altering a ROM byte changes its digest even if a finite output is coincidentally unchanged.

## Counterexamples, scientific limits and missing evidence

Software traps cannot protect against physical power loss, clock-domain crossing, cache errors or all timing faults. A future OS and interrupt node must add privilege and device exception semantics; the educational AT8 v0.1 ISA deliberately lacks them.

## Source and dependency ledger

**Primary orientation:** `RISCV-MANUAL` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 34. Independent source-language semantics and bounded compilation comparisons

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

To bootstrap future tools, it is useful to carry a tiny language implementation along with a separately executable definition of what its programs mean. The AT8 v0.2 language has no hidden host file system, network operations, calls or unbounded allocation; each program consists of bounded integer operations, memory reads/writes, port events, structured counted loops and explicit halt.

## Technical derivation and invariants

The key comparison is between the AST evaluator and the compiled machine, after projecting away reserved compiler counters. Compare the source accumulator, full 256-byte memory image, output trace, input consumption and termination. It is not meaningful to compare AST statement count with hardware microtick count; they measure different abstractions. Differential testing gains strength when the implementation paths are distinct.

## Executable method and reproduction requirements

An independent oracle exhausts all 65,536 pairs of immediate 8-bit addition inputs using compiled AT8 ROM, then tests hundreds of randomly nested loop programs against both atomic and microcycle emulators. Because the compiler produces labels and assembly, an assembler bug or source binding bug can manifest as an incorrect image, trapped branch or mismatched output.

## Constructed investigation

Use the nested source program `SET 0; REPEAT 2; REPEAT 3; ADD 2; END; END; HALT` to demonstrate 12. Check inputs and outputs by a separate evaluator and compare ROM hashes. Invalid source such as `REPEAT 0`, depth four, bad port or missing terminal HALT must be rejected.

## Counterexamples, scientific limits and missing evidence

Finite experiments do not prove arbitrary compiler correctness or absence of unknown optimization bugs. This edition makes no claims about self-hosting, C/LLVM compatibility, memory management, high-level OS services or real silicon.

## Source and dependency ledger

**Primary orientation:** `NAND2TETRIS` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 35. Physical manufacturing dependencies and the limits of metadata-based assurance

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A software ISA is not a fabricated computer. An engineer attempting to reconstruct AT8 on real silicon or discrete logic needs material identity, wafer/device characterization, dielectric and contact metrology, voltage-transfer curves, clock/reset integrity, memory retention, power/thermal testing, interconnect/layout documentation and independently measured hardware execution traces. The Manufacturing and Electronics nodes define these as separate physical evidence obligations.

## Technical derivation and invariants

The physical evidence condition is a conjunction of necessary verified predicates: `AcceptedHardware = AND_i VerifiedByQualifiedProcess(E_i)`. A text field named `verified`, a copied SHA-256, or an AI-generated report is not an external calibration witness. Without trusted origin and independent measurements, every physical requirement remains open even if all placeholders are populated. The checker therefore never promotes assertions supplied as metadata into a physical pass.

## Executable method and reproduction requirements

`physical_evidence_matrix` lists 12 required types and the blocking stages. It accepts at most recognized names as asserted metadata, reports those claims separately, and retains all unverified physical requirements under HOLD. The Manufacturing evidence lattice remains the source of the full process/assurance graph; v0.2 deliberately does not duplicate or overwrite it.

## Constructed investigation

Supply `{"wafer_characterization":{"claimed":true}, ...}` for all 12 categories. The output reports 12 claimed metadata types and 12 unverified types. The software arithmetic and ROM protection tests can pass in the same session, but the hardware gate stays HOLD. This is a meaningful negative control against false confidence.

## Counterexamples, scientific limits and missing evidence

This is an audit protocol, not a real metrology experiment. Future reviewers must independently examine raw instrumentation records, calibrations, geometry, materials, foundry process receipts, test-chip traces and revision hashes before claims of physical reconstructibility.

## Source and dependency ledger

**Primary orientation:** `MIT-6004` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.


---

# 36. From a finite AT8 compiler to operating systems and scientific AI

**ATLAS FORGE / Computer Architecture & Digital Hardware v0.2.0 / one original canonical federation**

Evidence tier: original bounded technical reconstruction, deterministic software tests, and independently authored finite oracles. **No fabricated processor, calibrated hardware, original publisher PDF or external scientific review is claimed.**

## Reconstruction question and definitions

A historical computer can be reconstructed along a chain of explicit interfaces: semiconductor material → transistors → logic gates → registers and memory → ISA/microarchitecture → assembler and tiny compiler → validated ROM → I/O and storage → runtime → operating system → scientific tools. AT8 v0.2 provides the finite ISA/assembler/compiler portion and a traceable control-flow/ecc/retirement verification layer; it does not fabricate or qualify earlier physical layers.

## Technical derivation and invariants

The reconstruction contract must avoid collapsing distinct proof tiers. A deterministic simulator establishes software transition equivalence. Independent finite oracles constrain software errors. A content hash protects byte identity. Scientific source review compares derivations with authoritative originals. Device measurements calibrate physical predictions, and controlled hardware execution establishes real operation. None can be substituted for another.

## Executable method and reproduction requirements

The next useful development steps are an explicit byte-level I/O protocol, reset and boot monitor, more general source language with variables and calls, assembler/linker with relocation, bounded OS services, formal property checking, and eventually real-gate/RTL implementations. Every new tool must have a second reference path and a clean offline rebuild. The original 30-domain roadmap includes separate Compiler Design and OS domains, which must be respected rather than absorbed into one inflated Computer Architecture milestone.

## Constructed investigation

Run an AT8 source-language program through parser, assembler, ROM ECC, machine retirement and source evaluator, producing a source hash, ROM hash, expected output and a physical-evidence HOLD record. Reconstruct this in a clean process without external services. Compare all reference states and preserve negative failure cases.

## Counterexamples, scientific limits and missing evidence

The current result is a software research increment inside the existing 15-node ATLAS FORGE federation. It does not claim a physical CPU, full operating system, self-hosting compiler, independently signed scientific review, or authenticated publisher originals. Manufacturing/Computer Architecture alignment and all historical releases stay preserved; Bitwork routing remains deferred.

## Source and dependency ledger

**Primary orientation:** `RISCV-MANUAL` — an exact-revision source card inside this same Computer Architecture node, drawn from official publisher URLs. The original publisher PDF/text bytes are *not* authenticated or redistributed in this edition. The derivation and code are original ATLAS FORGE educational work. Cross-node prerequisites: Electronics & Semiconductors for logic/cell physics; Manufacturing for metrology and evidence; Mathematics & Physics for formal methods; Computation for computability and algorithms. Source card relationships are not evidence of peer review. Preserve raw bytes, negative cases, model boundaries, license status, test receipts, and provenance.



---

## New v0.3.0 original research: boot integrity, execution and reconstruction

# 37. Immutable boot-image structure and AT8 machine-code identity

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`image=header(magic,version,flags,length,CRC32,SHA256) || ROM`

**Units and representation:** bytes, bit strings, aligned instruction PCs. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An original programmable machine needs a finite contract for loading instructions before it can run any compiler or operating system. AT8 uses a fixed two-byte instruction format, four general-purpose registers and 256 bytes maximum of ROM. The boot-image wrapper does not change the instruction set. It defines a **44-byte header**: 4-byte ASCII magic `AT8R`, 1-byte format version 3, 1-byte reserved flags 0, 2-byte big-endian ROM length, 4-byte big-endian CRC32, and a 32-byte raw SHA-256 digest, followed by the unmodified ROM payload. Total image length is exactly 44 + ROM length. The length must be even and within 2–256 bytes. The canonical encoder and decoder must agree byte-for-byte, not merely interpret the same program.

The mathematical property of a fixed header is that the parser can decide where each field begins without invoking code from the payload. The checksum protects against some accidental or unmodeled corruption; SHA-256 provides a cryptographic *digest*. Neither provides source authentication without an independently trusted reference and an appropriate signature or authenticated boot root. The decoder therefore reports `sha256_is_authentication=False`, and the image is not a secure-boot design. NIST SP 800-193 distinguishes firmware integrity from protecting authorized firmware changes; we use its categories as bibliography, not as a claim of NIST conformity.

## Reproduce this investigation offline

Assemble `LDI R0, 5; ADDI R0, 7; OUT R0, 0; HALT` to an eight-byte ROM. Generate an image of exactly 52 bytes. Parse magic/version/length independently with `struct.unpack('>4sBBHI32s', header)`, recalculate CRC32 and SHA-256 from the eight ROM bytes, then compare a second encoding byte-for-byte. Mutate the magic, reserved flags, version, payload length, CRC, digest and final byte one at a time. Every corruption must be rejected without executing any instruction.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `encode_boot_image, decode_boot_image`.

## Counterexamples, failure modes, and model scope

The reference does not include a persistent root of trust, key custody, signing authority, anti-rollback fuse, physical memory map, reset hardware, firmware flashing, ROM manufacturing, or measured boot timing. Parser success establishes syntax and self-consistency only. If an attacker controls both image and digest, the ordinary hash cannot identify an unauthorized image.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 38. ROM verification, corruption detection, and the limits of checksums

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`CRC32(ROM)==header_crc and SHA256(ROM)==header_hash`

**Units and representation:** CRC polynomial, bytes, hexadecimal digests. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Error detection and source authenticity are independent claims. CRC32 is a bounded polynomial remainder optimized for common accidental bit errors; SHA-256 is a cryptographic digest with stronger collision resistance. Recomputing either from the payload only verifies correspondence to the expected value, and that expected value must have its own trustworthy provenance. An archive containing an altered ROM and its matching altered digest can be internally consistent and still be unauthorized or scientifically incorrect.

The AT8 v0.3 decoder first validates the version and total length, then checks both CRC and SHA, and finally runs the inherited `validate_rom` instruction checker. Those steps deliberately fail closed. They protect against truncated images, altered reserved fields, odd instruction counts, unsupported opcodes, invalid branch targets, and inconsistent payload digests. ECC recovery is a separate layer that needs a known expected image digest. Its 13-bit codeword representation does not replace the ordinary image or secretly add bytes to the AT8 ISA.

## Reproduce this investigation offline

Build two valid images for different eight-byte programs and confirm their hashes differ. Corrupt the final payload byte but leave header intact: parser refuses. Now recalculate both CRC and SHA to match the changed payload: a self-consistent image may parse, but **there is still no proof that it came from the authorized creator**. Verify that changing reserved flags or writing a forged header of length 257 causes rejection. Preserve a clear evidence field `secure_boot_signature_verified=False`.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `decode_boot_image, ecc_recover_image_payload`.

## Counterexamples, failure modes, and model scope

CRC32 is not a signature and SHA-256 is not an authorization policy. Authenticity requires separately protected keys and a verified trust chain, revocation rules and physical recovery mechanisms. Publisher citations are likewise not authenticated source-file bytes. None of these controls is physically tested or installed on an actual processor.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 39. Two-slot boot recovery, staged updates, and version monotonicity

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`selected = argmax_generation(committed AND checksum_valid slots)`

**Units and representation:** generation uint32, exact byte images. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An update should not render a known-good boot path unreachable merely because a new image write was interrupted. The illustrative design stores two candidate slots, each with a nonnegative 32-bit generation counter, a complete versioned boot image and a Boolean commit marker. Selection rejects absent, uncommitted, malformed and digest-invalid slots; it selects the highest valid committed generation. If equal-generation slots have different ROM identities, selection refuses ambiguity instead of silently guessing. A new update must have a strictly higher generation than the selected committed version.

The staged model represents three abstract interruption points: before writing new bytes, after writing but before commit, and after commit. Until a new slot is committed and validated, the previous committed slot remains the preferred recovery candidate. A random torn-write pattern is outside this simplified model, so we must not claim real flash atomicity or rollback resistance against a capable attacker. An actual design needs write ordering, durable media guarantees, storage erase semantics, power-failure testing, authentication, secure anti-rollback state and wear limits.

## Reproduce this investigation offline

Start with generation 1 in slot A. Stage generation 2 in slot B and stop after data. The selection remains A. Resume and commit generation 2; the selection becomes B. Stage generation 3 back to A and commit; A becomes the latest. Corrupt the higher-generation payload and confirm the old committed slot is selected again. Attempt a generation-2 update onto generation 3: reject. Construct an equal-generation image conflict: refuse. Record each decision and its reason without asserting it happened to physical memory.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `BootSlot, stage_update, select_boot_slot`.

## Counterexamples, failure modes, and model scope

A mathematical commit Boolean is not an atomic persistent write. Boot selection is not a bootloader implemented in hardware, and no electrical test was performed. There are no authenticated firmware keys, nonvolatile endurance tests, tamper-resistant counters or power-loss waveforms. This is an educational recovery invariant and a checklist for a future real system.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 40. SECDED ROM redundancy, fault injection, and byte-identity restoration

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`extended Hamming(13,8): 1-bit correction, 2-bit detection`

**Units and representation:** 13-bit codewords; eight data bits per codeword. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The prior Computer Architecture v0.2 release already preserves a SECDED(13,8) reference encoding. This edition uses it as a local ROM recovery layer without changing ROM instruction bytes or the ISA. Each 8-bit source byte is mapped to 13 bits using positions 1,2,4,8 for Hamming parity, positions 3,5,6,7,9,10,11,12 for data and position 13 for overall parity. An odd total parity plus a nonzero syndrome identifies a single-bit error in positions 1–12; odd parity plus zero syndrome identifies the overall parity bit; even total parity with nonzero syndrome detects a double-bit corruption. Triple-bit patterns are **not** guaranteed to be detected or corrected.

A recovery pipeline first records the expected complete ROM identity, encodes its bytes and simulates a fault in a specific codeword. It decodes each codeword, rejects known double faults, and independently compares the fully reconstructed ROM's SHA-256 to the trusted expected image. A small coding-theory guarantee does not imply a storage-media failure-rate guarantee; actual SRAM, ROM, flash and radiation faults may be correlated in time and location.

## Reproduce this investigation offline

Take the eight-byte arithmetic ROM in chapter 37. For its first encoded byte, independently toggle each of 13 bits and verify recovery of the original ROM and one corrected word. Exhaust the 78 unordered pairs of bit positions and require every double-bit case to raise an uncorrectable error. Reconstruct the original boot-image digest and reject any result that does not match it. The finite oracle repeats the fault campaign on multiple other ROMs.

**Executable implementation:** `computer_atlas/v03_boot.py`. Public functions: `ecc_encode_image_payload, ecc_recover_image_payload`.

## Counterexamples, failure modes, and model scope

Extended Hamming(13,8) does not guarantee protection against three or more errors, burst corruption, memory address faults, malicious image replacement, ECC decoder faults or bad power supply. The trusted digest must be acquired through a separate authenticated channel for security claims. Physical fault-injection measurements remain an explicit HOLD gate.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 41. Instruction reachability, structural termination, and proof conservatism

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`CFG successors: JMP -> target; JZ/JNZ -> target and fallthrough; HALT -> none`

**Units and representation:** byte-addressed program counters and instruction counts. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

AT8 branches use absolute even ROM byte addresses. The abstract control-flow graph has one node for each decoded two-byte instruction; edges represent every *possible* successor under a conservative interpretation of conditional branches. A JMP has one target, JZ and JNZ have both target and fallthrough, HALT has none, and other instructions use PC+2. An edge that falls beyond ROM is a potential invalid termination, not an implicit HALT. The graph deliberately ignores register values and branches that could be logically infeasible in a particular run.

A reachable directed cycle makes this analysis unable to establish universal termination. It does not prove an infinite execution exists—such loops may be bounded by counter state, as the earlier structured compiler demonstrates. Conversely, an acyclic reachable graph whose every terminal node is HALT gives a bound on normal instruction retirements *provided no execution trap occurs*. This is weaker than a guarantee of successful completion with I/O, because an IN instruction can still trap on an exhausted input tape. Compute the maximum normal path length only for such finite acyclic all-HALT graphs. Unreachable instructions are reported, not deleted.

## Reproduce this investigation offline

For `LDI R0,2; LOOP: ADDI R0,255; JNZ R0, LOOP; HALT`, the graph contains a cycle and must report `cannot_prove_termination`, although actual execution halts after the counter reaches zero. For `LDI; ADDI; OUT; HALT`, it is acyclic with a four-instruction normal bound. A lone NOP has a fallthrough beyond ROM and no HALT, so refuse a normal-termination certificate. Explicitly distinguish reachable PCs from structural dead code after a HALT.

**Executable implementation:** `computer_atlas/v03_control.py`. Public functions: `control_flow_certificate`.

## Counterexamples, failure modes, and model scope

This is conservative static analysis, not SAT/SMT model checking, path sensitization, state-exhaustive proof, or real-time timing qualification. It does not prove absence of all traps, malicious firmware, unbounded physical response time, or liveness of external devices. Keep detailed counterexamples rather than claiming loop-free programs are generally safe.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 42. Compiler-to-ISA verification by three independently motivated semantics

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`compile(source)=ROM; evaluator(source,input)=SpecMachine(ROM,input)=MicrocodedMachine(ROM,input)`

**Units and representation:** AT8 bytes, bounded operation counts, deterministic I/O traces. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The compiler in ATLAS FORGE v0.2 takes a deliberately small structured language: SET/ADD/XOR/AND/OR, STORE/LOAD, IN/OUT, bounded nested REPEAT/END and one terminal HALT. It compiles to the unchanged 16-opcode, two-byte AT8 ISA. Register R0 holds the public accumulator, while registers R3..R1 are reserved for up to three loop counters; the compiler must not silently allocate beyond those registers. A separate source AST evaluator executes statements independently of machine-code decoding. The AT8 atomic specification and four-stage microcycle reference form two additional execution paths.

The engineering invariant is **agreement of observable states**, not merely the same final console number: check HALT status, R0, all 256 RAM bytes, output events in order and input-tape consumption counts. The microcycle model must agree with the atomic model at every instruction retirement. A deterministic receipt records source/ROM/image hashes, input-tape hash, program limits, result digest and the explicit lack of physical hardware evidence. An agreed-upon error in all models can still exist; external source review and independent implementations improve but do not eliminate this risk.

## Reproduce this investigation offline

Compile `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT`. The software models should store 12 in RAM[0], output 15 on port 0 and halt. Compare the AST evaluator's 256-byte memory with the machine's full memory, and confirm the output event list is exactly [(0,15)]. Repeat with IN port 1 receiving [7] and output 9 after adding 2. Refuse missing tape input, unbounded operation budget and unsupported syntax.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_program, evaluate_source, differential_retirement`.

## Counterexamples, failure modes, and model scope

This verified compiler is not a C compiler, linker, operating system, protected memory runtime, or fabricated processor. A content digest proves neither source authorship nor correct physical realization. The original Compiler Design and Operating Systems domains remain separately planned in the 30-domain program; do not inflate this Computer Architecture increment into their completion.

## Source register and rights

Bibliographic record `NAND2TETRIS-PROJECTS` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 43. A minimal job monitor with explicit failure isolation and durable receipts

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`Batch pass = AND_i(valid_software_receipt_i); failures must not be dropped`

**Units and representation:** job counts, deterministic hashes, bounded instruction budgets. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Operating systems eventually provide scheduling, process isolation, I/O and persistent state, but those features cannot simply be assumed in a four-register educational CPU. The AT8 v0.3 batch monitor is therefore an external **software harness** that runs up to eight bounded, independently reset AT8 programs. Every job has a source listing, an optional finite input tape and an instruction budget. The monitor compiles, verifies and executes jobs separately using the three comparison pathways; it records an individual pass or explicit failure record for each.

The batch acceptance condition is an AND of all job statuses. One failed program does not silently disappear because neighboring jobs passed. The monitor continues with remaining jobs to preserve diagnostic evidence, then reports `software_acceptance=False`. It cannot allocate asynchronous process address spaces or preempt a running hardware core; its isolation is achieved by constructing separate Python machine states and bounded execution, not by an MMU. The hashes are deterministic reproducibility receipts, not cryptographic attestations of a physical device.

## Reproduce this investigation offline

Submit two jobs: a finite arithmetic program expected to output 15, and an IN program with no input bytes. The first must carry a verified software receipt; the second must report a failed-closed `ValueError`, and the aggregate must be false. With two valid jobs, the aggregate becomes true. Reorder JSON dictionary keys representing the same input tape and check the canonical digest remains unchanged. Reject unsupported job fields and more than eight submitted jobs.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_job_batch, canonical_json_bytes`.

## Counterexamples, failure modes, and model scope

No OS scheduler, interrupts, privileged mode, memory protection, fault-tolerant physical storage, file system, virtual memory or real concurrency are implemented. Failure isolation within a Python list is not hardware containment. A later Operating Systems Atlas must test true process scheduling and protection on independently characterized hardware or appropriate validated emulation.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 44. Cache lines, address tags, write-through coherence, and memory locality

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`line=floor(address/line_size), index=line mod line_count, tag=floor(address/line_size)`

**Units and representation:** bytes, lines, tags, read hits/misses. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The direct-mapped cache reference introduces one bounded memory-hierarchy mechanism while leaving the AT8 ISA unchanged. A 256-byte RAM is divided into cacheable lines of 4, 8 or 16 bytes. Each access uses an aligned line base and a cache index equal to the line number modulo 2,4,8 or 16 lines. The tag is the corresponding base address. On a read miss the line is fetched from backing RAM; on a hit the cached byte is returned. Writes are **write-through and write-allocate**: backing RAM is updated immediately, and the indexed cache line is either patched or filled from the new RAM state.

The primary invariant is observational coherence for a single logical CPU: every cache read returns the value that would be returned by an immediate read of the backing RAM after the same writes. Two blocks may collide at the same cache index, causing eviction and a future miss. A cache invalidation discards local cached copies, but not backing RAM contents. The independent oracle executes thousands of random address reads/writes against a separate 256-byte array to check correctness even when tags collide repeatedly.

## Reproduce this investigation offline

Start with bytes 0–255 in RAM, an eight-byte line and four cache lines. Read address 0: miss; read address 1: hit; read address 32: conflicts at index 0 and evicts line 0; read address 0 again: miss. Write value 173 at address 14, invalidate the entire cache and read address 14: return 173 from backing RAM. Vary line sizes and line counts and compare against a direct RAM oracle after every operation.

**Executable implementation:** `computer_atlas/v03_cache.py`. Public functions: `SmallRAMCache`.

## Counterexamples, failure modes, and model scope

This is not an implemented transistor SRAM array or a tested FPGA cache. It excludes write buffering, stalls, refill latency, energy, concurrency, DMA, multiprocessor coherence, cache hierarchy, memory consistency, address translation and cache side-channel mitigations. A later software or hardware architecture can use it as an executable policy reference, not a hardware claim.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 45. Instruction atomicity, input tapes, traps and replayable I/O

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`valid instruction -> one committed state transition; trap -> no committed change`

**Units and representation:** instruction retirements, input bytes, output events. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

An instruction-level abstract machine should distinguish a valid execution step from a trap before architectural changes are committed. The existing AT8 model stages register, memory, I/O and program counter changes. If an IN instruction encounters an empty tape, the step traps without consuming input or modifying registers. If a conditional branch targets an invalid address, the fetch/decode contract rejects it. The four-stage microcycle model is compared with the atomic model at instruction retirement boundaries rather than claiming a physical clock rate.

The v0.3 job receipt includes the full observable input consumption, output event order and memory digest. Different input tapes may produce different legitimate outputs; a reproducible evaluation must preserve the exact tape bytes, port indices, and declared execution budget. A watchdog step budget bounds the simulator's work and should return an explicit bounded-stop result or refusal, not claim that an arbitrary source program terminated normally. The machine's `cycles` represent retired abstract instructions. A four-stage `microticks` count does not encode transistor path delay.

## Reproduce this investigation offline

For `IN R0, 1; ADDI R0, 2; OUT R0, 2; HALT`, a tape [7] on input port 1 yields [(2,9)] and advances cursor 1 by exactly one. With an empty tape, input exhaustion is a trap; compare pre- and post-state for equality. Audit the staged microcycle COMMIT events to ensure a trap does not mutate the architectural state. Repeat from a fresh machine instance and compare output and state digests.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `SpecMachine, MicrocodedMachine, differential_retirement`.

## Counterexamples, failure modes, and model scope

No physical port peripheral, bus, synchronizer, interrupt controller, DMA, I/O timing or system-call boundary is implemented. A deterministic event tape is a software reference, not equipment measurement or a real-time interaction certificate. Signed data origin and input authorization remain separate requirements.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 46. Byte-exact release replay, checkpoint identity and software evidence chains

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`receipt=SHA256(canonical JSON excluding own receipt field); replay results must agree`

**Units and representation:** SHA256 hashes, archive byte identities, immutable revisions. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

Long-term reconstructibility requires more than saving the last program. A release chain should preserve the exact predecessor archive hash, the direct incremental delta, all changed-member hashes, the complete resulting source manifest and a tested recovery script. The release's canonical checkpoint must identify the same revisioned state that its archive reconstructs. The AT8 boot workflow likewise hashes the source bytes, encoded ROM bytes, canonical boot image and canonical serialized input-tape mapping, then records the deterministic state and output digests. The receipt does not include its own hash while calculating its SHA-256, preventing a circular definition.

A replay is successful when a second fresh process recovers exactly the same ROM and observable result under the same bounded inputs, and independently checks its file hashes. Byte equality does not establish scientific truth, security authorization, correct license, fabricated hardware or independent peer review. A recovered file with the wrong registered original identity must be rejected even if it executes. Only an independently trusted publisher signature or other attestation could add authorship confidence.

## Reproduce this investigation offline

Hash the source listing and its assembled ROM, build the version-3 header, and record the empty or explicit input tapes with stable key ordering. Re-execute in an isolated Python interpreter, verify the receipt SHA-256, then deliberately reorder the dictionary keys and confirm canonical input identity is stable. Change one source byte and observe its source SHA change. Run an interrupted dual-slot update and preserve the original slot when the candidate did not commit.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_program, canonical_json_bytes`.

## Counterexamples, failure modes, and model scope

Python and zlib versions may affect ZIP compression and exact full ZIP byte hashes; raw source-file hashes can still prove file equivalence independently. Do not silently claim byte-exact restoration without checking actual target ZIP SHA. Publisher-original full PDFs were not imported into this release; their source cards remain citation/navigation only.

## Source register and rights

Bibliographic record `NIST-800193` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 47. Physical measurement requirements for a trusted booting computer

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`hardware_acceptance = AND(material, device, gate, clock, memory, boot, independent_trace)`

**Units and representation:** SI voltage, time, temperature, geometry and verification receipts. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The original Manufacturing and Electronics nodes provide a technical dependency chain for a computer, but a simulation cannot certify that silicon or discrete gates were fabricated. The minimum evidence groups include material identity, wafer or substrate characterization, transistor I–V and C–V, dielectric and contact metrology, gate transfer and timing across process/voltage/temperature, clock/reset integrity, physical memory retention, power/thermal behavior, layout/interconnect records, manufacturing receipts and independent execution traces. No physical evidence types are declared verified just because a JSON object asserts them. The `physical_evidence_matrix` explicitly returns all twelve types as unverified and six staged goals as blocked.

To advance, an independent laboratory or qualified practitioner must publish exact device identifiers, instrument calibration certificates and raw measurements. For firmware resilience, protection/detection/recovery is a useful high-level framework, but adding an unsigned CRC header alone does not implement NIST SP 800-193's protection controls. A real trusted boot would need cryptographic trust anchors, signature verification, rollback authorization, persistent storage semantics, power loss fault tests and physical attack-surface assessment. The abstract two-slot reference is a tool for documenting questions, not evidence those controls exist.

## Reproduce this investigation offline

Execute the AT8 source program through the independent software models, then query the physical evidence matrix. The software section produces a reproducible ROM/result digest. The physical section lists twelve missing evidence types and a HOLD status even when supplied a metadata mapping with all twelve keys set True. This distinguishes *a claim that someone observed a device* from *an independently validated measurement record*. Build the empty measurement dossier for future silicon or discrete-logic experiments.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `physical_evidence_matrix`.

## Counterexamples, failure modes, and model scope

No hardware processor, physical ROM boot, cryptographic authentication root, chip fabrication, device calibration, controlled timing corner, electrical safety approval or external peer review is established by this release. Even full functional software equivalence cannot substitute for those experiments. Explicit uncertainty preserves scientific credibility.

## Source register and rights

Bibliographic record `MIT-6004-2009` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---

# 48. Full-stack reconstruction ladder: from source program to trustworthy physical system

**ATLAS FORGE — Original canonical federation / Computer Architecture & Digital Hardware v0.3.0**

**Scientific/evidence classification:** original reconstruction synthesis, bounded deterministic software implementations, and independently coded finite oracles. Original publisher document transport, qualified independent scientific review, physical CPU production, and calibrated silicon measurements are not established.


## Why this matters for reconstruction

A future human or AI must be able to distinguish the contract of a small computer from the assumptions hidden in its implementation. This chapter records the exact mathematical or state-transition invariant, executable reference, expected counterexamples and missing physical evidence. It forms part of the same original ATLAS FORGE federation rather than a separate product.

## Governing equation or state transition

`source→compiler→ISA ROM→boot image→ECC→boot slot→CPU models→receipt→physical evidence gate`

**Units and representation:** AT8 bytes, bounded run budgets, explicit evidence-state labels. Original AT8 architecture remains sixteen opcode types, four 8-bit registers, 256 bytes each of ROM and RAM, two bytes per instruction and a bounded external input/output tape.

## Derivation and engineering principles

The strategic purpose of the Computer Architecture node is to preserve an independently rebuildable chain: digital logic and state → instruction semantics → assembler and compiler → versioned program image → reset/boot contract → execution trace → reproducible toolchain → operating system and scientific computation. AT8 v0.3 demonstrates a **bounded software vertical slice** of this chain without introducing a new ISA, Bitwork router, data service, general compiler or hardware fabrication claim.

The recommended reconstruction order is (1) verify source-code archive hashes and a known Python reference runtime; (2) run exact NAND/ALU truth tables and the 16-opcode AT8 reference; (3) compile the small structured language into a 2–256-byte aligned ROM; (4) generate and independently parse the fixed-header boot image; (5) optionally protect ROM bytes using SECDED and simulate a limited fault campaign; (6) stage a candidate into the dual-slot reference and select the latest valid committed image; (7) run the separate source AST, atomic machine and microcycle machine under identical finite input tapes; (8) record canonical receipts and compare the full observable memory/output state; (9) identify every missing physical prerequisite through the manufacturing evidence matrix. Each step is independently fail-closed.

The next true **Compiler Design** and **Operating Systems** domain nodes will need syntax, type, linking, procedure calls, stacks, object format, memory allocation, interrupts, multiple processes, system calls, I/O drivers, boot ROM and portable runtime semantics. The AT8 machine lacks a general CALL/RET and data-driven jump architecture, so a true nested call stack or preemptive operating system cannot be implemented faithfully without an explicit ISA extension. Do not pretend a host-side batch monitor solves these missing architectural capabilities. Preserve this limitation as part of the technological-continuity roadmap, not a defect to conceal.

## Reproduce this investigation offline

Start with two valid and one invalid AT8 structured program. Produce a source, ROM and image hash for each. Verify the two valid programs against three execution pathways and their expected output. Let the invalid program attempt missing port input; require an explicit failure while the remaining jobs still receive their receipts. Run the dual-slot interrupted update experiment, ECC correction campaign and the manufacturing physical-gate review. Reproduce all files and program traces on a clean computer from the immutable Atlas archive chain.

**Executable implementation:** `computer_atlas/v03_workflow.py`. Public functions: `verify_program, verify_job_batch, select_boot_slot`.

## Counterexamples, failure modes, and model scope

This is **not** a proven operating system, physical bootloader, authenticated secure boot, manufactured CPU or complete compiler toolchain. Nand2Tetris and MIT provide useful prior art; ATLAS FORGE has not demonstrated a new scientific law or an unprecedented computer ISA. Its contribution is structured, versioned, independently replayable reconstruction evidence, which must be evaluated against existing workflows.

## Source register and rights

Bibliographic record `NAND2TETRIS-PROJECTS` refers to an official publisher or course navigation page. Source identity is a locator, **not an authenticated locally retained publisher PDF** and not an assertion of licensing permission to redistribute that publication. The mathematical reconstruction, examples, and code in this Atlas chapter are newly authored. Independent external review and physical device measurement remain open gates.

## Exact federation dependencies

Earlier Computer Architecture v0.1 and v0.2 chapters retain byte-identical record revisions. Mathematical, Electronics, Manufacturing, Measurement, Computation and Energy nodes provide prerequisites. Cross-node links navigate exact versions, not proof of physical hardware. The canonical 30-domain queue is unchanged; Compiler Design and Operating Systems remain future domain work.


---



---

# Edition 0.4 — NAND datapath, bus and bootstrap refinement (Chapters 49–60)

# Chapter 49 — A reconstructible NAND netlist from the Boolean adder

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Reconstruction question
Can the Boolean ALU function be expressed as an explicit, finite, independently replayable gate network, rather than only Python integer arithmetic? A reproducible gate netlist requires a precise cell primitive, a unique signal name for every output, acyclic dependencies, and a fixed set of primary inputs/outputs.

## Derivation and construction
NAND(a,b)=NOT(a AND b) forms a functionally complete basis. Define n0=NAND(a,b), n1=NAND(a,n0), n2=NAND(b,n0), and x=NAND(n1,n2), so x=a XOR b. Set n3=NAND(x,carry), n4=NAND(x,n3), n5=NAND(carry,n3), sum=NAND(n4,n5), and next_carry=NAND(n0,n3). The nine-gate full-adder outputs satisfy sum+2 next_carry=a+b+carry for every input triple. Chain w such stages, passing the carry to the next lower-to-higher bit position, to implement unsigned addition modulo 2^w with an explicit carry-out.

The original AT8 v0.1 instruction format is left completely unchanged. The gate network supplies one possible implementation of the arithmetic function, not a new instruction-set architecture or a verified transistor layout.

## Reconstructible case
Build an 8-bit ripple netlist with 72 NAND instances. Apply a=255, b=1, c_in=0; the result is 0 with carry 1. Record the canonical sorted-key JSON netlist and SHA-256. A second process regenerates the same graph and digest. Exhaust the 65,536 possible pairs of 8-bit values and independently compare output against Python's native integer arithmetic; this shows finite functional equivalence under the stated Boolean semantics.

## Failure and fabrication boundaries
A correct netlist is not synthesizable physical RTL without clocking and cell mapping constraints. NAND count is not transistor count, die area, critical-path delay, or power consumption. No minimum voltage, fan-out capacity, source current, analog transition shape, process corner or timing library has been characterized. The graph parser rejects unknown wires, duplicate names, feedback introduced as a forward reference, nonbinary inputs and unsupported sizes. This rejection is part of the knowledge to preserve.

## Equation, implementation, and provenance

- **Key relation:** `s=a XOR b XOR c; cout=(ab) OR (c(a XOR b))`.
- **Reference algorithm:** `v04_gatelevel.ripple_adder_netlist; NandCircuit.eval`.
- **Units:** bits, NAND counts and structural gate levels.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 50 — Unknown-state propagation without invented register certainty

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Scientific question
What should a digital reconstruction report when a signal has not been shown to carry a valid binary voltage? Returning zero by default would silently hide uncertainty. A stronger reference uses the three-value set {0,1,X}, where X means a bit cannot be determined under the available logical information.

## Conservative logic
NAND has one useful forcing input: if either input is definitely zero, the output is definitely one, even if the other input is unknown. With both inputs definitely one, the output is zero; otherwise return X. This is a partial-information interpretation of Boolean NAND, not a probabilistic model of a transistor. It does not calculate whether a metastable latch resolves at a particular time. A known Boolean reconvergence can remain X in this simple calculus because it does not use relational constraints between unknown signals.

## Worked case
For a=0 and b=X, NAND is definitely 1. For a=1 and b=X, NAND is X. For a=b=1, it is 0. Feed these into an explicit one-bit full-adder netlist; the unknown can propagate through the carry path while specific outputs may remain determined when a forcing constant exists. Test all nine combinations of the three-valued inputs and require the interpreter to reject True/False booleans, strings and floating-point approximations as invalid logical encodings.

## Limits
A three-valued simulation does not guarantee physical safety. Hazards, simultaneous switching, metastability, analog thresholds, glitches, unknown-resolution times, static noise margin, race conditions, crosstalk and clock skew require different models and calibrated observations. For real devices, the Electronics node's voltage-noise windows and timing chapters are prerequisites. An X value is an epistemic indicator, not a new physical particle or discovery.

## Equation, implementation, and provenance

- **Key relation:** `NAND(0,X)=1; NAND(1,X)=X; NAND(X,X)=X`.
- **Reference algorithm:** `v04_gatelevel.nand3; NandCircuit.eval`.
- **Units:** 0, 1 and X (UNKNOWN, symbolic).
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 51 — NAND arithmetic, unsigned carry, and subtraction borrow conventions

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Arithmetic contracts
For a w-bit datapath the result is an unsigned integer in [0,2^w−1], with a carry-out bit encoding the high bit of the sum. The identity a+b+c_in=sum+2^w carry_out holds for every bounded input. Subtraction is implemented by complementing each bit of b and injecting carry_in=1, giving a+(2^w−1−b)+1. The final carry after subtraction is one exactly when unsigned a≥b: it represents **no borrow**, not borrow.

The first integer-width extension uses the same NAND network, not Python arithmetic inside the circuit interpreter. A separate independent oracle calculates ordinary integers and compares them, including edge values and wraps. The netlist has 9w gates for addition, and 10w for subtraction when each b bit is inverted via NAND(b,b).

## Worked cases
For w=8, a=255,b=1, addition yields result 0, carry 1. For a=0,b=1, subtraction yields result 255, carry 0. For a=b=127, subtraction yields zero and carry 1. All 65,536 pairs of 8-bit operands can be tested against an independent integer oracle for addition and again for subtraction. This finite exhaustive check is stronger than a collection of hand-selected examples, but it remains limited to the eight-bit abstract function.

## Signed arithmetic and handoff
Two's-complement overflow is different from carry; e.g. 127+1 overflows signed 8-bit range without an unsigned carry. AT8 flags must maintain the existing published semantics for ADDI and CMP. The Computer Architecture v0.1 ISA must not be extended or silently reinterpreted as RISC-V or the MIT Beta ISA. A hardware implementation would also require gate fan-out, timing, reset and interconnect constraints absent here.

## Equation, implementation, and provenance

- **Key relation:** `a+b+c_in = sum + (2^w) carry_out; a-b=a+(NOT b)+1 (mod 2^w)`.
- **Reference algorithm:** `v04_gatelevel.evaluate_add; computer_atlas.gates.alu8`.
- **Units:** binary words, carry and signed overflow flags.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 52 — Verifying gate arithmetic at each AT8 instruction retirement

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Refinement obligation
A computer can be modeled at several abstraction levels. The ISA specification defines architectural state transitions, a microcycle engine stages their implementation, and a Boolean datapath implements arithmetic expressions. A meaningful consistency check compares the externally visible committed state after each instruction, not just a final program output. A precise trap must leave the previous committed state unchanged.

The original AT8 exposes ADDI and CMP. At each such retirement, sample the pre-instruction register and immediate operand. The new NAND-only datapath calculates addition or complement-plus-one subtraction. Compare its result and carry with the existing atomic ISA state after the instruction. Then compare atomic and microcycle snapshots using the predecessor edition's differential retirement verifier. Do not modify original interpretation of reserved registers, flags or program-counter alignment.

## Worked execution
`LDI R0,255; ADDI R0,1; CMP R0,0; HALT` includes wraparound and comparison. The NAND adder must produce result zero with carry one on ADDI, and the comparator must not modify R0. A second program compiled from `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT` is verified from source AST to ROM, boot payload, atomic/microcycle execution and NAND arithmetic. Its output event is port 0, byte 15.

## Safety and scope
If either implementation traps, fails to halt within a bounded budget, or disagrees, return HOLD. Do not manufacture a successful refinement receipt after a failure. Testing finite programs does not prove all future programs are correct, and correctness of the simulated datapath does not demonstrate any CMOS implementation. Real silicon equivalence additionally needs gate-level RTL/netlist extraction, characterized timing, reset behavior, scan or formal validation and measured I/O.

## Equation, implementation, and provenance

- **Key relation:** `Refinement: GateResult(operand,immediate) = ISAResult(operand,immediate)`.
- **Reference algorithm:** `v04_gatelevel.certify_at8_arithmetic; v02_trace.differential_retirement`.
- **Units:** byte values and instruction retirement indexes.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 53 — Structural gate depth and hypothetical timing envelopes

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## From logic to timing, carefully
The logic graph defines a partial ordering among gates. If each NAND gate is assigned a positive delay interval [d_min,d_max], dynamic programming can propagate possible earliest and latest arrival times through an acyclic graph. At a gate, its earliest possible output response is bounded by the first input change plus the minimum assumed delay, while the latest possible response is bounded by the latest predecessor change plus the maximum assumed delay. These are **structural envelopes**, not sensitized timing paths proven under concrete input transitions.

For a homogeneous gate-delay abstraction with zero wiring delay, the longest path of D NAND levels has upper delay D d_max. The registered path must additionally include clock-to-Q, wire, setup/hold and uncertainty. Physical interconnect, loading and gate input slew can invalidate the single-delay assumption; the envelope must be relabeled hypothetical unless measured parameters are supplied.

## Worked case
Construct a one-bit full adder and an eight-bit ripple chain. Record the deterministic structural depth from the NAND graph. Set synthetic d_min=1 ps and d_max=3 ps, and calculate possible arrival envelopes. Repeat with twice the assumed maximum gate delay and observe the linear scaling. This is an exercise in dimensional reasoning, not a fabricated processor frequency estimate.

## Counterexamples
Reconvergent paths and glitches can cause output transitions not represented by a simple longest-path arrival summary. Fan-out changes effective load; uncharacterized wire lengths add propagation and RC delay; metastability violates a simple bounded binary timing model. The original Electronics timing material documents these caveats. An honest report retains both gate-function proof and independent physical timing HOLD gates.

## Equation, implementation, and provenance

- **Key relation:** `t_latest <= depth_max * t_gate,max (zero interconnect assumption)`.
- **Reference algorithm:** `NandCircuit.structural_depth; NandCircuit.gate_delay_bounds`.
- **Units:** NAND levels, seconds, declared min and max gate delays.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 54 — Harvard ROM/RAM separation and addressing boundaries

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Memory separation as an architectural invariant
AT8 is an educational Harvard machine: program ROM is immutable during normal execution and is stored separately from 256 bytes of writable data memory. The program counter addresses fixed two-byte instructions and must be even. RAM read and write addresses are byte indexes. The ISA also exposes four abstract input and output ports; these are **not** memory-mapped I/O and may not be silently reinterpreted as such.

The new reference bus provides distinct `fetch`, `read`, and `write` entry points. A ROM write is refused. All operations validate types and bounds before modifying memory; an out-of-range address must not cause a partial write or trace event. The transcript can be deterministically serialized to JSON and hashed, but a hash proves only internal consistency if its expected digest is anchored elsewhere.

## Worked case
Assemble `LDI R0,1; HALT`, fetch the first two ROM bytes at PC=0, write byte 255 at RAM address 0, and read back the same value. An odd PC=1 or RAM address 256 is rejected. Compare the transcript SHA-256 from two independent fresh runs with identical inputs. Deliberately request a ROM modification to demonstrate that the architecture has no such instruction.

## Verification boundary
A simulated read-only ROM cannot establish flash write protection or secure boot. Real hardware needs memory isolation, power/clock sequencing, permission logic, bus arbitration and timing measurements. The source-to-boot chain should retain provenance, a known trusted hash or signature, and measured device access traces before claiming that these abstractions correspond to physical components.

## Equation, implementation, and provenance

- **Key relation:** `ROM fetch PC even, 0<=PC+1<ROMlength; RAM 0<=address<256`.
- **Reference algorithm:** `v04_memory.HarvardBus; isa.validate_rom`.
- **Units:** bytes, addresses and transaction events.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 55 — Parity byte memory: detection, correction limits, and false confidence

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Finite detection theorem
A single even-parity bit is the XOR of all data bits. If an odd number of data bits flip but the stored parity bit remains unchanged, the observed parity differs and the detector flags an error. If an even number of data bits flip, parity remains consistent and the error can be undetected. The detector does not repair the data, identify which bit flipped or prove that the stored byte is authentic.

This is distinct from the predecessor's extended Hamming (13,8) ROM scheme, which provides a defined single-error-correct/double-error-detect guarantee under its codeword model. Neither code is a cryptographic authentication scheme, nor does either establish a physical bit-error rate.

## Counterexample
Write byte zero with even parity. Flip data bit 0: parity reports an error and returns UNKNOWN instead of a guessed byte. Reset the memory; flip bits 0 and 1 together. The resulting byte is 3 but has even parity, so the detector reports *parity consistent*, even though the data differs from the original. An evidence system that labels the second read as 'correct' would be making a false claim.

## Reconstruction controls
Keep injection masks and parity-bit faults as explicit trace events. Test all eight single-bit flips and at least one two-bit counterexample for every byte value. Separate `detected` from `corrected` and label unknown states. Manufacturing acceptance requires physical cell retention measurements, radiation/error-injection characterization, power-failure testing, measured ECC overhead, and independently validated operating limits.

## Equation, implementation, and provenance

- **Key relation:** `parity(byte) = popcount(byte) mod 2; parity(data xor mask) differs iff popcount(mask) odd`.
- **Reference algorithm:** `v04_memory.ParityByteMemory; v02_ecc.protect_rom`.
- **Units:** byte and parity bits.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 56 — Finite fair bus arbitration and its assumptions

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Causal arbitration model
When multiple masters compete for a shared bus, an explicit rule is required to select a winner. The simple round-robin arbiter rotates a pointer to one position after the last granted master. On every abstract arbitration cycle it grants the first requesting master encountered while traversing the master IDs modulo N. If none request, it grants no one and does not invent an access.

Under the assumptions that requests are sampled each cycle, a ready master remains requesting, and the arbiter is never reset or stalled, each continuously requesting master gets service within at most N arbitrations. This is **conditional fairness**. It does not prove bounded service under priority resets, hardware starvation, preemption, malformed requests, or clock-domain crossing.

## Worked case
For three masters all continuously requesting, the grant sequence is 0,1,2,0,1,2... . If only master 1 requests, it may be repeatedly granted, independent of the pointer. The reference returns `None` when nobody requests. Exhaust across N from two to eleven, and test boolean/type rejection to avoid accidentally treating Python `True` as an unsigned binary request.

## Interfaces to architecture
AT8 v0.1 does not have DMA or a multi-master architectural bus. This is a separate component-level research model, not an ISA extension. Before implementation in hardware, a bus designer must specify request/acknowledge timing, clock-domain boundaries, stalls, reset, error response, arbitration metadata, and fairness assumptions. The Electronics and Manufacturing nodes contain prerequisite timing and measurement evidence rules.

## Equation, implementation, and provenance

- **Key relation:** `grant_t = first requesting master at/after pointer_t (mod N)`.
- **Reference algorithm:** `v04_memory.RoundRobinArbiter`.
- **Units:** clock-indexed binary requests and master identifiers.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 57 — Source-to-boot reproduction and explicit trust boundaries

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Reconstructible end-to-end contract
A compiler bootstrap demonstration should connect source text to exact machine bytes and observable execution. The previous structured-language compiler translates a bounded language into an unchanged AT8/0.1 ROM. The canonical assembler/disassembler round-trip is checked for byte identity. The v0.3 AT8R/3 boot image wraps the ROM in a header with CRC32 and SHA-256. The image is decoded and selected through the simulated A/B boot mechanism. Finally, the structured-source AST evaluator, atomic ISA engine, microcycle interpreter and NAND arithmetic datapath must agree on the defined finite test case.

The release certificate records distinct SHA-256 values for source text, canonical assembly, ROM and boot image. They are deliberately not conflated. A receipt also stores output events, final RAM digest and NAND netlist hash. Re-running the same inputs must reproduce the same certificate bytes, including a final receipt hash computed from a canonical serialization of all other fields.

## Worked case
Compile `SET 5; ADD 7; STORE 0; XOR 3; OUT 0; HALT`. The resulting program stores twelve, produces the output byte fifteen on port zero, and halts. Retire it under both processor implementations; verify the ADDI path through the explicit NAND circuit. Then modify `SET 5` to `SET 6` and demonstrate that the source and ROM digests change.

## Security and physical boundaries
CRC32 detects some accidental corruptions; SHA-256 supports content identity if a trusted expected digest exists. Neither is a digital signature or an authenticated boot root. The A/B update is a simulated state transition, not evidence of flash atomicity under loss of power. NIST SP 800-193 discusses protective/detective/recovery properties of platform firmware; this candidate does not assert conformance. Required future evidence includes an authenticated key infrastructure, measured boot ROM behavior, real physical write-protection and independent verification.

## Equation, implementation, and provenance

- **Key relation:** `H_source=SHA256(UTF8 source); H_ROM=SHA256(compile(source)); H_image=SHA256(boot_image)`.
- **Reference algorithm:** `v04_bootstrap.bootstrap_certificate; v03_boot.encode_boot_image`.
- **Units:** UTF-8 bytes, ROM bytes, hashes and execution events.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 58 — Finite refinement receipts and fail-closed test batches

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Evidence proposition
Two implementations agreeing is useful but not sufficient to prove either correct. ATLAS FORGE's layered finite checks compare an independent structured-source evaluator, ISA reference, microcycle model and NAND arithmetic netlist. Disagreement is reported with explicit trace context. Successful finite cases are recorded as machine-readable claims with hashes and bounded input domains.

A batch runner should never report success for the entire collection simply because some programs finished. Each job receives a separate receipt indicating `passed` or `failed_closed`, and the batch status is the logical AND of these statuses. Unsupported instructions, exhausted input, program traps, nonterminating loops under the configured bound, and inconsistent outputs all become failures or HOLD—not omitted or substituted with invented traces.

## Worked challenge
Run a valid source-to-boot program, an invalid source program with an unrecognized operation, and a second valid program. The middle failure must be isolated and visible while the first and third receipts retain their own hashes. Re-run to compare canonical output. Then supply an intentionally infinite loop to the arithmetic refinement verifier and verify it returns HOLD rather than claiming all instructions were checked.

## Scientific caution
The independence here is algorithmic and finite; the same researchers wrote the test code, and a qualified external auditor has not signed it. Test fixtures cannot establish arbitrary program equivalence, computational complexity bounds, physical CPU behavior or secure execution. A published receipt's SHA-256 also does not establish author identity absent an authenticated trust anchor.

## Equation, implementation, and provenance

- **Key relation:** `expected_state = ISA(ROM,inputs) = microcycle(ROM,inputs) for retired steps`.
- **Reference algorithm:** `v04_bootstrap.verify_boot_batch; v02_trace.differential_retirement`.
- **Units:** instruction count, trace hashes and binary outputs.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 59 — Manufacturing evidence required to move from NAND models to physical processors

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Physical dependency ladder
The knowledge necessary to construct a physical computer spans materials, devices, fabricated gates, storage, clocks, interconnect and the full machine's observable behavior. A symbolic NAND netlist provides logic but no transistor-level electrical implementation. The Electronics Atlas models capacitance, MOSFET current, timing windows and memory retention under explicit approximations. The Manufacturing Atlas provides process dependencies, metrology, sample-size uncertainties, process capability and evidence gates. These must be linked by exact revisions, not assumed as already measured.

A plausible acceptance process must acquire independent physical evidence for material identity, geometry and doping, dielectric/oxide properties, transistor I–V/C–V across corners, gate transfer, delay and noise margins, clock/reset behavior, memory read/write retention, actual boot ROM programming, power integrity, thermal performance, and hardware instruction traces. Record instrument serials, calibration, raw samples, uncertainty, fixture layout, transport hashes and independently adjudicated negative results.

## Challenge and missing proof
The existing manufacturing-to-computer challenge can execute an AT8 software program and identify which of these physical evidence types are missing. A future laboratory may provide data for those stages, but a self-authored string like `calibrated=True`, a matching SHA-256 for user-provided metadata or a numerical test log is not a calibrated transistor measurement. Do not allow metadata assertions to automatically clear physical acceptance gates.

## Falsification and release gate
A valid gate-level NAND computation that fails measured voltage margins, measured setup/hold or ECC data retention is a failed physical reconstruction despite passing all software tests. Distinguish computational correctness, document provenance, physical observation and independent scientific acceptance in the final ledger. No fabricated processor, certified PDK or secure boot firmware is claimed by this v0.4 edition.

## Equation, implementation, and provenance

- **Key relation:** `hardware acceptance requires calibrated electrical, timing, retention and manufacturing evidence`.
- **Reference algorithm:** `v04_gatelevel.gate_delay_bounds; manufacturing_atlas v0.2 evidence lattice`.
- **Units:** volts, amps, seconds, Kelvin, geometry and uncertainties.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.


---

# Chapter 60 — Reconstructible computing runtime: what still separates AT8 from a general machine

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Technological continuity is a chain, not a single file
An independently reconstructible machine requires an end-to-end dependency graph. Starting from material science and electrical calibration, a manufacturer must produce reliable transistors and memory, combine them into gates and sequential logic, implement a verified ISA, provide a source-to-ROM build chain, and execute bounded diagnostic programs. An operating system introduces interrupts, processes, persistent storage, isolation and resource scheduling. An AI runtime additionally needs numeric kernels, model serialization, memory management, evaluation datasets and power/thermal controls.

AT8 currently provides a small original educational ISA, a constrained compiler, a boot-image format, atomic/microcycle reference models, software cache/bus simulations, arithmetic netlist proofs and reproducibility receipts. None of these implement a physical CPU, robust operating system, instruction pipeline with characterized hazards, memory protection or general model inference. The architecture must remain clear on exactly which link of the reconstruction chain each artifact verifies.

## Finite vertical slice
Take a bounded structured program, compile it to a fixed two-byte AT8 ROM, roundtrip its canonical assembly, encode and decode a versioned boot image, run it under independent source/ISA/microcycle models, check every ADDI/CMP against explicit NAND gates, and produce a deterministic receipt. Verify the output byte trace and RAM SHA-256. In a parallel manufacturing-evidence graph, mark all physical stages as HOLD until actual calibrated measurements are supplied.

## Next scope
The next iteration toward Computer Architecture scoped v1 should develop an independent gate/register-transfer implementation and documented synthesizable HDL, an assembler/linker and minimal boot/test runtime, bounded error handling, formal state invariants, simulation against external references, and hardware measurement acquisition. Only then should a human claim working physical reconstruction. ATLAS FORGE continues as one versioned federation; the original thirty-domain roadmap remains unmodified, and Bitwork routing follows completion of domain knowledge.

## Equation, implementation, and provenance

- **Key relation:** `scientific equations -> fabricated gates -> working memory -> ISA -> tools -> runtime -> AI workload`.
- **Reference algorithm:** `v04_bootstrap.bootstrap_certificate; v04_memory.HarvardBus`.
- **Units:** program bytes, states, timestamps, source evidence and calibrated instruments.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
