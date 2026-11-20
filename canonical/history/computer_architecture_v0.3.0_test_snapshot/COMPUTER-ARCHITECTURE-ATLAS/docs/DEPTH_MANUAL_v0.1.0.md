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

