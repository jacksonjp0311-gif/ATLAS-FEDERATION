from .clocks import LamportClock,VectorClock,precedes
from .quorums import majority_size
from .paxos import Acceptor,propose
from .crdts import GCounter
import json

def demonstration():
    a,b=LamportClock(),LamportClock()
    sent=a.send();received=b.receive(sent)
    winners=propose([Acceptor() for _ in range(3)],1,'archive-verified')
    left,right=GCounter(),GCounter()
    left.increment('A',2);right.increment('B',3)
    return {'send':sent,'receive':received,'majority3':majority_size(3),'chosen':winners[0],
            'merged_gcounter':left.merge(right).value,'scope':'finite educational reference, not physical verification'}
if __name__=='__main__':print(json.dumps(demonstration(),indent=2))
