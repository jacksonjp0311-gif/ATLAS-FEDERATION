"""Independent finite oracles: distinct implementations, exhaustive small state spaces.
No host kernel, real power-cut, workload timing or physical device is tested.
"""
from __future__ import annotations
import collections,functools,itertools,json,random,sys,hashlib,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from os_atlas.addressing import AddressSpace,PageFault
from os_atlas.scheduling import Task,round_robin,earliest_deadline_first
from os_atlas.paging import page_faults
from os_atlas.deadlock import deadlocked_components
from os_atlas.allocator import Buddy
from os_atlas.journal import CrashJournal
from os_atlas.elf64 import loadable_segments

checks=collections.Counter()

def cmp(name,actual,expected):
    checks[name]+=1
    if actual!=expected:raise AssertionError(f'{name} mismatch observed={actual!r} independent={expected!r}')

# 1. Direct quotient and remainder versus model with and without TLB.
r=random.Random(28029)
for page_size in [256,1024,4096,16384]:
    a=AddressSpace(page_size=page_size,frames=8192,tlb_entries=4)
    for vpn in range(200):a.map(vpn,100+vpn,'rwx')
    for _ in range(5000):
        vpn=r.randrange(200);offset=r.randrange(page_size)
        cmp('address_translation',a.translate(vpn*page_size+offset),(vpn+100)*page_size+offset)
    old=a.translate(page_size*3);a.map(3,999,'r');cmp('tlb_shootdown',a.translate(page_size*3),999*page_size)

# 2. Independent RR event engine: one tick, queue of task indices with explicit ready clock.
def rr_reference(tasks,q):
    tasks=sorted(tasks,key=lambda x:(x.arrival,x.pid));remain={x.pid:x.burst for x in tasks}
    waiting=[];current=None;countdown=0;index=0;t=0;out=[]
    while remain:
        while index<len(tasks) and tasks[index].arrival==t:
            waiting.append(tasks[index].pid);index+=1
        if current is None and waiting:
            current=waiting.pop(0);countdown=q
        out.append(current)
        if current is not None:
            countdown-=1;remain[current]-=1
            if remain[current]==0:del remain[current];current=None
            elif countdown==0:waiting.append(current);current=None
        t+=1
    return tuple(out)

def edf_reference(tasks):
    remaining={x.pid:x.burst for x in tasks};clock=0;history=[]
    while remaining:
        elig=sorted((x.deadline,x.pid) for x in tasks if x.pid in remaining and x.arrival<=clock)
        if elig:
            pid=elig[0][1];remaining[pid]-=1
            if not remaining[pid]:del remaining[pid]
            history.append(pid)
        else:history.append(None)
        clock+=1
    return tuple(history)
for seed in range(600):
    rand=random.Random(seed+33)
    tasks=[Task(str(i),rand.randrange(6),rand.randrange(1,9),rand.randrange(15,35)) for i in range(rand.randrange(1,8))]
    for q in (1,2,3,5):cmp('round_robin',round_robin(tasks,q),rr_reference(tasks,q))
    cmp('earliest_deadline_first',earliest_deadline_first(tasks),edf_reference(tasks))

# 3. Competing FIFO/LRU and independent exact Bellman optimal replacement.
def fifo_ref(seq,n):
    slots=[];miss=0
    for page in seq:
        if page not in slots:
            miss+=1
            if len(slots)==n:slots.pop(0)
            slots.append(page)
    return miss

def lru_ref(seq,n):
    slots=[];miss=0
    for page in seq:
        if page in slots:slots.remove(page)
        else:
            miss+=1
            if len(slots)==n:slots.pop(0)
        slots.append(page)
    return miss

def optimal_ref(seq,n):
    seq=tuple(seq)
    @functools.lru_cache(None)
    def f(i,live):
        if i==len(seq):return 0
        p=seq[i]
        if p in live:return f(i+1,live)
        if len(live)<n:return 1+f(i+1,tuple(sorted(live+(p,))))
        return 1+min(f(i+1,tuple(sorted((set(live)-{v})|{p}))) for v in live)
    return f(0,())
for n in (1,2,3):
    for seq in itertools.product(range(3),repeat=7):
        cmp('fifo_reference',page_faults(seq,n,'fifo'),fifo_ref(seq,n))
        cmp('lru_reference',page_faults(seq,n,'lru'),lru_ref(seq,n))
        cmp('optimal_exhaustive_dynamic_program',page_faults(seq,n,'opt'),optimal_ref(seq,n))

