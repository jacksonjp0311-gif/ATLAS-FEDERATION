"""Original ATLAS FORGE manufacturing v0.2 metrology and reconstruction kernels.

Built for a single canonical 14-node federation after verified Electronics v1RC
and archived Manufacturing v0.1 branch are reconciled. Standard library only.
No physical machine safety, provenance authenticity, fab qualification or peer review.
"""
from __future__ import annotations
import math
from statistics import NormalDist
from collections import deque


def _real(name,value,nonnegative=False,positive=False):
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError(f'{name}: finite real required')
    if (nonnegative and value<0) or (positive and value<=0):
        raise ValueError(f'{name}: outside permitted domain')
    return float(value)


def covariance_budget_psd(matrix, coefficients=None):
    """Validate real symmetric positive SEMIDEFINITE covariance, estimate sqrt(a' Σ a).

    Symmetry, diagonal>=0 and elementwise |Cij|<=sqrt(Cii Cjj) alone do NOT
    guarantee PSD. Uses symmetric Jacobi rotations on <=16x16 to reject
    negative eigenvalues beyond a scale-aware finite tolerance. Eigensolver is
    bounded reference math, NOT a proof of covariance measurement fidelity.
    """
    if not isinstance(matrix,(list,tuple)) or not 1<=len(matrix)<=16:
        raise ValueError('covariance requires 1..16 rows')
    n=len(matrix)
    if any(not isinstance(row,(list,tuple)) or len(row)!=n for row in matrix):
        raise ValueError('covariance must be square')
    a=[[_real('covariance entry',v) for v in row] for row in matrix]
    if coefficients is None:coeffs=[1.]*n
    else:
        if not isinstance(coefficients,(list,tuple)) or len(coefficients)!=n:raise ValueError('coefficient length')
        coeffs=[_real('sensitivity coefficient',x) for x in coefficients]
    scale=max(1e-300,max(abs(v) for row in a for v in row))
    atol=1e-12*scale
    for i in range(n):
        if a[i][i]<-atol:raise ValueError('negative diagonal covariance')
        if a[i][i]<0:a[i][i]=0.
        for j in range(i+1,n):
            if abs(a[i][j]-a[j][i])>atol:raise ValueError('covariance asymmetry')
            avg=(a[i][j]+a[j][i])/2
            a[i][j]=a[j][i]=avg
    # Jacobi eigenvalue sweeps for a symmetric matrix.
    q=[row[:] for row in a]
    for _ in range(100*n*n):
        off=max(((abs(q[i][j]),i,j) for i in range(n) for j in range(i+1,n)),default=(0,0,0))
        magnitude,p,k=off
        if magnitude<=1e-13*scale:break
        if q[p][k]==0:continue
        tau=(q[k][k]-q[p][p])/(2*q[p][k])
        t=math.copysign(1/(abs(tau)+math.sqrt(1+tau*tau)),tau) if tau!=0 else 1.
        c=1/math.sqrt(1+t*t);s=t*c
        app=q[p][p];akk=q[k][k];apk=q[p][k]
        q[p][p]=app-t*apk;q[k][k]=akk+t*apk;q[p][k]=q[k][p]=0.
        for j in range(n):
            if j in (p,k):continue
            jp=q[j][p];jk=q[j][k]
            q[j][p]=q[p][j]=c*jp-s*jk
            q[j][k]=q[k][j]=s*jp+c*jk
    else:raise ValueError('covariance eigensolver failed to converge')
    eigen=sorted(q[i][i] for i in range(n))
    if eigen[0] < -2e-10*scale:raise ValueError('covariance not positive semidefinite')
    variance=math.fsum(coeffs[i]*a[i][j]*coeffs[j] for i in range(n) for j in range(n))
    if variance < -1e-9*scale*max(1.,sum(abs(x) for x in coeffs)**2):
        raise ValueError('propagated variance negative')
    variance=max(0.,variance)
    return {'standard_uncertainty':math.sqrt(variance),'variance':variance,
            'minimum_covariance_eigenvalue':eigen[0],
            'jacobi_eigenvalues':tuple(eigen),'status':'valid_psd_within_numeric_tolerance',
            'metrology_certificate_authenticated':False}


def wilson_yield_interval(pass_count, total, confidence=.95):
    """Finite iid Bernoulli Wilson interval. No reliability claim without samples."""
    if type(pass_count) is not int or type(total) is not int or total<1 or not 0<=pass_count<=total:
        raise ValueError('integer successes and nonzero total required')
    conf=_real('confidence',confidence,positive=True)
    if not conf<1:raise ValueError('confidence must be <1')
    z=NormalDist().inv_cdf((1+conf)/2)
    p=pass_count/total
    den=1+z*z/total
    center=(p+z*z/(2*total))/den
    half=z*math.sqrt(p*(1-p)/total+z*z/(4*total*total))/den
    return {'estimated_pass_fraction':p,'lower':max(0.,center-half),
            'upper':min(1.,center+half),'confidence_level':conf,
            'model':'iid Bernoulli Wilson score, does not validate independence or unbiased sampling'}


