"""Small, inspectable causal teaching models with explicit computational limits.

A graph is supplied by the caller, not learned or certified here. d-separation
is a graphical property; a failed separation does not prove an association.
No source text is executed. Fractions preserve declared finite probabilities.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Iterable, Mapping
import re

class ModelError(ValueError):
    """Malformed input, unsupported size, impossible conditioning or missing support."""


def rational(value: str | int | float | Fraction) -> Fraction:
    if isinstance(value, bool):
        raise ModelError('Boolean is not a numeric probability')
    if not isinstance(value, (str,int,float,Fraction)):
        raise ModelError('Expected a rational-compatible scalar')
    if isinstance(value,str) and len(value)>100:
        raise ModelError('Numeric representation too long')
    text=str(value)
    for exponent in re.findall(r'[eE]([+-]?\d+)',text):
        if abs(int(exponent))>128:raise ModelError('Exponent outside teaching limit')
    try:
        result = value if isinstance(value,Fraction) else Fraction(str(value))
    except (ValueError,ZeroDivisionError,OverflowError) as exc:
        raise ModelError('Invalid finite rational') from exc
    if result.numerator.bit_length()>1024 or result.denominator.bit_length()>1024:
        raise ModelError('Rational precision exceeds teaching limit')
    return result


@dataclass(frozen=True)
class DAG:
    """Explicit finite acyclic graph, at most 20 named nodes."""
    nodes: tuple[str,...]
    edges: tuple[tuple[str,str],...]

    def __post_init__(self):
        if not isinstance(self.nodes,(tuple,list)) or not 1<=len(self.nodes)<=20:
            raise ModelError('Expected 1..20 nodes')
        if any(not isinstance(v,str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{0,39}',v) for v in self.nodes):
            raise ModelError('Invalid node name')
        if len(set(self.nodes))!=len(self.nodes): raise ModelError('Duplicate node')
        if not isinstance(self.edges,(tuple,list)) or len(self.edges)>190:
            raise ModelError('Expected an edge list with at most 190 entries')
        if any(not isinstance(e,(list,tuple)) or len(e)!=2 or any(not isinstance(v,str) for v in e) for e in self.edges):
            raise ModelError('Each edge must have two named endpoints')
        es=tuple(tuple(e) for e in self.edges)
        if len(set(es))!=len(es): raise ModelError('Duplicate edge')
        if any(a not in self.nodes or b not in self.nodes or a==b for a,b in es):
            raise ModelError('Unknown endpoint or self-loop')
        object.__setattr__(self,'nodes',tuple(self.nodes));object.__setattr__(self,'edges',es)
        self.topological_order()

    @classmethod
    def from_dict(cls, value: dict) -> 'DAG':
        if not isinstance(value,dict) or set(value)!={'nodes','edges'}: raise ModelError('Expected only nodes and edges')
        return cls(value['nodes'],value['edges'])

    def topological_order(self) -> tuple[str,...]:
        incoming={v:0 for v in self.nodes}; children={v:[] for v in self.nodes}
        for a,b in self.edges: incoming[b]+=1;children[a].append(b)
        todo=deque(sorted(v for v in self.nodes if incoming[v]==0)); result=[]
        while todo:
            a=todo.popleft();result.append(a)
            for b in sorted(children[a]):
                incoming[b]-=1
                if incoming[b]==0:todo.append(b)
        if len(result)!=len(self.nodes): raise ModelError('Directed cycle is unsupported')
        return tuple(result)

    def _set(self, values: Iterable[str]) -> set[str]:
        if isinstance(values,str): raise ModelError('Use a sequence of names, not a bare string')
        try: result=set(values)
        except (TypeError,ValueError) as exc: raise ModelError('Invalid node set') from exc
        if not result.issubset(self.nodes): raise ModelError('Unknown node in query')
        return result

    def ancestors(self, values: Iterable[str]) -> set[str]:
        found=self._set(values)
        while True:
            new=found|{a for a,b in self.edges if b in found}
            if new==found:return found
            found=new

    def descendants(self, value: str) -> set[str]:
        if value not in self.nodes:raise ModelError('Unknown node')
        found={value}
        while True:
            new=found|{b for a,b in self.edges if a in found}
            if new==found:return found-{value}
            found=new

    def d_separated(self, x: Iterable[str], y: Iterable[str], given: Iterable[str]=()) -> bool:
        """Ancestral-moral-graph criterion; no faithfulness assertion."""
        X,Y,Z=self._set(x),self._set(y),self._set(given)
        if not X or not Y or X&Y or X&Z or Y&Z:raise ModelError('Nonempty X,Y and pairwise disjoint sets required')
        relevant=self.ancestors(X|Y|Z); adj={n:set() for n in relevant}
        for a,b in self.edges:
            if a in relevant and b in relevant:adj[a].add(b);adj[b].add(a)
        for child in relevant:
            parents=[a for a,b in self.edges if b==child and a in relevant]
            for a,b in combinations(parents,2):adj[a].add(b);adj[b].add(a)
        seen=set(Z);todo=list(X)
        while todo:
            n=todo.pop()
            if n in seen:continue
            if n in Y:return False
            seen.add(n);todo.extend(adj[n]-seen)
        return True

    def backdoor(self, exposure: str, outcome: str, adjusted: Iterable[str]=()) -> dict:
        """Pearl's sufficient single-exposure back-door criterion, not complete identification."""
        Z=self._set(adjusted)
        if exposure not in self.nodes or outcome not in self.nodes or exposure==outcome:
            raise ModelError('Distinct known exposure and outcome required')
        if exposure in Z or outcome in Z:raise ModelError('Cannot adjust for exposure/outcome')
        prohibited=Z&self.descendants(exposure)
        cut=DAG(self.nodes,tuple((a,b) for a,b in self.edges if a!=exposure))
        blocks=cut.d_separated([exposure],[outcome],Z)
        valid=not prohibited and blocks
        return {'criterion':'single-exposure-backdoor-sufficient','valid_under_supplied_graph':valid,
                'descendants_of_exposure_in_set':sorted(prohibited),'blocks_backdoor_paths':blocks,
                'graph_truth_checked':False,'no_causal_effect_claim_from_graph_alone':True,
                'failure_does_not_prove_nonidentifiability':True}

    def minimal_backdoor_sets(self, exposure: str, outcome: str, observed: Iterable[str]) -> list[list[str]]:
        observed_set=self._set(observed)
        # Fail malformed endpoints before the search, even with no candidate covariates.
        self.backdoor(exposure,outcome,())
        candidates=sorted(observed_set-{exposure,outcome}-self.descendants(exposure))
        if len(candidates)>12:raise ModelError('Subset search limited to 12 candidate covariates')
        found=[]
        for size in range(len(candidates)+1):
            for z in combinations(candidates,size):
                S=set(z)
                if any(set(f).issubset(S) for f in found):continue
                if self.backdoor(exposure,outcome,z)['valid_under_supplied_graph']:found.append(list(z))
        return found


