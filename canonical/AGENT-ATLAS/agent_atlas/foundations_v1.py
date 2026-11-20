"""Reconstructible finite-model agent science, without hidden services.

All functions are pure, dependency-free and operate on author/caller-supplied
probabilities or graphs. They cannot authenticate task outcomes or actual
agent improvement. Deliberately narrow so that proofs and arithmetic are
understandable from source text alone.
"""
from __future__ import annotations
from collections import defaultdict
from heapq import heappush, heappop
from math import isfinite, log

class ReferenceModelError(ValueError):
    pass

def _float(x,name,*,nonnegative=False):
    if type(x) not in (float,int) or not isfinite(x):
        raise ReferenceModelError(f'{name} must be finite real')
    v=float(x)
    if nonnegative and v<0:raise ReferenceModelError(f'{name} must be nonnegative')
    return v

def _matrix(rows,n,m,name):
    if not isinstance(rows,list) or len(rows)!=n or any(not isinstance(r,list) or len(r)!=m for r in rows):
        raise ReferenceModelError(f'{name} must be {n}x{m} matrix')
    return [[_float(x,name,nonnegative=True) for x in row] for row in rows]

def _prob(row,name):
    if abs(sum(row)-1)>1e-9:raise ReferenceModelError(f'{name} must sum to 1')
    if any(not 0<=x<=1 for x in row):raise ReferenceModelError(f'{name} out of range')


def belief_update(prior:list,transition:list,observation_likelihood:list,observation:int)->dict:
    """POMDP filter: predict using P(s'|s,a), then normalize P(o|s').

    All inputs supplied; no observation model learned, no state inferred with
    guaranteed accuracy. Zero likelihood = unavailable posterior, not zero.
    """
    if not isinstance(prior,list) or not 1<=len(prior)<=16:raise ReferenceModelError('state count 1..16')
    n=len(prior);b=[_float(x,'prior',nonnegative=True) for x in prior];_prob(b,'prior')
    p=_matrix(transition,n,n,'transition')
    for i,row in enumerate(p):_prob(row,f'transition state {i}')
    if not isinstance(observation_likelihood,list) or len(observation_likelihood)!=n or any(not isinstance(row,list) for row in observation_likelihood):
        raise ReferenceModelError('likelihood must be state-by-observation matrix')
    no=len(observation_likelihood[0])
    if not 1<=no<=64:raise ReferenceModelError('observation category count 1..64 required')
    obs=_matrix(observation_likelihood,n,no,'observation likelihood')
    for i,row in enumerate(obs):_prob(row,f'observation state {i}')
    if type(observation) is not int or not 0<=observation<no:raise ReferenceModelError('observed category out of range')
    pred=[sum(b[i]*p[i][j] for i in range(n)) for j in range(n)]
    weights=[pred[j]*obs[j][observation] for j in range(n)]
    evidence=sum(weights)
    if evidence <= 1e-15:raise ReferenceModelError('observation probability zero; posterior not identified')
    result=[q/evidence for q in weights]
    return {'schema':'atlas.agent-belief-filter/1','prior':b,'predicted':pred,
       'observation_index':observation,'observation_probability':evidence,'posterior':result,
       'origin':'fully_supplied_pomdp_model','identification_verified':False,
       'limitations':['No model fitting, calibration, unmodeled state or actual agent observation',
                      'Bayesian posterior is conditional on specified transition and sensor likelihoods']}


