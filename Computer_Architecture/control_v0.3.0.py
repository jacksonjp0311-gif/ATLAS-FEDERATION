"""Conservative AT8 static control-flow, ROM reachability and control-table audit.

Acyclic all-HALT paths imply bounded normal completion *if no input or hardware
trap occurs*. Graph cycles cannot establish infinite execution or nontermination.
"""
from __future__ import annotations
from .isa import decode,validate_rom


def control_flow_certificate(rom:bytes):
    validate_rom(rom)
    decoded={i:decode(rom[i:i+2],i) for i in range(0,len(rom),2)}
    successors={};escape=[]
    for pc,inst in decoded.items():
        next_pc=pc+2
        if inst.name=='HALT':targets=[]
        elif inst.name=='JMP':targets=[inst.operand]
        elif inst.name in ('JNZ','JZ'):targets=[inst.operand,next_pc]
        else:targets=[next_pc]
        successors[pc]=tuple(sorted(set(v for v in targets if v in decoded)))
        if next_pc not in decoded and next_pc in targets:escape.append(pc)
    reachable=set();stack=[0]
    while stack:
        pc=stack.pop()
        if pc in reachable:continue
        reachable.add(pc);stack.extend(successors[pc])
    status={};has_cycle=False
    def walk(pc):
        nonlocal has_cycle
        if status.get(pc)==1:has_cycle=True;return
        if status.get(pc)==2:return
        status[pc]=1
        for nxt in successors[pc]:walk(nxt)
        status[pc]=2
    walk(0)
    reachable_escape=sorted(pc for pc in escape if pc in reachable)
    terminal=sorted(pc for pc in reachable if not successors[pc])
    terminal_without_halt=[pc for pc in terminal if decoded[pc].name!='HALT']
    prove=not has_cycle and not reachable_escape and not terminal_without_halt and bool(terminal)
    longest=None
    if prove:
        memo={}
        def depth(pc):
            if pc not in memo:memo[pc]=1+max([depth(n) for n in successors[pc]],default=0)
            return memo[pc]
        longest=depth(0)
    ram_reads=sorted({inst.operand for pc,inst in decoded.items() if pc in reachable and inst.name=='LOAD'})
    ram_writes=sorted({inst.operand for pc,inst in decoded.items() if pc in reachable and inst.name=='STORE'})
    inports=sorted({inst.operand for pc,inst in decoded.items() if pc in reachable and inst.name=='IN'})
    outports=sorted({inst.operand for pc,inst in decoded.items() if pc in reachable and inst.name=='OUT'})
    return {'schema':'atlas.at8-conservative-control/1',
        'reachable_program_counters':tuple(sorted(reachable)),
        'unreachable_program_counters':tuple(sorted(set(decoded)-reachable)),
        'reachable_cycle':has_cycle,'fallthrough_escapes':tuple(reachable_escape),
        'all_paths_to_halt_if_no_trap':prove,
        'max_instructions_if_no_trap':longest,
        'possible_input_exhaustion':bool(inports),
        'ram_read_addresses':tuple(ram_reads),'ram_write_addresses':tuple(ram_writes),
        'input_ports':tuple(inports),'output_ports':tuple(outports),
        'proof_scope':'structural control flow only; branch feasibility, data, interrupts, hardware timing unverified'}
