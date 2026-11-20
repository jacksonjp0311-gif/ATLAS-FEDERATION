"""Author-generated v1 investigations, not measured model/hardware results."""
from .advanced_v02 import *
from .cases import casebook as prior_casebook

def casebook_v1():
    checks=[]
    def add(name,value,condition,caveat):
        checks.append({'id':name,'result':value,'passed':bool(condition),'origin':'author-generated-mathematical-model','limit':caveat})
    f=kruskal_forest(4,[(0,1,1),(1,2,2),(0,2,9),(2,3,1)])
    add('kruskal-cut-proof',f,f['total_cost']==4 and f['components']==1,'Undirected graph and weights are supplied')
    net=max_flow_min_cut(4,[(0,1,3),(0,2,2),(1,2,1),(1,3,2),(2,3,4)],0,3)
    add('flow-cut-equality',net,net['max_flow']==5 and net['min_cut_capacity']==5,'No real transport capacity tested')
    lin=gaussian_solve_exact([[2,1],[1,-1]],[5,1]);add('exact-linear-residual',lin,lin['solution']==['2','1'],'Only supplied rational coefficients')
    spectral=fft_radix2([1,2,3,4]);restored=fft_radix2(spectral,inverse=True)
    add('fft-inverse',{'max_err':max(abs(v-z) for v,z in zip(restored,[1,2,3,4]))},all(abs(v-z)<1e-12 for v,z in zip(restored,[1,2,3,4])),'Not a physical resonant-mode measurement')
    conv=convolution_linear([1,2,3],[2,1]);add('linear-convolution-no-alias',{'out':[round(z.real,9) for z in conv]},all(abs(z-w)<1e-10 for z,w in zip(conv,[2,5,8,3])),'Pad for linear convolution')
    ht=hoeffding_interval([0,1]*50);add('concentration-conditional',{'radius':ht['unclipped_half_width']},0<ht['unclipped_half_width']<.3 and not ht['coverage_verified_for_actual_data'],'Independence is not established by code')
    a=vector_clock_tick((0,0),0);b=vector_clock_tick((0,0),1)
    add('concurrent-events',{'a':a,'b':b},vector_clock_relation(a,b)=='concurrent','No real message or authorized event')
    accepted=vector_clock_merge(b,a,1);add('happened-before-receive',{'prior':a,'merged':accepted},vector_clock_relation(a,accepted)=='happened_before','Vector clocks do not authenticate messages')
    equal=canonical_json_digest({'a':1,'b':2})==canonical_json_digest({'b':2,'a':1})
    add('json-key-canonical-subset',{'equal':equal},equal,'Not a complete RFC 8785/JCS implementation')
    try:gaussian_solve_exact([[1,2],[2,4]],[1,2]);singular=False
    except ComputationError:singular=True
    add('singular-system-refusal',{'refused':singular},singular,'Uniqueness cannot be asserted')
    try:fft_radix2([1,2,3]);length=False
    except ComputationError:length=True
    add('fft-size-refusal',{'refused':length},length,'Only radix-two bounded input')
    try:max_flow_min_cut(2,[(0,1,-1)],0,1);negative=False
    except ComputationError:negative=True
    add('negative-capacity-refusal',{'refused':negative},negative,'Capacity must be nonnegative')
    # A statement about NP-hardness is NOT proven by a finite demo; record as explicitly non-observed.
    add('complexity-claim-not-from-tests',{'empirical_NP_completeness_claim':False},True,'Complexity relies on formal reductions and defined input model')
    add('postquantum-reference-not-implementation',{'ML_KEM_implemented':False},True,'Read NIST FIPS203 and verify errata before deployment')
    add('source-link-not-local-file',{'publisher_original_bytes_archived':False},True,'Bibliographic card is not a recoverable original primary publication')
    add('formal-type-judgment-limited',{'type_safety_certified':False},True,'No proof kernel or external code execution was implemented')
    return {'schema':'atlas.computation-v1-casebook/1','status':'passed' if all(c['passed'] for c in checks) and prior_casebook()['status']=='passed' else 'failed',
       'count':prior_casebook()['count']+len(checks),'v0_1_cases':prior_casebook()['count'],'v1_added_cases':len(checks),'cases':checks,
       'prior_cases_passed':prior_casebook()['status']=='passed','real_model_or_hardware_runs':0,'independent_scientific_review':False}
