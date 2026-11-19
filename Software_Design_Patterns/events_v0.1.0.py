"""Small single-writer, content-addressed event chain (event sourcing).

Tampering is detectable only relative to an independently trusted head hash.
No distributed consensus, serialization over untrusted concurrent publishers, or
permanent external audit guarantee is provided by this educational example.
"""
from __future__ import annotations
import json
from .atomicfiles import ContentStore,SnapshotError
from .contracts import canonical_bytes

class EventChain:
    def __init__(self,store:ContentStore,tag='events'):
        if type(store) is not ContentStore:raise ValueError('ContentStore required')
        self.store=store;self.tag=tag

    def append(self,event:dict):
        if type(event) is not dict:raise ValueError('event must be bounded mapping')
        try:
            head=self.store.resolve(self.tag)['sha256']
            prior=json.loads(self.store.get(head))
            seq=prior['sequence']+1
        except SnapshotError as exc:
            # An existing pointer with missing/tampered data must NOT silently
            # reset the chain; only a truly missing head means a new chain.
            if (self.store.root/'heads'/self.tag).exists():raise
            head=None;seq=1
        record={'schema':'atlas.event-chain/1','sequence':seq,'prev_sha256':head,'event':event}
        raw=canonical_bytes(record)
        current=self.store.put(raw)
        self.store.publish(self.tag,current)
        return {'sequence':seq,'entry_sha256':current,'previous_sha256':head}

    def replay(self,maximum=1024):
        if type(maximum) is not int or not 1<=maximum<=10000:raise ValueError('bounded replay requested')
        try:head=self.store.resolve(self.tag)['sha256']
        except SnapshotError:
            if (self.store.root/'heads'/self.tag).exists():raise
            return {'events':tuple(),'head_sha256':None,'valid':True}
        seen=set();reverse=[];current=head
        while current:
            if current in seen or len(reverse)>=maximum:raise SnapshotError('cycle or overlong history')
            seen.add(current)
            row=json.loads(self.store.get(current))
            if type(row) is not dict or set(row)!={'schema','sequence','prev_sha256','event'} or row['schema']!='atlas.event-chain/1':
                raise SnapshotError('malformed event entry')
            if type(row['sequence']) is not int or row['sequence']<1:raise SnapshotError('invalid event sequence')
            reverse.append(row);current=row['prev_sha256']
        ordered=list(reversed(reverse))
        if any(row['sequence']!=i for i,row in enumerate(ordered,1)):
            raise SnapshotError('gap, reorder or missing sequence')
        return {'events':tuple(row['event'] for row in ordered),'head_sha256':head,
                'valid':True,'external_audit_signature_verified':False}
