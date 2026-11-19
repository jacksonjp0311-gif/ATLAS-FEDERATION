"""Finite, deterministic teaching schedulers. Not Linux EEVDF or scheduler ABI."""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque

@dataclass(frozen=True)
class Task:
    pid: str
    arrival: int
    burst: int
    deadline: int|None=None

def _check(tasks):
    tasks=tuple(tasks)
    if len({x.pid for x in tasks})!=len(tasks):raise ValueError('duplicate task')
    if any(not isinstance(x.pid,str) or not x.pid or not isinstance(x.arrival,int) or not isinstance(x.burst,int) or x.arrival<0 or x.burst<=0 or (x.deadline is not None and (not isinstance(x.deadline,int) or x.deadline<x.arrival)) for x in tasks):
        raise ValueError('invalid task')
    if len(tasks)>1000 or sum(x.burst for x in tasks)+max([x.arrival for x in tasks],default=0)>1000000:raise ValueError('large simulation')
    return tasks

def round_robin(tasks,quantum=2):
    tasks=_check(tasks)
    if not isinstance(quantum,int) or quantum<=0:raise ValueError('quantum positive')
    arrivals=sorted(tasks,key=lambda t:(t.arrival,t.pid));ready=deque()
    remain={x.pid:x.burst for x in tasks};idx=0;t=0;active=None;slice_left=0;timeline=[]
    while len(remain)>0:
        while idx<len(arrivals) and arrivals[idx].arrival<=t:
            ready.append(arrivals[idx].pid);idx+=1
        if active is None and ready:
            active=ready.popleft();slice_left=quantum
        timeline.append(active)
        if active is not None:
            remain[active]-=1;slice_left-=1
            if remain[active]==0:
                del remain[active];active=None
            elif slice_left==0:
                ready.append(active);active=None
        t+=1
    return tuple(timeline)

def earliest_deadline_first(tasks):
    tasks=_check(tasks)
    if any(x.deadline is None for x in tasks):raise ValueError('deadline required')
    remain={x.pid:x.burst for x in tasks};t=0;timeline=[]
    while remain:
        ready=[x for x in tasks if x.pid in remain and x.arrival<=t]
        if ready:
            selected=min(ready,key=lambda x:(x.deadline,x.pid))
            remain[selected.pid]-=1
            if remain[selected.pid]==0:del remain[selected.pid]
            timeline.append(selected.pid)
        else:timeline.append(None)
        t+=1
    return tuple(timeline)

def completion_metrics(tasks,timeline):
    tasks=_check(tasks);completion={}
    for tick,pid in enumerate(timeline):
        if pid is not None:completion[pid]=tick+1
    if set(completion)!={x.pid for x in tasks}:raise ValueError('incomplete trace')
    return {x.pid:{'completion':completion[x.pid],'turnaround':completion[x.pid]-x.arrival,'waiting':completion[x.pid]-x.arrival-x.burst} for x in tasks}
