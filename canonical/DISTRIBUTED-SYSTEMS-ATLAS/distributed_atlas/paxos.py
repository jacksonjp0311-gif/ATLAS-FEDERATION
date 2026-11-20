"""Single-decree Paxos Phase 1/2 acceptor and sequential proposer demonstration.
Educational: no asynchronous proposer orchestration, log membership change, or durable network.
"""
from dataclasses import dataclass
from typing import Optional
from .quorums import majority_size

@dataclass
class Acceptor:
    promised:int=-1
    accepted_n:int=-1
    accepted_value:str|None=None
    def promise(self,n):
        if type(n)!=int or n<0:raise ValueError('invalid ballot')
        if n>self.promised:
            self.promised=n
            return (self.accepted_n,self.accepted_value)
        return None
    def accept(self,n,value):
        if type(n)!=int or n<0 or not isinstance(value,str):raise ValueError('invalid proposal')
        if n<self.promised:return False
        self.promised=n
        self.accepted_n=n
        self.accepted_value=value
        return True

def propose(acceptors,ballot,value,reachable=None):
    """Returns (chosen_value, quorum_accept_count), or (None, 0) when no quorum.
    A proposal may be chosen only if a majority accepts; offline crash-stop model.
    """
    if not acceptors or type(ballot)!=int or ballot<0 or not isinstance(value,str):raise ValueError('invalid proposer request')
    ids=list(range(len(acceptors))) if reachable is None else sorted(set(reachable))
    if not set(ids).issubset(set(range(len(acceptors)))):raise ValueError('unrecognized acceptor')
    promises=[]
    for i in ids:
        p=acceptors[i].promise(ballot)
        if p is not None:promises.append((i,p))
    q=majority_size(len(acceptors))
    if len(promises)<q:return (None,0)
    prev=[(n,v) for _,(n,v) in promises if n>=0]
    selected=max(prev,key=lambda it:it[0])[1] if prev else value
    count=sum(acceptors[i].accept(ballot,selected) for i,_ in promises)
    return (selected if count>=q else None,count)

def unsafe_ignore_prior(acceptors,ballot,value):
    """Deliberate negative control: incorrect proposer can violate agreement."""
    accepted=[a for a in acceptors if a.promise(ballot) is not None]
    q=majority_size(len(acceptors))
    if len(accepted)<q:return None
    return value if sum(a.accept(ballot,value) for a in accepted)>=q else None
