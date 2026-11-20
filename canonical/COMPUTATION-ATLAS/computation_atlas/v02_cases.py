"""Computation Atlas 0.2, authored mathematical cases, no production measurements."""
from .advanced_v02 import (DisjointSets,kruskal_forest,max_flow_min_cut,gaussian_solve_exact,
 fft_radix2,convolution_linear,hoeffding_interval,vector_clock_tick,vector_clock_merge,vector_clock_relation,canonical_json_digest)
from .models import InvalidInput

def casebook_v02():
    cases=[]
    def add(title,check,observation,limits):
        cases.append({'title':title,'passed':bool(check),'observation':observation,'limitations':limits,'origin':'author_constructed'})
    d=DisjointSets(5);d.union(0,1);d.union(1,2)
    add('equivalence-class union',d.components==3 and d.same(0,2) and not d.same(0,4),d.components,'No actual network component observed')
    m=kruskal_forest(4,[(0,1,1),(1,2,2),(0,2,5),(2,3,1)])
    add('minimum spanning forest',m['total_cost']==4 and m['components']==1,m,'Weight is only for supplied static graph')
    f=max_flow_min_cut(4,[(0,1,3),(0,2,2),(1,2,1),(1,3,2),(2,3,4)],0,3)
    add('max flow meets min cut',f['max_flow']==f['min_cut_capacity']==5,f,'No provider or traffic measurement')
    s=gaussian_solve_exact([[2,1],[1,-1]],[5,1])
    add('exact linear system with rational residual',s['solution']==['2','1'],s,'Input measurement uncertainty not assessed')
    inv=fft_radix2(fft_radix2([1,2,3,4]),inverse=True)
    add('FFT round trip',all(abs(a-b)<1e-12 for a,b in zip(inv,[1,2,3,4])),[str(x) for x in inv],'Round trip is not general numerical stability')
    conv=convolution_linear([1,2,3],[2,1])
    add('zero-padded linear convolution',all(abs(x-y)<1e-10 for x,y in zip(conv,[2,5,8,3])),[str(x) for x in conv],'No physical response measured')
    h=hoeffding_interval([0,1]*50,.05)
    add('bounded-sample concentration inequality',h['n']==100 and not h['coverage_verified_for_actual_data'],h,'Independence cannot be verified from a numeric array')
    a=vector_clock_tick((0,0),0);b=vector_clock_tick((0,0),1)
    add('concurrent vector clocks',vector_clock_relation(a,b)=='concurrent',[a,b],'No authenticated external clock or message order')
    c=vector_clock_merge(b,a,1)
    add('message merge creates causal relation',vector_clock_relation(a,c)=='happened_before',c,'Message delivery itself is an input assertion')
    add('canonical JSON key order',canonical_json_digest({'a':1,'b':2})==canonical_json_digest({'b':2,'a':1}),'SHA256 equal','Not RFC8785 JCS or digital signature')
    return {'schema':'computation.atlas.casebook/2','version':'0.2.0','status':'passed' if all(x['passed'] for x in cases) else 'failed',
        'count':len(cases),'cases':cases,'live_AI_or_physical_measurement':False,'independent_expert_review':False}
