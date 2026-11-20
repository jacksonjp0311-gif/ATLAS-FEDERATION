"""A bounded direct-mapped, write-through, write-allocate cache for AT8 RAM.

Logical abstraction only: no coherence protocol, DMA, latency, power or silicon.
"""
from __future__ import annotations

class SmallRAMCache:
    def __init__(self,initial_ram:bytes|bytearray|None=None,line_size:int=8,line_count:int=4):
        if type(line_size) is not int or line_size not in (4,8,16) or type(line_count) is not int or line_count not in (2,4,8,16):
            raise ValueError('supported line size 4/8/16, lines 2/4/8/16')
        if initial_ram is None:initial_ram=bytes(256)
        if type(initial_ram) not in (bytes,bytearray) or len(initial_ram)!=256:raise ValueError('256 byte RAM required')
        self.ram=bytearray(initial_ram)
        self.line_size=line_size;self.line_count=line_count
        self.cache=[None]*line_count
        self.read_hits=0;self.read_misses=0;self.writes=0

    def _loc(self,address):
        if type(address) is not int or not 0<=address<256:raise ValueError('RAM address must be byte 0..255')
        base=(address//self.line_size)*self.line_size
        idx=(address//self.line_size)%self.line_count
        return base,idx,address-base

    def _refill(self,base,idx):
        self.cache[idx]=(base,bytearray(self.ram[base:base+self.line_size]))

    def read(self,address):
        base,idx,offset=self._loc(address)
        if self.cache[idx] is not None and self.cache[idx][0]==base:
            self.read_hits+=1
        else:
            self.read_misses+=1;self._refill(base,idx)
        return self.cache[idx][1][offset]

    def write(self,address,value):
        base,idx,offset=self._loc(address)
        if type(value) is not int or not 0<=value<256:raise ValueError('byte value required')
        self.ram[address]=value
        if self.cache[idx] is None or self.cache[idx][0]!=base:self._refill(base,idx)
        else:self.cache[idx][1][offset]=value
        self.writes+=1

    def invalidate(self):self.cache=[None]*self.line_count

    def report(self):
        return {'ram_sha256':__import__('hashlib').sha256(self.ram).hexdigest(),
                'reads_hit':self.read_hits,'reads_miss':self.read_misses,'writes':self.writes,
                'cache_coherence_hardware_verified':False,
                'scope':'single logical write-through cache; no physical timing or multi-core coherence'}
