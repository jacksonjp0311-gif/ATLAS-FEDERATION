"""Bounded dependency inversion and reconstructible build ordering."""
from __future__ import annotations
from hashlib import sha256
from .contracts import _name,canonical


def plan_dependencies(dependencies):
    """Stable Kahn topological sort of a node->prerequisites map.

    Reports cycles fail-closed, never silently discards them. Never executes tasks.
    """
    if type(dependencies) is not dict or not 1<=len(dependencies)<=256:
        raise ValueError('nonempty bounded dependency graph required')
    names=set(dependencies)
    for k,v in dependencies.items():
        _name(k)
        if type(v) not in (tuple,list) or len(v)>256:raise ValueError('bounded dependency list')
        if len(set(v))!=len(v):raise ValueError('duplicate dependency')
        for item in v:
            _name(item)
            if item not in names:raise ValueError('dependency outside manifest')
    indeg={k:len(dependencies[k]) for k in names};out={k:[] for k in names}
    for key,requires in dependencies.items():
        for req in requires:out[req].append(key)
    ready=sorted(k for k in names if indeg[k]==0);order=[]
    while ready:
        x=ready.pop(0);order.append(x)
        for y in sorted(out[x]):
            indeg[y]-=1
            if indeg[y]==0:
                ready.append(y);ready.sort()
    if len(order)!=len(names):raise ValueError('cycle in prerequisite graph; cannot construct safely')
    edges=tuple(sorted((a,b) for b,reqs in dependencies.items() for a in reqs))
    return {'schema':'atlas.pattern-build-order/1','order':tuple(order),
            'edges':edges,'graph_sha256':sha256(canonical({'nodes':sorted(names),'edges':edges})).hexdigest(),
            'physical_dependencies_proven':False}


def plan_layers(dependencies):
    plan=plan_dependencies(dependencies);depth={}
    for n in plan['order']:
        requires=dependencies[n]
        depth[n]=0 if not requires else max(depth[p] for p in requires)+1
    return tuple(tuple(sorted(n for n,d in depth.items() if d==i)) for i in range(max(depth.values())+1))
