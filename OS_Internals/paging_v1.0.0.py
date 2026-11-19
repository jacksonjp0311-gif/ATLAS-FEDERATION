"""Page replacement reference algorithms on finite, equal-size page traces."""
from __future__ import annotations
from collections import deque

def page_faults(references,frames,policy='fifo'):
    refs=tuple(references)
    if not isinstance(frames,int) or frames<=0 or frames>10000 or len(refs)>1000000 or policy not in ('fifo','lru','opt'):
        raise ValueError('invalid page replacement model')
    live=set();order=deque();last={};faults=0
    for pos,page in enumerate(refs):
        if page not in live:
            faults+=1
            if len(live)>=frames:
                if policy=='fifo':victim=order.popleft()
                elif policy=='lru':victim=min(live,key=lambda p:(last[p],str(p)))
                else:
                    # Evict farthest next use; deterministic tie break by str
                    def next_pos(p):
                        try:return refs.index(p,pos+1)
                        except ValueError:return len(refs)+1
                    victim=max(sorted(live,key=str),key=next_pos)
                live.remove(victim);last.pop(victim,None)
            live.add(page)
            if policy=='fifo':order.append(page)
        last[page]=pos
    return faults
