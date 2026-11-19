"""Causality is a partial order, not a wall clock. Fixed vector membership."""
from dataclasses import dataclass

@dataclass
class LamportClock:
    value: int = 0
    def __post_init__(self):
        if type(self.value) is not int or self.value < 0: raise ValueError('logical clock must be nonnegative integer')
    def local(self):
        self.value+=1; return self.value
    def send(self): return self.local()
    def receive(self, timestamp):
        if type(timestamp) is not int or timestamp < 0: raise ValueError('invalid timestamp')
        self.value=max(self.value,timestamp)+1
        return self.value

@dataclass
class VectorClock:
    members: tuple[str,...]
    node: str
    def __post_init__(self):
        if not self.members or len(self.members)!=len(set(self.members)) or self.node not in self.members or not all(isinstance(x,str) and x for x in self.members):
            raise ValueError('invalid fixed membership')
        self.values={m:0 for m in self.members}
    def local(self):
        self.values[self.node]+=1; return self.snapshot()
    def send(self):return self.local()
    def receive(self, stamp):
        if set(stamp)!=set(self.members) or any(type(x) is not int or x<0 for x in stamp.values()):
            raise ValueError('invalid vector')
        for m in self.members:self.values[m]=max(self.values[m],stamp[m])
        self.values[self.node]+=1
        return self.snapshot()
    def snapshot(self):return dict(self.values)

def precedes(a,b):
    """Strict component order. Equal stamps are not strict precedence."""
    if set(a)!=set(b) or not a: raise ValueError('incompatible vector clocks')
    if any(type(v)!=int or v<0 for v in list(a.values())+list(b.values())):raise ValueError('invalid clock component')
    return all(a[k]<=b[k] for k in a) and any(a[k]<b[k] for k in a)

def concurrent(a,b):return a!=b and not precedes(a,b) and not precedes(b,a)