def finite_horizon_mdp(transitions:list,rewards:list,terminal_values:list,horizon:int,discount:float=1.0)->dict:
    """Exact finite-horizon Bellman expectation backup for small finite MDP.

    transitions[s][a][next_s]; rewards[s][a][next_s] evaluated on a transition.
    terminal_values[s] declares continuation value after final action.
    """
    if type(horizon) is not int or not 1<=horizon<=64:raise ReferenceModelError('horizon 1..64')
    g=_float(discount,'discount')
    if not 0<=g<=1:raise ReferenceModelError('discount must be [0,1]')
    if not isinstance(transitions,list) or not 1<=len(transitions)<=16:raise ReferenceModelError('state count 1..16')
    n=len(transitions)
    if not isinstance(transitions[0],list) or not 1<=len(transitions[0])<=12:raise ReferenceModelError('action count 1..12')
    a_count=len(transitions[0]);T=[];G=[]
    if not isinstance(rewards,list) or len(rewards)!=n:raise ReferenceModelError('reward state count mismatch')
    for s in range(n):
        if not isinstance(transitions[s],list) or len(transitions[s])!=a_count or not isinstance(rewards[s],list) or len(rewards[s])!=a_count:
            raise ReferenceModelError('action count mismatch')
        t_actions=[];r_actions=[]
        for a in range(a_count):
            row=transitions[s][a]
            if not isinstance(row,list) or len(row)!=n:raise ReferenceModelError('transition next-state length mismatch')
            pr=[_float(x,'transition',nonnegative=True) for x in row];_prob(pr,'transition')
            reward=rewards[s][a]
            if not isinstance(reward,list) or len(reward)!=n:raise ReferenceModelError('reward next-state length mismatch')
            t_actions.append(pr);r_actions.append([_float(x,'reward') for x in reward])
        T.append(t_actions);G.append(r_actions)
    if not isinstance(terminal_values,list) or len(terminal_values)!=n:raise ReferenceModelError('terminal values require state count')
    v=[_float(x,'terminal value') for x in terminal_values]
    values=[v];policies=[]
    for _ in range(horizon):
        new=[];policy=[]
        for s in range(n):
            q=[sum(T[s][a][j]*(G[s][a][j]+g*v[j]) for j in range(n)) for a in range(a_count)]
            choice=max(range(a_count),key=lambda a:q[a]) # deterministic tie: first action
            new.append(q[choice]);policy.append(choice)
        v=new;values.append(v);policies.append(policy)
    return {'schema':'atlas.agent-bellman-finite/1','horizon':horizon,'discount':g,
        'start_values':values[-1],'first_action':policies[-1],
        'value_by_actions_remaining':values,'policy_by_actions_remaining':policies,
        'origin':'supplied_tiny_markov_model','real_agent_improvement_verified':False,
        'limitations':['Exact Bellman recursion only under fully observed finite Markov dynamics',
                       'No task reward validation, partial observability, multi-agent game, or model learning']}


def shortest_path_reference(graph:dict,start:str,goal:str,heuristic:dict|None=None)->dict:
    """Dijkstra witness plus optional A* candidate, avoiding heuristic overclaim.

    Nonnegative weighted edges. A* returns candidate, independently checked
    against Dijkstra; its optimality is NOT assumed from unverified heuristic.
    """
    if not isinstance(graph,dict) or not 1<=len(graph)<=128:raise ReferenceModelError('graph 1..128 nodes')
    nodes=set(graph)
    if any(not isinstance(k,str) or not k or not isinstance(v,dict) for k,v in graph.items()):
        raise ReferenceModelError('graph requires string IDs and adjacency dicts')
    if not isinstance(start,str) or not isinstance(goal,str) or start not in nodes or goal not in nodes:raise ReferenceModelError('unknown start/goal')
    edges={}
    for k,arcs in graph.items():
        edges[k]={}
        for v,w in arcs.items():
            if v not in nodes:raise ReferenceModelError('unknown target node')
            edges[k][v]=_float(w,'edge weight',nonnegative=True)
    h={k:0.0 for k in nodes}
    if heuristic is not None:
        if not isinstance(heuristic,dict) or set(heuristic)!=nodes:raise ReferenceModelError('heuristic must list all nodes')
        h={k:_float(v,'heuristic',nonnegative=True) for k,v in heuristic.items()}
    def search(use_h):
        heap=[(h[start] if use_h else 0,0,start)];best={start:0.0};parent={};expanded=0
        while heap:
            f,curr,node=heappop(heap)
            if curr!=best.get(node):continue
            expanded+=1
            if node==goal:
                route=[node]
                while route[-1] in parent:route.append(parent[route[-1]])
                return {'path':list(reversed(route)),'cost':curr,'expanded':expanded}
            for next_node,weight in sorted(edges[node].items()):
                new=curr+weight
                if new<best.get(next_node,float('inf')):
                    best[next_node]=new;parent[next_node]=node
                    heappush(heap,(new+(h[next_node] if use_h else 0),new,next_node))
        return {'path':None,'cost':None,'expanded':expanded}
    optimal=search(False);candidate=search(True)
    match=optimal['cost']==candidate['cost'] if optimal['cost'] is not None and candidate['cost'] is not None else optimal['cost']==candidate['cost']
    admissible=(h[goal]==0 and all(h[k]<=_dijkstra_cost_to_goal(k,goal,edges)+1e-12 for k in nodes)) if heuristic else True
    return {'schema':'atlas.agent-shortest-path/1','dijkstra_witness':optimal,'heuristic_candidate':candidate,
       'candidate_matches_witness':match,'heuristic_admissible_for_complete_graph':admissible,
       'heuristic_proved_from_input_graph':bool(heuristic),
       'limitations':['Dijkstra requires explicit nonnegative edges, no hidden costs or stochastic outcomes',
                      'A* candidate not guaranteed optimal when heuristic inadmissible',
                      'State graph and costs are caller-supplied, not automatically grounded in external tools']}

