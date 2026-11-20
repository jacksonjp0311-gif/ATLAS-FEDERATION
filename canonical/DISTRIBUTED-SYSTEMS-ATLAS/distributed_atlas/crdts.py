"""State-based join-semilattice models for replicas with stable unique IDs."""
from dataclasses import dataclass, field

@dataclass
class GCounter:
    values: dict[str,int]=field(default_factory=dict)
    def increment(self,node,by=1):
        if not isinstance(node,str) or not node or type(by)!=int or by<0: raise ValueError('invalid increment')
        self.values[node]=self.values.get(node,0)+by
        return self.value
    @property
    def value(self):return sum(self.values.values())
    def merge(self,other):
        if not isinstance(other,GCounter):raise ValueError('wrong CRDT type')
        keys=set(self.values)|set(other.values)
        return GCounter({k:max(self.values.get(k,0),other.values.get(k,0)) for k in sorted(keys)})

@dataclass
class ORSet:
    """Observed-remove set. Dots must be globally unique across ALL add operations."""
    adds:dict[str,set[str]]=field(default_factory=dict)
    removed:set[str]=field(default_factory=set)
    def add(self,value,dot):
        if not value or not dot or not isinstance(value,str) or not isinstance(dot,str):raise ValueError('invalid key or unique dot')
        if dot in self.removed or any(dot in x for x in self.adds.values()):raise ValueError('dot reused')
        self.adds.setdefault(value,set()).add(dot)
    def remove(self,value):self.removed.update(self.adds.get(value,set()))
    @property
    def value(self):return frozenset(k for k,dots in self.adds.items() if dots-self.removed)
    def merge(self,other):
        if not isinstance(other,ORSet):raise ValueError('wrong CRDT type')
        adds={k:self.adds.get(k,set())|other.adds.get(k,set()) for k in set(self.adds)|set(other.adds)}
        return ORSet(adds,self.removed|other.removed)