def normal_inspection_acceptance_risk(true_value,measurement_sigma,lsl,usl,guard_band):
    """P(accepted | specified TRUE value) under Gaussian zero-bias measurement noise.

    Accept reading only inside [LSL+guard, USL-guard]. Unlike Bayesian P(true
    good | reading), this quantity does not silently assume a prior.
    """
    actual=_real('true value',true_value)
    sigma=_real('measurement sigma',measurement_sigma,positive=True)
    lo=_real('lower spec',lsl);hi=_real('upper spec',usl)
    guard=_real('guard',guard_band,nonnegative=True)
    if not lo<hi or 2*guard>hi-lo:raise ValueError('invalid acceptance interval')
    norm=NormalDist(mu=actual,sigma=sigma)
    probability=norm.cdf(hi-guard)-norm.cdf(lo+guard)
    return {'accept_given_true_value_probability':min(1.,max(0.,probability)),
            'true_value_within_spec':lo<=actual<=hi,
            'reading_accept_interval':(lo+guard,hi-guard),
            'assumption':'Gaussian unbiased instrument error, specified true item value; no Bayesian posterior'}


def stable_process_capability(values,lsl,usl,stability_evidence,distribution_evidence):
    """Cp/Cpk conditional on supplied evidence flags; flags are NOT independently verified."""
    if not isinstance(values,(tuple,list)) or len(values)<8:raise ValueError('at least eight observations')
    sample=[_real('sample',v) for v in values]
    lo=_real('LSL',lsl);hi=_real('USL',usl)
    if not lo<hi:raise ValueError('LSL must be below USL')
    mean=math.fsum(sample)/len(sample)
    sigma=math.sqrt(math.fsum((v-mean)**2 for v in sample)/(len(sample)-1))
    if sigma==0:raise ValueError('observed zero variance cannot prove perfect process')
    if type(stability_evidence) is not bool or type(distribution_evidence) is not bool:
        raise ValueError('evidence declarations must be explicit booleans')
    if not (stability_evidence and distribution_evidence):
        return {'status':'HOLD_unverified_stability_or_distribution',
                'mean':mean,'sample_sigma':sigma,'cp':None,'cpk':None}
    return {'status':'conditional_on_user_declared_stability_and_distribution_not_authenticated',
            'mean':mean,'sample_sigma':sigma,
            'cp':(hi-lo)/(6*sigma),'cpk':min(hi-mean,mean-lo)/(3*sigma),
            'observations':len(sample)}


def _toposort(steps):
    if not isinstance(steps,dict) or not steps:raise ValueError('nonempty step mapping required')
    ids=set(steps)
    indeg={i:0 for i in ids};children={i:[] for i in ids}
    for ident,item in steps.items():
        if type(ident) is not str or not ident or not isinstance(item,dict):raise ValueError('invalid process step')
        deps=item.get('depends_on',[])
        if not isinstance(deps,(tuple,list)) or len(set(deps))!=len(deps) or ident in deps or not set(deps)<=ids:
            raise ValueError('invalid dependency reference')
        indeg[ident]=len(deps)
        for d in deps:children[d].append(ident)
    todo=deque(sorted(i for i in ids if indeg[i]==0));order=[]
    while todo:
        ident=todo.popleft();order.append(ident)
        for nxt in sorted(children[ident]):
            indeg[nxt]-=1
            if indeg[nxt]==0:todo.append(nxt)
    if len(order)!=len(ids):raise ValueError('process dependency cycle')
    return order


def resource_bounded_schedule(steps):
    """Deterministic feasible LIST schedule, not an optimal scheduling proof.

    Input {id:{duration_min:>=0, resource:'A', depends_on:[ids]}}.
    Each resource is unary; precedence and machine occupancy are enforced.
    """
    order=_toposort(steps)
    machines={};finished={};schedule={}
    for ident in order:
        item=steps[ident]
        minutes=_real('duration_min',item.get('duration_min'),nonnegative=True)
        resource=item.get('resource')
        if type(resource) is not str or not resource:raise ValueError('resource ID required')
        prereq=max((finished[d] for d in item.get('depends_on',[])),default=0.)
        earliest=max(prereq,machines.get(resource,0.))
        end=earliest+minutes
        if not math.isfinite(end):raise ValueError('unrepresentable schedule')
        finished[ident]=end;machines[resource]=end
        schedule[ident]={'resource':resource,'start_min':earliest,'end_min':end}
    return {'schedule':schedule,'makespan_min':max(finished.values()),
            'order':order,'optimizer':'deterministic list scheduling, not proven optimal',
            'resource_conflicts':0,'dependencies_violated':0}