def _dijkstra_cost_to_goal(start,goal,edges):
    h=[(0,start)];dist={start:0}
    while h:
        d,u=heappop(h)
        if d!=dist[u]:continue
        if u==goal:return d
        for v,w in edges[u].items():
            nd=d+w
            if nd<dist.get(v,float('inf')):dist[v]=nd;heappush(h,(nd,v))
    return float('inf')


def offline_importance_value(rows:list,*,max_weight:float=100.0)->dict:
    """IPS for logged binary rewards, with declared support and effective sample size.

    Not doubly robust; no claim of unconfounded logging or confidence intervals.
    """
    if not isinstance(rows,list) or not 2<=len(rows)<=10000:raise ReferenceModelError('2..10000 logged rows required')
    cap=_float(max_weight,'max_weight',nonnegative=True)
    if cap<1:raise ReferenceModelError('cap must be at least one')
    weighted=[];weights=[]
    for r in rows:
        if not isinstance(r,dict) or set(r)!={'logged_action','target_action','logging_probability','reward'}:
            raise ReferenceModelError('each row requires exact action, target, propensity and reward')
        if r['logged_action'] is None or r['target_action'] is None:raise ReferenceModelError('action ID missing')
        p=_float(r['logging_probability'],'logging propensity')
        if not 0<p<=1:raise ReferenceModelError('logging support absent or invalid')
        reward=_float(r['reward'],'reward')
        if not 0<=reward<=1:raise ReferenceModelError('bounded reward must be 0..1')
        w=(1/p if r['logged_action']==r['target_action'] else 0.0)
        if w>cap:raise ReferenceModelError('weight exceeds declared cap; refusing silent truncation')
        weights.append(w);weighted.append(w*reward)
    sw=sum(weights);sw2=sum(w*w for w in weights)
    if sw==0:raise ReferenceModelError('no target actions observed; cannot estimate')
    return {'schema':'atlas.agent-ips-illustration/1','n':len(rows),
      'ips_mean':sum(weighted)/len(rows),'self_normalized_ratio':sum(weighted)/sw,
      'effective_sample_size':sw*sw/sw2,'max_realized_weight':max(weights),
      'limitations':['Logging propensities and target policy are caller-supplied and unauthenticated',
                     'No confounding or policy-support diagnostics beyond supplied values; no causal policy proof',
                     'IPS and self-normalized IPS differ; neither interval nor genuine agent improvement is estimated']}
