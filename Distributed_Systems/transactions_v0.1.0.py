"""Two-phase commit state abstraction. Prepared and undecided participants block."""
from dataclasses import dataclass

@dataclass
class Participant:
    name:str
    state:str='INIT'
    def prepare(self,ready=True):
        if self.state!='INIT':raise ValueError('duplicate or invalid prepare')
        self.state='PREPARED' if ready else 'ABORTED'
        return self.state=='PREPARED'
    def decide(self,commit):
        if self.state=='ABORTED' and commit:raise ValueError('cannot commit aborted participant')
        if commit and self.state!='PREPARED':raise ValueError('cannot commit unprepared participant')
        if self.state=='COMMITTED' and not commit:raise ValueError('decision conflict')
        self.state='COMMITTED' if commit else 'ABORTED'
    @property
    def blocked(self):return self.state=='PREPARED'

def coordinate(participants,votes,coordinator_available=True):
    if len(participants)!=len(votes) or not participants:raise ValueError('vote mismatch')
    yes=[p.prepare(bool(v)) for p,v in zip(participants,votes)]
    if not coordinator_available:return 'NO_DECISION'
    commit=all(yes)
    for p in participants:
        p.decide(commit)
    return 'COMMIT' if commit else 'ABORT'
