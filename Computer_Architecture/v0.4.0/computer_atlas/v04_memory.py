"""ATLAS FORGE AT8 v0.4: typed ROM/RAM bus, parity faults, bounded arbitration.

These are mathematical interface contracts. They do not construct hardware memory,
provide ECC correction, establish retention, or prove electrical bus timing.
"""
from __future__ import annotations
import hashlib,json


def _byte(v):
    if type(v) is not int or not 0<=v<=255:raise ValueError('byte must be integer 0..255')
    return v


def _addr(v,limit):
    if type(v) is not int or not 0<=v<limit:raise ValueError('address out of bounds')
    return v


def _canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()


class HarvardBus:
    """Separate immutable program ROM and 256-byte mutable RAM; no memory-mapped I/O.

    Bus requests are abstract transactions. Device read and source timing are NOT
    implemented; a successful result says nothing about physical bus arbitration.
    """
    def __init__(self,rom:bytes):
        from .isa import validate_rom
        validate_rom(rom)
        self.rom=rom
        self.ram=bytearray(256)
        self.transcript=[]

    def fetch(self,pc:int):
        if type(pc) is not int or pc%2 or not 0<=pc+1<len(self.rom):
            raise ValueError('AT8 PC must be aligned and within ROM')
        data=bytes(self.rom[pc:pc+2])
        self.transcript.append(('fetch',pc,data.hex()))
        return data

    def read(self,address:int):
        address=_addr(address,256)
        val=self.ram[address]
        self.transcript.append(('read',address,val))
        return val

    def write(self,address:int,value:int):
        address=_addr(address,256);value=_byte(value)
        self.ram[address]=value
        self.transcript.append(('write',address,value))

    def write_rom(self,address:int,value:int):
        raise PermissionError('architecture has no instruction to modify program ROM')

    def transcript_receipt(self):
        return {'schema':'atlas.at8-bus-transactions/1','ops':len(self.transcript),
                'transactions_sha256':hashlib.sha256(_canonical(self.transcript)).hexdigest(),
                'RAM_sha256':hashlib.sha256(self.ram).hexdigest(),
                'ROM_sha256':hashlib.sha256(self.rom).hexdigest(),
                'physical_bus_implemented':False}


class ParityByteMemory:
    """Odd-weight bit flips detected by stored even parity; no correction.

    Even bit errors can go undetected, and parity itself may be corrupted.
    This toy model is NOT ECC, safe DRAM, or an actual soft-error rate.
    """
    def __init__(self,word_count=32):
        if type(word_count) is not int or not 1<=word_count<=256:
            raise ValueError('bounded word_count 1..256 required')
        self.data=[0]*word_count
        self.parity=[0]*word_count
        self.events=[]

    def write(self,address,value):
        a=_addr(address,len(self.data));v=_byte(value)
        self.data[a]=v;self.parity[a]=v.bit_count()%2
        self.events.append(('write',a,v))

    def inject_data_flip(self,address,bit_mask):
        a=_addr(address,len(self.data));mask=_byte(bit_mask)
        if mask==0:raise ValueError('nonzero fault mask required')
        self.data[a]^=mask;self.events.append(('fault',a,mask))

    def inject_parity_flip(self,address):
        a=_addr(address,len(self.data));self.parity[a]^=1
        self.events.append(('parity_fault',a))

    def read(self,address):
        a=_addr(address,len(self.data))
        observed=self.data[a].bit_count()%2
        if observed!=self.parity[a]:
            self.events.append(('detected',a))
            return {'status':'detected_parity_error','value':None,'correction_performed':False}
        self.events.append(('read',a,self.data[a]))
        return {'status':'parity_consistent_not_authentic','value':self.data[a],
                'correction_performed':False}

    def receipt(self):
        return {'schema':'atlas.at8-parity-byte-memory/1','words':len(self.data),
                'events_sha256':hashlib.sha256(_canonical(self.events)).hexdigest(),
                'parity_detects_all_double_bit_errors':False,
                'physical_bitcell_implemented':False}


class RoundRobinArbiter:
    """Small deterministic work-conserving scheduler, NOT hardware/CDC timing.

    Arbitrates requesters 0..N-1. Arbitration grants one ready request/cycle.
    A continuously requesting master is served within at most N arbitrations
    if all request bits are sampled every cycle, no resets and no stalls.
    """
    def __init__(self,masters=2):
        if type(masters) is not int or not 2<=masters<=16:raise ValueError('masters 2..16')
        self.masters=masters
        self.pointer=0
        self.grants=[]

    def tick(self,requests):
        if type(requests) not in (tuple,list) or len(requests)!=self.masters:
            raise ValueError('per-master request bits required')
        if any(type(x) is not int or x not in (0,1) for x in requests):
            raise ValueError('strict binary request vector')
        grant=None
        for j in range(self.masters):
            k=(self.pointer+j)%self.masters
            if requests[k]:
                grant=k;self.pointer=(k+1)%self.masters;break
        self.grants.append(grant)
        return grant

    def receipt(self):
        return {'schema':'atlas.at8-rr-bus-arbitration/1','cycles':len(self.grants),
                'grant_sha256':hashlib.sha256(_canonical(self.grants)).hexdigest(),
                'bounded_fairness_assumes_ready_requests':True,
                'independently_characterized_hardware':False}
