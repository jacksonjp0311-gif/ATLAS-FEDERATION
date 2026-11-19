"""Finite authority and stale-handle model; NOT a system-call sandbox."""
from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True)
class Handle:
    slot:int
    generation:int

class HandleTable:
    def __init__(self,capacity=128):
        if not 1<=capacity<=100000:raise ValueError('invalid capacity')
        self.capacity=capacity;self.table={};self.gens=[0]*capacity
    def grant(self,obj,rights):
        rights=frozenset(rights)
        if not rights or rights-set('rwx'):raise ValueError('bad rights')
        slot=next((i for i in range(self.capacity) if i not in self.table),None)
        if slot is None:raise MemoryError('full table')
        self.table[slot]=(self.gens[slot],obj,rights)
        return Handle(slot,self.gens[slot])
    def check(self,handle,right):
        if not isinstance(handle,Handle) or not isinstance(handle.slot,int) or not 0<=handle.slot<self.capacity:
            raise PermissionError('invalid handle')
        row=self.table.get(handle.slot)
        if row is None or row[0]!=handle.generation:raise PermissionError('stale handle')
        if right not in row[2]:raise PermissionError('denied')
        return row[1]
    def revoke(self,handle):
        if not isinstance(handle,Handle) or not isinstance(handle.slot,int) or not 0<=handle.slot<self.capacity:
            raise PermissionError('invalid handle')
        row=self.table.get(handle.slot)
        if row is None or row[0]!=handle.generation:
            raise PermissionError('stale handle')
        del self.table[handle.slot];self.gens[handle.slot]+=1
