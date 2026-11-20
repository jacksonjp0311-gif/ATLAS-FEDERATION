"""Executable investigations. All numbers are author-created, not experiments."""
from __future__ import annotations
from .models import *

def casebook():
    cases=[]
    def put(name,condition,observation,limitation):
        if not condition:raise AssertionError(name)
        cases.append({'name':name,'result':'passed','observation':observation,'limitation':limitation})
    h=counter_machine([('inc',0,1),('decjz',0,2,2),('halt',)],step_budget=4)
    put('two-counter halts',h['status']=='halted' and h['registers']==(0,0),h,'bounded input program only')
    u=counter_machine([('inc',0,0)],step_budget=8)
    put('budget is not a nonhalting oracle',u['status']=='unknown_budget_exhausted',u,'unknown not nonhalting')
    x=[('a',2),('b',1),('c',1),('d',0)]
    out=stable_mergesort(x,key=lambda t:t[1]);put('stable sorting',out==[('d',0),('b',1),('c',1),('a',2)],out,'one finite input')
    put('leftmost binary insertion',lower_bound([1,1,2,3],1)==0,'leftmost index 0','requires sorted input')
    g={'A':{'B':4,'C':1},'B':{'D':1},'C':{'B':1,'D':7},'D':{}}
    p=dijkstra(g,'A');put('graph shortest path certified',p['distances']['D']==3 and shortest_path_certificate(g,'A',p),p['distances'],'nonnegative weights only')
    neg={'A':{'B':1},'B':{'C':-3},'C':{'B':1}}
    put('negative cycle refused',bellman_ford(neg,'A')['status']=='reachable_negative_cycle','negative cycle reachable','no finite shortest path')
    put('dependency cycle refused',_reject_cycle(),'cycle rejection','does not prove general workflow liveness')
    put('edit distance',edit_distance('kitten','sitting')==3,3,'unit costs and textual units are characters')
    k=knapsack_01([2,3,4],[3,4,5],5)
    put('knapsack pseudo polynomial',k['value']==7 and k['indices']==(0,1),k,'runtime depends on capacity numeric value')
    gg,x,y=extended_gcd(-54,24)
    put('Bezout identity',gg==6 and -54*x+24*y==6,(gg,x,y),'arbitrary precision integers')
    it=interval_mul(rational_interval('-1/2','3/2'),rational_interval('-2','3'))
    put('rational enclosure',it==(Fraction(-3),Fraction(9,2)),list(map(str,it)),'requires exact rational endpoints')
    b=bisection(lambda t:t*t-2,1,2,continuous_confirmed=True,atol=1e-8)
    put('bisection interval under declared continuity',b['interval'][0]**2<=2<=b['interval'][1]**2,b,'caller continuity claim not independently proved')
    n=[1e16,1.,1.,-1e16]; naive=0.0
    for value in n:naive+=value
    put('floating point accumulation risk',naive==0. and fsum(n)==2.,{'naive_left_to_right':naive,'fsum':fsum(n)},'Kahan not always exact; built-in sum may compensate')
    put('Shannon entropy binary fair',abs(shannon_entropy([.5,.5])-1)<1e-12,1,'requires declared probability distribution')
    put('finite certificate catches wrong sort',not sorted_permutation_certificate([2,1],[1,1]),'rejected invalid output','certificate covers only the inspected input')
    put('prefix-free code',prefix_free(['0','10','11']) and not prefix_free(['0','01']),'correct prefix decision','no optimality claim')
    return {'status':'passed','cases':cases,'count':len(cases),'scope':'author-created offline mathematical cases only'}

def _reject_cycle():
    try:topological_order({'A':['B'],'B':['A']})
    except InvalidInput:return True
    return False
