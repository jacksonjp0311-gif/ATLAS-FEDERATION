"""Fail-closed ELF64 little-endian PT_LOAD parser: parses only, never executes."""
from __future__ import annotations
from dataclasses import dataclass
import struct
@dataclass(frozen=True)
class Segment:
    address:int
    flags:int
    initialized:bytes
    zero_fill:int

def loadable_segments(blob:bytes,max_segment=16<<20):
    if not isinstance(blob,bytes) or len(blob)<64 or blob[:4]!=b'\x7fELF' or blob[4:6]!=b'\x02\x01' or blob[6]!=1:
        raise ValueError('unsupported ELF header')
    e=struct.unpack_from('<16sHHIQQQIHHHHHH',blob,0)
    ident,typ,machine,version,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstr=e
    if typ not in (2,3) or machine not in (62,183) or version!=1 or ehsize!=64 or phentsize!=56 or phnum>1024 or phoff>len(blob) or phnum*phentsize>len(blob)-phoff:
        raise ValueError('invalid program header table')
    segments=[]
    for i in range(phnum):
        kind,pflags,off,vaddr,paddr,filesz,memsz,align=struct.unpack_from('<IIQQQQQQ',blob,phoff+i*phentsize)
        if kind!=1:continue
        if filesz>memsz or memsz>max_segment or off>len(blob) or filesz>len(blob)-off or (align not in (0,1) and (align&(align-1) or off%align !=vaddr%align)):
            raise ValueError('unsafe or invalid PT_LOAD')
        segments.append(Segment(vaddr,pflags,blob[off:off+filesz],memsz-filesz))
    if not segments:raise ValueError('no loadable segments')
    if any(a.address>b.address for a,b in zip(segments,segments[1:])):raise ValueError('PT_LOAD unsorted')
    return tuple(segments)
