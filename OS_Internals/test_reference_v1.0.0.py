from __future__ import annotations
import os,random,struct,unittest
from os_atlas.addressing import AddressSpace,PageFault
from os_atlas.scheduling import Task,round_robin,earliest_deadline_first,completion_metrics
from os_atlas.paging import page_faults
from os_atlas.allocator import Buddy
from os_atlas.deadlock import deadlocked_components
from os_atlas.capabilities import HandleTable,Handle
from os_atlas.journal import CrashJournal
from os_atlas.elf64 import loadable_segments

def tiny_elf(data=b'CODE',memsz=16,flags=5,alignment=0x1000,offset=0x1000,vaddr=0x401000):
    # Test-only constructed minimal ELF64; no instruction execution.
    h=struct.pack('<16sHHIQQQIHHHHHH',b'\x7fELF\x02\x01\x01'+b'\x00'*9,2,62,1,vaddr,64,0,0,64,56,1,0,0,0)
    ph=struct.pack('<IIQQQQQQ',1,flags,offset,vaddr,0,len(data),memsz,alignment)
    return h+ph+b'\x00'*(offset-120)+data

class TestAddressing(unittest.TestCase):
    def test_map(self):
        a=AddressSpace(frames=32);a.map(3,7)
        self.assertEqual(a.translate(3*4096+91),7*4096+91)
        self.assertEqual(a.translate(3*4096+91),7*4096+91)
        self.assertEqual((a.hits,a.misses),(1,1))
    def test_permissions(self):
        a=AddressSpace();a.map(1,2,'rx')
        self.assertEqual(a.translate(4096,'x'),8192)
        with self.assertRaises(PageFault):a.translate(4096,'w')
    def test_privilege(self):
        a=AddressSpace();a.map(1,1,'r',user=False)
        with self.assertRaises(PageFault):a.translate(4096)
        self.assertEqual(a.translate(4096,user=False),4096)
    def test_tlb_invalidation(self):
        a=AddressSpace();a.map(1,1);a.translate(4096);a.map(1,3);self.assertEqual(a.translate(4096),3*4096)
    def test_unmap(self):
        a=AddressSpace();a.map(0,0);a.translate(1);a.unmap(0)
        with self.assertRaises(PageFault):a.translate(1)
    def test_bad(self):
        for kwargs in [dict(page_size=0),dict(page_size=1000),dict(frames=0),dict(tlb_entries=-1)]:
            with self.subTest(kwargs=kwargs),self.assertRaises(ValueError):AddressSpace(**kwargs)
    def test_invalid_permission(self):
        a=AddressSpace()
        for perm in ['', 'rr','rb','RX']:
            with self.subTest(perm=perm),self.assertRaises(ValueError):a.map(1,2,perm)
    def test_fault(self):
        a=AddressSpace()
        for addr in [-1,1<<48]:
            with self.assertRaises(PageFault):a.translate(addr)
        with self.assertRaises(PageFault):a.translate(1)

class TestScheduling(unittest.TestCase):
    def test_rr_known(self):self.assertEqual(round_robin([Task('A',0,3),Task('B',1,2)],2),('A','A','B','B','A'))
    def test_idle(self):self.assertEqual(round_robin([Task('late',3,2)]),(None,None,None,'late','late'))
    def test_empty(self):self.assertEqual(round_robin([]),())
    def test_metrics(self):
        jobs=[Task('A',0,3),Task('B',1,2)];m=completion_metrics(jobs,round_robin(jobs,2))
        self.assertEqual(m['A'],{'completion':5,'turnaround':5,'waiting':2})
        self.assertEqual(m['B'],{'completion':4,'turnaround':3,'waiting':1})
    def test_edf_preempt(self):self.assertEqual(earliest_deadline_first([Task('A',0,4,10),Task('B',1,1,2)]),('A','B','A','A','A'))
    def test_edf_no_deadline(self):
        with self.assertRaises(ValueError):earliest_deadline_first([Task('a',0,1)])
    def test_invalid(self):
        with self.assertRaises(ValueError):round_robin([Task('a',0,1),Task('a',0,1)])
        with self.assertRaises(ValueError):round_robin([Task('b',0,0)])
        with self.assertRaises(ValueError):round_robin([Task('a',0,1)],0)
        with self.assertRaises(ValueError):round_robin([Task('a',-1,1)])
    def test_work_conservation(self):
        for n in range(1,8):
            jobs=[Task(str(i),i%3,1+i%4) for i in range(n)]
            trace=round_robin(jobs,3)
            self.assertEqual(len([t for t in trace if t is not None]),sum(j.burst for j in jobs))
            self.assertEqual(len(set(trace)-{None}),n)
            self.assertEqual(sum(j.burst for j in jobs),len(earliest_deadline_first([Task(j.pid,j.arrival,j.burst,j.arrival+100) for j in jobs]))-sum(x is None for x in earliest_deadline_first([Task(j.pid,j.arrival,j.burst,j.arrival+100) for j in jobs])))

