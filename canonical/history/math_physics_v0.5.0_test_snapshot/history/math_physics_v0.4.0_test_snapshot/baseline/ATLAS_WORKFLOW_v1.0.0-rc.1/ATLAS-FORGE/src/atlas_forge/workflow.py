"""Executable Measurement-first release discipline.

All eight gates must be supported, reviewed and scope-bound. A test pass cannot
supply a peer review, a Windows run, a held-out evaluation, or a Bitwork run.
This checks supplied evidence; it does not cryptographically authenticate people.
"""
from __future__ import annotations
from pathlib import Path
from .common import ContractError, canonical, sha, safe_path, strict_json

GATES={
 'G1':'Declared scope and frozen question families',
 'G2':'Primary-source evidence and explicit coverage gaps',
 'G3':'Scientific methods, units and edge cases',
 'G4':'Generic common-contract conformance across enabled nodes',
 'G5':'Exact, budgeted, evidence-preserving context',
 'G6':'Pinned real Bitwork to Atlas to actual AI execution',
 'G7':'Frozen held-out comparative retrieval and answer evaluation',
 'G8':'Clean builds, supported platforms and release integrity',
}


def subject_digest(root: Path) -> str:
    """Bind decisions to the release input bytes. Receipt/docs-only changes excluded.

    Excludes generated receipts and manifests so recording a decision is possible;
    includes source, nodes, schemas, tests, skills, examples and workflow criteria.
    """
    excluded={'.git','.venv','venv','__pycache__','.pytest_cache','build','dist','receipts','output'}
    selected={}
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if any(x in excluded or x.endswith('.egg-info') for x in rel.parts):continue
        if not p.is_file() or p.suffix in {'.pyc','.pyo'} or p.name=='MANIFEST.sha256':continue
        if rel.parts[0]=='docs':continue
        if rel.as_posix()=='workflow/gate_decisions.json':continue
        if p.is_symlink():raise ContractError('symlink release input')
        selected[rel.as_posix()]=sha(p.read_bytes())
    return sha(canonical(selected))


def gate_report(root: Path) -> dict:
    root=root.resolve()
    state=strict_json((root/'workflow/state.json').read_bytes())
    criteria=strict_json((root/'workflow/acceptance.json').read_bytes())
    decisions=strict_json((root/'workflow/gate_decisions.json').read_bytes())
    if state.get('schema')!='atlas.workflow/1' or state.get('active_node')!='measurement-atlas':raise ContractError('unsupported active workflow')
    if criteria.get('schema')!='atlas.acceptance/1' or set(criteria.get('gates',{}))!=set(GATES):raise ContractError('all eight acceptance gates required')
    entries=decisions.get('gates',{})
    if decisions.get('schema')!='atlas.gate-decisions/1' or set(entries)!=set(GATES):raise ContractError('all eight gate decisions required')
    subject=subject_digest(root);criteria_hash=sha(canonical(criteria));out=[]
    for key,title in GATES.items():
        d=entries[key];errors=[];status=d.get('status','missing');evidence=d.get('evidence',[])
        if status not in {'passed','partial','blocked','not_run'}:errors.append('unknown gate status')
        checked=[];kinds=set()
        if not isinstance(evidence,list):errors.append('evidence list required');evidence=[]
        for e in evidence:
            try:
                p=safe_path(root,e['path']);digest=sha(p.read_bytes())
                if digest!=e['sha256']:raise ContractError('evidence hash mismatch')
                checked.append({'path':e['path'],'sha256':digest})
                if status=='passed':
                    receipt=strict_json(p.read_bytes())
                    if receipt.get('result')!='passed' or receipt.get('subject_sha256')!=subject:raise ContractError('receipt not passed or release inputs differ')
                    if receipt.get('execution_kind') not in {'local_actual','remote_actual'}:raise ContractError('fixture or unrun evidence cannot pass a gate')
                    kinds.add(receipt.get('kind'))
            except (ValueError,OSError,KeyError,TypeError) as exc:errors.append(str(exc))
        if status=='passed':
            if not evidence:errors.append('pass needs evidence')
            if not set(criteria['gates'][key]['required_evidence_kinds'])<=kinds:errors.append('required evidence kinds missing')
            if d.get('subject_sha256')!=subject:errors.append('gate evidence is for different release inputs')
            if d.get('criteria_sha256')!=criteria_hash:errors.append('acceptance criteria changed')
            if not d.get('reviewed_by') or not d.get('reviewed_at'):errors.append('review decision required')
        out.append({'gate':key,'title':title,'status':'invalid' if errors else status,'evidence':checked,'errors':errors,'remaining':d.get('remaining',[])})
    frozen=criteria.get('status')=='frozen_owner_approved' and bool(criteria.get('approved_by')) and bool(criteria.get('frozen_at'))
    ready=frozen and all(g['status']=='passed' for g in out)
    return {'schema':'atlas.gate-report/1','active_node':'measurement-atlas','target':'1.0.0','subject_sha256':subject,'criteria_sha256':criteria_hash,
            'v1_ready':bool(ready),'next_domain_allowed':bool(ready),'criteria_frozen':bool(frozen),'gates':out,
            'review_authenticity':'local operator record; no third-party identity attestation'}


def authorize_next_domain(root: Path, requested: str) -> dict:
    r=gate_report(root)
    if requested=='measurement-atlas':return {'allowed':True,'reason':'active domain'}
    if not r['next_domain_allowed']:raise ContractError('Measurement v1 acceptance incomplete; next-domain work is blocked')
    return {'allowed':True,'requested':requested,'measurement_subject_sha256':r['subject_sha256']}
