"""One-command offline, self-contained Software Design Patterns demonstration."""
from pathlib import Path
import json,tempfile
from .workflow import RecoveryWorkflow,SimulatedInterruption
from .contracts import canonical_bytes
from .resilience import CircuitBreaker


def main():
    def pure_sum(p):return {'sum':p['a']+p['b']}
    with tempfile.TemporaryDirectory(prefix='atlas-patterns-') as folder:
        with RecoveryWorkflow(folder) as s:
            a=s.apply('sum0001',{'a':5,'b':7},pure_sum)
            try:s.apply('sum0002',{'a':8,'b':9},pure_sum,interrupt_after_commit=True)
            except SimulatedInterruption:pass
        with RecoveryWorkflow(folder) as s:
            recovered=s.recover()
            verified=s.journal.verify_replay()
            assert recovered['recovered'] and verified['rows']==2
            assert a['command']['result']=={'sum':12}
            print(json.dumps({'schema':'atlas.software-patterns-demo/1','offline_demo':'passed',
                 'journal_records':verified['rows'],'recovered_stale_snapshot':recovered['recovered'],
                 'power_loss_hw_certified':False,'external_exactly_once_proven':False},indent=2))
if __name__=='__main__':main()
