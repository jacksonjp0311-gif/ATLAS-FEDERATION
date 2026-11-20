"""Crash-injection reference: SQLite journal authoritative, derived snapshot repair.

The database transaction and filesystem pointer are NOT one atomic transaction.
After an interruption between them, a restarted process can rebuild a derived
snapshot from the independently integrity-checked journal. None of this proves
exactly-once external equipment control or physical power-failure durability.
"""
from __future__ import annotations
from pathlib import Path
from .ledger import CommandJournal
from .atomicfiles import ContentStore,SnapshotError
from .contracts import canonical_bytes,digest

class SimulatedInterruption(RuntimeError): pass

class RecoveryWorkflow:
    def __init__(self,root):
        self.root=Path(root)
        self.root.mkdir(parents=True,exist_ok=True)
        self.journal=CommandJournal(self.root/'commands.sqlite3')
        self.store=ContentStore(self.root/'snapshots')

    def close(self):self.journal.close()
    def __enter__(self):return self
    def __exit__(self,*args):self.close()

    def _snapshot(self):
        verified=self.journal.verify_replay()
        data={'schema':'atlas.offline-recovery-view/1','command_head_sha256':verified['head_sha256'],
              'commands':list(self.journal.records())}
        result=self.store.put(canonical_bytes(data))
        self.store.publish('current',result)
        return {'sha256':result,'count':len(data['commands'])}

    def apply(self,command_id,payload,reducer,interrupt_after_commit=False):
        if type(interrupt_after_commit) is not bool:raise ValueError('Boolean interruption flag required')
        committed=self.journal.execute(command_id,payload,reducer)
        if interrupt_after_commit:
            raise SimulatedInterruption('DB committed; derived snapshot not published')
        snap=self._snapshot()
        return {'command':committed,'snapshot':snap}

    def recover(self):
        """Rebuild missing/stale derived view from authoritative local journal.

        A corrupt existing pointer is refused by the storage layer rather than
        silently overwritten. An operator would need a separately anchored
        trusted copy or explicit manual repair procedure.
        """
        verified=self.journal.verify_replay()
        try:
            head=self.store.resolve('current')
            existing=__import__('json').loads(head['data'])
            if existing['command_head_sha256']==verified['head_sha256']:
                return {'recovered':False,'view_sha256':head['sha256'],
                        'command_count':len(existing['commands'])}
        except SnapshotError:
            if (self.store.root/'heads/current').exists():raise
        snap=self._snapshot()
        return {'recovered':True,'view_sha256':snap['sha256'],
                'command_count':snap['count']}
