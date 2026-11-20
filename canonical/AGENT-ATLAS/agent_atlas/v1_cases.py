"""Transparent offline v1 reference cases; not a model quality benchmark."""
from .foundations_v1 import (belief_update,finite_horizon_mdp,shortest_path_reference,
                              offline_importance_value,ReferenceModelError)


def casebook_v1():
    cases=[]
    def add(name,result,good,kind='synthetic_authored'):
        cases.append({'id':name,'origin':kind,'passed':bool(good),'result':result})
    b=belief_update([.6,.4],[[.9,.1],[.3,.7]],[[.8,.2],[.1,.9]],0)
    add('belief-update-observation',b,abs(b['posterior'][0]- .528/.562)<1e-12)
    try:
        belief_update([.5,.5],[[1,0],[0,1]],[[0,1],[0,1]],0)
        zero=False
    except ReferenceModelError:zero=True
    add('impossible-observation-refusal',{'refused':zero},zero)
    t=[[[1,0],[.5,.5]],[[0,1],[.2,.8]]]
    r=[[[0,0],[2,2]],[[0,0],[1,1]]]
    m=finite_horizon_mdp(t,r,[0,0],2,.9)
    add('finite-horizon-bellman',m,len(m['start_values'])==2 and all(x>=0 for x in m['start_values']))
    g={'S':{'A':1,'B':1},'A':{'G':1},'B':{'G':4},'G':{}}
    # If a goal is popped before the cheaper A path, the huge h(A) is invalid.
    a=shortest_path_reference(g,'S','G',{'S':0,'A':100,'B':0,'G':0})
    add('inadmissible-heuristic-counterexample',a,a['dijkstra_witness']['cost']==2 and a['heuristic_candidate']['cost']==5 and not a['candidate_matches_witness'])
    d=shortest_path_reference(g,'S','G')
    add('zero-heuristic-matches-dijkstra',d,d['candidate_matches_witness'] and d['dijkstra_witness']['cost']==2)
    logged=[{'logged_action':'A','target_action':'A','logging_probability':.5,'reward':1},
            {'logged_action':'B','target_action':'A','logging_probability':.5,'reward':0},
            {'logged_action':'A','target_action':'A','logging_probability':.5,'reward':0},
            {'logged_action':'B','target_action':'A','logging_probability':.5,'reward':1}]
    e=offline_importance_value(logged)
    add('policy-evaluation-ips',e,abs(e['ips_mean']-.5)<1e-12 and abs(e['self_normalized_ratio']-.5)<1e-12 and abs(e['effective_sample_size']-2)<1e-12)
    try:offline_importance_value([{'logged_action':'A','target_action':'A','logging_probability':.01,'reward':1}]*2,max_weight=10)
    except ReferenceModelError:cap=True
    else:cap=False
    add('low-propensity-refusal',{'refused':cap},cap)
    try:finite_horizon_mdp([[[.8,.1]]],[[[0,0]]],[0],1)
    except ReferenceModelError:invalid=True
    else:invalid=False
    add('improper-transition-refusal',{'refused':invalid},invalid)
    return {'schema':'atlas.agent-v1-casebook/1','status':'passed' if all(c['passed'] for c in cases) else 'failed',
      'count':len(cases),'cases':cases,'physical_agent_runs':0,'real_world_success_verification':False,
      'source_data_used':'publisher bibliography; constructed numeric cases only',
      'scientific_peer_review':False}