def datum_rigid_transform_xy(point_xy,origin_xy,rotation_radians,scale=1.):
    """2D rigid rotation + translation; optional isotropic scale for calibration."""
    if not isinstance(point_xy,(list,tuple)) or len(point_xy)!=2 or not isinstance(origin_xy,(list,tuple)) or len(origin_xy)!=2:
        raise ValueError('point and origin length two')
    x,y=(_real('point',v) for v in point_xy)
    tx,ty=(_real('translation',v) for v in origin_xy)
    th=_real('rotation',rotation_radians)
    s=_real('scale',scale,positive=True)
    cs=math.cos(th);sn=math.sin(th)
    return (tx+s*(cs*x-sn*y),ty+s*(sn*x+cs*y))


def traceability_chain_audit(records,target_id,reference_date_yyyymmdd):
    """Audit declared traceability DOCUMENTATION, never assert source authenticity.

    Each {id:{parent,unit,uncertainty,valid_through,sha256}}.
    A SHA256 string is only a claim until original bytes and issuer checked.
    """
    if not isinstance(records,dict) or type(target_id) is not str or target_id not in records:
        raise ValueError('traceability item missing')
    if type(reference_date_yyyymmdd) is not int or not 20000101<=reference_date_yyyymmdd<=99991231:
        raise ValueError('reference date required')
    seen=set();path=[];issues=[];current=target_id
    while current is not None:
        if current in seen:raise ValueError('calibration parent cycle')
        seen.add(current)
        item=records.get(current)
        if not isinstance(item,dict):issues.append(f'missing record {current}');break
        unit=item.get('unit');parent=item.get('parent')
        if not unit or type(unit) is not str:issues.append(f'{current}: missing unit')
        try: u=_real('declared uncertainty',item.get('standard_uncertainty'),nonnegative=True)
        except ValueError:issues.append(f'{current}: missing uncertainty')
        date=item.get('valid_through')
        if type(date) is not int or date<reference_date_yyyymmdd:issues.append(f'{current}: calibration expired or date missing')
        declared=item.get('sha256')
        if not (type(declared) is str and len(declared)==64 and all(k in '0123456789abcdef' for k in declared)):
            issues.append(f'{current}: no recorded SHA-256')
        path.append(current)
        if parent is not None and type(parent) is not str:issues.append(f'{current}: invalid parent type');break
        current=parent
    return {'status':'documentation_present_not_source_authenticated' if not issues else 'HOLD_missing_traceability_documentation',
            'chain':tuple(path),'issues':tuple(issues),'original_source_bytes_authenticated':False,
            'calibration_certificates_independently_verified':False}


def manufacturing_evidence_gate(steps,artifact_ids,recorded_evidence):
    """Typed prerequisite evidence ledger; detects absent evidence and blocked stages.

    Evidence is merely *recorded metadata*, not authenticated lab work. A release
    can be structurally ready but never externally certified by this function.
    """
    order=_toposort(steps)
    if not isinstance(artifact_ids,(tuple,list)) or not all(type(x) is str and x for x in artifact_ids):
        raise ValueError('artifact IDs must be nonempty strings')
    if not isinstance(recorded_evidence,dict):raise ValueError('evidence mapping required')
    available=set(artifact_ids);step_report={};missing_all=set()
    for sid in order:
        step=steps[sid]
        req=step.get('inputs',[]);outs=step.get('outputs',[]);requires=step.get('required_evidence',[])
        if not all(isinstance(x,(list,tuple)) for x in (req,outs,requires)):
            raise ValueError('step fields must be lists')
        if any(type(x) is not str or not x for x in (*req,*outs,*requires)):
            raise ValueError('invalid input/output or required evidence ID')
        missing_inputs=sorted(set(req)-available)
        missing_evidence=sorted(x for x in requires if not recorded_evidence.get(x))
        blocked=bool(missing_inputs or missing_evidence or any(step_report[d]['status']!='recorded_complete_not_external_certified' for d in step.get('depends_on',[])))
        status='HOLD_missing_inputs_or_evidence' if blocked else 'recorded_complete_not_external_certified'
        step_report[sid]={'status':status,'missing_inputs':missing_inputs,'missing_evidence':missing_evidence}
        missing_all.update(missing_evidence)
        if not blocked:
            for x in outs:
                if x in available:raise ValueError('artifact produced twice')
                available.add(x)
    return {'steps':step_report,'missing_evidence_ids':tuple(sorted(missing_all)),
            'structurally_complete':all(v['status']=='recorded_complete_not_external_certified' for v in step_report.values()),
            'independently_certified':False,'physical_devices_fabricated':False,
            'scope':'recorded artifact/evidence declaration only; no authentication of contents or physical processes'}
