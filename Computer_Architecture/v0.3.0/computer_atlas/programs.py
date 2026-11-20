"""Small, original, deterministic AT8 teaching programs and expected results."""
from .isa import assemble

ARITHMETIC_AND_MEMORY = '''
    LDI R0, 5
    ADDI R0, 7
    STORE R0, 0
    XORI R0, 3
    OUT R0, 0
    HALT
'''

COUNTDOWN = '''
    LDI R0, 3
loop:
    OUT R0, 0
    ADDI R0, 255 ; decrement modulo 256
    JNZ R0, loop
    HALT
'''

READ_AND_STORE = '''
    IN R1, 1
    ADDI R1, 2
    STORE R1, 4
    LOAD R3, 4
    OUT R3, 2
    HALT
'''

BRANCH_EQUAL = '''
    LDI R0, 5
    CMP R0, 5
    JZ R0, not_taken ; JZ checks register, not flag!
    JMP equal_value
not_taken:
    LDI R1, 99
equal_value:
    OUT R0, 0
    HALT
'''
# The BRANCH_EQUAL illustration demonstrates an important semantic difference:
# JZ checks a register, NOT the flags computed by CMP. Avoid treating it as BEQ.


def examples():
    return {
        'arithmetic_memory':assemble(ARITHMETIC_AND_MEMORY),
        'countdown':assemble(COUNTDOWN),
        'input_output':assemble(READ_AND_STORE),
    }
