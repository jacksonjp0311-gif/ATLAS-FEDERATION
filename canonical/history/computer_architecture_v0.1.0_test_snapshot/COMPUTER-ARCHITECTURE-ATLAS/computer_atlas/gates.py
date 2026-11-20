"""Elementary NAND-only reconstruction of a finite combinational 8-bit ALU.

No transistors, timing, glitches or static noise margins. Provides an independently
checkable Boolean path between Electronics NAND primitives and AT8 ADDI semantics.
"""

def _bit(b):
    if type(b) is not int or b not in (0,1):raise ValueError('bit is integer 0 or 1')
    return b


def nand(a,b):return 1-(_bit(a)&_bit(b))


def nand_xor(a,b):
    x=nand(a,b)
    return nand(nand(a,x),nand(b,x))


def full_adder(a,b,carry_in):
    x=nand_xor(a,b)
    s=nand_xor(x,carry_in)
    cout=nand(nand(a,b),nand(x,carry_in))
    return (s,cout)


def ripple_add(a,b,width=8,carry_in=0):
    if type(width) is not int or not 1<=width<=32 or type(a) is not int or type(b) is not int:
        raise ValueError('finite unsigned integer words and width 1..32 required')
    if not 0<=a<2**width or not 0<=b<2**width:
        raise ValueError('operands outside selected width')
    carry=_bit(carry_in)
    result=0
    for j in range(width):
        bit,carry=full_adder((a>>j)&1,(b>>j)&1,carry)
        result|=bit<<j
    return result,carry


def alu8(a,b,op):
    if type(a) is not int or type(b) is not int or not 0<=a<256 or not 0<=b<256:
        raise ValueError('ALU operands must be unsigned bytes')
    if op=='ADD':
        result,carry=ripple_add(a,b,8)
        overflow=int(bool((~(a^b)&(a^result))&128))
    elif op=='XOR':result=a^b;carry=0;overflow=0
    elif op=='AND':result=a&b;carry=0;overflow=0
    elif op=='OR':result=a|b;carry=0;overflow=0
    elif op=='CMP':
        result,carry=ripple_add(a,255^b,8,1)
        overflow=int(bool(((a^b)&(a^result))&128))
    else:raise ValueError('unsupported ALU function')
    return {'value':result,'zero':int(result==0),'negative':(result>>7)&1,
            'carry':carry,'overflow':overflow}
