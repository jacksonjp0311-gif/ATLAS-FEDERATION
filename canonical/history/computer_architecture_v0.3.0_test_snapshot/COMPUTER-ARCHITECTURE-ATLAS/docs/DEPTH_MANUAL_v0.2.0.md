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

