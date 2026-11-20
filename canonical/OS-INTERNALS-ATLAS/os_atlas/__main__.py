from .addressing import AddressSpace
from .scheduling import Task,round_robin
from .paging import page_faults
from .allocator import Buddy
from .journal import CrashJournal

def main():
    a=AddressSpace();a.map(1,5,'rw')
    b=Buddy();block=b.alloc(28)
    j=CrashJournal();j.begin('tx1');j.set('tx1','key','value');j.commit('tx1');j.flush();j.crash()
    print({'mapped':a.translate(4096+12),'round_robin':round_robin([Task('A',0,3),Task('B',1,2)],2),'lru_faults':page_faults([1,2,1,3,1],2,'lru'),'buddy_block':block,'recovered':j.recover()})
if __name__=='__main__':main()
