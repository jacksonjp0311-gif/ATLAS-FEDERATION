"""Wait-for graph SCC deadlock model: single-instance, stable resource ownership."""
from __future__ import annotations

def deadlocked_components(edges):
    graph={}
    for a,b in edges:
        graph.setdefault(a,set()).add(b);graph.setdefault(b,set())
    index=0;stack=[];onstack=set();idx={};low={};groups=[]
    def visit(v):
        nonlocal index
        idx[v]=low[v]=index;index+=1
        stack.append(v);onstack.add(v)
        for w in sorted(graph[v],key=str):
            if w not in idx:
                visit(w);low[v]=min(low[v],low[w])
            elif w in onstack:low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            nodes=[]
            while True:
                w=stack.pop();onstack.remove(w);nodes.append(w)
                if w==v:break
            if len(nodes)>1 or (nodes and nodes[0] in graph[nodes[0]]):
                groups.append(tuple(sorted(nodes,key=str)))
    if len(graph)>1000:raise ValueError('graph too large')
    for v in sorted(graph,key=str):
        if v not in idx:visit(v)
    return tuple(sorted(groups,key=lambda x:tuple(map(str,x))))
