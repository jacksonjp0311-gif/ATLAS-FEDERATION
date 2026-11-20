"""Documented calibration links; not independently certified metrological traceability."""
from __future__ import annotations
from datetime import date


def audit_chain(nodes, edges, *, measurement_id, as_of=None):
    """Identify missing and cyclic calibration linkage. Returns a documentation audit.

    Nodes: id, kind, description, source_url, valid_through (ISO date or null).
    Edges: child, parent; node may link upward to a reference standard.
    No claimed certificate authenticity or numerical uncertainty verification.
    """
    # Supply as_of for deterministic/replayable audits; the legacy default is today.
    if as_of is None: as_of = date.today().isoformat()
    try: audit_date = date.fromisoformat(as_of)
    except (TypeError, ValueError) as exc: raise ValueError('as_of must be an ISO date') from exc
    if not isinstance(nodes,list) or not isinstance(edges,list):raise ValueError('nodes and edges lists required')
    mapping={}
    for n in nodes:
        if not isinstance(n,dict) or not isinstance(n.get('id'),str) or not n['id'] or n['id'] in mapping:
            raise ValueError('unique node IDs required')
        mapping[n['id']]=n
    if measurement_id not in mapping:raise ValueError('measurement not found')
    parents={k:[] for k in mapping}
    for e in edges:
        if not isinstance(e,dict) or set(e)!={'child','parent'}:raise ValueError('edge must have child and parent')
        a,b=e['child'],e['parent']
        if a not in mapping or b not in mapping:raise ValueError('dangling calibration link')
        parents[a].append(b)
    visited=set();active=set();cycle=False;terminals=set();missing=[];expired=[]
    def walk(v):
        nonlocal cycle
        if v in active:cycle=True;return
        if v in visited:return
        active.add(v)
        node=mapping[v]
        if not node.get('description') or not node.get('source_url'):missing.append(v)
        until=node.get('valid_through')
        if until is not None:
            try: d=date.fromisoformat(until)
            except (TypeError,ValueError):raise ValueError('invalid validity date')
            if d < audit_date:expired.append(v)
        if not parents[v]:terminals.add(v)
        for p in parents[v]:walk(p)
        active.remove(v);visited.add(v)
    walk(measurement_id)
    reference_paths=[x for x in terminals if mapping[x].get('kind')=='reference_standard']
    return {'schema':'measurement-atlas.traceability-audit.v1', 'measurement_id':measurement_id, 'as_of':as_of,
            'visited_nodes':sorted(visited),'terminal_nodes':sorted(terminals),'reference_standard_terminals':sorted(reference_paths),
            'cycles_detected':cycle,'missing_documentation':sorted(set(missing)), 'expired_documentation':sorted(set(expired)),
            'documented_chain_complete':not cycle and not missing and not expired and len(terminals)>0 and len(reference_paths)==len(terminals),
            'limitation':'Checks structural documentation only; does not authenticate calibration certificates, competence, uncertainties, or SI traceability.'}
