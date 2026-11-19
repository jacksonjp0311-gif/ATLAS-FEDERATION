"""Deterministic finite state-machine pattern with constrained transition graph.

No implicit transition, user-supplied code execution, thread-safety, or physical
side-effect atomicity is inferred from this educational reference.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,json

class TransitionError(ValueError):pass

@dataclass(frozen=True)
class Transition:
    source:str
    event:str
    destination:str

class StateMachine:
    def __init__(self, states, initial, transitions):
        if type(states) not in (tuple,list) or not 1<=len(states)<=64 or any(type(s) is not str or not s for s in states):
            raise TransitionError('finite state names required')
        if len(set(states))!=len(states) or initial not in states:raise TransitionError('invalid state set or initial')
        self.states=tuple(states)
        self.current=initial
        self.graph={}
        if type(transitions) not in (list,tuple) or len(transitions)>256:raise TransitionError('bounded transitions required')
        for t in transitions:
            if type(t) is not Transition or t.source not in states or t.destination not in states or type(t.event) is not str or not t.event:
                raise TransitionError('unknown transition state or event')
            key=(t.source,t.event)
            if key in self.graph:raise TransitionError('ambiguous duplicate transition')
            self.graph[key]=t.destination
        self.history=[]

    def step(self,event):
        if type(event) is not str:raise TransitionError('string event required')
        key=(self.current,event)
        if key not in self.graph:raise TransitionError('undefined transition refused')
        prior=self.current;self.current=self.graph[key]
        self.history.append((prior,event,self.current))
        return self.current

    def receipt(self):
        raw=json.dumps(self.history,sort_keys=True,separators=(',',':')).encode()
        return {'state':self.current,'transitions':len(self.history),
                'history_sha256':hashlib.sha256(raw).hexdigest(),
                'physical_side_effect_transaction_proven':False}


def recovery_machine():
    """Explicit recovery sequence; names are abstract, not actual machinery."""
    return StateMachine(('idle','prepared','verified','committed','hold'), 'idle', (
        Transition('idle','prepare','prepared'),Transition('prepared','validate','verified'),
        Transition('prepared','reject','hold'),Transition('verified','commit','committed'),
        Transition('verified','reject','hold'),Transition('hold','reset','idle'),
        Transition('committed','reset','idle')))
