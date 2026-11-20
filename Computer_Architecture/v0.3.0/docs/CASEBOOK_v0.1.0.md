# ATLAS FORGE — AT8 RECONSTRUCTION CASEBOOK v0.1.0

**18 constructed test cases, not measured physical experiments.** AT8 is an original 8-bit educational architecture inside the canonical ATLAS FORGE federation. Expected values must be independently reproduced and compared with source/model boundary conditions.

## Case 01_isa_encoding: 2-byte encoding

**Inputs/fixture:** `LDI R0,5; HALT`.

**Expected observable result:** `1005f000`.

**Independent test condition:** Bytes high nibble=opcode; low nibble=register. Reserved bits and length rejected.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 02_labels_branches: two-pass symbolic assembly

**Inputs/fixture:** `LDI R0,3; LOOP: OUT R0,0; ADDI R0,255; JNZ R0,LOOP; HALT`.

**Expected observable result:** `None`.

**Independent test condition:** Assembler resolves LOOP to byte address 2; output is 3,2,1.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 03_unsigned_arithmetic: unsigned 8-bit wrap

**Inputs/fixture:** `255 + 1 modulo 256`.

**Expected observable result:** `0`.

**Independent test condition:** Result 0 and carry 1, no signed overflow.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 04_signed_overflow: signed two’s-complement overflow

**Inputs/fixture:** `127 + 1`.

**Expected observable result:** `128`.

**Independent test condition:** 8-bit result=128, negative=1, overflow=1, carry=0.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 05_nand_full_adder: NAND-only circuit

**Inputs/fixture:** `all 8 a,b,carry combinations`.

**Expected observable result:** `8`.

**Independent test condition:** Every truth table satisfies s + 2cout = a + b + carry.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 06_store_load: register-to-RAM-to-register

**Inputs/fixture:** `LDI R3,77; STORE R3,200; LOAD R2,200; HALT`.

**Expected observable result:** `77`.

**Independent test condition:** RAM[200]=R2=77 and ROM remains immutable.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 07_independent_execution: microcoded vs atomic spec

**Inputs/fixture:** `
    LDI R0, 5
    ADDI R0, 7
    STORE R0, 0
    XORI R0, 3
    OUT R0, 0
    HALT
`.

**Expected observable result:** `15`.

**Independent test condition:** Two execution models have identical architectural snapshots after every commit.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 08_io_tapes: deterministic input and output

**Inputs/fixture:** `
    IN R1, 1
    ADDI R1, 2
    STORE R1, 4
    LOAD R3, 4
    OUT R3, 2
    HALT
`.

**Expected observable result:** `9`.

**Independent test condition:** Input tape {port 1:[7]} -> output {port 2:9}, one input consumed.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 09_exhausted_input: input exhaustion trap

**Inputs/fixture:** `IN R0,0; HALT`.

**Expected observable result:** `input_exhausted`.

**Independent test condition:** No register, RAM, flag, PC, cursor or I/O mutation.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 10_countdown: bounded branch loop

**Inputs/fixture:** `
    LDI R0, 3
loop:
    OUT R0, 0
    ADDI R0, 255 ; decrement modulo 256
    JNZ R0, loop
    HALT
`.

**Expected observable result:** `(3, 2, 1)`.

**Independent test condition:** Output port 0 events 3,2,1 in order; halts.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 11_infinite_program: bounded non-halting program

**Inputs/fixture:** `JMP 0`.

**Expected observable result:** `bounded_step_budget`.

**Independent test condition:** Run returns non-halted after supplied finite instruction budget.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 12_malformed_rom: reserved-byte rejection

**Inputs/fixture:** `F0 01`.

**Expected observable result:** `illegal`.

**Independent test condition:** Nonzero reserved HALT operand refused before execution.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 13_unaligned_branch: branch target alignment

**Inputs/fixture:** `JMP 3`.

**Expected observable result:** `illegal`.

**Independent test condition:** Odd byte address refused by assembler and ROM validator.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 14_reset_vector: deterministic power-on reset

**Inputs/fixture:** `PC=0, R0..R3=0, 256 RAM bytes=0`.

**Expected observable result:** `0`.

**Independent test condition:** No physical power-on reset, SRAM retention or clock is modeled.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 15_flag_contract: CMP updates flags without changing selected register

**Inputs/fixture:** `LDI R0,5; CMP R0,5; HALT`.

**Expected observable result:** `5`.

**Independent test condition:** CMP Z=1 but R0 remains 5; JZ still tests register, not flag.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 16_program_roundtrip: disassembler/assembler byte identity

**Inputs/fixture:** `assemble(disassemble(binary))`.

**Expected observable result:** `True`.

**Independent test condition:** Round-trip preserves exact ROM byte sequence for valid images.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 17_manufacturing_handoff: evidence-gated physical reconstruction

**Inputs/fixture:** `six process steps, 12 evidence types missing`.

**Expected observable result:** `12`.

**Independent test condition:** Software succeeds while manufactured CPU status remains HOLD.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

## Case 18_source_fidelity: source card vs authenticated primary file

**Inputs/fixture:** `six bibliographic cards`.

**Expected observable result:** `0`.

**Independent test condition:** No original publisher technical bytes authenticated or certified by a reviewer.

**Evidence:** constructed executable software example, not a physical processor experiment. Exact expected behavior is documented by the AT8 ISA and is tested in the local Python suites or in the federation continuity challenge.

