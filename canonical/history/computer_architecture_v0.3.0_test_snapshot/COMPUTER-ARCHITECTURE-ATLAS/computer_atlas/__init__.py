"""ATLAS FORGE original 15-node federation, Computer Architecture AT8/0.1.

Standard-library educational machine reconstruction with independently testable
architecture and microcode implementations; no fabricated hardware claim.
"""
from .isa import assemble, disassemble, encode, decode, validate_rom
from .gates import nand, full_adder, ripple_add, alu8