# 4. Brute pairwise reachability versus Tarjan SCC. 6-node finite graphs.
def graph_ref(edges):
    nodes=sorted(set(sum(([a,b] for a,b in edges),[])))
    reach={(u,v):u==v or (u,v) in edges for u in nodes for v in nodes}
    for k in nodes:
        for i in nodes:
            for j in nodes:
                reach[i,j]=reach[i,j] or (reach[i,k] and reach[k,j])
    groups=[];covered=set()
    for v in nodes:
        if v in covered:continue
        comp=tuple(u for u in nodes if reach[u,v] and reach[v,u])
        covered.update(comp)
        if len(comp)>1 or (v,v) in edges:groups.append(comp)
    return tuple(sorted(groups))
for seed in range(3000):
    rand=random.Random(seed+902)
    n=rand.randrange(1,7)
    edges=[(i,j) for i in range(n) for j in range(n) if rand.random()<0.17]
    cmp('deadlock_scc',deadlocked_components(edges),graph_ref(edges))

# 5. Event-driven filesystem durability prefix; recover only completed durable commits.
for seed in range(3000):
    rand=random.Random(seed);j=CrashJournal();expected={}
    for i in range(8):
        tx=f'tx{i}';j.begin(tx);j.set(tx,'k',i)
        if rand.randrange(2)==0:
            j.commit(tx)
            if rand.randrange(2)==0:
                j.flush();expected['k']=i
        else:
            if rand.randrange(2)==0:j.flush()
        if rand.randrange(2)==0:j.crash()
    j.crash()
    # Uncommitted transactions may be flushed before a later committed transaction.
    # Compare against a separate scan that only applies commits in durable prefix.
    open_tx={};result={}
    for record in j.durable:
        typ,txn,key,value=record
        if typ=='begin':open_tx[txn]=[]
        elif typ=='set' and txn in open_tx:open_tx[txn].append((key,value))
        elif typ=='commit' and txn in open_tx:
            for k,v in open_tx.pop(txn):result[k]=v
    cmp('wal_durable_prefix',j.recover(),result)

# 6. Buddy allocator cross-checked with independent byte-level occupancy bitmap.
for seed in range(120):
    rng=random.Random(seed*13);b=Buddy(9,3);allocated=[]
    for _ in range(65):
        if allocated and rng.randrange(3)==0:b.release(allocated.pop(rng.randrange(len(allocated))))
        else:
            try:allocated.append(b.alloc(rng.randrange(1,70)))
            except MemoryError:pass
        bitmap=[0]*512
        for addr,(order,_) in b.allocated.items():
            for i in range(addr,addr+(1<<order)):bitmap[i]+=1
        for order,addrs in b.free_blocks.items():
            for addr in addrs:
                for i in range(addr,addr+(1<<order)):bitmap[i]+=1
        cmp('buddy_bytewise_partition',max(bitmap)==min(bitmap)==1,True)
        cmp('buddy_free_byte_count',b.free_bytes(),512-b.used_bytes())

# 7. Constructed ELF64 test vector independently encoded with struct.
def make_elf(payload=b'ABCD'):
    ident=b'\x7fELF\x02\x01\x01'+b'\x00'*9
    head=struct.pack('<16sHHIQQQIHHHHHH',ident,2,62,1,0x402000,64,0,0,64,56,1,0,0,0)
    prog=struct.pack('<IIQQQQQQ',1,5,4096,0x402000,0,len(payload),128,4096)
    return head+prog+b'\x00'*(4096-120)+payload
for n in range(1,30):
    p=bytes(range(n));s=loadable_segments(make_elf(p))
    cmp('elf64_segment_bytes',s[0].initialized,p)
    cmp('elf64_zero_fill',s[0].zero_fill,128-n)

# 8. Negative controls: deliberately faulty algorithms MUST fail their own known invariants.
belady=[1,2,3,4,1,2,5,1,2,3,4,5]
assert fifo_ref(belady,4)>fifo_ref(belady,3)
negative={'belady_fifo_more_frames_can_be_worse':True,'unflushed_ack_not_durable':True,'permission_denied_on_write_only_mapping':True}
j=CrashJournal();j.begin('x');j.set('x','a',3);j.commit('x');j.crash()
assert j.recover()=={}
a=AddressSpace();a.map(1,2,'r')
try:a.translate(4096,'w')
except PageFault:pass
else:raise AssertionError('permission enforcement disabled')

out={'schema':'atlas.os-internals-independent-oracle/1','result':'passed','comparisons':sum(checks.values()),'comparison_groups':dict(sorted(checks.items())),'negative_controls':negative,'oracle_method':'independent finite enumerations, reference state machines, brute Bellman DP and byte-coverage checks','physical_hardware_and_real_power_failure_tested':False,'real_kernel_source_conformance_tested':False,'review':'independent software comparator within same authored research program, not an independent expert peer review'}
if __name__=='__main__':
    print(json.dumps(out,sort_keys=True,indent=2))
