"""AT8 control-flow, decoding, and static termination analysis (bounded software).

No instructions are executed. Structural properties are *conservative*: a loop
may terminate dynamically despite being marked as not structurally guaranteed;
input availability, electrical timing and hardware safety are not analyzed.
"""
from __future__ import annotations
from collections import defaultdict
from .isa import decode,validate_rom,BRANCHES


def control_flow_analysis(rom: bytes):
    image=validate_rom(rom)
    n=len(rom);nodes=list(range(0,n,2));edges={};terminal=set();may_trap=set()
    for pc in nodes:
        inst=decode(rom[pc:pc+2],pc)
        if inst.name=='HALT':edges[pc]=tuple();terminal.add(pc);continue
        nextpc=pc+2
        targets=[inst.operand] if inst.name=='JMP' else ([nextpc,inst.operand] if inst.name in ('JNZ','JZ') else [nextpc])
        clean=set()
        for q in targets:
            if q>=n:may_trap.add(pc)
            else:clean.add(q)
        edges[pc]=tuple(sorted(clean))
    reachable=set();todo=[0]
    while todo:
        p=todo.pop()
        if p not in reachable:
            reachable.add(p);todo.extend(edges[p])
    # Reachable cycle detection via a three-color DFS. For bounded ROM <=128
    # instructions, recursion depth is safe under Python's default limit.
    state={};cyclic_nodes=set()
    def visit(pc,path):
        state[pc]=1;path.append(pc)
        for q in edges[pc]:
            if q not in reachable:continue
            if state.get(q,0)==0:visit(q,path)
            elif state[q]==1:cyclic_nodes.update(path[path.index(q):])
        path.pop();state[pc]=2
    visit(0,[])
    dead_ends={p for p in reachable if not edges[p] and p not in terminal}
    has_trap=bool(reachable&may_trap)
    proof=(not cyclic_nodes and not has_trap and not dead_ends and bool(reachable&terminal))
    # A proof concerns control-flow shape only; execution can trap due to input.
    return {'schema':'atlas.at8-control-flow/1','rom_instructions':image['instructions'],
      'reachable_pcs':tuple(sorted(reachable)),
      'unreachable_pcs':tuple(sorted(set(nodes)-reachable)),
      'reachable_halts':tuple(sorted(reachable&terminal)),
      'reachable_structural_cycles':tuple(sorted(cyclic_nodes)),
      'reachable_falloff_traps':tuple(sorted(reachable&may_trap)),
      'all_structural_paths_terminate_at_halt':proof,
      'physical_hardware_verified':False,
      'limitations':'conservative branch feasibility, excludes input exhaustion, dynamic timing and physical faults'}