class BinaryModel:
    """Fully specified binary causal Bayesian network, at most 12 nodes.

    Conditional tables must cover every parent configuration. Interventions
    replace the assigned node's factor. This is model evaluation, not inference
    of causal structure or of unmeasured mechanisms from observational data.
    """
    def __init__(self, graph: DAG, tables: Mapping[str,Mapping[str,object]]):
        if not isinstance(graph,DAG) or len(graph.nodes)>12:raise ModelError('Binary model needs a DAG with <=12 nodes')
        if not isinstance(tables,Mapping) or set(tables)!=set(graph.nodes):raise ModelError('One table per node required')
        self.graph=graph;self.parents={v:tuple(sorted(a for a,b in graph.edges if b==v)) for v in graph.nodes}
        self.tables={}
        for v in graph.nodes:
            if not isinstance(tables[v],Mapping):raise ModelError('Invalid conditional table')
            expected={''.join(map(str,bits)) for bits in product((0,1),repeat=len(self.parents[v]))}
            if set(tables[v])!=expected:raise ModelError('Missing or extra parent configurations')
            self.tables[v]={k:rational(p) for k,p in tables[v].items()}
            if any(not 0<=p<=1 for p in self.tables[v].values()):raise ModelError('Probability outside [0,1]')

    def _assignment(self, value: Mapping[str,int] | None) -> dict[str,int]:
        if value is None:return {}
        if not isinstance(value,Mapping) or any(k not in self.graph.nodes or type(v)is not int or v not in (0,1) for k,v in value.items()):
            raise ModelError('Assignment must map known nodes to integer zero or one')
        return dict(value)

    def joint(self, do: Mapping[str,int] | None=None) -> list[tuple[dict[str,int],Fraction]]:
        D=self._assignment(do); result=[]
        for values in product((0,1),repeat=len(self.graph.nodes)):
            a=dict(zip(self.graph.nodes,values));mass=Fraction(1)
            for v in self.graph.nodes:
                if v in D:
                    if a[v]!=D[v]:mass=Fraction(0);break
                else:
                    key=''.join(str(a[p]) for p in self.parents[v]);p=self.tables[v][key]
                    mass*=p if a[v] else 1-p
            if mass:result.append((a,mass))
        if sum((p for _,p in result),Fraction(0))!=1:raise ModelError('Joint mass not normalized')
        return result

    def probability(self, event: Mapping[str,int], given: Mapping[str,int] | None=None, do: Mapping[str,int] | None=None) -> Fraction:
        E,G=self._assignment(event),self._assignment(given)
        numerator=denominator=Fraction(0)
        for row,mass in self.joint(do):
            if all(row[v]==a for v,a in G.items()):
                denominator+=mass
                if all(row[v]==a for v,a in E.items()):numerator+=mass
        if denominator==0:raise ModelError('Conditioning event has zero probability')
        return numerator/denominator


