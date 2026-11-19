"""Bounded Strategy, Adapter, Factory, Decorator and Pipeline examples.

These are explicit, small compositions. They do not claim distributed execution,
thread-safety, security or electrical system authority.
"""
from __future__ import annotations
from .contracts import canonical_bytes,digest,ContractError

class StrategyRegistry:
    def __init__(self):self._items={}
    def register(self,name,func):
        if type(name) is not str or not name.isidentifier() or not callable(func) or name in self._items:
            raise ValueError('unique named callable strategy required')
        if len(self._items)>=64:raise ValueError('bounded strategies')
        self._items[name]=func
    def execute(self,name,payload):
        if name not in self._items:raise ValueError('unknown strategy')
        return self._items[name](payload)

class PortAdapter:
    """Normalize offline device records, reject undeclared units or identity."""
    def __init__(self,source_units):
        if source_units not in ('V','mV'):raise ValueError('voltage units V or mV only')
        self.units=source_units
    def normalize(self,sample):
        if type(sample) is not dict or set(sample)!={'sensor','voltage'}:raise ValueError('sensor/voltage mapping required')
        sensor=sample['sensor'];voltage=sample['voltage']
        if type(sensor) is not str or not sensor or len(sensor)>64:raise ValueError('invalid sensor id')
        if type(voltage) not in (int,float) or not -1_000_000<=voltage<=1_000_000:raise ValueError('invalid voltage')
        v=float(voltage)/(1000.0 if self.units=='mV' else 1.0)
        return {'sensor':sensor,'voltage_V':v,'evidence':'unit normalized only; not a calibrated physical signal'}

def build_adapter(config):
    if type(config) is not dict or set(config)!={'source_units'}:raise ValueError('factory config exact schema')
    return PortAdapter(config['source_units'])

class Pipeline:
    def __init__(self,steps):
        if type(steps) not in (tuple,list) or not 1<=len(steps)<=32 or any(not callable(f) for f in steps):
            raise ValueError('bounded pipeline of functions required')
        self.steps=tuple(steps)
    def run(self,value):
        v=value;trace=[]
        for index,step in enumerate(self.steps):
            v=step(v)
            trace.append({'step':index,'result_sha256':digest(v)})
        return {'result':v,'trace':tuple(trace)}

def audited(action,events:list):
    """Decorator that records only result identity, not side-effect rollback."""
    if not callable(action) or type(events) is not list:raise ValueError('callback and mutable event list required')
    def invoke(data):
        result=action(data)
        events.append({'digest':digest(result),'status':'completed','external_side_effects_rolled_back':False})
        return result
    return invoke