class TestPaging(unittest.TestCase):
    def test_belady(self):
        ref=[1,2,3,4,1,2,5,1,2,3,4,5]
        self.assertEqual((page_faults(ref,3),page_faults(ref,4)),(9,10))
    def test_fifo(self):self.assertEqual(page_faults([1,2,1,3,1],2),4)
    def test_lru(self):self.assertEqual(page_faults([1,2,1,3,1],2,'lru'),3)
    def test_opt(self):self.assertEqual(page_faults([1,2,1,3,1],2,'opt'),3)
    def test_miss_all_unique(self):self.assertEqual(page_faults(range(50),3),50)
    def test_empty(self):self.assertEqual(page_faults([],3,'opt'),0)
    def test_invalid(self):
        with self.assertRaises(ValueError):page_faults([1],0)
        with self.assertRaises(ValueError):page_faults([1],1,'bogus')
    def test_opt_dominates(self):
        for seed in range(40):
            r=random.Random(seed);ref=[r.randrange(7) for _ in range(25)]
            for frames in [1,2,3,4]:
                self.assertLessEqual(page_faults(ref,frames,'opt'),page_faults(ref,frames,'fifo'))
                self.assertLessEqual(page_faults(ref,frames,'opt'),page_faults(ref,frames,'lru'))

class TestBuddy(unittest.TestCase):
    def test_allocation_sizes(self):
        b=Buddy(10,3);a=b.alloc(9);self.assertEqual(b.used_bytes(),16);self.assertEqual(b.requested_bytes(),9)
        self.assertEqual(b.free_bytes(),1024-16);b.release(a);self.assertEqual(b.free_bytes(),1024)
    def test_merge(self):
        b=Buddy(8,2);a=[b.alloc(4) for _ in range(64)];self.assertEqual(b.free_bytes(),0)
        for i in reversed(a):b.release(i)
        self.assertEqual(b.free_blocks[8],{0})
    def test_full(self):
        b=Buddy(6,4);b.alloc(64)
        with self.assertRaises(MemoryError):b.alloc(1)
    def test_double_free(self):
        b=Buddy(6,2);a=b.alloc(3);b.release(a)
        with self.assertRaises(ValueError):b.release(a)
    def test_reuse(self):
        b=Buddy(8,3);p=b.alloc(5);b.release(p);self.assertEqual(b.alloc(5),p)
    def test_invalid(self):
        with self.assertRaises(ValueError):Buddy(2,3)
        with self.assertRaises(ValueError):Buddy().alloc(0)
        with self.assertRaises(ValueError):Buddy(5,3).alloc(33)
    def test_randomized_invariant(self):
        b=Buddy(10,3);rng=random.Random(909);active=[]
        for _ in range(350):
            if active and rng.randrange(3)==0:b.release(active.pop(rng.randrange(len(active))))
            else:
                try:active.append(b.alloc(rng.randrange(1,130)))
                except MemoryError:pass
            self.assertTrue(b.validate())
        for a in active:b.release(a)
        self.assertEqual(b.free_bytes(),1<<10)

class TestDeadlock(unittest.TestCase):
    def test_two(self):self.assertEqual(deadlocked_components([('a','b'),('b','a')]),(('a','b'),))
    def test_self(self):self.assertEqual(deadlocked_components([('a','a')]),(('a',),))
    def test_chain(self):self.assertEqual(deadlocked_components([('a','b'),('b','c')]),())
    def test_components(self):self.assertEqual(deadlocked_components([('a','b'),('b','a'),('c','d'),('d','c')]),(('a','b'),('c','d')))
    def test_nested(self):self.assertEqual(deadlocked_components([('a','b'),('b','c'),('c','a'),('c','d')]),(('a','b','c'),))