def standardize_binary(rows: list[dict], target_weights: Mapping[str,object]) -> dict:
    """Exact weighted group rates. Causal assumptions remain an external obligation."""
    if not isinstance(rows,list) or not rows or len(rows)>10000:raise ModelError('Expected 1..10000 group rows')
    if not isinstance(target_weights,Mapping) or not target_weights:raise ModelError('Explicit target weights required')
    if any(not isinstance(z,str) or not z for z in target_weights):raise ModelError('Stratum IDs must be nonempty strings')
    weights={z:rational(w) for z,w in target_weights.items()}
    if any(w<0 for w in weights.values()) or sum(weights.values())!=1:raise ModelError('Nonnegative target weights must sum exactly to one')
    groups={}
    for row in rows:
        if not isinstance(row,dict) or set(row)!={'stratum','treatment','n','successes'}:raise ModelError('Unexpected grouped-data fields')
        z,a,n,s=(row[k] for k in ('stratum','treatment','n','successes'))
        if not isinstance(z,str) or not z or type(a)is not int or a not in (0,1) or type(n)is not int or type(s)is not int or not 0<=s<=n or n>10**12:
            raise ModelError('Invalid counts or treatment')
        if (z,a) in groups:raise ModelError('Duplicate stratum-treatment row')
        groups[z,a]=(n,s)
    rates={0:Fraction(0),1:Fraction(0)}
    for z,w in weights.items():
        if w==0:continue
        for a in (0,1):
            if (z,a) not in groups or groups[z,a][0]==0:raise ModelError('Positive target stratum lacks treatment support')
            n,s=groups[z,a];rates[a]+=w*Fraction(s,n)
    totals={a:sum(n for (z,b),(n,s) in groups.items() if a==b) for a in (0,1)}
    if any(n==0 for n in totals.values()):raise ModelError('Both treatments must be observed')
    crude={a:Fraction(sum(s for (z,b),(n,s) in groups.items() if a==b),totals[a]) for a in (0,1)}
    return {'standardized_rates':{str(a):str(rates[a]) for a in rates},'standardized_difference':str(rates[1]-rates[0]),
            'crude_rates':{str(a):str(crude[a]) for a in crude},'crude_difference':str(crude[1]-crude[0]),
            'causal_assumptions_verified':False,'uncertainty_interval':None,
            'target_weights':{z:str(w) for z,w in weights.items()},
            'required_for_causal_interpretation':['well-defined intervention and consistency','sufficient conditional exchangeability','positivity in target strata','appropriate sampling and measurement'],
            'warning':'Crude rates use the supplied sample; standardized rates use the declared target. Different targets need not be comparable.'}
