"""A crash-prefix model of write-ahead logging; not a physical durability claim."""
from __future__ import annotations
import hashlib,json

def _encode(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
class CrashJournal:
    def __init__(self):
        self.durable=[];self.volatile=[];self.active={}
    def begin(self,txn):
        if txn in self.active or not isinstance(txn,str) or not txn:raise ValueError('bad transaction')
        self.active[txn]=[];self.volatile.append(('begin',txn,None,None))
    def set(self,txn,key,value):
        if txn not in self.active:raise ValueError('unknown transaction')
        if not isinstance(key,str) or not key:raise ValueError('invalid key')
        self.active[txn].append((key,value));self.volatile.append(('set',txn,key,value))
    def commit(self,txn):
        if txn not in self.active:raise ValueError('unknown transaction')
        del self.active[txn];self.volatile.append(('commit',txn,None,None))
    def flush(self):
        self.durable.extend(self.volatile);self.volatile=[]
    def crash(self):
        self.volatile=[];self.active={}
    def recover(self):
        pending={};state={}
        for op,txn,key,value in self.durable:
            if op=='begin':pending[txn]=[]
            elif op=='set' and txn in pending:pending[txn].append((key,value))
            elif op=='commit' and txn in pending:
                for k,v in pending.pop(txn):state[k]=v
        return state
    def durable_digest(self):return hashlib.sha256(_encode(self.durable)).hexdigest()
