"""Bounded 4-KiB style page translation model; not an MMU or TLB implementation."""
from __future__ import annotations
from dataclasses import dataclass
from collections import OrderedDict

class PageFault(LookupError):
    def __init__(self, reason):
        self.reason=reason
        super().__init__(reason)

@dataclass(frozen=True)
class Mapping:
    frame: int
    permissions: str
    user: bool

class AddressSpace:
    def __init__(self, page_size=4096, frames=1024, tlb_entries=16, asid=0):
        if page_size<256 or page_size&(page_size-1) or frames<=0 or tlb_entries<0 or asid<0:
            raise ValueError('invalid address-space dimensions')
        self.page_size=page_size;self.frames=frames;self.asid=asid;self.limit=(1<<48)
        self.table={};self.tlb=OrderedDict();self.tlb_entries=tlb_entries
        self.hits=0;self.misses=0

    def map(self, virtual_page:int, frame:int, permissions='rw', user=True):
        if not isinstance(virtual_page,int) or not 0<=virtual_page<self.limit//self.page_size:
            raise ValueError('bad virtual page')
        if not isinstance(frame,int) or not 0<=frame<self.frames:
            raise ValueError('bad physical frame')
        if not permissions or set(permissions)-set('rwx') or len(set(permissions))!=len(permissions):
            raise ValueError('bad permission set')
        self.table[virtual_page]=Mapping(frame,permissions,bool(user))
        self.tlb.pop((self.asid,virtual_page),None)  # shootdown on every change

    def unmap(self, virtual_page:int):
        self.table.pop(virtual_page,None);self.tlb.pop((self.asid,virtual_page),None)

    def translate(self, virtual_address:int, access='r', user=True):
        if not isinstance(virtual_address,int) or not 0<=virtual_address<self.limit:
            raise PageFault('invalid-address')
        if access not in ('r','w','x'):
            raise ValueError('access must be r,w,x')
        vpn,offset=divmod(virtual_address,self.page_size)
        key=(self.asid,vpn)
        if key in self.tlb:
            mapping=self.tlb.pop(key);self.tlb[key]=mapping;self.hits+=1
        else:
            mapping=self.table.get(vpn);self.misses+=1
            if mapping is None:raise PageFault('not-present')
            if self.tlb_entries:
                self.tlb[key]=mapping
                if len(self.tlb)>self.tlb_entries:self.tlb.popitem(last=False)
        if user and not mapping.user:raise PageFault('privilege')
        if access not in mapping.permissions:raise PageFault('permission')
        return mapping.frame*self.page_size+offset
