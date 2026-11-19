"""Deterministic circuit breaker, bounded retry, token bucket and quota bulkhead.

Simulated monotonic logical time, no wall clock sleeps or external service. These
models test decisions, not distributed availability or production SLOs.
"""
from __future__ import annotations
from dataclasses import dataclass

class Rejected(ValueError): pass

class CircuitBreaker:
    def __init__(self,fail_threshold=3,reset_after=10):
        if type(fail_threshold) is not int or not 1<=fail_threshold<=100:raise ValueError('threshold 1..100')
        if type(reset_after) is not int or not 1<=reset_after<=10**6:raise ValueError('reset interval positive')
        self.threshold=fail_threshold;self.reset_after=reset_after
        self.state='closed';self.failures=0;self.opened_at=None
        self.probe_inflight=False;self.last_tick=-1;self.events=[]

    def _check_time(self,tick):
        if type(tick) is not int or tick<0 or tick<self.last_tick:raise ValueError('nondecreasing integer logical tick required')
        self.last_tick=tick

    def allow(self,tick):
        self._check_time(tick)
        if self.state=='open' and tick-self.opened_at>=self.reset_after:
            self.state='half_open';self.probe_inflight=False
        if self.state=='open':return False
        if self.state=='half_open':
            if self.probe_inflight:return False
            self.probe_inflight=True
        return True

    def record(self,success,tick):
        self._check_time(tick)
        if type(success) is not bool:raise ValueError('Boolean result required')
        if self.state=='open':raise Rejected('open circuit cannot accept results')
        if self.state=='half_open' and not self.probe_inflight:raise Rejected('probe was not admitted')
        if success:
            self.state='closed';self.failures=0;self.probe_inflight=False;self.opened_at=None
        else:
            self.failures+=1
            if self.state=='half_open' or self.failures>=self.threshold:
                self.state='open';self.opened_at=tick;self.probe_inflight=False
        self.events.append((tick,success,self.state))

    def snapshot(self):
        return {'state':self.state,'failures':self.failures,'opened_at':self.opened_at,
                'logical_tick':self.last_tick,'external_dependency_qualified':False}


def bounded_retry(operation, retries, retryable):
    """Explicit retry only for caller-designated exceptions. No external exactly-once guarantee."""
    if type(retries) is not int or not 0<=retries<=20:raise ValueError('retries 0..20')
    if not callable(operation) or not callable(retryable):raise ValueError('callables required')
    attempts=0
    for i in range(retries+1):
        attempts+=1
        try:return {'value':operation(),'attempts':attempts,'success':True}
        except Exception as exc:
            if not retryable(exc) or i==retries:raise
    raise RuntimeError('unreachable')

class Bulkhead:
    def __init__(self,limits):
        if type(limits) is not dict or not limits or len(limits)>32 or any(type(k) is not str or not k or type(v) is not int or not 1<=v<=128 for k,v in limits.items()):
            raise ValueError('bounded named positive lane limits required')
        self.capacity=dict(limits);self.used={k:0 for k in limits}

    def acquire(self,lane):
        if lane not in self.used:raise ValueError('unknown lane')
        if self.used[lane]>=self.capacity[lane]:return False
        self.used[lane]+=1;return True

    def release(self,lane):
        if lane not in self.used or self.used[lane]<=0:raise ValueError('unbalanced release')
        self.used[lane]-=1

    def snapshot(self):return {'capacity':dict(self.capacity),'allocated':dict(self.used),'process_isolation_proven':False}