class TestCapabilities(unittest.TestCase):
    def test_rights(self):
        t=HandleTable();h=t.grant('file1','r');self.assertEqual(t.check(h,'r'),'file1')
        with self.assertRaises(PermissionError):t.check(h,'w')
    def test_stale(self):
        t=HandleTable(1);a=t.grant('a','r');t.revoke(a);b=t.grant('b','r')
        self.assertNotEqual(a,b)
        with self.assertRaises(PermissionError):t.check(a,'r')
        self.assertEqual(t.check(b,'r'),'b')
    def test_revoke_stale(self):
        t=HandleTable();h=t.grant(1,'w');t.revoke(h)
        with self.assertRaises(PermissionError):t.revoke(h)
    def test_full(self):
        t=HandleTable(1);t.grant('a','r')
        with self.assertRaises(MemoryError):t.grant('b','r')
    def test_bad(self):
        t=HandleTable()
        with self.assertRaises(ValueError):t.grant('a','BAD')
        with self.assertRaises(PermissionError):t.check(Handle(999,0),'r')

class TestJournal(unittest.TestCase):
    def test_commit_flush(self):
        j=CrashJournal();j.begin('t');j.set('t','x',1);j.commit('t');j.flush();j.crash();self.assertEqual(j.recover(),{'x':1})
    def test_commit_not_flush(self):
        j=CrashJournal();j.begin('t');j.set('t','x',1);j.commit('t');j.crash();self.assertEqual(j.recover(),{})
    def test_begin_flush_then_crash(self):
        j=CrashJournal();j.begin('t');j.set('t','x',1);j.flush();j.crash();self.assertEqual(j.recover(),{})
    def test_multiple(self):
        j=CrashJournal()
        for i in range(4):
            j.begin(str(i));j.set(str(i),'x',i);j.commit(str(i));j.flush()
        j.crash();self.assertEqual(j.recover(),{'x':3})
    def test_incomplete_tail(self):
        j=CrashJournal();j.begin('a');j.set('a','x',1);j.commit('a');j.flush()
        j.begin('b');j.set('b','x',9);j.flush();j.crash();self.assertEqual(j.recover(),{'x':1})
    def test_duplicate(self):
        j=CrashJournal();j.begin('t')
        with self.assertRaises(ValueError):j.begin('t')
        with self.assertRaises(ValueError):j.commit('other')
    def test_deterministic_digest(self):
        a=CrashJournal();b=CrashJournal()
        for j in (a,b):j.begin('t');j.set('t','x',1);j.commit('t');j.flush()
        self.assertEqual(a.durable_digest(),b.durable_digest())

class TestElf(unittest.TestCase):
    def test_valid(self):
        segs=loadable_segments(tiny_elf())
        self.assertEqual(len(segs),1);self.assertEqual(segs[0].address,0x401000)
        self.assertEqual(segs[0].initialized,b'CODE');self.assertEqual(segs[0].zero_fill,12)
    def test_not_elf(self):
        with self.assertRaises(ValueError):loadable_segments(b'not-elf')
    def test_trunc(self):
        with self.assertRaises(ValueError):loadable_segments(tiny_elf()[:-1])
    def test_memsize(self):
        with self.assertRaises(ValueError):loadable_segments(tiny_elf(memsz=1))
    def test_alignment(self):
        with self.assertRaises(ValueError):loadable_segments(tiny_elf(alignment=3))
    def test_unbounded(self):
        with self.assertRaises(ValueError):loadable_segments(tiny_elf(memsz=1<<30))
    def test_wrong_class(self):
        x=bytearray(tiny_elf());x[4]=1
        with self.assertRaises(ValueError):loadable_segments(bytes(x))
    def test_offset_overflow(self):
        x=bytearray(tiny_elf());struct.pack_into('<Q',x,64+8,1<<63)
        with self.assertRaises(ValueError):loadable_segments(bytes(x))

if __name__=='__main__':unittest.main()
