"""Power-of-two buddy allocator with explicit alignment, fragmentation and coalescence."""
from __future__ import annotations
class Buddy:
    def __init__(self,max_order=12,min_order=4):
        if not isinstance(max_order,int) or not isinstance(min_order,int) or min_order<0 or max_order<min_order or max_order>26:raise ValueError('invalid orders')
        self.max_order=max_order;self.min_order=min_order
        self.free_blocks={k:set() for k in range(min_order,max_order+1)}
        self.free_blocks[max_order].add(0)
        self.allocated={}
    def alloc(self,size):
        if not isinstance(size,int) or not 0<size<=1<<self.max_order:raise ValueError('invalid allocation size')
        order=max(self.min_order,(size-1).bit_length())
        k=next((v for v in range(order,self.max_order+1) if self.free_blocks[v]),None)
        if k is None:raise MemoryError('no suitable free block')
        addr=min(self.free_blocks[k]);self.free_blocks[k].remove(addr)
        while k>order:
            k-=1;self.free_blocks[k].add(addr+(1<<k))
        self.allocated[addr]=(order,size)
        self.validate();return addr
    def release(self,addr):
        if addr not in self.allocated:raise ValueError('unknown or freed address')
        order,_=self.allocated.pop(addr)
        while order<self.max_order and (addr^(1<<order)) in self.free_blocks[order]:
            mate=addr^(1<<order)
            self.free_blocks[order].remove(mate)
            addr=min(addr,mate);order+=1
        self.free_blocks[order].add(addr)
        self.validate()
    def used_bytes(self):return sum(1<<order for order,_ in self.allocated.values())
    def requested_bytes(self):return sum(size for _,size in self.allocated.values())
    def free_bytes(self):return sum((1<<k)*len(b) for k,b in self.free_blocks.items())
    def validate(self):
        intervals=[]
        for k,addrs in self.free_blocks.items():
            for a in addrs:
                if a%(1<<k):raise AssertionError('misaligned free block')
                intervals.append((a,a+(1<<k)))
        for a,(k,_) in self.allocated.items():
            if a%(1<<k):raise AssertionError('misaligned allocated block')
            intervals.append((a,a+(1<<k)))
        intervals.sort()
        if not intervals or intervals[0][0]!=0 or intervals[-1][1]!=(1<<self.max_order) or any(a[1]!=b[0] for a,b in zip(intervals,intervals[1:])):
            raise AssertionError('allocation coverage overlap/hole')
        return True
